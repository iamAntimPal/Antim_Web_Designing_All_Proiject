# HTML Meter Element Guide

The `<meter>` element represents a scalar measurement within a known range (e.g., ratings, disk usage, or test scores). Unlike `<progress>`, it is not for task completion.

---

## Table of Contents
1. [Basic Concepts](#1-basic-concepts)  
2. [Browser Rendering](#2-browser-rendering)  
3. [Advanced Styling](#3-advanced-styling)  
4. [Dynamic Updates](#4-dynamic-updates-with-javascript)  
5. [Accessibility](#5-accessibility)  
6. [Use Cases](#6-use-cases--alternatives)  
7. [Common Pitfalls](#7-common-pitfalls)  
8. [Example](#8-example)

---

### 1. Basic Concepts
| Attribute | Description | Default |
|-----------|-------------|---------|
| `min`     | Minimum value | `0`    |
| `max`     | Maximum value | `1`    |
| `value`   | Current value (required) | `0` |
| `low`     | Lower threshold (≥ `min`) | - |
| `high`    | Upper threshold (≤ `max`) | - |
| `optimum` | Ideal value (affects color) | - |

**Example**:
```html
<meter min="0" max="100" value="75" low="30" high="80" optimum="90"></meter>
```

---

### 2. Browser Rendering
- Browsers show color gradients:
  - 🟢 **Green**: Near `optimum`.
  - 🟡/🔴 **Yellow/Red**: In `low`/`high` ranges.
- **Fallback text** for older browsers:
  ```html
  <meter value="0.7">70%</meter>
  ```

---

### 3. Advanced Styling
Customize with CSS pseudo-elements (browser-specific):

**WebKit (Chrome/Safari)**:
```css
meter::-webkit-meter-bar {
  background: #eee;
  border: 1px solid #ccc;
}

meter::-webkit-meter-optimum-value { background: green; }
meter::-webkit-meter-suboptimum-value { background: orange; }
meter::-webkit-meter-even-less-good-value { background: red; }
```

**Firefox**:
```css
meter {
  -moz-appearance: none;
  background: linear-gradient(to right, green 70%, orange 70%);
}
```

---

### 4. Dynamic Updates with JavaScript
Update values interactively:
```javascript
const meter = document.querySelector('meter');
meter.value = 85; // Set new value
meter.addEventListener('click', () => meter.value = Math.random() * 100);
```

---

### 5. Accessibility
- Native ARIA support (`role="meter"`).
- Use `<label>` for clarity:
  ```html
  <label for="diskUsage">Disk Usage:</label>
  <meter id="diskUsage" value="0.8"></meter>
  ```

---

### 6. Use Cases & Alternatives
- **Use `<meter>` for**: Fixed-range values (e.g., battery level, survey results).
- **Avoid for**: Progress tracking (use `<progress>`).
- **Alternatives**: SVG/Canvas for complex visuals.

---

### 7. Common Pitfalls
⚠️ **Avoid**:
- Mismatched ranges (ensure `min ≤ low ≤ high ≤ max`).
- Missing `value` attribute.
- Overlooking cross-browser styling differences.

---

### 8. Example
```html
<meter 
  min="0" 
  max="100" 
  value="75" 
  low="30" 
  high="80" 
  optimum="90"
  style="--custom-meter-color: blue;"
>
  75% <!-- Fallback text -->
</meter>
```

---

🌟 Master the `<meter>` element to enhance data visualization in your projects!
