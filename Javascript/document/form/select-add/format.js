// selectタグのID取得
var select = document.getElementById(selectタグのID名);
// option要素の宣言
var option = document.createElement('option');
// option要素のvalue属性に値をセット
option.setAttribute('value', 値);
// option要素に値をセット
option.innerHTML = 値;
// 作成したoption要素をselectタグに追加
select.appendChild(option);
