#!/usr/bin/python3

import sys
import pandas as pd
import os

df = pd.read_csv('./docker_image_info.csv')
print(df.to_string())

DOCKER_IMAGES_TAR_PATH = ''
DOCKER_IMAGES_UNTAR_PATH = ''
DOCKER_IMAGES_DEDUP_PATH = ''

os.chdir(sys.argv[1])
if not os.path.exists("./images_tar"):
    os.mkdir("./images_tar")
DOCKER_IMAGES_TAR_PATH = sys.argv[1] + 'images_tar'
print(DOCKER_IMAGES_TAR_PATH)

if not os.path.exists("./images_untar"):
    os.mkdir("./images_untar")
DOCKER_IMAGES_UNTAR_PATH = sys.argv[1] + 'images_untar'
print(DOCKER_IMAGES_UNTAR_PATH)

if not os.path.exists("./images_dedup"):
    os.mkdir("./images_dedup")
DOCKER_IMAGES_DEDUP_PATH = sys.argv[1] + 'images_dedup'
print(DOCKER_IMAGES_DEDUP_PATH)

def dedup_images():
    os.chdir(DOCKER_IMAGES_DEDUP_PATH)
    print(os.getcwd())
    for i in range(0,df.shape[0]):
        image = df.loc[i]
        print(image)

        if not os.path.exists(image['REPOSITORY'] + '_dedup'):
            mkdir_image = 'mkdir ' + image['REPOSITORY'] + '_dedup'
            print(mkdir_image)
            os.system(mkdir_image)

            cp_to_dedup = 'cp -r ' + DOCKER_IMAGES_UNTAR_PATH + '/' + image['REPOSITORY'] + ' ' + image['REPOSITORY'] + '_dedup'
            print(cp_to_dedup)
            os.system(cp_to_dedup)

            jdupes_iamge = 'jdupes -r --link-hard ' + image['REPOSITORY'] + '_dedup'
            print(jdupes_iamge)
            os.system(jdupes_iamge)

def stat_dedup_ratio():
    os.chdir(DOCKER_IMAGES_DEDUP_PATH)
    print(os.getcwd())
    for i in range(0,df.shape[0]):
        image = df.loc[i]
        print('\n\n' + image['REPOSITORY'] + ': ' + image['SIZE'])

        jdupes_retio = "jdupes -mr " + image['REPOSITORY'] + '_dedup'
        os.system(jdupes_retio)

        fdupes_retio = "fdupes -mr " + image['REPOSITORY'] + '_dedup'
        os.system(fdupes_retio)

dedup_images()
stat_dedup_ratio()
print('Successfully')
