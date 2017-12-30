clear,lines(0),clc
global A B D S xi Xt v Xbox Tbox i h hit
A = [-3.8 0;-0.1 -3.5]; // 定数行列 //
B = [0;1];
D = [-0.2 0;0.1 -0.2];
P = [12.954 -0.18401;-0.18401 14.09];
Q = [48.151 0.021903;0.021903 48.223];
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
t = 0:dt:10; // ０～１０秒までを時間刻み0.0１秒で分割 //

clear subfile
exec('/home/lab7-d11/デスクトップ/Scilab/subfile.sce');
y1 = ode(X,0,t,subfile)
y1(:,1)

for j = 1:1:100
  sigma = S*y1(:,j); // 切換関数 //
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
    u = -inv(S*B)*((S*A*y1(1,j)')+(S*D*Xt1)-xi*v); // むだ時間前 //
  else
    u = -inv(S*B)*((S*A*y1(1,j)')+(S*D*y1(j-h/dt,j-h/dt)')-xi*v);
    // むだ時間経過後 //
  end
  Sigmabox = sigma;
  Ubox = u;
end
n = 1; // グラフ //
for z = -1:0.1:1;
  p = -inv(S(1,2))*S(1,1)*z;
  Xx(1,n) = z;
  Yy(1,n) = p;
  n = n+1;
end
clf
subplot(221),plot2d(t,y1(1,:)),xgrid(2)
xlabel('Time   [s]')
ylabel('Displacement   [m]')
subplot(222),plot2d(t,Ubox),xgrid(2)
xlabel('Time   [s]')
ylabel('Control Input   [N]')
subplot(223),plot2d(t,Sigmabox),xgrid(2)
xlabel('Time   [s]')
ylabel('Swiching Function')
subplot(224),plot2d(y1(:,1),y1(:,2),Xx,Yy,'r:'),xgrid(2)
xlabel('X1   [m]')
ylabel('X2   [m]')