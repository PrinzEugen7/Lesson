<?php

// 配列を宣言・初期化
$ships = array("ku"=>"Fubuki", "se"=>"Yamato", "ko"=>"Akagi");

krsort($ships);

// 配列の中身表示
foreach ($ships as $key => $name) {
    echo "$key:$name\n";
}

?>
