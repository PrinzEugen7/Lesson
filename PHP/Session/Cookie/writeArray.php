<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Test</title>

<?php

// クッキー書き込み
setcookie ("fubuki[1]", "吹雪");
setcookie ("fubuki[2]", "白雪");
setcookie ("fubuki[3]", "初雪");

// クッキー読み込み・表示
if (isset($_COOKIE["fubuki"]))
{
  $array = $_COOKIE["fubuki"];
  print"$array[1]<br>";
  print"$array[2]<br>";
  print"$array[3]";
}
else { }

?>
</head>
  
<body>

</body>
</html>
