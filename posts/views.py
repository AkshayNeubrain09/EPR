from django.shortcuts import render
import pandas as pd
import numpy as np
# Create your views here.

df = pd.read_csv('epr.csv')

def index(request):
    shape = df.shape[0]
    names = df.Name
    account_url = df.account_url
    bio = df.bio
    post_desc = df.post_desc
    post_img = df.post_img
    rows= []
    for i,r in df.iterrows():
        rows.append(r)
    context = {
        'rows':rows
    }
    return render(request, 'index.html',context)