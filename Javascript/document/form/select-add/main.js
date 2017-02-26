function setSelect( idName, elementName, menu )
{
    // 入力ボックスの値を取得
    var id = document.getElementById(idName);

    // メニュー項目のセット
    for ( var i in menu ) 
    {
        var element = document.createElement(elementName);
        element.setAttribute('value', i);
        element.innerHTML = menu[i];
        id.appendChild( element );
    }
}

// 初期化
function init()
{
    // 連想配列
    var menu = {
        'Natsumi' : 'なつみ',
        'Renge'   : 'れんげ',
        'Hotaru'  : 'ほたる',
        'Komari'  : 'こまり'
    };
    // selectの初期化
    setSelect( 'select', 'option', menu );
}

function main()
{
    // 入力ボックスの値を取得
    var str = document.formName.selectName.value;
    // 結果表示
    alert(str);  
}
