<?php

// クラス定義
class Fubuki{
  // メンバ変数(インスタンス変数)
  public $name = "艦名";
  public $arm1 = "装備1";
  public $arm2 = "装備2";
  // コンストラクタ
  function __construct($name, $arm1, $arm2){
    $this->name = $name;
    $this->arm2 = $arm1;
    $this->arm1 = $arm2;
  }
}

// インスタンス生成(1番艦吹雪)
$fubuki = new Fubuki("吹雪", "12.7cm連装砲", "61cm三連装魚雷");

// インスタンス生成(2番艦白雪)
$shirayuki = new Fubuki("吹雪", "12.7cm連装砲", "未装備");

// 表示
print"$fubuki->name\n";
print"$fubuki->arm1\n";
print"$fubuki->arm2\n";
print"$fubuki->arm3";
