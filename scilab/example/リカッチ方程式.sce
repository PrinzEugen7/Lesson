//ƒŠƒJƒbƒ`•û’ö®
A=[0 1;0 -1]; b=[0;1]; 
r=1; Q=diag([4 1]); B= inv(r)*b*b'; 
P=ricc(A,B,Q,'cont'), spec(P)
k=-inv(r)*b'*P
spec(A+b*k)

