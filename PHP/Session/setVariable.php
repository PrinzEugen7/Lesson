<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Test</title>

<?php

// セッション開始
session_start();

// セッション変数「date」が無い場合
if (!isset($_SESSION["date"])) {
  print("セッション変数を作成します");
  $_SESSION["date"] = date('c');
}
?>

</head>
  
<body>

</body>
</html>
