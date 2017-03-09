<?php

// 配列を宣言・初期化
$datas = array(100, 51, 22, 65);

asort($datas);

// 配列の中身表示
foreach ($datas as $data) {
    echo "$data \n";
}

?>
