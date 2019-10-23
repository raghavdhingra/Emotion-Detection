//alert();
const player = document.getElementById('player');
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');
const captureButton = document.getElementById('capture');
const closeBtn = document.getElementById("closeBtn");
const overlay = document.getElementById("overlay");

const constraints = {
  video: true,
};

captureButton.addEventListener('click', () => {
  // Draw the video frame to the canvas.
    overlay.classList.remove("none");
    context.drawImage(player, 0, 0, canvas.width, canvas.height);
});

// Attach the video stream to the video element and autoplay.
navigator.mediaDevices.getUserMedia(constraints)
  .then((stream) => {
    player.srcObject = stream;
  });

  closeBtn.addEventListener("click",()=>{
    overlay.classList.add("none");
  });