function xdot = myfunc4(t,x)
 xdot = zeros(2,1);
 a=0.5;
 xdot(1) = -a*x(1)-sin(x(2));
 xdot(2) = x(1);
endfunction
