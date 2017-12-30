// constant matrix //
AF = [-2 1 0;0 0 1;0 0 1];
BF = [0;0;1];
S = [1 2 1];

// Discretized system //
h = 0.02; // sampling time //
cont = syslin('c',AF,BF,S);
disc = dscr(cont,h); // Discretized system //
[A,B,Sd] = abcd(disc);

// initail conditions //
X=[0.5 1.0 1.5]';
K=10;

// solving cpntrol input u //
lines(0)
for i = 1:250;
  sigma = S*X; // switching function //
  U = -inv(S*BF)*(S*AF*X)-K*sigma/norm(sigma);
  dX =A*X+B*U;
  
  // saving data //
  Xh1(:,i) = X;
  Uh1(1,i) = U;
  Sh1(1,i) = sigma;
  X = dX;
end

// plot //
clf()
tt =0:h:(i-1)*h;
subplot(222),plot(tt,Uh1),xgrid(2)
title('制御入力')
xlabel('Time   [s]')
ylabel('Control Input   [N]')
subplot(221),plot(tt,Xh1(1,:),tt,Xh1(2,:),tt,Xh1(3,:)),xgrid(2)
title('変数')
xlabel('Time   [s]')
ylabel('Displacement   [m]')
subplot(223),plot(tt,Sh1),xgrid(2)
title('切換関数')
xlabel('Time   [s]')
ylabel('Swiching Function')
clear tt Uh1 Xh1 Sh1;