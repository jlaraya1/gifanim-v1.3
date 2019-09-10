cd ..\..
cd C:\gifanimn\
"c:\python26\python.exe" "ejecute.py" foo
cd fotos2
convert -delay 50 *.jpg  anim_largo.gif
cd ..\fotos3
convert -resample 45x45 *.jpg IMNPro.png 
convert -delay 100 resample 45x45 *.png  anim_corto.gif
copy/y anim_corto.gif \\tierra\rtdm\anim_corto.gif

