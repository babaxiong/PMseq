# coding:utf-8

import pymongo as pm
import pandas as pd
import os
import sys
# import argparse
import io
import codecs

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)

# def get_options():
#     parser=argparse.ArgumentParser(description="A description of what the program does")
#     parser.add_argument('-p',choices=['bac','fun','vir','par','data.stat','sample.info'], type=str, required=True, help="Choose one")
#     parser.add_argument('-l', type=str, required=True, default='#Sample', help="-l '#Sample'")
#     parser.add_argument('-v', type=str, required=True, nargs='+', help="-v 19S0058257 19S0058211" )
#     parser.add_argument('-o', required=False, type=str, help="out dir")
#     if len(sys.argv) == 1 or sys.argv[1] in ['-h', '--help']:
#         parser.print_help()
#         sys.exit()
#     args=parser.parse_args()
#     return args

class mongo:
    
    def __init__(self, col, lab, val, out):
        self.col = col
        self.lab = lab
        self.val = val
        self.out = out


    def find(self):
        values_list = self.val
        global mydb
        mycoll = mydb[self.col]
        html_string = '''
<html>
{% load static %}
    <head><title>HTML Pandas Dataframe with CSS</title></head>
    <link rel="stylesheet" type="text/css" href="{% static 'df_style.css' %}">
    <body>
        {table}
    </body>
</html>.
'''
        with codecs.open(r'data.html', 'w', encoding='utf-8') as f:
            for v in values_list:
                mydata = mycoll.find({self.lab: v}, {"_id": 0})
                data = pd.DataFrame(list(mydata))
                print(data.to_csv(sep='\t', index=False))
                f.write(html_string.format(table=data.to_html(classes='mystyle')))
        f.close()


    def download(self):
        global mydb
        mycoll = mydb[self.col]
        out_dir = os.path.abspath(self.out)
        values_list = self.val
        
        for v in values_list:
            if self.col in ['bac', 'fun', 'vir', 'par']:
                myname = "%s.%s.final.anno" % (v, self.col)
            else:
                myname = "%s.%s" % (v, self.col)
            mydata = mycoll.find({self.lab:v}, {"_id":0})
            mydata = pd.DataFrame(list(mydata))
            mydata.to_excel("%s.xlsx" % (myname), index = False)


if __name__=='__main__':
    # options = get_options()
    col = input("请输入表格类型：(bac, fun, vir, par, data.stat, sample.info)")
    lab = input("请输入搜索标签：(#Sample)")
    val = input("请输入搜索值：")
    out = input("请输入下载路径：(可选)")

    coon = pm.MongoClient(host='172.25.11.25', port=27017)
    mydb = coon.PMseq
    mymongo = mongo(col, lab, val, out)
    if out is not None:
        mymongo.download()
    else:
        mymongo.find()