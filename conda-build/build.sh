#!/bin/bash

mkdir $PREFIX/Darts_BHT_bin
python setup.py install


cp Darts_BHT/rmatspipeline.so $PREFIX/Darts_BHT_bin
cp bin/Darts_BHT $PREFIX/Darts_BHT_bin
chmod +x $PREFIX/Darts_BHT_bin/Darts_BHT
ln -sf $PREFIX/Darts_BHT_bin/Darts_BHT $PREFIX/bin/Darts_BHT
