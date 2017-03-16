<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Test</title>

<?php

// DB接続
$id = new mysqli('localhost', 'root', 'password', 'sarvant');

if (!$id) {
    print "DB接続失敗<br>";
}

print "DB接続成功<br>";

// DB切断
$closed_flag = mysqli_close($id);

if (!$closed_flag){
    print "DB切断失敗<br>";
}

print "DB切断成功<br>";

?>
</head>
  
<body>
</body>
</html>
