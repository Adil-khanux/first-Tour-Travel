from django.http import HttpResponse
from django.http import HttpResponseRedirect


## html page k liye 

from django.shortcuts import render
# django forms ko import krne k liye 
from .forms import meraform
from service.models import Service
from news.models import News



def homePage(request):

   # data={
       # 'title':'Home Page New',
      #  'Name':'Adil Khan',
      #  'clist':['PHP','JAVA','PYTHON','DJANGO'],
       # 'Student_Details':[
         #   {'name':'Adil khan','phone':8218370897},
        #    {'name':'pradeep','phone':9368276791}
       # ],
        
     #   'numbers':[],
      #  'even':[10,20,30,40,45,89]
        
   # }



   servicesData=Service.objects.all()
   news_data=News.objects.all()

   data={
    'checkdata':servicesData,
    'newsData':news_data
    }


   return render(request,"index.html",data)



def course(request):
    return HttpResponse("Welcome My Course Playlist")

def courseDetails(request,courseid):
    return HttpResponse ("This is my courseid:",courseid)


def Blogs(request):
    return HttpResponse("This is my blog page")


def insideBlog(request,name):
    return HttpResponse(name)











# about page pr value get krke display kradi
def aboutUs(request):
    if request.method=="GET":
        output=request.GET.get('info')
    return render(request,"about.html",{'output':output})


def helpPage(request):
    return render(request,"help.html",)
    
   
def servicePage(request):
    return render(request,"service.html",)


def contactPage(request):
    return render(request,"contact.html",)

def tripleh(request,trip):
    return render(request,trip,"trip-leh.html",)


def userform(request):
    fn=meraform() # django form ki class ko store kiya 
    finalans=0
    data={'foram':fn}
    try:
        if request.method=="POST":
            n1=int (request.POST.get('num1'))
            n2= int (request.POST.get('num2'))
            finalans = n1+n2
            print(n1+n2)
            # dictionary hmne isliye bnai taaki n1 n2 ki value ko store krske key m or usko html page pr print kra sket value1 or value 2 label m
            data={
                'n1':n1,
                'n2':n2,
                'output':finalans,
                'foram':fn
            }
            # about us page pr form ki value ko dekhne k liye url bnaya .format string k help s parameter m value store krakr print kradi
          #  url="/about-us/?info={}".format(finalans)
          #  return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"form.html",data)

def submitform(request):
    data={}
    try:

        if request.method == "POST":

            n1=int (request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            finalans = n1+n2

            data={
         
                'res':finalans

             }

           # return HttpResponse("Data submit successfully",finalans)
    #return HttpResponse(request)

    except:
        pass
    
    
    return render(request,"submitform.html",data)


def calculator(request):
    c=''
    try:

        if request.method == "POST":

            num1=eval (request.POST.get('number1'))
            num2=eval(request.POST.get('number2'))
            opr=request.POST.get('opr')

            if opr=="+":
                c=num1+num2
            elif opr=="-":
                c=num1-num2
            elif opr=="*":
                c=num1*num2
            elif opr=="/":
                c=num1/num2
            else:
                c=num1%num2
    
    except:
        c="Invalid operator........"
          
    return render(request,"calculator.html",{'d':c})



def evenodd(request):
    c=''
    try:

        if request.method == "POST":
            if request.POST.get("number1")=="":
                 return render(request,"evenodd.html",{'error':True})


            n=eval(request.POST.get('number1'))
    

            if n%2==0:
                c="Even number"
            else:
                c="Odd number"
    
    except:
        pass
          
    return render(request,"evenodd.html",{'d':c})

def marksheet(request):
    data={}
    if request.method=="POST":
        if any(request.POST.get(f) == '' for f in ['sub1', 'sub2', 'sub3', 'sub4', 'sub5', 'sub6']):
                return render(request, "marksheet.html", {'error': True})



        s1=eval(request.POST.get('sub1'))
        s2=eval(request.POST.get('sub2'))
        s3=eval(request.POST.get('sub3'))
        s4=eval(request.POST.get('sub4'))
        s5=eval(request.POST.get('sub5'))
        s6=eval(request.POST.get('sub6'))
        t=s1+s2+s3+s4+s5+s6
        p=t*100/600
        if p>=60:
            d="First Div"
        elif p>=48:
            d="Second Div"
        else:
            d="Third Div"
        data={
            'total':t,
            'percentage':p,
            'div':d
        }
        print(t)
        
    return render (request,"marksheet.html",data)

def newsdetails(request,newsid):
    print(newsid)
    news_data=News.objects.get(id=newsid)
    data={
        'newsDescription':news_data
    }
    return render(request,"news_details.html",data)

    
 






