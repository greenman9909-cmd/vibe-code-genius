# Animation customization guide

## Profiles

| Profile | Character | Best for | Default intensity |
|---|---|---|---:|
| `instant` | State changes with no decorative travel | Dense admin tools, accessibility-first flows | 0.0 |
| `restrained` | Short, quiet confirmation motion | Research, finance, technical products | 0.7 |
| `precise` | Directional transitions that explain hierarchy | Navigation-heavy applications | 0.8 |
| `energetic` | More visible reveals and gesture feedback | Consumer products and onboarding | 0.9 |
| `editorial` | Slow, intentional entrance rhythm | Storytelling and portfolio surfaces | 0.8 |

## Runtime customization

```ts
type MotionPreferences = {
  profile: 'instant' | 'restrained' | 'precise' | 'energetic' | 'editorial';
  intensity: number; // 0..1
  reduced: 'replace' | 'minimize' | 'off';
};
```

Expose preferences through design tokens or a provider. Never make users hunt for a motion setting, and never override an operating-system reduced-motion preference without an explicit product decision.

## Component recipe

1. Define the semantic state.
2. Assign a motion token.
3. Provide the stable end state first.
4. Animate transform/opacity only where possible.
5. Cancel or reverse on interruption.
6. Test keyboard, touch, reduced motion, slow CPU, and 375px layouts.

## Anti-patterns

Avoid bounce defaults, infinite decorative loops, cursor trails, scroll-jacking, hover zoom on important content, animated focus rings that disappear, and transitions longer than the task requires.
