<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Test</title>

<?php

// セッション開始
session_start();

// セッションIDの確認
// セッションIDがクッキーに無い場合
if (!isset($_COOKIE["PHPSESSID"])) {
  print('セッション開始');
}
// セッションIDがクッキーにある場合
else {
  print('セッションID： '.$_COOKIE["PHPSESSID"]);
}

?>

</head>
  
<body>

</body>
</html>
