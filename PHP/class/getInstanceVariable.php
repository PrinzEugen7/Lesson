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
print"$fubuki->name";
