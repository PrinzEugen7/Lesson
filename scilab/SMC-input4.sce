lines(0)
// 定数行列 //
AF = [1 1 0;0 2 1;0 0 1];
BF = [0;0;1];
S = [20 10 1];
// むだ時間 //
L = 0.5;
L1 = 0.5;
LL = 500*L;
LL1 = 500*L1;

// 離散化システム //
h = 0.002; // サンプリング時間 //
cont = syslin('c',AF,BF,S);
disc = dscr(cont,h); // 離散化 //
[A,B,Sd] = abcd(disc);

// 初期条件 //
X = [1 2 3]';
zc = [1 2 3]';
zh = [1 2 3]';
K = 10;

//　スライディングモード制御とスミス法 //
for i = 1:2500;
  sigma = S*X; // 切換超平面 //
  sigma1 = S*(-(X-zh)+zc); // スミス法を用いた切換超平面 //
  U(i) = -inv(S*BF)*(S*AF*X)-K*sigma/norm(sigma);
  u(i) = -inv(S*BF)*(S*AF*(-(X-zh)+zc))-K*sigma1/norm(sigma1);
  
  if i<=LL // むだ時間経過前 //
    UL = 0;
  else // むだ時間経過後 //
    UL = U(i-LL);
  end
  if i<=LL1 // むだ時間経過前 //
    UL1 = 0;
  else // むだ時間経過後 //
    UL1 = U(i-LL1);
  end
 
  dX = A*X+B*UL;
  dzc = A*zc+B*u(i);
  dzh = A*zh+B*UL1;

  Xh1(:,i) = X;
  Wh1(:,i) = -(X-zh)+zc;
  Uh1(1,i) = UL;
  Sh1(1,i) = sigma;
  Sh2(1,i) = sigma1;
  
  X = dX;
  zc = dzc;
  zh = dzh;
  
end

// グラフ作成 //
clf()
tt =0:h:(i-1)*h;
xset("window",0);
subplot(222),plot(tt,Uh1),xgrid
title('Control Input')
xlabel('Time   [s]')
ylabel('Control Input   [N]')
subplot(221),plot(tt,Xh1(1,:),tt,Xh1(2,:),tt,Xh1(3,:)),xgrid
title('Parameter')
xlabel('Time   [s]')
ylabel('Displacement   [m]')
subplot(223),plot(tt,Sh1),xgrid
title('Swiching Function')
xlabel('Time   [s]')
ylabel('Swiching Function')
xset("window",1);
subplot(222),plot(tt,Uh1),xgrid
title('Control Input')
xlabel('Time   [s]')
ylabel('Control Input   [N]')
subplot(221),plot(tt,Wh1(1,:),tt,Wh1(2,:),tt,Wh1(3,:)),xgrid
title('Parameter')
xlabel('Time   [s]')
ylabel('Displacement   [m]')
subplot(223),plot(tt,Sh2),xgrid
title('Swiching Function')
xlabel('Time   [s]')
ylabel('Swiching Function')
clear tt Uh1 Xh1 Sh1 Wh1 Sh2;