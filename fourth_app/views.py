from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d = {'author':'kevin','age':16,'lst':['pycharm','quillbot','chatgpt'],'bdate':datetime.datetime.now(),'courses':[
        {
            'id':1,
            'name':'python',
            'fee':5000
        },
        {
            'id':2,
            'name':'django',
            'fee':3000
        }

    ]}
    return render(request, 'fourth_app/home.html',context=d) #or u could only use d it will work the same