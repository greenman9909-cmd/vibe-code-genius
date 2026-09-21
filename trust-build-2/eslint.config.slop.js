/**
 * ESLint Shareable Config for Design Slop Detection
 * Reference: references/signs-of-ai-design.md
 */

module.exports = {
  rules: {
    "no-purple-gradients": {
      create(context) {
        return {
          JSXAttribute(node) {
            if (node.name.name === "className" && typeof node.value?.value === "string") {
              const val = node.value.value;
              if (/\b(bg-gradient|from-|via-|to-)\b/.test(val)) {
                context.report({
                  node,
                  message: "Banned Tailwind gradient utility detected. See references/signs-of-ai-design.md (C015, C016).",
                });
              }
            }
          },
        };
      },
    },
    "no-gradient-text": {
      create(context) {
        return {
          JSXAttribute(node) {
            if (node.name.name === "className" && typeof node.value?.value === "string") {
              const val = node.value.value;
              if (val.includes("text-transparent") && val.includes("bg-clip-text")) {
                context.report({
                  node,
                  message: "Banned gradient text ('text-transparent' + 'bg-clip-text'). See references/signs-of-ai-design.md (C001, C018, C040).",
                });
              }
            }
          },
        };
      },
    },
    "no-arbitrary-colors": {
      create(context) {
        return {
          JSXAttribute(node) {
            if (node.name.name === "className" && typeof node.value?.value === "string") {
              const val = node.value.value;
              if (/\b(bg|text|border)-\[#[0-9a-fA-F]{3,8}\]/.test(val)) {
                context.report({
                  node,
                  message: "Banned arbitrary color utility ('bg-[#...]'). Use design tokens. See references/signs-of-ai-design.md (C012).",
                });
              }
            }
          },
        };
      },
    },
    "no-emoji-in-jsx-text": {
      create(context) {
        const emojiRegex = /[\u{1F300}-\u{1F6FF}\u{1F900}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/u;
        return {
          JSXText(node) {
            if (emojiRegex.test(node.value)) {
              context.report({
                node,
                message: "Banned emoji characters in JSX text. Use semantic SVG icons instead. See references/signs-of-ai-design.md (C044).",
              });
            }
          },
        };
      },
    },
    "no-arbitrary-border-radius": {
      create(context) {
        return {
          JSXAttribute(node) {
            if (node.name.name === "className" && typeof node.value?.value === "string") {
              const val = node.value.value;
              if (/\brounded-\[[^\]]+\]/.test(val)) {
                context.report({
                  node,
                  message: "Banned border-radius value outside the token scale. Use defined radii (sm, md, lg, full). See references/signs-of-ai-design.md (L020).",
                });
              }
            }
          },
        };
      },
    },
  },
};
