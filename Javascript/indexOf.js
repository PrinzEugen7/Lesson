// ページロード時に実行
window.onload = function () {
  var str = "2016-12-12 0:00",
  target = "2016-12-12";

  if (str.indexOf(target) !== -1) {
    alert("前方一致");
  }
};
