from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d = {'author':'kevin','age':16,'value':['a', 'b', 'c', 'd'],
         'lst':['pycharm','quillbot','chatgpt'],
         'slash':"i'm kevin",
         'val':'',
         'valu':25,
         'v':123456789,
         'line':"one two three",
         'upper':'AMIN',
         'lower':'amin',
         'timenow':datetime.datetime.now(),
         'var':['states',['kanses',['lawrence','topeka'],'illinois']],
         'main':[
            {'name': 'zed', 'age': 19},
            {'name': 'amy', 'age': 22},
            {'name': 'joe', 'age': 31},
        ],
         'bdate':datetime.datetime.now(),
         'courses':[
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