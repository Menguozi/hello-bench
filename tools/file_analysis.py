#!/usr/bin/python3

import os
import sys
import puremagic
import hashlib
import shutil

def classify_by_type():
    print('classify_by_type: ', sys.argv[1])
    os.chdir(sys.argv[1])

    none_type = 0
    known_type = 0
    known_ext = 0
    unknown_ext = 0
    empty_file = 0
    link_cnt = 0
    for root, ds, fs in os.walk(os.getcwd()):
        for f in fs:
            fullname = os.path.join(root, f)
            if os.path.islink(fullname):
                link_cnt += 1
            else:
                # print(fullname)
                # print(os.path.getsize(fullname))
                if os.path.getsize(fullname):
                    magic = puremagic.magic_file(fullname)
                    if(not len(magic)):
                        destname = sys.argv[2] + '/types/unknown/' + hashlib.md5(fullname.encode("utf8")).hexdigest()
                        shutil.copy(fullname, destname)
                        # print(fullname)
                        os.system('file ' + fullname)
                        none_type = none_type + 1
                    else:
                        ext = puremagic.from_file(fullname)
                        # print(ext)
                        destname = sys.argv[2] + '/types/' + magic[0].extension[1:] + '/' + hashlib.md5(fullname.encode("utf8")).hexdigest()
                        if(magic[0].extension[1:]):
                            shutil.copy(fullname, destname)
                            known_ext += 1
                        else:
                            unknown_ext += 1
                            # print(magic[0])
                        known_type = known_type + 1
                else:
                    destname = sys.argv[2] + '/types/empty/' + hashlib.md5(fullname.encode("utf8")).hexdigest()
                    shutil.copy(fullname, destname)
                    empty_file += 1
    
    print('link_cnt: ',link_cnt)
    print('none_type: ',none_type)
    print('known_type: ',known_type)
    print('\tknown_ext: ',known_ext)
    print('\tunknown_ext: ',unknown_ext)
    print('empty_file: ',empty_file)

def classify_by_flag():
    print('classify_by_flag: ', sys.argv[1])
    os.chdir(sys.argv[1])

    file_cnt = 0
    dir_cnt = 0
    file_link_cnt = 0
    dir_link_cnt = 0
    others_cnt = 0
    d_cnt = 0
    f_cnt = 0
    for root, ds, fs in os.walk(os.getcwd()):
        for d in ds:
            d_cnt += 1
            fullpath = os.path.join(root, d)
            if os.path.islink(fullpath):
                dir_link_cnt += 1
            elif os.path.isdir(fullpath):
                dir_cnt += 1
            else:
                others_cnt += 1
        for f in fs:
            f_cnt += 1
            fullpath = os.path.join(root, f)
            if os.path.islink(fullpath):
                file_link_cnt += 1
            elif os.path.isfile(fullpath):
                file_cnt += 1
            else:
                others_cnt += 1
    
    print('d_cnt: ',d_cnt)
    print('f_cnt: ',f_cnt)
    print('dir_cnt: ',dir_cnt)
    print('dir_link_cnt: ',dir_link_cnt)
    print('file_cnt: ',file_cnt)
    print('file_link_cnt: ',file_link_cnt)
    print('others_cnt: ',others_cnt)

if __name__ == '__main__':
    classify_by_type()
    classify_by_flag()