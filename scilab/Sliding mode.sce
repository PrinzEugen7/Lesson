clc
clear all
format ('e',15)
global ni;
global dy; //xの微分値//
//----setup---//
sampling=0.1;//sampling time of simulation
//kaisu=1000;
//timespan=sampling*kaisu;% simulation time
//--- initial state ----
x0=[-10 ]; //initial condition
disp('It is under calculation now!!')
//================= 初期値条件1============================================
ni=1;
tend=1000; //6000 応答時間に合わせて変える
while(ni <= tend)
[Tn,Yn]=ode45(@slidingmode_ren2_eq2,[0 sampling],x0,[]); //変えること
if ni==1
YY(1,:)=Yn(1,1:1);
DY(1,:)=dy;
TT(1,:)=Tn(1,1);
else
YY(ni,:)=Yn(size(Yn,1),1:1);
DY(ni,:)=dy;
TT(ni,1)=sampling*ni;
end
//---- Up data------
size(Yn,1);
x0=Yn(size(Yn,1),1:1);
ni=ni+1;
end
hold on
figure(1)
plot([-15; 15] ,[-0.5*(-15) ; -0.5*15] ,'g' );
plot([-15 15],[0 0],'k')
plot([0 0],[15 -15],'k')
plot(YY(:,1) ,DY,'b','linewidth',2);
ax1=findobj(gca,'Type','Axes','Visible','on');
set(ax1,'fontsize',12); %目盛りを大きく
axis([-15 +15 -15 +15])
xlabel('x','fontsize',12);
ylabel('y','fontsize',12)
title('切換線上の位相平面軌跡','fontsize',12)
text(-10,6,' x(0) = -10' );
//================= 初期値条件2============================================
//--- initial state ----
x0=[ +10 ]; //initial condition
ni=1;
tend=1000; //6000 応答時間に合わせて変える
while(ni <= tend)
[Tn,Yn]=ode45(@slidingmode_ren2_eq2,[0 sampling],x0,[]); //変えること
if ni==1
YY(1,:)=Yn(1,1:1);
DY(1,:)=dy;
TT(1,:)=Tn(1,1);
else
YY(ni,:)=Yn(size(Yn,1),1:1);
DY(ni,:)=dy;
TT(ni,1)=sampling*ni;
end
//---- Up data------
size(Yn,1);
x0=Yn(size(Yn,1),1:1);
ni=ni+1;
end
plot(YY(:,1) ,DY,'b','linewidth',2);
text( +10,-4,' x(0) = +10' );
hold off
function dy=slidingmode_ren2_eq2(t,y);
//---2006.6.13----
global ni
global dy
dy=zeros(1,1);
dy(1,1) = -0.5*y(1,1);