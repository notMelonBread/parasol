const video = document.getElementById("video")
const canvas = document.getElementById("picture")
const shutter = document.getElementById("shutter")

navigator.mediaDevices.getUserMedia({
    video: true,
    audio: false,
}).then(stream => {
    video.srcObject = stream;
    video.play()
}).catch(e => {
    console.log(e)
})


function OnClickVideo() {

    const a = document.createElement('a');
    let canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    let context = canvas.getContext('2d');

    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    a.href = canvas.toDataURL('image/png');
    a.download = 'snapshot.png';
    a.click();

}