//‚QŽŸ’x‚ê—v‘f‚ÌƒXƒeƒbƒv‰ž“š
function [sys]=secondsys(zeta)
s=%s; omg=1;
G=omg^2/(s^2+2*zeta*omg*s+omg^2);
sys=syslin('c',G);
endfunction
//
t=0:0.1:10;
y1=csim('step',t,secondsys(0.4));
y2=csim('step',t,secondsys(0.6));
y3=csim('step',t,secondsys(0.8));
y4=csim('step',t,secondsys(1.0));
y5=csim('step',t,secondsys(1.2));
plot2d(t',[y1',y2',y3',y4',y5'])

