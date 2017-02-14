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

// 初期化
app.initialize();

// 「撮影ボタン」が押された時の処理
function takePictures(){
    navigator.camera.getPicture(cameraSuccess, cameraError, { quality: 80, destinationType: Camera.DestinationType.DATA_URL });
}
// 撮影成功時の処理
function cameraSuccess(image){
    var img = document.getElementById("image");
    img.src = "data:image/jpeg;base64," + image;
}
// 撮影失敗時の処理
function cameraError(message){
    alert("Failed!!: " + message);
}
