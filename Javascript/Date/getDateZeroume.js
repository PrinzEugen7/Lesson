function getDate(day) {
  var date = new Date();
  date.setDate(date.getDate() + day);
  var year  = date.getFullYear();
  // 0埋めして取得
  var month = ("0"+(date.getMonth() + 1)).slice(-2);
  var day   = ("0"+date.getDate()).slice(-2);
  return String(year) + "-" + String(month) + "-" + String(day);
}

// ページロード時に実行
window.onload = function () {
  alert(getDate(0)); // 2017-05-05
};
