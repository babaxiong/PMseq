# -*- coding: gbk -*-
import cx_Oracle
import os
import pandas as pd


os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'
conn = cx_Oracle.connect('pmSeq/KAOCNpJXsE3@192.168.225.4:1521/orcl')
cursor = conn.cursor()
sql_cmd = "SELECT * FROM DX_SIMS.DX0594_AUTOANALYSE "
all_data = cursor.execute(sql_cmd)



conn.close()