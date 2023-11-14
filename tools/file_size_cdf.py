#!/usr/bin/python3

import os
import sys
import puremagic
import hashlib
import shutil
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import subprocess

def size_cdf():
    print('size_cdf: ', sys.argv[1])
    os.chdir(sys.argv[1])

    size_list = []
    zst_list = []
    for root, ds, fs in os.walk(os.getcwd()):
        for f in fs:
            fullname = os.path.join(root, f)
            # fullname = fullname.replace(' ', '_')
            # fullname = fullname.replace('(', '_')
            # fullname = fullname.replace(')', '_')
            # fullname = fullname.replace('+', '_')
            # os.rename(os.path.join(root, f), fullname)
            if not os.path.islink(fullname) and os.path.isfile(fullname):
                if os.path.getsize(fullname) and os.path.getsize(fullname) < 256*1024:
                    # print(fullname, os.path.getsize(fullname)/1024.0)
                    size_list.append(os.path.getsize(fullname)/1024.0)
                    zst = fullname + '.zst'
                    ret = os.system('zstd -15 -f ' + fullname)
                    if ret:
                        continue
                    try :
                        zst_list.append(os.path.getsize(zst)/1024.0)
                    except Exception as err:
                        continue
                    ret = os.system('rm -rf ' + zst)
                    if ret:
                        continue
    list.sort(size_list)
    size_array = np.array(size_list)
    print('nums: ', size_array.shape[0])
    print('min: ', np.amin(size_array))
    print('max: ', np.amax(size_array))
    print('average: ', np.average(size_array))
    print('var: ', np.var(size_array))

    list.sort(zst_list)
    zst_size_array = np.array(zst_list)
    print('nums: ', zst_size_array.shape[0])
    print('min: ', np.amin(zst_size_array))
    print('max: ', np.amax(zst_size_array))
    print('average: ', np.average(zst_size_array))
    print('var: ', np.var(zst_size_array))

    res_freq = stats.relfreq(size_array, numbins=100)
    x = res_freq.lowerlimit + np.linspace(0, res_freq.binsize * res_freq.frequency.size, res_freq.frequency.size)
    pdf_value = res_freq.frequency
    cdf_value = np.cumsum(res_freq.frequency)
    # print(x)
    # print(pdf_value)
    # print(cdf_value)

    # plt.plot(x, pdf_value)
    # plt.subplot(1, 2, 1)
    plt.plot(x, cdf_value)
    plt.savefig('/home/menguozi/workspace/hello-bench/tools/file_size.jpg')
    # plt.show()

    zst_res_freq = stats.relfreq(zst_size_array, numbins=100)
    zst_x = res_freq.lowerlimit + np.linspace(0, zst_res_freq.binsize * zst_res_freq.frequency.size, zst_res_freq.frequency.size)
    zst_pdf_value = zst_res_freq.frequency
    zst_cdf_value = np.cumsum(zst_res_freq.frequency)
    # print(x)
    # print(pdf_value)
    # print(cdf_value)

    # plt.plot(x, pdf_value)
    # plt.subplot(1, 2, 2)
    plt.plot(zst_x, zst_cdf_value)
    plt.savefig('/home/menguozi/workspace/hello-bench/tools/zst_size.jpg')

if __name__ == '__main__':
    size_cdf()