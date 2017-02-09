// クラスの定義
var Kanmusu = function(name, type)
{
    // メンバ変数(インスタンス変数)
    this.name = name;
    this.type  = type;
}

// プロトタイプ内でメソッド定義
Kanmusu.prototype.show = function() {
        alert("艦名：" + this.name + "\n艦種：" + this.type);
}

function main()
{
    // インスタンスの生成
    var fubuki = new Kanmusu("吹雪", "駆逐艦");
    // メソッドを呼び出して実行
    fubuki.show();
}
