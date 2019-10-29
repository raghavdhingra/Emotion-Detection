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
    document.getElementById("saveCapturedImage").classList.remove("none");
    document.getElementById("upload").classList.add("none");
});

// Attach the video stream to the video element and autoplay.
navigator.mediaDevices.getUserMedia(constraints)
  .then((stream) => {
    player.srcObject = stream;
  });

closeBtn.addEventListener("click",()=>{
    overlay.classList.add("none");
});



// function dataURItoBlob(dataURI) {
//     // convert base64/URLEncoded data component to raw binary data held in a string
//     var byteString;
//     if (dataURI.split(',')[0].indexOf('base64') >= 0)
//         byteString = atob(dataURI.split(',')[1]);
//     else
//         byteString = unescape(dataURI.split(',')[1]);
//     // separate out the mime component
//     var mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];
//     // write the bytes of the string to a typed array
//     var ia = new Uint8Array(byteString.length);
//     for (var i = 0; i < byteString.length; i++) {
//         ia[i] = byteString.charCodeAt(i);
//     }
//     return new Blob([ia], {type:mimeString});
//     }