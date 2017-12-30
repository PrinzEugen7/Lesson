//最適フィードバックゲイン
A=[0 1;0 -1]; b=[0;1]; 
r=1; Q=diag([4 1]); C=[sqrtm(Q);[0 0]]; d=[0;0;sqrt(r)]; 
k=lqr(syslin('c',A,b,C,d))
spec(A+b*k)

