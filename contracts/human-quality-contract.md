# Human Quality Contract

The product should read, look, and behave like a deliberate piece of engineering made for its actual users—not like a generic template produced to satisfy a checklist.

## Product language

- Use the vocabulary of the product, domain, and user request. Prefer concrete nouns and verbs over marketing filler.
- Do not manufacture proof, metrics, testimonials, urgency, social proof, or precision.
- Avoid repetitive AI cadences: stacked slogans, rule-of-three filler, fake contrast statements, repeated section kickers, and generic words such as "seamless", "powerful", "revolutionary", or "next-generation" unless the evidence genuinely requires them.
- Error, empty, loading, success, and confirmation copy must tell the user what happened and what they can do next.
- If existing/reference copy is intentionally preserved, record that rather than "cleaning" it into a new voice.

## Interface judgment

- Do not ban a visual pattern solely because an AI detector dislikes it. Judge patterns against the product category, reference evidence, brand system, accessibility, and task.
- Avoid default generated-UI composition: identical card grids, every region inside a rounded container, decorative gradients/glows, gratuitous badges, centered marketing heroes, random glass, and motion without information value.
- A component exists because the product has a repeated interaction/state—not because abstraction looks tidy.
- New surfaces must inherit the approved hierarchy, density, typography, spacing, responsive behavior, and motion language.
- Preserve visible focus, semantic structure, readable contrast, keyboard operation, reduced-motion behavior, and meaningful labels.

## Engineering judgment

- Prefer the smallest clear solution that satisfies the contract. Do not introduce factories, managers, adapters, services, hooks, stores, providers, or configuration layers without a concrete repeated need.
- Name code after domain concepts and observable behavior. Avoid generic names such as dataManager, helper2, commonUtil, magicService, or processThing.
- Prefer native HTML/CSS/browser primitives when they meet the project's Baseline/browser target and accessibility requirements; use JavaScript/framework abstractions when they add real product value.
- Do not replace stable working framework conventions merely to use a newer API.
- Treat performance as measured behavior: inspect loading, responsiveness, unnecessary JavaScript, duplicated work, image/font behavior, and long tasks instead of adding speculative micro-optimizations.
- Every network path needs loading, empty, error, cancellation/retry behavior appropriate to the product.

## Evidence discipline

- Blog posts, videos, courses, community repos, and conference talks are research inputs, not automatic rules.
- Record publication date, author/source, and whether a transcript/caption/code sample was actually available.
- Cross-check behavior-changing guidance against current primary documentation, standards, source code, or reproducible tests before promotion.
- One source may justify a walkthrough note. Repeated verified evidence may justify a reference or validator. Contract changes require tests.

## Completion

The final ship gate must reject technically passing output that is still obviously generic, contradictory, placeholder-heavy, confusing, inaccessible, or inconsistent with the declared product/reference. "Humanized" does not mean decorative polish; it means specific decisions, coherent behavior, honest copy, and observable quality.
