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

def untar_images():
    os.chdir(DOCKER_IMAGES_UNTAR_PATH)
    print(os.getcwd())
    for i in range(0,df.shape[0]):
        image = df.loc[i]
        print(image)

        if not os.path.exists(image['REPOSITORY']):
            mkdir_image = 'mkdir ' + image['REPOSITORY']
            print(mkdir_image)
            os.system(mkdir_image)
        
            image_untar = 'tar -xvf ' + DOCKER_IMAGES_TAR_PATH + '/' + image['REPOSITORY'] + '.tar' + ' -C ' + image['REPOSITORY']
            print(image_untar)
            os.system(image_untar)

            layertar_find = 'find ' + image['REPOSITORY'] + ' -name layer.tar'
            print(layertar_find)
            result = os.popen(layertar_find)  
            res = result.read()  
            for ltar in res.splitlines():  
                print(ltar)
                untar_path = ltar[0:len(ltar) - 9]
                print(untar_path)
                layertar_untar = 'tar -xvf ' + ltar + ' -C ' + untar_path
                print(layertar_untar)
                os.system(layertar_untar)
                rm_layertar = "rm " + ltar
                os.system(rm_layertar)

untar_images()
print('Successfully')
