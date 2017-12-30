//極の回転位置とステップ応答波形の変化
s=%s;
div=200; pnum=5; time=30;
t=0:time/div:time;
syst=zeros(pnum,div); poles=zeros(2,pnum);
//
omg=0.5;
for k=1:pnum
  zeta = 0.2*k;
  N=omg^2; D=s^2+2*zeta*omg*s+omg^2;
  G=N/D;
  poles(:,k)=roots(D);
  sys=csim('step',t,syslin('c',G));
  for j=1:div+1
    syst(k,j)=sys(j);
  end
end
vp=poles(1,:); vpc=poles(2,:);
xset("window",0);clf();
plot2d(real(vp)',[imag(vp)',imag(vpc)'],-2*ones(1,pnum),...
                 axesflag=5,rect=[-1,-0.8,1,0.8]);
xset("window",1);clf(); plot2d(t,syst');

