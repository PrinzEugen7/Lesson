s=%s;
G=1/(1+2*s);
omg=0:0.01:100;
Gj=horner(G,omg*%i);
x=real(Gj); y=imag(Gj);
plot2d(x,y,axesflag=5,rect=[-0.1,-0.6,1.2,0.1]);
