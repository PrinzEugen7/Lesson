clear,echo off,format short e,clc
global A B D S xi Xt Xbox Tbox i h hit
A = [-3.8 0;-0.1 -3.5]; // 定数行列 //
B = [0;1];
D = [-0.2 0;0.1 -0.2];

setlmis([])
P = lmivar(1,[2 1])
Q = lmivar(1,[2 1])
lmiterm[(1 1 1 1),1,A,'s']
lmiterm[(1 1 1 2),1,1)
lmiterm[(1 1 2 1),1,D)
lmiterm[(1 2 2 2),-1,1)
lmiterm[(-2 1 1 1),1,1)
lmiterm[(-3 1 1 2),1,1)
LMISYS = getlmis
[fmin,xfeas] = feasp(LMISYS)
pause
P = dec2mat(LMISYS,xfeas,P)
Q = dec2mat(LMISYS,xfeas,Q)
R = 1;
S = inv(R)*B'*P

xi = 1;
h = 1; // むだ時間 //

X =[1;0]; // 初期状態 //
Xt =X;
Xt1 =X;

i=0;
hit = 1;
dt = 0.01; // 時間刻み //
t = 0:dt:10; // ０～１０秒までを時間刻み0.０１秒で分割 //

[t1,y1] = ode45('subfile',t,X);

for j = 1:(10/dt+1)
  sigma = S*y1(j,:)'; // 切換関数 //
  if sigma < 0
    v = 1;
  end
  if sigma > 0
    v = -1;
  end
  if sigma == 0
    v = 0;
  end
  if j<=h/dt+1
    u = -inv(C*B)*((C*A*y1(j,:)')+(C*D*Xti)-xi*v); // むだ時間前 //
  else
    u = -inv(C*B)*((C*A*y1(j,:)')+(C*D*y1(j-h/dt,:)')-xi*v);
    // むだ時間経過後 //
  end
  Sigmabox(j,1) = sigma;
  Ubox(j,1) = u;
end
n = 1; // グラフ //
for z = -1:0.1:1;
  p = -inv(C(1,2))*C(1,1)*z;
  Xx(1,n) = z;
  Yy(1,n) = p;
  n = n+1;
end
clf
subplot(221),plot(t1,y1),xgrid(2)
xlabel('Time   [s]')
ylabel('Displacement   [m]')
subplot(222),plot(t1,Ubox),xgrid(2)
xlabel('Time   [s]')
ylabel('Control Input   [N]')
subplot(223),plot(t1,Sigmabox),xgrid(2)
xlabel('Time   [s]')
ylabel('Swiching Function')
subplot(224),plot(y1(:,1),y1(:,2),Xx,Yy,'r:'),xgrid(2)
xlabel('X1   [m]')
ylabel('X2   [m]')