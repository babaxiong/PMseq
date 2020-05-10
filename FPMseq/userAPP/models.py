from django.db import models
from mongoengine import *
from mongoengine.connection import connect
from mongoengine.fields import StringField

# Create your models here.

connect('PMseq', host='172.25.11.25', port=27017)

class data_stat(Document):
    Sample = r'#Sample'
    Sample = StringField()
    Result = StringField()
    Total = StringField()
    Filter_rate = StringField()
    UMhost = StringField()
    Host_rate = StringField()
    Rlowc_umhost = StringField()
    Map_bac = StringField()
    Superior_bac = StringField()
    All_bac = StringField()
    Strin_bac = StringField()
    Map_vir = StringField()
    Superior_vir = StringField()
    All_vir = StringField()
    Strin_vir = StringField()
    Map_fungi = StringField()
    Superior_fungi = StringField()
    All_fungi = StringField()
    Strin_fungi = StringField()
    Map_para = StringField()
    Superior_vir = StringField()
    Superior_vir = StringField()
    Superior_vir = StringField()
    Superior_vir = StringField()
    Superior_vir = StringField()
    Superior_vir = StringField()
    
    
