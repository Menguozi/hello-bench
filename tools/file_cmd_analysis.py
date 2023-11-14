#!/usr/bin/python3

import os
import sys
import hashlib
import shutil

if not os.path.exists(sys.argv[2] + '/file_md5'):
    os.mkdir(sys.argv[2] + '/file_md5')
FILE_MD5 = sys.argv[2] + '/file_md5'

def classify_by_file_cmd():
    print('classify_by_file_cmd: ', sys.argv[1])
    os.chdir(sys.argv[1])

    none_type = 0
    known_type = 0
    empty_file = 0
    link_cnt = 0

    for root, ds, fs in os.walk(os.getcwd()):
        for f in fs:
            fullname = os.path.join(root, f)
            print(fullname)
            if os.path.islink(fullname):
                link_cnt += 1
            elif os.path.isfile(fullname):
                if os.path.getsize(fullname):
                    file_cmd_ret = os.popen('file ' + fullname).read()
                    pos = file_cmd_ret.find(': ')
                    type = file_cmd_ret[pos + 2:]
                    type_md5 = hashlib.md5(type.encode("utf8")).hexdigest()

                    if not os.path.exists(FILE_MD5 + '/' + type_md5):
                        os.mkdir(FILE_MD5 + '/' + type_md5)

                    destname = FILE_MD5 + '/' + type_md5 + '/' + hashlib.md5(fullname.encode("utf8")).hexdigest()
                    shutil.copy(fullname, destname)
                    known_type = known_type + 1
                else:
                    if not os.path.exists(FILE_MD5 + '/' + 'empty/'):
                        os.mkdir(FILE_MD5 + '/' + 'empty/')
                    destname = FILE_MD5 + '/empty/' + hashlib.md5(fullname.encode("utf8")).hexdigest()
                    shutil.copy(fullname, destname)
                    empty_file += 1
            else:
                none_type += 1
    
    print('link_cnt: ',link_cnt)
    print('none_type: ',none_type)
    print('known_type: ',known_type)
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
    classify_by_file_cmd()
    classify_by_flag()