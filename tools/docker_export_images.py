#!/usr/bin/python3

import sys
import pandas as pd
import os

df = pd.read_csv('./docker_image_info.csv')
print(df.to_string())

DOCKER_IMAGES_TAR_PATH = ''

os.chdir(sys.argv[1])
if not os.path.exists("./images_tar"):
    os.mkdir("./images_tar")
DOCKER_IMAGES_TAR_PATH = sys.argv[1] + 'images_tar'
print(DOCKER_IMAGES_TAR_PATH)

def export_images():
    os.chdir(DOCKER_IMAGES_TAR_PATH)
    print(os.getcwd())
    for i in range(0,df.shape[0]):
        image = df.loc[i]
        print(image)

        if not os.path.exists(image['REPOSITORY'] + '.tar'):
            docker_save = 'docker save ' + image['IMAGE ID'] + ' > '+ image['REPOSITORY'] + '.tar'
            print(docker_save)
            os.system(docker_save)

export_images()
print('Successfully')
