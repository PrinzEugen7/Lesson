function getDate(day) {
  var date = new Date();
  date.setDate(date.getDate() + day);
  var year  = date.getFullYear();
  var month = date.getMonth() + 1;
  var day   = date.getDate();
  return String(year) + "-" + String(month) + "-" + String(day);
}

// ページロード時に実行
window.onload = function () {
  alert(getDate(7));
};

