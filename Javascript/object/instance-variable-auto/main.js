// クラスの定義
var Kanmusu = function()
{
    // メンバ変数(インスタンス変数)
    this.name;
    this.type;
}

function main()
{
    // インスタンスの生成
    var fubuki = new Kanmusu();
    // 代入
    fubuki.name = "吹雪";
    fubuki.type = "駆逐艦";
	// 新たに追加
    fubuki.mainGun = "12.7cm50口径連装砲";
    // 結果表示
    alert(fubuki.mainGun);
}
