// In WAVE file, the sampling rate are 44.1kHz, 32kHz, 22.05kHz,
// 16kHz, 11.025kHz and 8kHz
t=soundsec(1); //1sec sound time, the default sampling rate is 22050.
do=sin(2*%pi*264*t);
mi=sin(2*%pi*330*t);
so=sin(2*%pi*396*t);
snd=[do,mi,so];
savewave('oto.wav',snd);
