<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Test</title>

<?php

// DB接続
$db = new mysqli('localhost', 'root', 'password', 'sarvant');

if (!$db) {
    print "DB接続失敗<br>";
}

print "DB接続成功<br>";

// データ更新
$cmd = 'UPDATE artoria SET name = "nero bride" where name = "nero claudius";';
$result1 = mysqli_query($db, $cmd);
if (!$result1) {
    print("データ更新に失敗<br>".mysqli_error($db));
}

// データ取得
$cmd = 'SELECT name FROM artoria';
$result2 = mysqli_query($db, $cmd);
if (!$result2) {
    print("データ取得に失敗<br>");
}

// 取得した値を表示 
while ($row = mysqli_fetch_assoc($result2)) {
    print($row['name'].'<br>');
}

// DB切断
$closed_flag = mysqli_close($db);

if (!$closed_flag){
    print "DB切断失敗<br>";
}

print "DB切断成功<br>";

?>
</head>
  
<body>
</body>
</html>
