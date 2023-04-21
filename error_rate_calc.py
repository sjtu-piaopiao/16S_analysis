#!/usr/bin/env python
# coding: utf-8

import numpy as np
from pandas import *
import sys
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all" 


def over_splitting(df):
    dir={}
    n=0
    for i in df.index:
        if len(df.columns)-df.loc[i].value_counts()[0] >= 2:
            dir[i]=len(df.columns)-df.loc[i].value_counts()[0]
            n+=1
    return round(n/len(df.index),3)

def over_merging(df):
    dir={}
    n=0
    for i in df.columns:
        if len(df.index)-df[i].value_counts()[0] >= 2:
            dir[i]=len(df.index)-df[i].value_counts()[0]
            n+=1
    return round(n/len(df.columns),3)

n=0
for i in [0,0.001,0.002,0.003,0.004,0.005,0.006,0.007,0.008,0.009,0.010,0.011,0.012,0.013,0.014,0.015,0.016,0.017,0.018,0.019,0.020,0.021,0.022,0.023,0.024,0.025,0.026,0.027,0.028,0.029,0.030]:
    otu=read_csv("amplicon_error/"+sys.argv[1]+"/"+sys.argv[2]+"."+sys.argv[1]+".{}.shared".format(i),sep='\t',engine='python').set_index('Group')
    df=otu.copy().dropna(axis=1, how='any')
    del df['label']
    if 'numOtus' in df.columns:
    	del df['numOtus']
    else:
        del df['numASVs']
    a=over_splitting(df)
    b=over_merging(df)
    c=a+b
    print(i,'\t',a,'\t',b,'\t',round(c,3))
    n+=1
n
