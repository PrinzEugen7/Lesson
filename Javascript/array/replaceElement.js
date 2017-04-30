function replaceElement(array, before, after) {
  for(var i=0; i<array.length; i++){
    array[i] = array[i].replace(before, after);
  }
  return array;
}

// ページロード時に実行
window.onload = function () {
  var data = ["2016-12-12 0:00", "2016-12-12 1:00", "2016-12-12 2:00"];
  var date = "2016-12-12 ";
  var array = replaceElement(data, date, ""); // 0:00, 1:00, 2:00
  alert(array);
};
