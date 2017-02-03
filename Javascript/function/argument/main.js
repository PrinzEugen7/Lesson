// ユーザ関数を宣言・定義
function func(x1, x2)
{
    x1 = x1 * 10;
    x2 = x2 * 10;
  
    alert("x1=" + x1 +", x2=" + x2);
}

function main()
{
    // 変数の宣言・初期化
    var x = 10, y = 10;
	// ユーザ関数を実行
    func(x, y); 
	// x, yの中身を表示
    alert("x=" + x + ", y=" + y);
}
