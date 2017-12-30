//最適レギュレータ（離散時間系）
A=[0 1;1 0]; b=[0;1]; c=[1 0]; d=0;, x0=[2;1]; 
r=1; Q=diag([1 1]); B=b; R=r; G=B*inv(R)*B';
P=ricc(A,G,Q,'disc'); 
k=-inv(r+b'*P*b)*b'*P*A; Ak=A+b*k
t=0:1:10; v=0*t;
x=ltitr(Ak,b,v,x0);
clf(); plot2d(t',x')
xtitle("Optimal regulator response","time [s]","state variables x1 and x2")

