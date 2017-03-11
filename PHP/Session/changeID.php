<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Test</title>

<?php

// セッション開始
session_start();
// セッションIDの変更
session_id('fatego');
// セッションIDの取得
$id = session_id();
// セッション名の表示
print "セッションID：$id";

?>
</head>
  
<body>
</body>
</html>
