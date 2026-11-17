/* AltisSports — public evidence exercise pilot.
   No analytics, network calls, storage, scoring, or automated submission.
   A future exercise must be explicitly enabled in QUESTION_SETS before it appears. */
(function () {
  "use strict";

  const QUESTION_SETS = Object.freeze({
    "as3-ar001": {
      id: "as3-ar001",
      caseId: "AR-001",
      title: "Challenge the Evidence — WT Virtual Taekwondo",
      framework: "AS³ — provisional inspection architecture",
      object: "World Taekwondo-governed Virtual Taekwondo contest configuration, WT Rules v4.0 (11 April 2026), co-located multi-station Field of Play, official WT technology-provider stack",
      frozenAt: "2026-08-27",
      caseUrl: "https://altissports.com/applied/ar-001/",
      evidenceUrl: "https://github.com/Sohadot/AltisSports/blob/main/research/applied-reference/AR-001_AS3_EVIDENCE_MATRIX.md",
      questions: [
        {
          id: "arena-boundary",
          layers: "AS³ / L3",
          category: "Arena evidence boundary",
          question: "Does a shared Game Room establish geographically distributed synchronous competition?",
          context: "AR-001 documents a co-located contest. Connected devices and a shared match state do not by themselves establish geographically separated opponents. Assess what the cited material can support.",
          options: [
            { value: "supported", label: "Yes — supported by the cited evidence" },
            { value: "not_evidenced", label: "No — not evidenced by the cited material" },
            { value: "undetermined", label: "Cannot determine from these sources" },
            { value: "challenge", label: "I challenge the framing of this question" }
          ]
        },
        {
          id: "rule-implementation",
          layers: "AS³ / L4 · L7",
          category: "Rule / implementation seam",
          question: "Which missing evidence would best connect written rules to the behavior of a particular contest?",
          context: "WT Rules v4.0 and provider documentation for VTKD v1.3.0 are distinct artifacts. A public event-to-software-build mapping has not been established for AR-001.",
          options: [
            { value: "version-crosswalk", label: "A clause-to-software behavior crosswalk" },
            { value: "deployment-lock", label: "A verified event configuration and build record" },
            { value: "adjudication-trace", label: "An inspectable decision and override trace" },
            { value: "other", label: "A different piece of evidence (describe below)" },
            { value: "undetermined", label: "Cannot prioritize from these sources" }
          ]
        },
        {
          id: "measurement-comparability",
          layers: "AS³ / L5 · L6",
          category: "Measurement / comparability seam",
          question: "What evidence would most help inspect measurement comparability across the contest stations?",
          context: "Wearable tracking is documented; public evidence is narrower on calibration, comparable measurement conditions, and how sensor data become contest outcomes.",
          options: [
            { value: "calibration", label: "Station-specific calibration conditions" },
            { value: "repeatability", label: "Cross-device repeatability and uncertainty results" },
            { value: "scoring-trace", label: "A trace from sensor observations to scoring decisions" },
            { value: "other", label: "A different validation condition (describe below)" },
            { value: "undetermined", label: "Cannot prioritize from these sources" }
          ]
        }
      ]
    }
  });

  function createEmptyResponses(exercise) {
    return exercise.questions.map((item) => ({ questionId: item.id, choice: "", note: "" }));
  }

  function choiceLabel(question, value) {
    const match = question.options.find((choice) => choice.value === value);
    return match ? match.label : "Not selected";
  }

  function makeReport(exercise, responses) {
    return {
      kind: "exploratory_public_evidence_observation",
      exerciseId: exercise.id,
      caseId: exercise.caseId,
      caseBoundary: exercise.object,
      caseFrozenAt: exercise.frozenAt,
      framework: exercise.framework,
      sources: [exercise.caseUrl, exercise.evidenceUrl],
      status: "personal observations only — not a formal review or assessment by AltisSports",
      observations: exercise.questions.map((question, index) => ({
        questionId: question.id,
        as3Layers: question.layers,
        prompt: question.question,
        choice: responses[index]?.choice || "",
        choiceLabel: choiceLabel(question, responses[index]?.choice || ""),
        note: String(responses[index]?.note || "").trim().slice(0, 2000)
      }))
    };
  }

  function reportAsText(report) {
    const lines = [
      "ALTISSPORTS / CHALLENGE THE EVIDENCE",
      "Public exploratory evidence observations — no grade, certification, or formal review",
      "Case: " + report.caseId,
      "Object: " + report.caseBoundary,
      "Object lock: " + report.caseFrozenAt,
      "Framework: " + report.framework,
      "Case source: " + report.sources[0],
      "Evidence matrix: " + report.sources[1],
      ""
    ];
    for (const [index, observation] of report.observations.entries()) {
      lines.push((index + 1) + ". " + observation.as3Layers + " — " + observation.prompt);
      lines.push("Assessment: " + observation.choiceLabel);
      lines.push("Evidence / condition: " + (observation.note || "Not provided"));
      lines.push("");
    }
    lines.push("Scope: Personal observations. No automated submission, endorsement, or sport-recognition conclusion.");
    return lines.join("\n");
  }

  function boot() {
    const root = document.getElementById("challenge-root");
    if (!root) return;
    const exercise = QUESTION_SETS["as3-ar001"];
    const responses = createEmptyResponses(exercise);
    const stageIds = ["stage-case", "stage-inspect", "stage-reflect"];
    let stage = 0;
    let questionIndex = 0;
    const byId = (id) => document.getElementById(id);
    const steps = Array.from(byId("challenge-steps").querySelectorAll("li"));
    const optionsRoot = byId("question-options");
    const noteField = byId("question-note");

    function setStage(next) {
      stage = next;
      stageIds.forEach((id, index) => { byId(id).hidden = index !== next; });
      steps.forEach((step, index) => {
        step.classList.toggle("current", index === next);
        step.classList.toggle("completed", index < next);
        if (index === next) step.setAttribute("aria-current", "step");
        else step.removeAttribute("aria-current");
      });
      if (next === 1) {
        renderQuestion();
      } else if (next === 2) {
        renderReflection();
        byId("reflect-heading").setAttribute("tabindex", "-1");
        byId("reflect-heading").focus({ preventScroll: true });
      } else {
        byId("case-heading").setAttribute("tabindex", "-1");
        byId("case-heading").focus({ preventScroll: true });
      }
      root.scrollIntoView({ behavior: "instant", block: "start" });
    }

    function renderObservation() {
      const question = exercise.questions[questionIndex];
      const response = responses[questionIndex];
      byId("live-assessment").textContent = choiceLabel(question, response.choice);
      byId("live-note").textContent = response.note.trim() || "No note yet.";
    }

    function renderQuestion() {
      const question = exercise.questions[questionIndex];
      const response = responses[questionIndex];
      byId("question-layer").textContent = question.layers;
      byId("question-type").textContent = question.category;
      byId("question-title").textContent = question.question;
      byId("question-context").textContent = question.context;
      byId("prompt-counter").textContent = "Prompt " + String(questionIndex + 1).padStart(2, "0") + " / " + String(exercise.questions.length).padStart(2, "0");
      byId("question-next").firstChild.textContent = questionIndex === exercise.questions.length - 1 ? "Review observations " : "Next prompt ";
      byId("question-alert").hidden = true;
      optionsRoot.replaceChildren();

      for (const option of question.options) {
        const label = document.createElement("label");
        label.className = "choice";
        const input = document.createElement("input");
        input.type = "radio";
        input.name = "question-choice";
        input.value = option.value;
        input.checked = response.choice === option.value;
        input.addEventListener("change", () => {
          response.choice = option.value;
          byId("question-alert").hidden = true;
          renderObservation();
        });
        label.append(input, document.createTextNode(option.label));
        optionsRoot.append(label);
      }

      noteField.value = response.note;
      renderObservation();
      byId("question-title").focus({ preventScroll: true });
    }

    function renderReflection() {
      const list = byId("reflection-list");
      list.replaceChildren();
      exercise.questions.forEach((question, index) => {
        const response = responses[index];
        const li = document.createElement("li");
        const layer = document.createElement("span");
        layer.className = "reflection-index";
        layer.textContent = "0" + (index + 1) + " / " + question.layers;
        const h3 = document.createElement("h3");
        h3.textContent = question.question;
        const choice = document.createElement("p");
        const strong = document.createElement("strong");
        strong.textContent = "Your assessment: ";
        choice.append(strong, document.createTextNode(choiceLabel(question, response.choice)));
        const note = document.createElement("p");
        note.className = "reflection-note";
        note.textContent = "Evidence / condition: " + (response.note.trim() || "Not provided");
        li.append(layer, h3, choice, note);
        list.append(li);
      });
      byId("export-status").textContent = "";
      byId("manual-copy").hidden = true;
    }

    function currentReport() { return makeReport(exercise, responses); }
    byId("begin-challenge").addEventListener("click", () => setStage(1));
    byId("question-back").addEventListener("click", () => {
      if (questionIndex === 0) setStage(0);
      else { questionIndex--; renderQuestion(); }
    });
    byId("question-next").addEventListener("click", () => {
      if (!responses[questionIndex].choice) {
        byId("question-alert").hidden = false;
        optionsRoot.querySelector("input")?.focus();
        return;
      }
      if (questionIndex < exercise.questions.length - 1) { questionIndex++; renderQuestion(); }
      else setStage(2);
    });
    noteField.addEventListener("input", () => {
      responses[questionIndex].note = noteField.value.slice(0, 2000);
      renderObservation();
    });
    byId("reflect-back").addEventListener("click", () => { questionIndex = exercise.questions.length - 1; setStage(1); });
    byId("restart-challenge").addEventListener("click", () => {
      responses.forEach((response) => { response.choice = ""; response.note = ""; });
      questionIndex = 0;
      setStage(0);
    });
    byId("copy-record").addEventListener("click", async () => {
      const summary = reportAsText(currentReport());
      try {
        if (!navigator.clipboard?.writeText) throw new Error("Clipboard not available");
        await navigator.clipboard.writeText(summary);
        byId("export-status").textContent = "Summary copied. It has not been submitted.";
        byId("manual-copy").hidden = true;
      } catch (_error) {
        const box = byId("manual-record");
        box.value = summary;
        byId("manual-copy").hidden = false;
        box.select();
        byId("export-status").textContent = "Clipboard access is unavailable here. Select and copy the record below.";
      }
    });
    byId("download-record").addEventListener("click", () => {
      const content = JSON.stringify(currentReport(), null, 2) + "\n";
      const blob = new Blob([content], { type: "application/json;charset=utf-8" });
      const url = URL.createObjectURL(blob);
      const anchor = document.createElement("a");
      anchor.href = url;
      anchor.download = "altissports-ar-001-evidence-observations.json";
      document.body.append(anchor);
      anchor.click();
      anchor.remove();
      setTimeout(() => URL.revokeObjectURL(url), 1000);
      byId("export-status").textContent = "JSON prepared for download on your device. Nothing was submitted.";
    });
  }

  if (typeof document !== "undefined") {
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot, { once: true });
    else boot();
  }
  if (typeof module !== "undefined" && module.exports) {
    module.exports = { QUESTION_SETS, createEmptyResponses, choiceLabel, makeReport, reportAsText };
  }
}());
