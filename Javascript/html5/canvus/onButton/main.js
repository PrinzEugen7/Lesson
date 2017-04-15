window.onload = function () {
    cv = document.getElementById('cv');
    ctx = cv.getContext("2d");
    ctx.fillRect(20,30,100,50);
    
    btn = document.getElementById('btn');
    btn.style.position="absolute";
    btn.style.left = 30 + "px";
    btn.style.top = 50 + "px";
    x = 20;
    btn.onclick = function () {
        ctx.clearRect(0,0,300,300);
        ctx.fillRect(x,30,100,50);
        x += 5;
    };
};
