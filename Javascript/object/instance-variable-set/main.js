// クラスの定義
var Kanmusu = function(name, type)
{
    // メンバ変数(インスタンス変数)
    this.name = name;
    this.type  = type;
}

function main()
{
    // インスタンスの生成
    var fubuki = new Kanmusu("吹雪", "駆逐艦");
    // 値を取得
    var ship = fubuki.name;
    // 結果表示
    alert(ship);
}
