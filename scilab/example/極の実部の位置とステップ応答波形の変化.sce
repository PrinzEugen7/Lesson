//極の実部の位置とステップ応答波形の変化
s=%s;
div=200; pnum=10; time=10;
t=0:time/div:time;
syst=zeros(pnum,div);
//
for k=1:pnum
  p=-0.2*k+3*%i; pc=conj(p);
  D=poly([p,pc],"s"); N=10;
  G=N/D;
  sys=csim('step',t,syslin('c',G));
  for j=1:div+1
    syst(k,j)=sys(j);
  end
end
kk=1:1:pnum;
vp=-0.2*kk+3*%i; vpc=conj(vp);
xset("window",0);clf();
plot2d(real(vp)',[imag(vp)',imag(vpc)'],...
    -2*ones(1,pnum),axesflag=5,rect=[-2.5,-4,0.5,4]);
xset("window",1);clf();
plot3d(t,kk,syst');

