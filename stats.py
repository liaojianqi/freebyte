#!/usr/bin/env python3
#coding: utf-8
import os

# 统计当前目录下每个文件类型的个数
type_dict = dict()

def stats(dire):
    files = os.listdir(dire)
    for f in files:
        if f.endswith(".git") or f.endswith(".idea"):
            continue
        if os.path.isdir(dire + "/" + f):
            stats(dire + "/" + f)
        else:
            ext = os.path.splitext(f)[1]
            if not ext:
                ext = os.path.splitext(f)[0]
            type_dict.setdefault(ext,0)
            type_dict[ext] += 1

stats("/Users/loinliao/mycode/py/freebyte")
for each_type in type_dict.keys():
    print('%-15s%-10d' % ("[" + each_type + "]", type_dict[each_type]))
