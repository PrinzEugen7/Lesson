<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Test</title>

<?php

$link = mysqli_connect('localhost', 'root', 'password');
// 接続失敗時
if (!$link) {
    print "DB接続失敗<br>";
}

// 接続成功時
print "DB接続成功<br>";

$flag = mysqli_close($link);

// 切断失敗時
if (!$flag){
    print "DB切断失敗<br>";
}

// 切断成功時
print "DB切断成功<br>";

?>
</head>
  
<body>
</body>
</html>
