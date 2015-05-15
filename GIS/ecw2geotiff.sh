#!/bin/bash

# @author Pablo Sanxiao <psanxiao@icarto.es>
# @license GPL v3

src_dir=${1}
dest_dir=${2}

for i in `ls ${src_dir}/*ECW`; do
    s=${i##*/}
    echo Processing $s
    name=${s%.ECW}
    ../bin/FWTools-2.0.6/bin_safe/gdal_translate -a_srs "EPSG:23029" -of GTiff $i ${dest_dir}/$name.tif \
        -co COMPRESS=JPEG -co TILED=yes -co BLOCKXSIZE=512 -co BLOCKYSIZE=512 ;
done

for i in `ls ${dest_dir}/*tif`; do
    gdaladdo -r average $i 2 4 8 16;
done