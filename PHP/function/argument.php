<?php

// ユーザ関数を宣言・定義
function func($x1, $x2)
{
    $x1 = $x1 * 10;
    $x2 = $x2 * 10;
  
    print "x1=$x1 x2=$x2\n";
}


// 変数の宣言・初期化
$x = 10;
$y = 10;

// ユーザ関数を実行
func($x, $y); 
print "x=$x y=$y";

?>
