function func() {
  // ブロックスコープが使えない
  {
    var message = 'にゃんぱすー';
  }
  
  alert(message);
}
