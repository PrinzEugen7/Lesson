// prog1e3s (Scilab)
// x...x2, v...x1
clear myfunc4
getf('/home/lab7-d11/デスクトップ/Scilab/myfunc4.sce');
tt=0:0.1:20;
xx=ode([4 ; 0], 0, tt, myfunc4);
xbasc();
plot2d(tt,xx(1,:),1);
plot2d(tt,xx(2,:),2);
pause;
xbasc();
plot2d(xx(2,:),xx(1,:))