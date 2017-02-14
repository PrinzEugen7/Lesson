var app = {
    initialize: function() {
        this.bindEvents();
    },
    bindEvents: function() {
        document.addEventListener('deviceready', this.onDeviceReady, false);
    },
    onDeviceReady: function() {
        var button = document.getElementById("take_pictures");
        button.addEventListener("click", takePictures);
    }
};

app.initialize();

// 写真撮影ボタンを押した時に呼ばれる
function takePictures(){
    navigator.camera.getPicture(cameraSuccess, cameraError, { quality: 80, destinationType: Camera.DestinationType.DATA_URL });
}
// 写真撮影が成功した時
function cameraSuccess(image){
    var img = document.getElementById("image");
    img.src = "data:image/jpeg;base64," + image;
}
// 失敗した時
function cameraError(message){
    alert("Failed!!: " + message);
}
