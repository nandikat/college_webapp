from django.shortcuts import render
import mysql.connector as sqltor
from main_page.models import Student
from main_page.models import Scores
from main_page.models import TimeTable
from main_page.models import Fees
from main_page.models import Attendance
from main_page.models import Tutor
from django.db import connection
from django.contrib.sessions.middleware import SessionMiddleware
    
# Create your views here.
def first(request):

    #if request.session.session_key is None:
    #    print('New Key')
    #    request.session.session_key=(sessionStore.create()).session_key
        
    return render(request,'home.html')

def login_f(request):
    print(request.method,request.session.session_key)
    
    if request.method=="POST":
        dict1=request.POST
        x=dict1.get("fname")
        y=dict1.get("pwd1")
        #print(x,y)
        qs = Student.objects.filter(name=x, pwd=y)
        if qs.exists():
            print("login_f1")
            nmlst = list(qs.values('name','roll_no'))
            #print(q.values('name'))
            va=list(nmlst[0].values())[0]
            
            print(va)
            rln = list(nmlst[0].values())[1]
            print(rln)
            print("login_f")
            request.session['username'] = rln
            
            return render(request,'student_login.html', {'srol':va})
        #,{'srol':va})
        else:
            return render(request,'login.html')   
    else:
        return render(request,'login.html')
     
    
##    return render(request,'login.html')

def logout(request):
   try:
      del request.session['username']
   except:
      pass
   return HttpResponse("<strong>You are logged out.</strong>")

def student_login_top(request):
    print(student_login_top)
    return render(request,'student_login_top.html')

def student_log(request):
    #print(request.method,request.session.session_key)
    print("student log")
    return render(request,'student_login.html')

def score(request):
    print("score")
    #if request.method=="GET":
        
    #x=dict1.get("fname")
    #y=dict1.get("pwd1")
    x=0
        #print(x,y)
    if request.session.has_key('username'):
      x = request.session['username']
      
    qs = Scores.objects.filter(roll_no=x)
    print("score 2")
    if qs.exists():
        print("score 3")
        nmlst = list(qs.values('roll_no','subject_1','subject_2','subject_3','subject_4','subject_5','subject_6','semester'))
        #print(q.values('name'))
        va=list(nmlst[0].values())
        va2=nmlst
        
        print(va)
        print(va2)
        print("score 4")
        #print({'srol':va2})
        return render(request,'score.html', {'srol':va2})
    
    else:
        return render(request,'score.html')

def time_table(request):
    print("score")
    #if request.method=="GET":
        
    #x=dict1.get("fname")
    #y=dict1.get("pwd1")
    x=0
    if request.session.has_key('username'):
      x = request.session['username']
      print(x)
        #print(x,y)
    rs=Student.objects.filter(roll_no=x)
    print("hello")
    nm=list(rs.values('course','semester'))
    print(nm)
    nm1=list(nm[0].values())
    nm2=(nm1[0])
    nm3=(nm1[1])
    print(nm3)
    print(nm2)
    qs = TimeTable.objects.filter(course=nm2,semester=nm3)
    print("score 2")
    if qs.exists():
        print("score 3")
        nmlst = list(qs.values('time','monday','tuesday','wednesday','thursday','friday'))
        #print(q.values('name'))
        va=list(nmlst[0].values())
        va2=nmlst
        
        print(va)
        print(va2)
        print("score 4")
        #print({'srol':va2})
        return render(request,'time_table.html', {'trol':va2})
    
    else:
        return render(request,'time_table.html')

def fee(request):
    print("score")
    #if request.method=="GET":
        
    #x=dict1.get("fname")
    #y=dict1.get("pwd1")
    x=0
    if request.session.has_key('username'):
      x = request.session['username']
        #print(x,y)
    qs = Fees.objects.filter(roll_no=x)
    print("score 2")
    if qs.exists():
        print("score 3")
        nmlst = list(qs.values('total','paid'))
        nmlst1=list(qs.values('total','paid'))[0]
        print(nmlst)
        #dic = nmlst1[0]
        print(nmlst1['total'])

        
        #print(nmlst1)
        #nmlst2=list(nmlst1[0].values())
        #print("this is",nmlst2)
        due=nmlst1['total'] - nmlst1['paid']
        #print(due)
##        print(qs['total'])
##        print(qs.get("total"))
##        due=qs.values('total')-qs.values('paid')
##        print(due)
        #print(q.values('name'))
        va=list(nmlst[0].values())
        va2=nmlst
        
        #print(va)
        #print(va2)
        print("score 4")
        #print({'srol':va2})
        return render(request,'fees.html', {'frol':va2,'due':due})
    
    else:
        return render(request,'fees.html')


def attendance(request):
    print("attendance")
    #if request.method=="GET":
        
    #x=dict1.get("fname")
    #y=dict1.get("pwd1")
    x=0
    if request.session.has_key('username'):
      x = request.session['username']
        #print(x,y)
    qs = Attendance.objects.filter(roll_no=x)
    print("attendance 2")
    if qs.exists():
        print("attendance 3")
        nmlst = list(qs.values('date','status'))
        #print(q.values('name'))
        va=list(nmlst[0].values())
        va2=nmlst
        
        print(va)
        print(va2)
        print("score 4")
        #print({'srol':va2})
        return render(request,'attendance.html', {'arol':va2})
    
    else:
        return render(request,'attendance.html')

def tutor(request):
    if request.method=='POST':
         qs = request.POST
         print(request.POST)
         print(qs)
         a=qs.get("nname")
         b=qs.get("cname")
         c=qs.get("roll")
         d=qs.get("sub1")
         e=qs.get("sub2")
         f=qs.get("sub3")
         g=qs.get("sub4")
         h=qs.get("sub5")
         i=qs.get("sub6")
         print(a)
         print(b)
         print(c)
         print(d)
         print(e)
         print(f)
         print(g)
         print(h)
         print(i)
         mycon=sqltor.connect(host="localhost",user="root",passwd="admin",database="xyz_college")
         print("hey")
         if mycon.is_connected==False:
             print("error")
         else:
             cursor=mycon.cursor()
             x="INSERT INTO tutor(name,course,roll_no,subject_1,subject_2,subject_3,subject_4,subject_5,subject_6) VALUES('{}','{}',{},'{}','{}','{}','{}','{}','{}')".format(a,b,c,d,e,f,g,h,i)
             cursor.execute(x)
             mycon.commit()
             print("how are you?")
                
         
        
         
##         if request.POST.get('name') and request.POST.get('course'):
##                            print("hello again")
##                            post=Post()
##                            post.name=request.POST.get('name')
##                            post.save()
         return render(request,'tutor.html')
    else:
                            
        return render(request,'tutor.html')
    
    
    

    
