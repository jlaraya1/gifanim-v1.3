#!/bin/bash
# Rutina para ejecucion en tiempo real usando crontab
cd /home/jlaraya/gifimn
python ejecute.py
cd fotos2
convert -delay 50 *.jpg  anim_largo.gif
#display anim_largo.gif
cd ../fotos3
convert -delay 100 -resample 45x45  *.jpg anim_corto.gif

echo "***Compilacion exitosa***"
