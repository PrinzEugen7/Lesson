// 関数f(x)
var f = function(x){
  return x*x - 4.0;
};

// 導関数f'(x)
var df = function(x){
  return 2.0*x;
};

// ニュートン法
var newtonMethod = function(a, eps){
    var i = 0;
    while(i<1000){
        i++;
        // 漸化式
        ah = a - f(a)/df(a)
        // 収束条件(近似解の変化が十分小さい)を満たせば計算終了
        if (Math.abs(ah - a) < eps) break;
        //　近似解の更新
        a = ah    
    }  
    return a;
    
};


window.onload=function () {
    alert(newtonMethod(1.0, 0.0001)); // 2.0000000929222947
};
