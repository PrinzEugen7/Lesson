c=1; r=0.8; cr = c*r;
t=0:0.1:5;
yi=(1/cr)*exp(-t/cr); ys=1-exp(-t/cr);
clf(); plot2d(t',[yi' ys'],[-1,-5])
