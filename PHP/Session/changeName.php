<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Test</title>

<?php

// セッション開始
session_start();
// セッション名の変更
session_name("fatego");
// セッション名の取得
$name = session_name();
// セッション名の表示
print "セッション名：$name";

?>
</head>
  
<body>
</body>
</html>
