#!/usr/bin/env python3
"""Local validation for Web Surface Gate v0.1. Standard library only."""
from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
CANONICAL_ORIGIN = "https://altissports.com"
PUBLIC_ROUTES = [
    "/",
    "/spatial-sport/",
    "/as3/",
    "/evidence/",
    "/cite/",
    "/governance/",
    "/applied/ar-001/",
]
ROUTE_FILES = {
    "/": DOCS / "index.html",
    "/spatial-sport/": DOCS / "spatial-sport" / "index.html",
    "/as3/": DOCS / "as3" / "index.html",
    "/evidence/": DOCS / "evidence" / "index.html",
    "/cite/": DOCS / "cite" / "index.html",
    "/governance/": DOCS / "governance" / "index.html",
    "/applied/ar-001/": DOCS / "applied" / "ar-001" / "index.html",
    "/404.html": DOCS / "404.html",
}
FORBIDDEN = [
    r"RWS-\d+",
    r"RW-001",
    r"invitation",
    r"monetiz",
    r"buyer logic",
    r"strategic buyer",
    r"@gmail\.com",
    r"dispatch",
]
ASR_FORBIDDEN_AS_PUBLISHED = [
    r"ASR-001 is (a |an )?(published|ratified|adopted|recognized) standard",
    r"published standard",
]


class Page(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self._in_title = False
        self.h1: list[str] = []
        self._in_h1 = False
        self.canonical = ""
        self.description = ""
        self.og: dict[str, str] = {}
        self.twitter: dict[str, str] = {}
        self.lang = ""
        self.links: list[str] = []
        self.json_ld: list[str] = []
        self._in_ld = False
        self.skip = False
        self.nav = False
        self.main = False
        self.viewport = False
        self._in_script_type = ""

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "html":
            self.lang = d.get("lang", "")
        if tag == "title":
            self._in_title = True
        if tag == "h1":
            self._in_h1 = True
        if tag == "a" and d.get("href"):
            self.links.append(d["href"])
        if tag == "link" and d.get("rel") == "canonical":
            self.canonical = d.get("href", "")
        if tag == "meta":
            if d.get("name") == "description":
                self.description = d.get("content", "")
            if d.get("name") == "viewport":
                self.viewport = True
            if d.get("property", "").startswith("og:"):
                self.og[d["property"]] = d.get("content", "")
            if d.get("name", "").startswith("twitter:"):
                self.twitter[d["name"]] = d.get("content", "")
        if tag == "a" and "skip" in d.get("class", ""):
            self.skip = True
        if tag == "nav":
            self.nav = True
        if tag == "main":
            self.main = True
        if tag == "script" and d.get("type") == "application/ld+json":
            self._in_ld = True

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag == "h1":
            self._in_h1 = False
        if tag == "script":
            self._in_ld = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_h1:
            self.h1.append(data)
        if self._in_ld:
            self.json_ld.append(data)


def resolve_local(href: str, from_route: str) -> Path | None:
    if href.startswith("mailto:") or href.startswith("#"):
        return None
    parsed = urlparse(href)
    if parsed.scheme in {"http", "https"}:
        if parsed.netloc == "altissports.com" and parsed.path.startswith("/assets/"):
            return DOCS / parsed.path.lstrip("/")
        return None
    path = urlparse(urljoin(CANONICAL_ORIGIN + from_route, href)).path
    if path.endswith("/"):
        candidate = DOCS / path.lstrip("/") / "index.html"
        if candidate.exists():
            return candidate
    candidate = DOCS / path.lstrip("/")
    return candidate


def main() -> int:
    errors: list[str] = []
    pages: dict[str, Page] = {}

    required_files = [
        DOCS / "robots.txt",
        DOCS / "sitemap.xml",
        DOCS / "CNAME",
        DOCS / ".nojekyll",
        DOCS / "site.webmanifest",
        DOCS / "assets" / "css" / "site.css",
        DOCS / "assets" / "img" / "favicon.svg",
        DOCS / "assets" / "img" / "og.jpg",
        DOCS / "assets" / "img" / "og-altissports-spatial-2026.jpg",
        DOCS / "assets" / "img" / "favicon-32.png",
        DOCS / "assets" / "img" / "apple-touch-icon.png",
    ]
    for p in required_files:
        if not p.exists():
            errors.append(f"missing file {p.relative_to(ROOT)}")

    cname = (DOCS / "CNAME").read_text(encoding="utf-8").strip()
    if cname != "altissports.com":
        errors.append(f"CNAME is {cname!r}, expected 'altissports.com'")

    robots = (DOCS / "robots.txt").read_text(encoding="utf-8")
    if "Sitemap: https://altissports.com/sitemap.xml" not in robots:
        errors.append("robots.txt missing sitemap line")
    if "Disallow: /404.html" not in robots:
        errors.append("robots.txt should disallow 404.html")

    sitemap = (DOCS / "sitemap.xml").read_text(encoding="utf-8")
    sitemap_locs = re.findall(r"<loc>(.*?)</loc>", sitemap)
    expected = [CANONICAL_ORIGIN + r for r in PUBLIC_ROUTES]
    if sitemap_locs != expected:
        errors.append(f"sitemap locs {sitemap_locs} != {expected}")
    if "404" in sitemap:
        errors.append("sitemap must not include 404")

    titles = []
    descriptions = []
    for route, path in ROUTE_FILES.items():
        if not path.exists():
            errors.append(f"missing page {route}")
            continue
        html = path.read_text(encoding="utf-8")
        page = Page()
        page.feed(html)
        pages[route] = page
        titles.append(page.title.strip())
        descriptions.append(page.description.strip())

        if page.lang != "en":
            errors.append(f"{route} lang={page.lang!r}")
        if not page.viewport:
            errors.append(f"{route} missing viewport")
        if len(page.h1) != 1 and not (len(page.h1) >= 1):
            errors.append(f"{route} missing h1")
        if not page.title.strip():
            errors.append(f"{route} missing title")
        if not page.description.strip() or len(page.description) > 200:
            errors.append(f"{route} description missing or too long ({len(page.description)})")
        if not page.canonical:
            errors.append(f"{route} missing canonical")
        elif not page.canonical.startswith("https://altissports.com"):
            errors.append(f"{route} canonical not apex https: {page.canonical}")
        if "www." in page.canonical:
            errors.append(f"{route} canonical uses www: {page.canonical}")
        if route != "/404.html" and page.canonical != CANONICAL_ORIGIN + route:
            errors.append(f"{route} canonical {page.canonical} != {CANONICAL_ORIGIN + route}")
        for key in ("og:title", "og:description", "og:url", "og:image"):
            if key not in page.og:
                errors.append(f"{route} missing {key}")
        for key in ("twitter:card", "twitter:title", "twitter:image"):
            if key not in page.twitter:
                errors.append(f"{route} missing {key}")
        if route != "/404.html":
            social_image = CANONICAL_ORIGIN + "/assets/img/og-altissports-spatial-2026.jpg"
            if page.og.get("og:image") != social_image:
                errors.append(f"{route} must reference the versioned social image")
            if page.twitter.get("twitter:image") != social_image:
                errors.append(f"{route} Twitter image differs from Open Graph image")
            if page.og.get("og:image:type") != "image/jpeg":
                errors.append(f"{route} missing social image MIME type")
            if page.og.get("og:image:width") != "1200" or page.og.get("og:image:height") != "630":
                errors.append(f"{route} incorrect social image dimensions")
            if not page.og.get("og:image:alt") or not page.twitter.get("twitter:image:alt"):
                errors.append(f"{route} missing social image alternative text")
        if not page.skip or not page.nav or not page.main:
            errors.append(f"{route} missing skip/nav/main landmarks")
        if route != "/404.html" and not page.json_ld:
            errors.append(f"{route} missing JSON-LD")
        for blob in page.json_ld:
            try:
                json.loads(blob)
            except json.JSONDecodeError as exc:
                errors.append(f"{route} invalid JSON-LD: {exc}")

        for href in page.links:
            local = resolve_local(href, route)
            if local is None:
                continue
            if not local.exists():
                errors.append(f"{route} broken local link {href} -> {local}")

        lower = html.lower()
        for pat in FORBIDDEN:
            if re.search(pat, html, re.I):
                errors.append(f"{route} contains forbidden pattern {pat}")
        if "asr-001" in lower:
            if "unpublished" not in lower and "working draft" not in lower:
                errors.append(f"{route} mentions ASR-001 without unpublished/working draft language")
            for pat in ASR_FORBIDDEN_AS_PUBLISHED:
                if re.search(pat, html, re.I) and "not a published standard" not in lower:
                    if "unpublished" not in lower:
                        errors.append(f"{route} may present ASR as published ({pat})")

        css_hrefs = re.findall(r'href="(/assets/css/[^"]+)"', html)
        for href in css_hrefs:
            if not (DOCS / href.lstrip("/")).exists():
                errors.append(f"{route} missing stylesheet {href}")

    if len(set(titles)) != len(titles):
        errors.append(f"duplicate titles: {titles}")
    if len(set(descriptions)) != len(descriptions):
        errors.append("duplicate meta descriptions")

    css = (DOCS / "assets" / "css" / "site.css").read_text(encoding="utf-8")
    if "@media (prefers-reduced-motion: reduce)" not in css:
        errors.append("CSS missing reduced-motion")
    if "@media (max-width: 40rem)" not in css and "@media (max-width: 44rem)" not in css:
        errors.append("CSS missing a mobile breakpoint")
    if ":focus-visible" not in css:
        errors.append("CSS missing focus-visible")

    # Local HTTP smoke: files exist for every public route (GitHub Pages 200 analogue).
    for route in PUBLIC_ROUTES:
        path = ROUTE_FILES[route]
        if not path.exists() or path.stat().st_size < 500:
            errors.append(f"{route} missing or too small to be a real page")

    if errors:
        print("FAIL: Web Surface Gate v0.1 validation")
        for e in errors:
            print("  -", e)
        return 1
    print("PASS: Web Surface Gate v0.1 local validation")
    print(f"  pages: {len(ROUTE_FILES)}")
    print(f"  sitemap urls: {len(sitemap_locs)}")
    print("  canonical origin: https://altissports.com/")
    print("  ASR-001 status language present where named")
    print("  no invitation/dispatch/buyer/monetization strings in docs/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
