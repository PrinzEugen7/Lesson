<?php

// クラス定義
class Fubuki{
  // メンバ変数(インスタンス変数)
  public $name = "艦名";
  public $arm1 = "装備1";
  public $arm2 = "装備2";
}

// インスタンス生成
$fubuki = new Fubuki();

// インスタンス変数に値を代入
$fubuki->name = "吹雪";
$fubuki->arm1 = "12.7cm連装砲";
$fubuki->arm2 = "61cm三連装魚雷";

// 表示
print"$fubuki->name\n";
print"$fubuki->arm1\n";
print"$fubuki->arm2";
