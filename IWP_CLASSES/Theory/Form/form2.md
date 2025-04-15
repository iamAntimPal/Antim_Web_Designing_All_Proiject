# **HTML Forms**

## **Index**
1. [Form Basics](#1-form-basics)  
2. [Form Elements](#2-form-elements)  
   - 2.1 [Text Input](#21-text-input)  
   - 2.2 [Email/URL/Tel](#22-emailurltel)  
   - 2.3 [Password](#23-password)  
   - 2.4 [Textarea](#24-textarea)  
   - 2.5 [Select Dropdown](#25-select-dropdown)  
   - 2.6 [Checkboxes](#26-checkboxes)  
   - 2.7 [Radio Buttons](#27-radio-buttons)  
   - 2.8 [File Upload](#28-file-upload)  
   - 2.9 [Date/Time Pickers](#29-datetime-pickers)  
   - 2.10 [Color Picker](#210-color-picker)  
   - 2.11 [Range Slider](#211-range-slider)  
   - 2.12 [Buttons](#212-buttons)  
   - 2.13 [Hidden Input](#213-hidden-input)  
   - 2.14 [Datalist](#214-datalist)  
   - 2.15 [Fieldset & Legend](#215-fieldset--legend)  
3. [Form Attributes](#3-form-attributes)  
4. [CSS Styling](#4-css-styling)  
5. [Validation](#5-validation)  
6. [Accessibility](#6-accessibility)  
7. [Example Project](#7-example-project)  

---

## **1. Form Basics**
### **Structure**
```html
<form action="/submit" method="POST" autocomplete="on">
  <!-- Form elements go here -->
  <button type="submit">Submit</button>
</form>
```

**Key Attributes**:
- `action`: URL to submit data to.
- `method`: `GET` (appends data to URL) or `POST` (sends data in request body).
- `autocomplete`: Enable/disable auto-fill (`on`/`off`).
- `novalidate`: Disable browser validation.

---

## **2. Form Elements**
### **2.1 Text Input**
```html
<label for="username">Username:</label>
<input 
  type="text" 
  id="username" 
  name="username" 
  placeholder="Enter username" 
  minlength="3" 
  maxlength="20"
>
```

**Attributes**:
- `placeholder`: Hint text.
- `minlength`/`maxlength`: Length constraints.

---

### **2.2 Email/URL/Tel**
```html
<input type="email" required> <!-- Validates email format -->
<input type="url" placeholder="https://example.com">
<input type="tel" pattern="[0-9]{10}" title="10-digit number">
```

---

### **2.3 Password**
```html
<input 
  type="password" 
  minlength="8" 
  pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"
  title="Must contain 8+ chars, uppercase, lowercase, and number"
>
```

---

### **2.4 Textarea**
```html
<textarea 
  id="bio" 
  name="bio" 
  rows="5" 
  cols="30" 
  maxlength="500"
></textarea>
```

---

### **2.5 Select Dropdown**
```html
<select name="country" multiple size="3">
  <optgroup label="Asia">
    <option value="india">India</option>
    <option value="japan">Japan</option>
  </optgroup>
  <option value="usa">USA</option>
</select>
```

**Attributes**:
- `multiple`: Allow multiple selections.
- `size`: Visible options.

---

### **2.6 Checkboxes**
```html
<label><input type="checkbox" name="skills" value="html"> HTML</label>
<label><input type="checkbox" name="skills" value="css"> CSS</label>
```

---

### **2.7 Radio Buttons**
```html
<label><input type="radio" name="plan" value="basic"> Basic</label>
<label><input type="radio" name="plan" value="pro" checked> Pro</label>
```

---

### **2.8 File Upload**
```html
<input 
  type="file" 
  accept=".jpg,.png" 
  multiple 
  capture="camera"
>
```

**Attributes**:
- `accept`: Allowed file types.
- `multiple`: Select multiple files.
- `capture`: Direct camera access.

---

### **2.9 Date/Time Pickers**
```html
<input type="date" min="2024-01-01" max="2024-12-31">
<input type="time" step="900"> <!-- 15-minute intervals -->
<input type="datetime-local">
<input type="month">
<input type="week">
```

---

### **2.10 Color Picker**
```html
<input type="color" value="#ff0000">
```

---

### **2.11 Range Slider**
```html
<input 
  type="range" 
  min="0" 
  max="100" 
  step="5" 
  value="50"
>
```

---

### **2.12 Buttons**
```html
<button type="submit">Submit</button>
<button type="reset">Clear</button>
<button type="button">Custom Action</button>
```

---

### **2.13 Hidden Input**
```html
<input type="hidden" name="user_id" value="12345">
```

---

### **2.14 Datalist**
```html
<input 
  list="browsers" 
  name="browser"
>
<datalist id="browsers">
  <option value="Chrome">
  <option value="Firefox">
  <option value="Safari">
</datalist>
```

---

### **2.15 Fieldset & Legend**
```html
<fieldset>
  <legend>Subscription Options</legend>
  <label><input type="radio" name="sub"> Monthly</label>
  <label><input type="radio" name="sub"> Yearly</label>
</fieldset>
```

---

## **3. Form Attributes**
| Attribute      | Description                          | Example                     |
|----------------|--------------------------------------|-----------------------------|
| `readonly`     | Prevents modification                | `<input readonly>`          |
| `disabled`     | Disables the element                 | `<input disabled>`          |
| `required`     | Mandatory field                      | `<input required>`          |
| `pattern`      | Regex validation                     | `pattern="[A-Za-z]+"`       |
| `min`/`max`    | Numeric/date range                   | `min="1" max="10"`          |
| `step`         | Input increments                     | `<input type="number" step="0.5">` |

---

## **4. CSS Styling**
### **Custom Checkboxes**
```css
input[type="checkbox"] {
  appearance: none;
  width: 20px;
  height: 20px;
  border: 2px solid #4CAF50;
  border-radius: 4px;
}

input[type="checkbox"]:checked {
  background: url('checkmark.svg') no-repeat center;
}
```

---

### **Responsive Layout**
```css
.form-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

@media (max-width: 600px) {
  .form-container {
    grid-template-columns: 1fr;
  }
}
```

---

## **5. Validation**
### **HTML5 Validation**
```html
<input 
  type="number" 
  min="1" 
  max="5" 
  required 
  oninput="validity.valid||(value='')"
>
```

### **JavaScript Validation**
```javascript
document.querySelector("form").addEventListener("submit", (e) => {
  const password = document.getElementById("password");
  if (password.value.length < 8) {
    e.preventDefault();
    alert("Password must be at least 8 characters");
  }
});
```

---

## **6. Accessibility**

- Use `<label>` with `for` matching `id`.
- Add `aria-describedby` for error messages:

  ```html
  <input 
    type="text" 
    aria-describedby="nameError"
  >
  <span id="nameError" class="error">Invalid name</span>
  ```

---

## **7. Example Project**

```html
<form action="/register" method="POST" class="registration-form">
  <h2>Registration Form</h2>
  
  <div class="form-group">
    <label for="name">Full Name:</label>
    <input 
      type="text" 
      id="name" 
      name="name" 
      required 
      pattern="[A-Za-z ]+"
    >
    <span class="error-message">Letters only</span>
  </div>

  <div class="form-group">
    <label for="email">Email:</label>
    <input 
      type="email" 
      id="email" 
      name="email" 
      required
    >
  </div>

  <div class="form-group">
    <label for="dob">Date of Birth:</label>
    <input 
      type="date" 
      id="dob" 
      name="dob" 
      max="2005-01-01"
    >
  </div>

  <button type="submit">Register</button>
</form>
```

```css
.registration-form {
  max-width: 600px;
  margin: 20px auto;
  padding: 25px;
  background: #f8f9fa;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.form-group {
  margin-bottom: 20px;
}

input[type="text"],
input[type="email"],
input[type="date"] {
  width: 100%;
  padding: 12px;
  border: 2px solid #ced4da;
  border-radius: 6px;
  transition: border-color 0.3s;
}

input:focus {
  border-color: #4CAF50;
  outline: none;
}

.error-message {
  color: #dc3545;
  font-size: 0.9em;
  display: none;
}

input:invalid + .error-message {
  display: block;
}
```
