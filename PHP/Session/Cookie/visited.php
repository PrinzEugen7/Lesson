<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Test</title>

<?php
    // クッキー"visited"がある場合
    if (isset($_COOKIE["visited"]))
	{    // 訪問回数を+1
        $count = $_COOKIE["visited"] + 1;
    }else  // クッキー"visited"がない場合(最初の訪問なので1)
	{
        $count = 1;
    }
    print"訪問回数：$count";
    $flag = setcookie("visited", $count);
?>
</head>
  
<body>

</body>
</html>
