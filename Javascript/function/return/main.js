// ユーザ関数を宣言・定義
function func(x1, x2)
{
  
    var x3 = 0;
  
    x3 = x1 * x2;
 
    return x3;  // 変数xを戻り値に設定(呼び出し側へ送る)
}

function main()
{    // 変数の宣言・初期化
    var x = 10, y = 10, z = 0;
  
    z = func(x, y);  // ユーザ関数を実行(戻り値x3の値を変数zへ代入)
  
    alert("z=" + z);
}
