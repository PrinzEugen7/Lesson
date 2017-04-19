// dx(t)/dt
var dxdt = function(x){
    var c = 0.001;
    var r = 100;
    var e = 10 ;
    return (e-x)/r/c;
};

// オイラー法
var euler = function(x0, t0, tn, n){
    x = x0;
    t = t0;
    h = (tn - t0) /n;
    X = new Array(n);
    // 漸化式を計算
    for(i=0; i<n; i++){
        x += dxdt(x) * h;
        X[i] = x;
        t = t0 + i*h;
    }
    return X;
};


window.onload=function () {
    alert(euler(0, 0, 1, 100)); // x(0)～x(1.0)の値を配列表示
};
