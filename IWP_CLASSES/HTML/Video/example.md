## **1. Basic Video Embedding**

This is the simplest way to embed a video using the `<video>` tag.

#### Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Basic Video Example</title>
</head>
<body>
  <h1>Basic Video Embedding</h1>
  <video src="video.mp4" controls width="600"></video>
</body>
</html>
```

#### Explanation

- `src="video.mp4"`: Specifies the path to the video file.
- `controls`: Adds playback controls (play, pause, volume, etc.).
- `width="600"`: Sets the width of the video player.

---

### **2. Supporting Multiple Formats**

To ensure compatibility across browsers, you can provide multiple video sources.

#### Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Multiple Video Formats</title>
</head>
<body>
  <h1>Supporting Multiple Video Formats</h1>
  <video controls width="600">
    <source src="video.mp4" type="video/mp4">
    <source src="video.webm" type="video/webm">
    <source src="video.ogg" type="video/ogg">
    Your browser does not support the video tag.
  </video>
</body>
</html>
```

#### Explanation

- The browser will try to load the first supported format.
- If none of the formats are supported, the fallback text (`Your browser does not support the video tag.`) is displayed.

---

### **3. Adding a Poster Image**

You can display a thumbnail image as a placeholder until the video starts playing.

#### Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Video with Poster</title>
</head>
<body>
  <h1>Video with Poster Image</h1>
  <video controls poster="thumbnail.jpg" width="600">
    <source src="video.mp4" type="video/mp4">
  </video>
</body>
</html>
```

#### Explanation

- `poster="thumbnail.jpg"`: Displays the specified image as a placeholder before the video starts playing.

---

### **4. Autoplay and Looping**

You can make the video autoplay and loop continuously.

#### Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Autoplay and Loop</title>
</head>
<body>
  <h1>Autoplay and Loop</h1>
  <video autoplay loop muted width="600">
    <source src="video.mp4" type="video/mp4">
  </video>
</body>
</html>
```

#### Explanation

- `autoplay`: Automatically starts playing the video when the page loads.
- `loop`: Loops the video continuously.
- `muted`: Mutes the audio by default (required for autoplay in most browsers).

---

### **5. Adding Subtitles**

You can add subtitles or captions to your video for accessibility.

#### Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Video with Subtitles</title>
</head>
<body>
  <h1>Video with Subtitles</h1>
  <video controls width="600">
    <source src="video.mp4" type="video/mp4">
    <track src="subtitles_en.vtt" kind="subtitles" srclang="en" label="English">
    <track src="subtitles_fr.vtt" kind="subtitles" srclang="fr" label="French">
  </video>
</body>
</html>
```

#### Explanation

- `track`: Adds subtitles or captions.
- `src="subtitles_en.vtt"`: Path to the subtitle file (in `.vtt` format).
- `kind="subtitles"`: Specifies that this track contains subtitles.
- `srclang="en"`: Language of the subtitle (e.g., English).
- `label="English"`: A human-readable name for the subtitle track.

---

### **6. Styling the Video Player**

You can style the video player using CSS.

#### Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Styled Video Player</title>
  <style>
    video {
      border: 5px solid #ccc;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
      width: 100%;
      max-width: 800px;
    }
  </style>
</head>
<body>
  <h1>Styled Video Player</h1>
  <video controls>
    <source src="video.mp4" type="video/mp4">
  </video>
</body>
</html>
```

#### Explanation

- The CSS styles the video player with a border, rounded corners, and a shadow effect.

---

### **7. Controlling the Video with JavaScript**

You can control the video player programmatically using JavaScript.

#### Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Video Controls</title>
</head>
<body>
  <h1>JavaScript Video Controls</h1>
  <video id="myVideo" controls width="600">
    <source src="video.mp4" type="video/mp4">
  </video>
  <br><br>
  <button onclick="playPause()">Play/Pause</button>
  <button onclick="makeBig()">Big</button>
  <button onclick="makeSmall()">Small</button>

  <script>
    var video = document.getElementById("myVideo");

    function playPause() {
      if (video.paused) {
        video.play();
      } else {
        video.pause();
      }
    }

    function makeBig() {
      video.width = 800;
    }

    function makeSmall() {
      video.width = 400;
    }
  </script>
</body>
</html>
```

#### Explanation

- `playPause()`: Toggles between playing and pausing the video.
- `makeBig()` and `makeSmall()`: Dynamically change the video's width.

---

### **8. Complete Example**

Here’s a complete example combining all the features discussed above:

#### Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Complete Video Example</title>
  <style>
    video {
      border: 5px solid #ccc;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
      width: 100%;
      max-width: 800px;
    }
  </style>
</head>
<body>
  <h1>Complete Video Example</h1>
  <video id="myVideo" controls poster="thumbnail.jpg" width="600">
    <source src="video.mp4" type="video/mp4">
    <source src="video.webm" type="video/webm">
    <track src="subtitles_en.vtt" kind="subtitles" srclang="en" label="English">
    Your browser does not support the video tag.
  </video>
  <br><br>
  <button onclick="playPause()">Play/Pause</button>
  <button onclick="makeBig()">Big</button>
  <button onclick="makeSmall()">Small</button>

  <script>
    var video = document.getElementById("myVideo");

    function playPause() {
      if (video.paused) {
        video.play();
      } else {
        video.pause();
      }
    }

    function makeBig() {
      video.width = 800;
    }

    function makeSmall() {
      video.width = 400;
    }
  </script>
</body>
</html>
```

#### Explanation

- `poster="thumbnail.jpg"`: Specifies the path to the thumbnail image to display before the video starts playing.
- `width="600"`: Sets the initial width of the video player.
- `controls`: Adds playback controls (play, pause, volume, etc.).
