// クラスの定義
var Kanmusu = function(name, type)
{
    // メンバ変数(インスタンス変数)
    this.name = "艦名";
    this.type = "艦種";
}

function main()
{
    // インスタンスの生成
    var fubuki = new Kanmusu();
    // インスタンス変数の値を取得
    var shipName = fubuki.name;
    // 結果表示
    alert(shipName);
}
