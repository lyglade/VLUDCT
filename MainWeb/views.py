# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
import os

# Create your views here.
def uploadfile(request):  
    if request.method == "POST":
        f = request.FILES.get('personico')
        baseDir = os.path.dirname(os.path.abspath(__name__));
        jpgdir = os.path.join(baseDir,'static','jpg');
        
        filename = os.path.join(jpgdir,f.name);
        fobj = open(filename,'wb');
        for chrunk in f.chunks():
            fobj.write(chrunk);
        fobj.close();
        return render_to_response('uploadfile.html',{'personico':f.name});
            
    else:
        return render_to_response('uploadfile.html');