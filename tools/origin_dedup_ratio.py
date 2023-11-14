#!/usr/bin/python3

import sys
import pandas as pd
import os

df = pd.read_csv('./docker_image_info.csv')
print(df.to_string())

DOCKER_IMAGES_TAR_PATH = ''
DOCKER_IMAGES_UNTAR_PATH = ''

os.chdir(sys.argv[1])
if not os.path.exists("./images_tar"):
    os.mkdir("./images_tar")
DOCKER_IMAGES_TAR_PATH = sys.argv[1] + 'images_tar'
print(DOCKER_IMAGES_TAR_PATH)

if not os.path.exists("./images_untar"):
    os.mkdir("./images_untar")
DOCKER_IMAGES_UNTAR_PATH = sys.argv[1] + 'images_untar'
print(DOCKER_IMAGES_UNTAR_PATH)

def stat_dedup_ratio():
    os.chdir(DOCKER_IMAGES_UNTAR_PATH)
    print(os.getcwd())
    for i in range(0,df.shape[0]):
        image = df.loc[i]
        print('\n\n' + image['REPOSITORY'] + ': ' + image['SIZE'])

        jdupes_retio = "jdupes -mr " + image['REPOSITORY']
        os.system(jdupes_retio)

        fdupes_retio = "fdupes -mr " + image['REPOSITORY']
        os.system(fdupes_retio)

stat_dedup_ratio()
print('Successfully')
