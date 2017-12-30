clear,lines(0),clc
global A B D S xi Xt Xbox Tbox i h hit
A = [1 1 0;0 2 1;0 0 2]; // 定数行列 //
B = [0 0 1]';
D = [1 0 0;0 1 0;0 0 1]

// 部分行列 //
A11 = [1 1;0 2];A12 = [0;1];A21 = [0 0];A22 = 2;
B2 =1;

// 極配置 //
Rp1 = -3; // Real part of eigenvalue ramda1 //
Ip1 = 0; // Imaginary part of eigenvalue ramda1 //
Rp2 = -4; // Real part of eigenvalue ramda2 //
Ip2 = 0; // Imaginary part of eigenvalue ramda2 //
p = [Rp1+Ip1*sqrt(-1) Rp2+Ip2*sqrt(-1)];
K = ppol(A11,A12,p)

// 超平面の設計 //
S2 = eye(1);
disp('Hyperplane vector');
S = S2*[K eye(1)]

xi = 1;
h = 1; // むだ時間 //
X =[1 0.5 0]' // 初期状態 //
Xt =X;
Xt1 =X;
i=0;
hit = 1;
dt = 0.01; // 時間刻み //
t = 0:dt:10 // ０～１０秒までを時間刻み0.０１秒で分割 //

clear subfile
exec('/home/lab7-d11/デスクトップ/Scilab/subfile.sce');
y1 = ode(X,0,t,subfile)

for j = 1:(10/dt+1)
  sigma = S*y1(j,:,:)'; // 切換関数 //
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
