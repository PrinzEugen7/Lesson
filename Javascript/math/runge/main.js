// dx(t)/dt
var dxdt = function(x){
    var c = 0.001;
    var r = 100;
    var e = 10 ;
    return (e-x)/r/c;
};

// ニュートン法
var runge = function(x0, t0, tn, n){
    x = x0;
    t = t0;
    h = (tn - t0) /n;
    X = new Array(n);
    // 漸化式を計算
    for(i=0; i<n; i++){
        X[i] = x;
        d1 = dxdt(x);
        d2 = dxdt(x + d1*h*0.5);
        d3 = dxdt(x + d2*h*0.5);
        d4 = dxdt(x + d3*h);
        x += (d1 + 2 * d2 + 2 * d3 + d4)*(h/6.0); 
    }
    return X;
};


window.onload=function () {
    alert(runge(0, 0, 1, 100));
};
