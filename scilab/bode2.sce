s=poly(0,'s')/2/%pi
G=1/(1+s);
sys=syslin('c',G);
f = logspace(-3,1,100);
w=2*%pi*f
bode(sys,w)
xlabel("角周波数[rad/sec]")

