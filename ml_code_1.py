# -*- coding: utf-8 -*-
"""ml code 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/182CK_wO9jLXvmpVk-G62HH4bQ2tuYn97
"""

import numpy as np
import pandas as pd

df = pd.read_csv('C:\Users\Admin\Downloads\laptop_price.csv',encoding='latin-1')
df.head(1299)
this='Full HD'
df['Full HD']=df['ScreenResolution'].str.find(this)
x=df.pop('Full HD')
x=x.replace(to_replace=0,value=1)
x=x.replace(to_replace=-1,value=0)
data={'Full HD':x}
df1=pd.DataFrame(data)

print(df1)

