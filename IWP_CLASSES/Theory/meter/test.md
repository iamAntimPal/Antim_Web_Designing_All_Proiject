

# HTML Meter & Progress Elements: From Basics to Advanced

## 1. Introduction
### What are they?
- **`<meter>`**: Represents a scalar value within a **known range** (e.g., battery level, ratings).
- **`<progress>`**: Shows the **completion status** of a task (e.g., file upload, download).

### Key Differences
| Feature                | `<meter>`                  | `<progress>`               |
|------------------------|----------------------------|----------------------------|
| **Use Case**           | Static value in a range    | Dynamic task progress      |
| **Indeterminate State**| Not supported              | Supported (omit `value`)   |
| **Attributes**         | `min`, `max`, `low`, `high`| `max`, `value`             |

---

## 2. Basic Usage
### Meter Example
```html
<meter min="0" max="100" value="75"></meter>
```

### Progress Example
```html
<!-- Determinate -->
<progress value="50" max="100"></progress>

<!-- Indeterminate -->
<progress max="100"></progress>
```

---

## 3. Attributes Deep Dive
### Meter Attributes
| Attribute | Description                  | Default |
|-----------|------------------------------|---------|
| `min`     | Minimum value                | `0`     |
| `max`     | Maximum value                | `1`     |
| `value`   | Current value (required)     | `0`     |
| `low`     | Lower threshold              | `min`   |
| `high`    | Upper threshold              | `max`   |
| `optimum` | Ideal value (affects styling)| `max`   |

### Progress Attributes
| Attribute | Description                  | Default |
|-----------|------------------------------|---------|
| `max`     | Total task value             | `1`     |
| `value`   | Current progress             | `0`     |

---

## 4. Styling Basics
### Default Browser Styles
Both elements have basic OS/browser-dependent styling. Override with CSS:

```css
/* Base styles */
meter, progress {
  width: 300px;
  height: 25px;
  border: 1px solid #ccc;
  border-radius: 15px;
  background: #f0f0f0;
}
```

---

## 5. Advanced Cross-Browser Styling
### Meter Styling
```css
/* WebKit (Chrome/Safari) */
meter::-webkit-meter-bar {
  background: #f0f0f0;
  border-radius: 15px;
}

meter::-webkit-meter-optimum-value {
  background: linear-gradient(90deg, #4CAF50, #8BC34A);
  border-radius: 15px;
}

/* Firefox */
meter {
  -moz-appearance: none;
  background: linear-gradient(90deg, #4CAF50 75%, #f0f0f0 75%);
}
```

### Progress Styling
```css
/* WebKit (Chrome/Safari) */
progress::-webkit-progress-bar {
  background: #f0f0f0;
  border-radius: 15px;
}

progress::-webkit-progress-value {
  background: linear-gradient(90deg, #2196F3, #03A9F4);
  border-radius: 15px;
}

/* Firefox */
progress {
  -moz-appearance: none;
  background: #f0f0f0;
}

progress::-moz-progress-bar {
  background: linear-gradient(90deg, #2196F3, #03A9F4);
}
```

---

## 6. JavaScript Interactivity
### Dynamic Updates
```javascript
// Update meter value
const meter = document.querySelector('meter');
meter.value = 90;

// Update progress with animation
function animateProgress(progressElement, target) {
  let current = 0;
  const interval = setInterval(() => {
    progressElement.value = current++;
    if (current > target) clearInterval(interval);
  }, 20);
}

animateProgress(document.querySelector('progress'), 100);
```

---

## 7. Accessibility
### Best Practices
1. **Labeling**:
```html
<label for="storage">Storage:</label>
<meter id="storage" value="0.8">80%</meter>
```

2. **ARIA Attributes**:
```html
<meter 
  value="0.7" 
  aria-valuemin="0" 
  aria-valuemax="1" 
  aria-valuenow="0.7"
>
  70%
</meter>
```

3. **Color Contrast**: Ensure styled bars meet WCAG contrast ratios.

---

## 8. Advanced Use Cases
### Meter Example: Battery Indicator
```html
<div class="battery">
  <meter 
    min="0" 
    max="100" 
    low="20" 
    high="80" 
    optimum="100" 
    value="45"
  ></meter>
  <span>45%</span>
</div>

<style>
.battery meter {
  --height: 30px;
  width: 150px;
  border-radius: 5px 5px 0 0;
  transform: rotate(270deg);
  writing-mode: vertical-rl;
}
</style>
```

### Progress Example: File Upload
```html
<progress id="uploadProgress" max="100"></progress>
<button onclick="simulateUpload()">Upload</button>

<script>
function simulateUpload() {
  const progress = document.getElementById('uploadProgress');
  let value = 0;
  const interval = setInterval(() => {
    progress.value = value++;
    if (value > 100) clearInterval(interval);
  }, 50);
}
</script>
```

---

## 9. Common Pitfalls
⚠️ **Avoid These**:
1. **Invalid Ranges**:
```html
<!-- BAD: low > high -->
<meter min="0" max="100" low="60" high="30"></meter>
```

2. **Missing Fallback**:
```html
<!-- BAD: No text fallback -->
<meter value="0.7"></meter>

<!-- GOOD -->
<meter value="0.7">70%</meter>
```

3. **Overlapping Attributes**:
```html
<!-- BAD: max < value -->
<progress max="50" value="60"></progress>
```

---

## 10. Browser Support
| Element    | Chrome | Firefox | Safari | Edge | IE   |
|------------|--------|---------|--------|------|------|
| `<meter>`  | 8+     | 16+     | 5.1+   | 12+  | No   |
| `<progress>`| 8+     | 14+     | 5.1+   | 12+  | 10+  |

**Polyfills**: Use [progress-polyfill](https://github.com/LeaVerou/progress-polyfill) for older browsers.

---

## 11. Final Examples
### Styled Meter with Thresholds
```html
<meter 
  min="0" 
  max="100" 
  low="30" 
  high="70" 
  optimum="90" 
  value="85"
  style="--meter-fill: linear-gradient(90deg, red 30%, yellow 30%, green 70%)"
>
  85%
</meter>
```

### Animated Progress Bar
```html
<progress id="animatedProgress" max="100"></progress>
<button onclick="animateProgress(this.previousElementSibling, 100)">
  Start Task
</button>
