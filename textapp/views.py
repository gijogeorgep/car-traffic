# import email
from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse,HttpResponseRedirect

from .models import *
from django.contrib import messages
from django.db.models import Max, Min,Count,Sum,Avg

import numpy as np
from PIL import Image
import cv2
import tensorflow as tf
import os
from flask_cors import CORS, cross_origin
from utils.utils import decodeImage
from predict import traffic

import cv2
import tensorflow as tf

def udp(request):
    # if(request.POST):
    # email="admin@gmail.com"
    # password="admin"

    # s=Login.objects.create(username=email,password=password,usertype='admin',status='requested')
    # s.save()
    # messages.info(request,"already added")
    model_path = "Traffic.h5"
    loaded_model = tf.keras.models.load_model(model_path)
    videoCaptureObject = cv2.VideoCapture(0)
    print("****************************************************************")
    result = True
    while(True):
        ret,frame = videoCaptureObject.read()
        # ret, frame = videoCaptureObject.read() 

            # Display the resulting frame 
        cv2.imshow('frame', frame) 
        # cv2.imwrite("NewPicture.jpg",frame)
        result = False 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            cv2.imwrite("NewPicture.jpg",frame)
            break
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    imagename = "NewPicture.jpg"
    image = cv2.imread(imagename)
    print(image)
    print("****************************************************************")

    image_fromarray = Image.fromarray(image, 'RGB')
    resize_image = image_fromarray.resize((30, 30))
    print("****************************************************************")

    expand_input = np.expand_dims(resize_image,axis=0)
    input_data = np.array(expand_input)
    input_data = input_data/255
    pred = loaded_model.predict(input_data)
    result = pred.argmax()
    print("****************************************************************")

    print(result)
    if result == 0:
        prediction = 'Speed limit (20km/h)'
        print("image",prediction)
    elif result == 1:
        prediction = 'Speed limit (30km/h)'
        print("image",prediction)
    elif result == 2:
        prediction = 'Speed limit (50km/h)'
        print("image",prediction)
    elif result == 3:
        prediction = 'Speed limit (60km/h)'
        print("image",prediction)
    elif result == 4:
        prediction = 'Speed limit (70km/h)'
        print("image",prediction)
    elif result == 5:
        prediction = 'Speed limit (80km/h)'
        print("image",prediction)
    elif result == 6:
        prediction = 'End of speed limit (80km/h)'
        print("image",prediction)
    elif result == 7:
        prediction = 'Speed limit (1000km/h)'
        print("image",prediction)
    elif result == 8:
        prediction = 'Speed limit (120km/h)'
        print("image",prediction)
    elif result == 9:
        prediction = 'No passing'
        print("image",prediction)
    elif result == 10:
        prediction = 'No passing veh over 3.5 tons'
        print("image",prediction)
    elif result == 11:
        prediction = 'Right-of-way at intersection'
        print("image",prediction)
    elif result == 12:
        prediction = 'Priority road'
        print("image",prediction)
    elif result == 13:
        prediction = 'Yield'
        print("image",prediction)
    elif result == 14:
        prediction = 'Stop'
        print("image",prediction)
    elif result == 15:
        prediction = 'No vehicles'
        print("image",prediction)
    elif result == 16:
        prediction = 'Veh > 3.5 tons prohibited'
        print("image",prediction)
    elif result == 17:
        prediction = 'No entry'
        print("image",prediction)
    elif result == 18:
        prediction = 'General caution'
        print("image",prediction)
    elif result == 19:
        prediction = 'Dangerous curve left'
        print("image",prediction)
    elif result == 20:
        prediction = 'Dangerous curve right'
        print("image",prediction)
    elif result == 21:
        prediction = 'Double curve'
        print("image",prediction)
    elif result == 22:
        prediction = 'Bumpy road'
        print("image",prediction)
    elif result == 23:
        prediction = 'Slippery road'
        print("image",prediction)
    elif result == 24:
        prediction = 'Road narrows on the right'
        print("image",prediction)
    elif result == 25:
        prediction = 'Road work'
        print("image",prediction)
    elif result == 26:
        prediction = 'Traffic signals'
        print("image",prediction)
    elif result == 27:
        prediction = 'Pedestrians'
        print("image",prediction)
    elif result == 28:
        prediction = 'Children crossing'
        print("image",prediction)
    elif result == 29:
        prediction = 'Bicycles crossing'
        print("image",prediction)
    elif result == 30:
        prediction = 'Beware of ice/snow'
        print("image",prediction)
    elif result == 31:
        prediction = 'Wild animals crossing'
        print("image",prediction)
    elif result == 32:
        prediction = 'End speed + passing limits'
        print("image",prediction)
    elif result == 33:
        prediction = 'Turn right ahead'
        print("image",prediction)
    elif result == 34:
        prediction = 'Turn left ahead'
        print("image",prediction)
    elif result == 35:
        prediction = 'Ahead only'
        print("image",prediction)
    elif result == 36:
        prediction = 'Go straight or right'
        print("image",prediction)
    elif result == 37:
        prediction = 'Go straight or left'
        print("image",prediction)
    elif result == 38:
        prediction = 'Keep right'
        print("image",prediction)
    elif result == 39:
        prediction = 'Keep left'
        print("image",prediction)
    elif result == 40:
        prediction = 'Roundabout mandatory'
        print("image",prediction)
    elif result == 41:
        prediction = 'End of no passing'
        print("image",prediction)
    elif result == 42:
        prediction = 'End no passing veh > 3.5 tons'
        print("image",prediction)
    import pyttsx3;
    engine = pyttsx3.init()
    engine.say(prediction)
    engine.runAndWait()
    return render(request,"user/prediction.html",{"prediction":prediction})
    


    return HttpResponseRedirect("/prediction")

def Drowsiness(request):
    import finalintegration
    return render(request,"user/prediction.html")
from django.core.files.storage import FileSystemStorage

def imagebyenter(request):
    if request.POST:
        image=request.FILES['image']
        fs=FileSystemStorage()
        filename=fs.save(image.name,image)
        fileurl=fs.url(filename)

        model_path = "Traffic.h5"
        loaded_model = tf.keras.models.load_model(model_path)

        imagename = image
        print(fileurl)
        image = cv2.imread("D:/project sample/car traffic/textapp/static"+fileurl)

        image_fromarray = Image.fromarray(image, 'RGB')
        resize_image = image_fromarray.resize((30, 30))
        expand_input = np.expand_dims(resize_image,axis=0)
        input_data = np.array(expand_input)
        input_data = input_data/255
        pred = loaded_model.predict(input_data)
        result = pred.argmax()

        
        if result == 0:
            prediction = 'Speed limit (20km/h)'
            print("image",prediction)
        elif result == 1:
            prediction = 'Speed limit (30km/h)'
            print("image",prediction)
        elif result == 2:
            prediction = 'Speed limit (50km/h)'
            print("image",prediction)
        elif result == 3:
            prediction = 'Speed limit (60km/h)'
            print("image",prediction)
        elif result == 4:
            prediction = 'Speed limit (70km/h)'
            print("image",prediction)
        elif result == 5:
            prediction = 'Speed limit (80km/h)'
            print("image",prediction)
        elif result == 6:
            prediction = 'End of speed limit (80km/h)'
            print("image",prediction)
        elif result == 7:
            prediction = 'Speed limit (1000km/h)'
            print("image",prediction)
        elif result == 8:
            prediction = 'Speed limit (120km/h)'
            print("image",prediction)
        elif result == 9:
            prediction = 'No passing'
            print("image",prediction)
        elif result == 10:
            prediction = 'No passing veh over 3.5 tons'
            print("image",prediction)
        elif result == 11:
            prediction = 'Right-of-way at intersection'
            print("image",prediction)
        elif result == 12:
            prediction = 'Priority road'
            print("image",prediction)
        elif result == 13:
            prediction = 'Yield'
            print("image",prediction)
        elif result == 14:
            prediction = 'Stop'
            print("image",prediction)
        elif result == 15:
            prediction = 'No vehicles'
            print("image",prediction)
        elif result == 16:
            prediction = 'Veh > 3.5 tons prohibited'
            print("image",prediction)
        elif result == 17:
            prediction = 'No entry'
            print("image",prediction)
        elif result == 18:
            prediction = 'General caution'
            print("image",prediction)
        elif result == 19:
            prediction='no parking'
            print("image",prediction)
        elif result == 19:
            prediction = 'Dangerous curve left'
            print("image",prediction)
        elif result == 20:
            prediction = 'Dangerous curve right'
            print("image",prediction)
        elif result == 21:
            prediction = 'Double curve'
            print("image",prediction)
        elif result == 22:
            prediction = 'Bumpy road'
            print("image",prediction)
        elif result == 23:
            prediction = 'Slippery road'
            print("image",prediction)
        elif result == 24:
            prediction = 'Road narrows on the right'
            print("image",prediction)
        elif result == 25:
            prediction = 'Road work'
            print("image",prediction)
        elif result == 26:
            prediction = 'Traffic signals'
            print("image",prediction)
        elif result == 27:
            prediction = 'Pedestrians'
            print("image",prediction)
        elif result == 28:
            prediction = 'Children crossing'
            print("image",prediction)
        elif result == 29:
            prediction = 'Bicycles crossing'
            print("image",prediction)
        elif result == 30:
            prediction = 'Beware of ice/snow'
            print("image",prediction)
        elif result == 31:
            prediction = 'Wild animals crossing'
            print("image",prediction)
        elif result == 32:
            prediction = 'End speed + passing limits'
            print("image",prediction)
        elif result == 33:
            prediction = 'Turn right ahead'
            print("image",prediction)
        elif result == 34:
            prediction = 'Turn left ahead'
            print("image",prediction)
        elif result == 35:
            prediction = 'Ahead only'
            print("image",prediction)
        elif result == 36:
            prediction = 'Go straight or right'
            print("image",prediction)
        elif result == 37:
            prediction = 'Go straight or left'
            print("image",prediction)
        elif result == 38:
            prediction = 'Keep right'
            print("image",prediction)
        elif result == 39:
            prediction = 'Keep left'
            print("image",prediction)
        elif result == 40:
            prediction = 'Roundabout mandatory'
            print("image",prediction)
        elif result == 41:
            prediction = 'End of no passing'
            print("image",prediction)
        elif result == 42:
            prediction = 'End no passing veh > 3.5 tons'
            print("image",prediction)
        return render(request,"user/prediction.html",{"prediction":prediction})
        
    import pyttsx3;
    engine = pyttsx3.init()
    engine.say(prediction)
    engine.runAndWait()
    return render(request,"user/enterimage.html")
    
def predict(request):

    return render(request,"user/prediction.html")





def registration(request):
    if request.POST:
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phoneno"]
        address=request.POST["address"]
        username=request.POST["username"]
        dob=request.POST["dob"]
        password=request.POST["password"]
        img=request.FILES["img"]
       
        if not Login.objects.filter(username=email).exists():
                login=Login.objects.create(username=username,password=password,usertype='user',status='approved')
                login.save()

                obj=Userregistration.objects.create(name=name,email=email,address=address,phone=phone,dob=dob,uname=username,img=img)
                obj.save
                # message.info(request,"user added successfully")
    return render(request,"common/registration.html")

def index(request):
    return render(request,"common/index.html")


def About(request):
    return render(request,"common/About.html")

def adminhome(request):
    return render(request,"admin/index.html")

def userhome(request):
    return render(request,"user/index.html")

def driverhome(request):
    return render(request,"driver/index.html")

def driverreg(request):
    if request.POST:
        name=request.POST.get("name")
        address=request.POST.get("address")
        contact=request.POST.get("contact")
        email=request.POST.get("email")
        password=request.POST.get("password")
        
        s=Driver.objects.create(dname=name,daddress=address,dcontact=contact,demail=email,dpassword=password)
        s.save()
        did=Driver.objects.aggregate(Max('id'))
        print(did)
        did=did['id__max']
        did=Driver.objects.get(id=did)
        print(did)

    # print(mark)
        s=Login.objects.create(username=email,password=password,usertype='driver',status='requested',driverid=did)
        s.save()
        messages.info(request,"already added")
    return render(request,"common/driverreg.html")



def userreg(request):
    if request.POST:
        name=request.POST.get("name")
        address=request.POST.get("address")
        username=request.POST["username"]
        contact=request.POST.get("contact")
        email=request.POST.get("email")
        password=request.POST.get("password")
        img=request.POST.get(img)
        
        s=User.objects.create(uname=name,uaddress=address,ucontact=contact,uemail=email,upassword=password)
        s.save()
        s=Login.objects.create(username=username,password=password,usertype='user',status='requested')
        s.save()
        messages.info(request,"already added")
    return render(request,"common/userreg.html")




def logins(request):
    msg=""
    if request.POST:
        try:
            name=request.POST.get("username")
            password=request.POST.get("password")
            request.session["uname"]=name
            s=Login.objects.get(username=name,password=password)
            if s.usertype=='admin':
                return HttpResponseRedirect("/adminhome")
            elif s.usertype=='user':
                s=Login.objects.get(username=name)
                id=s.id
                request.session['uid']=id

                return HttpResponseRedirect("/userhome")
            elif s.usertype=='driver':
                s=Driver.objects.get(demail=name)
                id=s.id
                request.session['did']=id

                return HttpResponseRedirect("/driverhome")
            else: 
                msg="invalid Username Or password"
        except:
            msg="invalid Username Or password"
    return render(request,"common/login.html",{"msg":msg})




def adminviewdriver(request):  
    s=Driver.objects.filter(status='')
    print(s)
    if request.GET:
        id=request.GET.get("id")
        s=Driver.objects.get(id=id)
        username=s.demail
        s=Login.objects.filter(username=username).update(status='approved')
        s=Driver.objects.filter(id=id).update(status='approved')
        return HttpResponseRedirect("/adminviewdriver")
    return render(request,"admin/viewdriver.html",{"data":s})


def adminviewuser(request):  
    s=User.objects.all()
    print(s)
    return render(request,"admin/viewuser.html",{"data":s})
def profile(request):  
    s=Userregistration.objects.filter(uname=request.session["uname"])
    print(s)
    return render(request,"user/profile.html",{"data":s})

def userviewdriver(request):  
    s=Driver.objects.all()
    uid=request.session['uid']
    if request.GET:
        id=request.GET.get("id")
        driverdetails=Driver.objects.get(id=id)
        userdetails=User.objects.get(id=uid)
        import datetime
        date=datetime.datetime.now()
        s=Booking.objects.create(uid=userdetails,did=driverdetails,date=date,status='requested')
        return HttpResponseRedirect("/userviewdriver")
    return render(request,"user/viewdriver.html",{"data":s})




def userviewbooking(request):  

    uid=request.session['uid']
    select=Booking.objects.filter(uid=uid)
    return render(request,"user/viewbooking.html",{"data":select})




def driverviewbooking(request):  
    uid=request.session['did']
    print(uid)
    select=Booking.objects.filter(did=uid)
    print(select)
    abcd='approved'
    if request.GET:
        id=request.GET.get("id")
        select=Booking.objects.filter(id=id).update(status='approved')
        return HttpResponseRedirect("/driverhome")
        
    return render(request,"driver/viewbooking.html",{"data":select,"abcd":abcd})




def ddetection(request):
    from textapp import cd
    return HttpResponseRedirect("/userhome")




def driverdetection(request):
    from textapp import cd
    return HttpResponseRedirect("/driverhome")















































# def addstudent(request):
#     if request.POST:
#         fname=request.POST.get("fname")
#         age=request.POST.get("age")
#         gender=request.POST.get("gender")
#         profile=request.FILES.get("img")
#         s=Student.objects.create(fname=fname,age=age,gender=gender,profile=profile)
#         s.save()
#         messages.info(request,"already added")
#     return render(request,"students.html")

# from django.db import connection

# from django.db.models import Q
# def viewstudent(request):
#     s=Student.objects.all()
#     print(s)
#     for i in s:
#         print(i.fname)
#     print(connection.queries)
#     t=Student.objects.get(id=2)
#     u=t
#     print(t)
#     print(t.fname)

#     t=Student.objects.filter(id=2,fname='manu')
#     print(t)
#     # print(t.fname)
#     for i in t:
#         print(i.fname)

#     t=Student.objects.filter(Q(id=2)| Q(fname='manu'))
#     print("*"*100)
#     print(t)
#     for i in t:
#         print(i.fname)
#     print("*"*100)

#     return render(request,"students.html",{'s':s,'t':t,'u':u})



# def updates(request):
#     s=Student.objects.get(id=2).update(fname='binimol')
#     s.save()
#     s=Student.objects.filter(fname='arjun').update(fname='binimol')
#     s.save()
#     return HttpResponse("hello")




# def deletes(request):
#     s=Student.objects.get(id=2).delete()
    
#     s=Student.objects.filter(fname='arjun').delete()
    
#     ##########    OR  ############
#     s=Student.objects.filter(fname='anu')
#     s.delete()
#     return HttpResponse("hello")


# def orderbyquery(request):
#     s=Student.objects.filter(fname='binimol').order_by('id')  ## Assending Order
#     s=Student.objects.filter(fname='binimol').order_by('_id')# desending order
#     return HttpResponse("hello")







# def marks(request):
#     # id=request.session['id']
#     id=1
#     if request.POST:
#         mark1=request.POST.get("mark1")
#         mark2=request.POST.get("mark2")
#         mark3=request.POST.get("mark3")
#         mark4=request.POST.get("mark4")
#         id=1
#         apl=Student.objects.get(id=1)
#         s=Mark.objects.create(mark1=mark1,mark2=mark2,mark3=mark3,mark4=mark4,studid=apl)
#         s.save()
#     return render(request,"mark.html")


# # def viewmark(request):
# #     s=Mark.objects.all()
# #     return render(request,"mark.html",{"mark":s})


# from django.db.models import Max, Min,Count,Sum,Avg


# def viewmark(request):
#     s=Mark.objects.aggregate(Min('mark1'))
#     print(s)
#     # print(mark)
#     return render(request,"mark.html",{"mark":s})

# # from django.contrib.auth.models import User



# # def adduser(request):
# #     # id=request.session['id']
# #     u=User.objects.create_user(first_name='jk',last_name='lm',username='dsdsds')
# #     u.save()
# #     # return render(request,"mark.html")
# #     return HttpResponse("hello")

# # from django.contrib.auth.models import authenticate,logout



# # def checkuser(request):
# #     # id=request.session['id']
# #     u=authenticate(username='hello',password='hjk')
# #     if u is not None:
# #         print("dkshdfsfshjf")
# #     else:
# #         print("jkashdajkh")
# #     # return render(request,"mark.html")
# #     return HttpResponse("hello")





# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# # from .forms import studreg
# # def reg(request):
# #     if request.POST:
# #         fm=studreg(request.POST)
# #         if fm.is_valid():
# #             fm.save()
# #     else:
# #         fm=studreg()
# #     return render(request,"hello.html",{"fm":fm})