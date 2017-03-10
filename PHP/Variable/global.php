<?php

function myFunc(){
     global $msg;
     $msg = "約束された勝利の剣";
}

myFunc();
print $msg;
    
?>
