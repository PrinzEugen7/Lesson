s=%s;
omgn=1.0; zeta=0.5;
G=omgn^2/(s^2+2*zeta*omgn*s+omgn^2);
omg=0:0.01:100;
Gj=horner(G,omg*%i);
x=real(Gj); y=imag(Gj);
clf();plot2d(x,y,axesflag=5,rect=[-0.5,-1.2,1.2,0.1]);
