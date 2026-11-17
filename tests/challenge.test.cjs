const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const { QUESTION_SETS, createEmptyResponses, choiceLabel, makeReport, reportAsText } = require('../docs/assets/js/challenge.js');

const exercise = QUESTION_SETS['as3-ar001'];
const route = path.join(__dirname, '..', 'docs', 'challenge', 'ar-001', 'index.html');

test('one bounded, enabled public pilot; three independent evidence prompts', () => {
  assert.deepEqual(Object.keys(QUESTION_SETS), ['as3-ar001']);
  assert.equal(exercise.caseId, 'AR-001');
  assert.match(exercise.object, /co-located multi-station Field of Play/);
  assert.equal(exercise.frozenAt, '2026-08-27');
  assert.deepEqual(exercise.questions.map((q) => q.id), [
    'arena-boundary', 'rule-implementation', 'measurement-comparability'
  ]);
  assert.ok(exercise.questions.every((q) => q.options.some((o) => o.value === 'undetermined')));
});

test('unanswered prompts remain unanswered; no default verdict', () => {
  const responses = createEmptyResponses(exercise);
  assert.equal(responses.length, 3);
  assert.ok(responses.every((r) => r.choice === '' && r.note === ''));
  assert.equal(choiceLabel(exercise.questions[0], ''), 'Not selected');
});

test('export keeps evidence context, uncertainty and user-written notes', () => {
  const responses = createEmptyResponses(exercise);
  responses[0].choice = 'challenge';
  responses[0].note = 'A reliable configuration record could change my view.';
  responses[1].choice = 'undetermined';
  responses[2].choice = 'repeatability';
  const report = makeReport(exercise, responses);
  assert.equal(report.kind, 'exploratory_public_evidence_observation');
  assert.equal(report.observations[0].choiceLabel, 'I challenge the framing of this question');
  assert.equal(report.observations[1].choiceLabel, 'Cannot prioritize from these sources');
  assert.equal(report.observations[0].note, responses[0].note);
  assert.match(report.sources[1], /AR-001_AS3_EVIDENCE_MATRIX/);
  assert.equal(Object.hasOwn(report, 'score'), false);
  assert.equal(Object.hasOwn(report, 'identity'), false);
  assert.equal(Object.hasOwn(report, 'certification'), false);
  assert.match(reportAsText(report), /No automated submission/);
});

test('source records do not mutate when exports are modified', () => {
  const responses = createEmptyResponses(exercise);
  responses[0].note = ' x '.repeat(1000);
  const report = makeReport(exercise, responses);
  assert.ok(report.observations[0].note.length <= 2000);
  report.observations[0].note = 'mutated';
  assert.notEqual(responses[0].note, 'mutated');
});

test('public page declares canonical and privacy boundaries without submission form', () => {
  const page = fs.readFileSync(route, 'utf8');
  const script = fs.readFileSync(path.join(__dirname, '..', 'docs', 'assets', 'js', 'challenge.js'), 'utf8');
  assert.match(page, /rel="canonical" href="https:\/\/altissports\.com\/challenge\/ar-001\/"/);
  assert.match(page, /nothing is sent to AltisSports/i);
  assert.match(page, /mailto:agent@sohadot\.com/);
  assert.match(page, /not a formal external review/i);
  assert.doesNotMatch(page, /<form\b/i);
  assert.doesNotMatch(script, /\bfetch\s*\(|\bXMLHttpRequest\b|\blocalStorage\b|\bsessionStorage\b|\bsendBeacon\s*\(/);
});
