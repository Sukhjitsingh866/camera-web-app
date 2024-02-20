<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewpoint" content="width=device-width, initial-scale=1">
        
        <title>Camera Mobile Website</title>

        <link rel="stylesheet" href="style.css">

    </head>
    <body>

        <main id="camera">
            <canvas id="camera-view"></canvas>

            <video id="camera-device" autoplay playsinline></video>
            <img alt="" id="photo-display">
            <button id="front-camera-button">Front Camera</button>
            <button id="take-photo-button">Take Photo</button>
        </main>

        <script src="app.js"></script>
    </body>
</html>