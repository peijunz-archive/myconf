FROM=/usr/share/javascript/mathjax
NB=/usr/lib/python3.6/site-packages/notebook
TO=$NB/static/components/MathJax
JS=$NB/static/notebook/js/main.min.js
DIR1=fonts/HTML-CSS/TeX
DIR2=jax/output/HTML-CSS/fonts/TeX
ln -s $FROM/$DIR1 $TO/$DIR1
ln -s $FROM/$DIR2 $TO/$DIR2
sed -i 's/\(availableFonts:\).*/\1 \["STIX-Web", "TeX"\]/g' $JS

