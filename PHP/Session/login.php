<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Test</title>

<?php

// ユーザ名・パスワード
$user = 'fubuki';
$pass = 'kongo';

// Authorizationヘッダが無い場合
if (!isset($_SERVER['PHP_AUTH_USER'])){
    // ログイン画面を表示
    header('WWW-Authenticate: Basic realm="Private Page"');
    header('HTTP/1.0 401 Unauthorized');
　　　　// 「キャンセル」ボタンが押された場合
    die('ページを閲覧するにはログインしてください');
}else{
    // ログイン画面で「OK」ボタンが押された場合、ユーザ名とパスをチェック
    if ($_SERVER['PHP_AUTH_USER'] != $user || $_SERVER['PHP_AUTH_PW'] != $pass){
        header('WWW-Authenticate: Basic realm="Private Page"');
        header('HTTP/1.0 401 Unauthorized');
	// ユーザ名とパスが間違っている場合
        die('ユーザ名かパスが間違っています');
    }
　　　　// ユーザ名とパスが合っていた場合
    die(' ログインに成功しました。');
}

?>
</head>
  
<body>

</body>
</html>
