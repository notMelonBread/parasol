const video = document.getElementById("video");
const shutter = document.getElementById("shutter");

navigator.mediaDevices.getUserMedia({
    video: true,
    audio: false
}).then(stream => {
    video.srcObject = stream;
    video.play();
}).catch(e => {
    console.log(e);
});

function onClickVideo() {
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    const imageDataURL = canvas.toDataURL('image/png');

    // Ajaxリクエストで写真データを送信
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/upload_photo', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            console.log('写真が送信されました');
        }
    };
    xhr.send(JSON.stringify({ photo: imageDataURL }));
}
