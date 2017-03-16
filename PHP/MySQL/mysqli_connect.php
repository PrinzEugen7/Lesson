<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Test</title>

<?php

$flag = mysqli_connect('localhost', 'root', 'password');
// 接続失敗した場合
if (!$flag) {
    die('DBに接続失敗。'.mysqli_error());
}

// 接続成功した場合
print "DBに接続成功";

?>
</head>
  
<body>
</body>
</html>
