mkdir output
parec -d alsa_output.usb-Corsair_Corsair_Gaming_H2100_Headset-00.analog-stereo.monitor | lame -r --quiet -q 3 --lowpass 17 --abr 128 - output/rec.mp3
