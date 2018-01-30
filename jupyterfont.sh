#! /usr/bin/env bash

# Jupyter Math
FROM=/usr/share/javascript/mathjax
NB=/usr/lib/python3.6/site-packages/notebook
TO=$NB/static/components/MathJax
JS=$NB/static/notebook/js/main.min.js
DIR1=fonts/HTML-CSS/TeX
DIR2=jax/output/HTML-CSS/fonts/TeX
ln -s $FROM/$DIR1 $TO/$DIR1
ln -s $FROM/$DIR2 $TO/$DIR2
sed -i 's/\(availableFonts:\).*/\1 \["STIX-Web", "TeX"\],/g' $JS
sed -i 's/\(preferredFont:\).*/\1 "TeX",/g' $JS
sed -i 's/\(webFont:\).*/\1 "TeX",/g' $JS

# MPL Font
file="/usr/lib64/python3.6/site-packages/matplotlib/mpl-data/matplotlibrc"
if [ -f $file ]
then
  sed -i "s/#*\(font.sans-serif *:\).*/\1 Droid Sans Fallback/g" $file
  sed -i "s/#*\(axes.unicode_minus *:\).*/\1 False/g" $file
  echo "matplotlibrc found and font is configured"
else
  echo "$file not found!"
  echo "Please run locate matplotlibrc to find similiar file locattion"
fi
