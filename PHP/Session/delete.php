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
// セッション変数「date」がある場合
else{
  // セッション変数の取得
  $date = $_SESSION["date"];
  print "前回の訪問日時：$date";
  // セッション変数の日時更新 
  $_SESSION["date"] = date('c');
    }
?>

</head>
  
<body>
<a href="logout.php">ログアウト</a>
</body>
</html>
