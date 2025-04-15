
# HTML Meter & Progress Elements Guide

Learn to use `<meter>` for scalar measurements and `<progress>` for task completion.

---

## Table of Contents
1. [Meter vs. Progress](#1-meter-vs-progress)  
2. [Meter Element](#2-meter-element)  
3. [Progress Element](#3-progress-element)  
4. [Styling Meter](#4-styling-meter)  
5. [Styling Progress](#5-styling-progress)  
6. [Dynamic Updates](#6-dynamic-updates)  
7. [Accessibility](#7-accessibility)  
8. [Examples](#8-examples)  

---

### 1. Meter vs. Progress
| Feature          | `<meter>`                     | `<progress>`                |
|------------------|-------------------------------|-----------------------------|
| **Use Case**     | Known range values (e.g., ratings) | Task completion (e.g., downloads) |
| **Attributes**   | `min`, `max`, `low`, `high`   | `max`, `value`              |
| **Indeterminate**| Not supported                 | Supported (omit `value`)    |

---

### 2. Meter Element
```html
<meter 
  min="0" 
  max="100" 
  value="75" 
  low="30" 
  high="80" 
  optimum="90"
>
  75% <!-- Fallback text -->
</meter>
```

**Key Attributes**:
- `min`/`max`: Define range
- `value`: Current value (required)
- `low`/`high`: Thresholds for color coding
- `optimum`: Ideal value

---

### 3. Progress Element
```html
<!-- Determinate -->
<progress value="70" max="100"></progress>

<!-- Indeterminate -->
<progress max="100"></progress>
```

**Key Attributes**:
- `value`: Current progress (omit for indeterminate)
- `max`: Total value

---

### 4. Styling Meter
Custom CSS for modern browsers:

```css
/* Base style */
meter {
  width: 200px;
  height: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background: #f0f0f0;
}

/* WebKit (Chrome/Safari) */
meter::-webkit-meter-bar {
  background: #f0f0f0;
  border-radius: 10px;
}

meter::-webkit-meter-optimum-value {
  background: linear-gradient(to right, #4CAF50, #8BC34A);
  border-radius: 10px;
}

/* Firefox */
meter {
  -moz-appearance: none;
  background: linear-gradient(to right, #4CAF50 75%, #f0f0f0 75%);
}
```

---

### 5. Styling Progress
Cross-browser progress styling:

```css
/* Base style */
progress {
  width: 200px;
  height: 20px;
  border: none;
  border-radius: 10px;
  background: #f0f0f0;
}

/* WebKit (Chrome/Safari) */
progress::-webkit-progress-bar {
  background: #f0f0f0;
  border-radius: 10px;
}

progress::-webkit-progress-value {
  background: linear-gradient(to right, #2196F3, #03A9F4);
  border-radius: 10px;
}

/* Firefox */
progress {
  -moz-appearance: none;
  background: #f0f0f0;
}

progress::-moz-progress-bar {
  background: linear-gradient(to right, #2196F3, #03A9F4);
  border-radius: 10px;
}
```

---

### 6. Dynamic Updates
```javascript
// Update meter
const meter = document.querySelector('meter');
meter.value = 85;

// Update progress
const progress = document.querySelector('progress');
progress.value = 50;

// Animated progress
function animateProgress(element, target) {
  let current = 0;
  const timer = setInterval(() => {
    element.value = current++;
    if (current > target) clearInterval(timer);
  }, 20);
}
```

---

### 7. Accessibility
- Use `<label>` associations
- Provide fallback text for older browsers
- Ensure color contrast meets WCAG standards

---

### 8. Examples
**Meter with Custom Colors**:
```html
<meter 
  min="0" 
  max="100" 
  value="45" 
  style="--meter-bg: #ffeb3b; --meter-fill: #ff9800"
>
  45%
</meter>
```

**Animated Progress Bar**:
```html
<progress id="animatedProgress" max="100"></progress>
<button onclick="animateProgress(this.previousElementSibling, 100)">
  Start Download
</button>
```

---

🌟 Use these elements to create meaningful data visualizations while maintaining accessibility and performance!
```

This version includes:
- Clear comparison between `<meter>` and `<progress>`
- Dedicated styling sections for both elements
- Cross-browser CSS solutions
- Dynamic JavaScript examples
- Accessibility considerations
- Ready-to-use code snippets

The structure uses:
- Comparison tables for quick reference
- Color-coded examples
- Progressive enhancement patterns
- Modern CSS techniques (gradients, animations)
- Clear separation of concepts