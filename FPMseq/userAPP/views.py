# coding:utf-8

from django.shortcuts import render
from django.http import StreamingHttpResponse
import pymongo 
import pandas as pd
import os
import sys
import argparse
import io
import codecs

mycon = pymongo.MongoClient(host='172.25.11.25', port=27017)
mydb = mycon.PMseq
# Create your views here.
def PMseq(request):
    return render(request, 'PMseq.html')
    
def find(request):
    return render(request, 'find.html')
    
def findresult(request):
    global mydb
    coll = request.GET.get('coll', None)
    header = request.GET.get('header', None)
    val = request.GET.get('sample', None)
    mycoll = mydb[coll]
    print(coll, header, val)
    html_string = """
<!DOCTYPE html>
<html>
    <head><title>HTML Pandas Dataframe with CSS</title></head>
    <link rel="stylesheet" type="text/css" href="../static/admin/css/df_style.css">
    <body>
        {table}
    </body>
</html>
"""
    with codecs.open(r'D:\工作\project\FPMseq\userAPP\templates\print.html', 'w', encoding='utf-8') as f:
        mydata = mycoll.find({header: val}, {"_id": 0})
        data = pd.DataFrame(list(mydata))
        # print(data.to_csv(sep='\t', index=False))
        f.write(html_string.format(table=data.to_html(index=0, classes='mystyle')))
    f.close()
    return render(request, 'print.html')


def download(request):
    global mydb
    coll = request.GET.get('coll', None)
    header = request.GET.get('header', None)
    val = request.GET.get('sample', None)
    mycoll = mydb[coll]
    if coll in ['bac', 'fun', 'vir', 'par']:
        myname = "%s.%s.final.anno.xlsx" % (val, coll)
    else:
        myname = "%s.%s.xlsx" % (val, coll)
    # print(myname, val)
    data = mycoll.find({header: val}, {"_id": 0})
    data = pd.DataFrame(list(data))
    print(data.to_csv(sep='\t', index=False))
    data.to_excel("D:\\工作\\project\\FPMseq\\userAPP\\download\\%s" % (myname), index=False)
    filename = os.path.join('D:\\工作\\project\\FPMseq\\userAPP\\download', myname)
    the_file_name = myname   # 显示在弹出对话框中的默认的下载文件名
    response = StreamingHttpResponse(readFile(filename))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    return response


def readFile(filename, chunk_size=512):
    with open(filename, 'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break
