//‚PŽŸ’x‚ê—v‘f‚Ì’¼—ñÚ‘±
k=1; t1=1; t2=1.5;
t=0:0.1:10;
y1=k-(k/(t1-t2))*(t1*exp(-t/t1) - t2*exp(-t/t2));
clf(); plot2d(t,y1)

