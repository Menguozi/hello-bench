#!/usr/bin/bash

docker image ls > docker_image_ls.txt

head -1 docker_image_ls.txt | awk '{printf "%s,%s,%s %s,%s,%s\n",$1,$2,$3,$4,$5,$6}' > docker_image_info.csv

sed -i '1d' docker_image_ls.txt

cat docker_image_ls.txt | awk '{printf "%s,%s,%s,%s %s %s,%s\n",$1,$2,$3,$4,$5,$6,$7}' >> docker_image_info.csv