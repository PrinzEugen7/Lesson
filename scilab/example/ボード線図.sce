s=%s;
G=1/(1+2*s);
sys=syslin("c",G);
clf();bode(sys,1e-2,1e1,0.01)
