# Autotest UI — project instructions

Python/pytest/Playwright test framework for the separate UI Course Test Application. Start with
the [context index](.aqa-context/INDEX.md) and read the relevant part of PROJECT for source evidence, setup, and known
limitations. Superpowers owns the work process; reusable AQA Skills supply general criteria. This file sets the
conventions specific to this repository.

## Structure and names

- Keep the existing path: **Tests → Pages → Components → Elements → Playwright**. Tests own the scenario, test data and
  expected outcomes. Pages own routes, page-level state and composition. Components own actions and checks scoped to
  their widget or entity. Elements own reusable locators, browser primitives, atomic assertions and their
  logging/Allure/UI Coverage instrumentation.
- Place tests under `tests/<domain>/test_*.py`; follow nearby `Test<Domain>` groupings and registered pytest markers
  in [pyproject.toml](pyproject.toml). Use `test_<behavior>[_when_<condition>]`, names such as `new_course_title` and
  `expected_dashboard_url`, `<Feature>Page` and `<Widget>Component`. Name methods for their effect: `click_<target>`,
  `fill`, `check_<observable>`. Preserve existing interfaces when unrelated to the change.
- Use short English Allure titles for scenario intent and meaningful steps for non-obvious actions. No blanket
  Google-style docstring requirement: a clear test name, title and body normally suffice. Add a docstring for a
  non-obvious fixture/helper contract (scope, precondition, side effect, cleanup); use Google-style sections when useful
  for callers. Do not repeat titles, type hints or obvious fixture names.

## Data, assertions and outcomes

- Use [fixtures/pages.py](fixtures/pages.py) for page setup. Use the fresh `page` path for registration or login under
  test; use `page_with_state` for authenticated prerequisites, when the scenario permits it. Prepare only the starting
  state in fixtures and validate material preconditions. Keep the action under test and the final check visible in the
  test body.
- Use named values for meaningful boundaries, identities and before/after inputs. Small self-explanatory literals are
  fine. Keep file assets in `testdata/`; use settings or an existing fixture for environment-dependent inputs. Add a
  fixture/factory only for repeated setup or independent resource lifecycles. Verify empty/populated state when it is
  required; do not rely on order of test execution.
- Derive expectations from the applicable requirement, input, or controlled starting state. Existing tests and app code
  can explain behavior; they do not supply an undocumented requirement. Match the entity acted on. For create/edit,
  check distinguishing fields of that entity; if the claim is persistence, reopen or reload and locate it again. Check
  cardinality or untouched records when the claim requires it. A loaded toolbar, successful click or generic toast alone
  does not prove a save.
- Locate assertions at the lowest layer that owns their meaning: retrying `expect` in Elements; field/row/widget checks
  in Components; route or page-level invariants in Pages; scenario-specific comparisons and business outcomes in tests.
  Pass expected values in from the test when they depend on its data. Plain `assert` is fine for already collected
  values, not for waiting on the DOM.
- Do not add an assertion package to mirror the API projects. Extract a focused comparison only when multiple tests need
  the same cross-page or domain check and existing components cannot own it cleanly. Keep setup, actions and scenario
  outcomes distinguishable; document intentional readiness checks inside action helpers.

## Locators, timing and isolation

- Reuse existing Element/Component hooks and stable `data-testid` values. Scope repeated IDs inside a uniquely
  identified card or row before interacting; accessible role/name or label is appropriate when it expresses the UI
  contract. Use positional selection only for an explicit ordering assertion or a controlled single-match prerequisite.
  An implicit `.nth(0)` is not evidence of uniqueness.
- Preserve the [Element coverage path](elements/base_element.py) when adding calls or selectors. Verify that runtime and
  coverage selectors represent the same target, including scope, index and nested controls. A direct Playwright call
  outside this path is not tracked automatically; do not add ad hoc tracking in a test. See PROJECT for known XPath
  limitations.
- Use Playwright actionability for the action and web-first assertions for the resulting UI state. If a specific network
  event is part of the scenario, subscribe before the trigger and match it by the relevant method, path or identity;
  then check the visible result. Avoid fixed sleeps, blanket waits and retries or timeout increases without evidence.
- Check context scope, seeded StorageState and any server-side resources separately. For parallel cases that mutate
  shared backing data, use test-owned identities/records and clean up only those resources; if ownership is unavailable,
  establish the scope before running in parallel. A new browser context isolates its browser storage; it cannot roll
  back writes to a shared service. The browser-only course app is documented in PROJECT.
- [Default routing](tools/playwright/mocks.py) skips static assets. Do not assume the preview's image content is loaded
  just because an element is visible. For test-specific routing, scope the mock to the scenario/action and state which
  behavior it replaces. A stubbed response can test UI handling; it cannot verify real service behavior.

## Review and verification

- Review changes against the requirement, prerequisites, action, observable result, target identity and cleanup. Look
  for a plausible defect that would still pass, including wrong-card selection, hidden parallel interference or
  insufficient postconditions. Separate confirmed weaknesses from hypotheses and style suggestions. Cite the test and
  helper lines that demonstrate each actionable issue.
- For instability, inspect the first available failed trace, video, console/log and network evidence; compare browser,
  test/worker and initial data before attributing cause. Check the action and subsequent state separately. Preserve
  existing artifacts and use the current reporting facilities instead of ad hoc prints or attachments.
- Read [checks and artifact effects](.aqa-context/PROJECT.md#checks-and-artifacts) before executing pytest. Even
  collection can initialize directories; UI runs can write data. Do not provision services, change dependencies/CI or
  remove reports as part of routine test work. Logs, Allure metadata, traces, video and auth state can contain sensitive
  data: never copy or publish unreviewed artifacts.
