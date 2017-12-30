clear, clc
lines(0)
//------------- Constant matrix -----------//

AF=[-2 1 0;0 0 1;0 0 1];
BF=[0 0 1]';
S=[1 2 1];
Im=S*BF;

//---------- Discretized system -----------//

h = 0.02; //---- Sampling time ----//
cont = syslin('c',AF,BF,S);
disc = dscr(cont,h); // Discretized system //
[A,B,Sd] = abcd(disc);

//-------- Initail conditions -------------//
X=[0.5 1.0 1.5]';
u=0;

//---------- Solving control input u --------------//

disp('');
disp('recommending value is -5');
alfa=input('alfa='); // alfa<0 (alfa=-5) //

for i=1:250;
sigma=S*X; //---- Switching function ----//
Ueq=-S*AF*X; //---- Eq.(3.197) ----//
U=Ueq+alfa*sign(sigma); //---- Eq.(3.198) ----//
dX=A*X+B*U;

//-------------- Saving data -----------------//
Xf1(:,i)=X;
Uf1(1,i)=U;
Sf1(1,i)=sigma;
X=dX;
end

//----------- Plotting results -----------//
clf
tt=0:h:(i-1)*h;
subplot(222),plot(tt,Uf1),xgrid(2)
title('')
xlabel('Time   [s]')
ylabel('Control Input  [N]')

subplot(221),plot(tt,Xf1(1,:),tt,Xf1(2,:),tt,Xf1(3,:)),xgrid(2)
xlabel('Time   [s]')
ylabel('Displacement [m]')

subplot(223),plot(tt,Sf1),xgrid(2)
xlabel('Time   [s]')
ylabel('Switching Function')
clear tt Uf1 Xf1 Sf1;