file="/usr/lib64/python3.6/site-packages/matplotlib/mpl-data/matplotlibrc"
if [ -f $file ]
then
  sed -i "s/#*\(font.sans-serif *:\).*/\1 Droid Sans Fallback/g" $file
  echo "matplotlibrc found and font is configured"
else
  echo "$file not found!"
  echo "Please run locate matplotlibrc to find similiar file locattion"
fi

