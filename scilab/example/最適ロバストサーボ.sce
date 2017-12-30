//最適ロバストサーボ
Ae=[0 1 0;0 -1 1;0 0 0]; be=[0;0;1]; ce=[1 0 0]; 
re=1; Qe=ce'*ce; Be= inv(re)*be*be'; 
Pe=ricc(Ae,Be,Qe,'cont'), spec(Pe)
ke=-inv(re)*be'*Pe; Z=[0 1 0;0 -1 1;1 0 0];
k=ke*inv(Z); k1=[k(1) k(2)], k2=k(3)

