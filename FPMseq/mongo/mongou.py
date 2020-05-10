# -*- coding:utf-8 -*-

import pandas as pd
import pymongo
import json
import sys
import argparse
import os

def get_json(file):
    global anno
    anno_pd = pd.read_csv(file, delimiter="\t", engine="python", error_bad_lines=False, encoding='gbk')
    anno = json.loads(anno_pd.T.to_json()).values()
    return

def v5(data, stype):
    PMseq = db_coon.PMseq
    mycoll = PMseq[stype]
    mycoll.insert_many(data)


def usage():
    parser=argparse.ArgumentParser(description="A description of what the program does")
    parser.add_argument()


def get_options():
    parser=argparse.ArgumentParser(description="A description of what the program does")
    parser.add_argument('-c',choices=['bac','fun','vir','par','data.stat','sample'], type=str, help="Choose one")
    parser.add_argument("--file", '-f', required=True, type=str, nargs='+', help="file path")
    if len(sys.argv) == 1 or sys.argv[1] in ['-h', '--help']:
        parser.print_help()
        sys.exit()
    args=parser.parse_args()
    return args



def main():    
    options = get_options()
    db_coon = pymongo.MongoClient(host='172.25.11.25', port=27017)
    file_path = os.path.abspath(options.file)
    stype = options.c
    for file in file_path:
        anno = []
        get_json(file)
        v5(anno,stype)


if __name__ == '__main__':
    main()