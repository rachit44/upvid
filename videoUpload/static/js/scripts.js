const fileInput = document.getElementById('fileInput');
const previewContainer = document.getElementById('previewContainer');
const previewElement = document.getElementById('previewElement');

fileInput.addEventListener('change', function (event) {
    const file = event.target.files[0];
    if (file && file.type.startsWith('video/')) {
        // If the file is a valid video, generate a URL and set it as the source
        const videoURL = URL.createObjectURL(file);
        previewElement.src = videoURL;
        previewElement.load(); // Reload to reflect the new source

        previewContainer.style.display = 'block';
    } else {
        // If the file is not a video, display an alert and clear the preview
        alert('Unsupported file type! Please upload a valid video.');
        previewElement.src = ''; // Clear the video source
        previewContainer.style.display = 'none'; // Hide the preview container
    }
});

// JavaScript to handle video preview
const videoInput = document.getElementById('videoInput');
const showVideo = document.getElementById('showVideo');

videoInput.addEventListener('change', function (event) {
    const file = event.target.files[0];  // Get the selected file
    if (file) {
        const videoURL = URL.createObjectURL(file);  // Create a blob URL
        showVideo.src = videoURL;  // Set the video source
        showVideo.load();  // Reload the video
    }
});