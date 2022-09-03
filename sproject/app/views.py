from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from app.models import Booking,Employee,Match,Payment,Player,Price
from django.contrib.auth.hashers import make_password
import datetime
import csv
from django.core.paginator import Paginator
import requests
from django.http import JsonResponse



# Create your views here.



def signin(request):


    if request.method == 'POST':
        username = request.POST.get('uname')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'signin.html', context)



def signout(request):
    logout(request)
    messages.success(request,"successfully logout")
    return redirect('home')
    return HttpResponse('logout')






def signup(request):
    if request.method=="POST":
        handleusername=request.POST.get('username')
        address=request.POST.get('address')
         
        email=request.POST.get('email')
        password= request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        myuser=User.objects.create(username=handleusername,email=email,password = make_password(password)) 
        if myuser:
           messages.success(request,"You are SignUp")
        else:
           messages.error(request,"Invalid Creditial")
        
        
    return render(request, 'signup.html')


def home(request):
     return render(request, 'base.html')  

def booking(request):
     
    if request.method == "POST":
         
        booker_name=request.POST.get('Bname')
        price=request.POST.get('Price')
        contactnumber=request.POST.get('Contactnumber')
        start_time=request.POST.get('Starttime')
        end_time=request.POST.get('Endtime')

        bookingExists = Booking.objects.filter(start_time=start_time)
        if bookingExists:
            messages.error(request,"Booking on the same time already exists.")    
        else:
            booking=Booking(booker_name=booker_name,price=price,contactnumber=contactnumber,start_time=start_time,end_time=end_time)
            save=booking.save()
            if booking.save()==save:
                messages.success(request,"Booking Data has been saved.")
            else:
                messages.error(request,"Booking Data hasnot been saved.")    
    return render(request, 'Booking.html')

        


def employee(request):
     
    if request.method == "POST":
         
        employee_name=request.POST.get('name')
        address=request.POST.get('address')
        citizenshipnumber=request.POST.get('Citizenshipnumber')
        contactnumber=request.POST.get('Contactnumber')
        post=request.POST.get('post')
        employee=Employee(employee_name=employee_name,address=address,citizenshipnumber=citizenshipnumber,contactnumber=contactnumber,post=post)
        save=employee.save()
        if employee.save()==save:
            messages.success(request,"Employee Data has been saved.")
        else:
            messages.error(request,"Employee Data hasnot been saved.")  
    return render(request, 'Employee.html')

def match(request):
     
    if request.method == "POST":
         
        start_time=request.POST.get('Starttime')
        price=request.POST.get('price')
        duration=request.POST.get('duration')
        end_time=request.POST.get('endtime')
        match=Match(start_time=start_time,price=price,duration=duration,end_time=end_time)
        save=match.save()
        if match.save()==save:
            messages.success(request,"Match Data has been saved.")
        else:
            messages.error(request,"Match Data hasnot been saved.")  
    return render(request, 'Match.html')

def payment(request):
     
    if request.method == "POST":
        
        teamname=request.POST.get('Teamname')  
        address=request.POST.get('address')
        email=request.POST.get('email')
        status=request.POST.get('status')
        amount=request.POST.get('amount')
        method=request.POST.get('payment_method')
        payment=Payment(status=status,amount=amount,method=method,teamname=teamname,address=address,email=email)
        save=payment.save()
        if payment.save()==save:
            messages.success(request,"Payment Data has been saved.")
        else:
            messages.error(request,"Payment Data hasnot been saved.")  
    return render(request, 'Payment.html')

def player(request):
     
    if request.method == "POST":
         
        player_Teamname=request.POST.get('teamname')
        address=request.POST.get('address')
        contactnumber=request.POST.get('Contactnumber')
        player=Player(player_Teamname=player_Teamname,address=address,contactnumber=contactnumber)
        save=player.save()
        if player.save()==save:
            messages.success(request,"Player Data has been saved.")
        else:
            messages.error(request,"Player Data hasnot been saved.")  
    return render(request, 'Player.html')

def price(request):
      
    if request.method == "POST":
         
        start_time=request.POST.get('Starttime')
        price = request.POST.get('price')
        end_time=request.POST.get('endtime')
        day=request.POST.get('day')
        price=Price(start_time=start_time,end_time=end_time,day=day,price=price)
        save=price.save()
        if price.save()==save:
            messages.success(request,"Price Data has been saved.")
        else:
            messages.error(request,"Price Data hasnot been saved.")  
    return render(request, 'Price.html')   

def Browse(request):
    return render(request, 'browse.html')

def Search(request): 
    query=request.GET.get('query','')
    data=Booking.objects.filter(booker_name__icontains=query)
    data1=Player.objects.filter(player_Teamname__icontains=query)
    data2=Employee.objects.filter(employee_name__icontains=query)
    data3=Match.objects.filter(duration__icontains=query)
    data4=Price.objects.filter(price__icontains=query)
    params={'data':data,'data1':data1,'data2':data2,'data3':data3,'data4':data4}
    return render(request, 'search.html',params)  

def Dashboard(request):
    booking=Booking.objects.all()
    price=Price.objects.all()
    player=Player.objects.all()
    employee=Employee.objects.all()
    match=Match.objects.all()
    payment=Payment.objects.all()
    context={"data":booking,"a":employee,"b":price,"mat":match,"payment":payment,"e":player}
    return render(request, 'dashboard.html',context)    

def Bookingdata(request):
    booking=Booking.objects.all()
    paginator=Paginator(booking,4)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={"data":booking,
      "page_obj":page_obj
    
    }
    return render(request, 'bookingdata.html',context) 


def Pricedata(request):
    price=Price.objects.all()
    paginator=Paginator(price,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={"data":price,"page_obj":page_obj}
    return render(request, 'pricedata.html',context) 

def Playerdata(request):
    player=Player.objects.all()
    paginator=Paginator(player,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={"data":player,"page_obj":page_obj}
    return render(request, 'playerdata.html',context) 

def Employeedata(request):
    employee=Employee.objects.all()
    paginator=Paginator(employee,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={"data":employee,"page_obj":page_obj}
    return render(request, 'employeedata.html',context) 

def Matchdata(request):
    match=Match.objects.all()
    paginator=Paginator(match,4)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={"data":match,"page_obj":page_obj}
    return render(request, 'matchdata.html',context)  


def Paymentdata(request):
    payment=Payment.objects.all()
    paginator=Paginator(payment,4)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={"data":payment,"page_obj":page_obj}
    return render(request, 'paymentdata.html',context)   



def Csv(request):

    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['booker_name', 'price', 'start_time', 'end_time','contactnumber'])
    

    for member in Booking.objects.all().values_list('booker_name', 'price', 'start_time', 'end_time','contactnumber'):
        
    
     writer.writerow(member)

    response['Content-Disposition'] = 'attachment; filename="booking.csv"'

    return response


               


def BookingDelete(request,id):
    book=Booking.objects.get(pk=id)
    book.delete()
    return redirect(Bookingdata) 

def Update(request):
    return render(request, 'update.html')

def pricetag(request):
    return render(request, 'pricetag.html')


def Schedule(request):
    data=Booking.objects.all()
    paginator=Paginator(data,4)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    content={'views':data,"page_obj":page_obj
    }
    
    return render(request, 'schedule.html',content)
    
def EmployeeDelete(request,id):
    employ=Employee.objects.get(pk=id)
    employ.delete()
    return redirect(Employeedata) 

def MatchDelete(request,id): 
    match=Match.objects.get(pk=id)
    match.delete()
    return redirect(Matchdata) 

def PlayerDelete(request,id): 
    player=Player.objects.get(pk=id)
    player.delete()
    return redirect(Playerdata)     

def PriceDelete(request,id): 
    price=Price.objects.get(pk=id)
    price.delete()
    return redirect(Pricedata)  

def EditBooking(request,id):
    booking = Booking.objects.get(pk=id)
    data=Booking.objects.all()
    contents={'views':booking,'data':data}
    return render(request,'UpdateBooking.html',contents) 

def UpdateBooking(request,id):
    booking = Booking.objects.get(pk=id)
    booking.booker_name=request.POST['Bname']
    booking.price=request.POST['Price']
    booking.contactnumber=request.POST['Contactnumber']
    booking.start_time=request.POST['Starttime']
    booking.end_time=request.POST['Endtime']
    booking.save()
    return redirect(Bookingdata)

    
def EditEmployee(request,id):
    employee = Employee.objects.get(pk=id)
    data=Employee.objects.all()
    contents={'views':employee,'data':data}
    return render(request,'UpdateEmployee.html',contents) 
   

  

def UpdateEmployee(request,id):
    employee = Employee.objects.get(pk=id)
    employee.employee_name=request.POST['name']
    employee.address=request.POST['address']
    employee.citizenshipnumber=request.POST['Citizenshipnumber']
    employee.contactnumber=request.POST['Contactnumber']
    employee.post=request.POST['post']
    employee.save()
    return redirect(Employeedata)

def EditMatch(request,id):
    match = Match.objects.get(pk=id)
    data=Match.objects.all()
    contents={'views':match,'data':data}
    return render(request,'UpdateMatch.html',contents)     
     

def UpdateMatch(request,id):
    match= Match.objects.get(pk=id)
    match.start_time=request.POST['Starttime']
    match.end_time=request.POST['endtime']
    match.duration=request.POST['duration']
    match.price=request.POST['price']
    match.save()
    return redirect(Matchdata)

def EditPrice(request,id):
    price = Price.objects.get(pk=id)
    data=Price.objects.all()
    contents={'views':price,'data':data}
    return render(request,'UpdatePrice.html',contents)
    

def UpdatePrice(request,id):
    price = Price.objects.get(pk=id)
    price.start_time=request.POST['Starttime']
    price.end_time=request.POST['endtime']
    price.price=request.POST['price']
    price.day=request.POST['day']
    price.save()
    return redirect(Pricedata)

def EditPlayer(request,id):
    player = Player.objects.get(pk=id)
    data=Player.objects.all()
    contents={'views':player,'data':data}
    return render(request,'UpdatePlayer.html',contents)
    


def UpdatePlayer(request,id):
    player = Player.objects.get(pk=id)
    player.address=request.POST['address']
    price.contactnumber=request.POST['Contactnumber']
    player.player_Teamname=request.POST['teamname']
    player.save()
    return redirect(Playerdata)                               

       
def khaltirequest(request):
    # match=Match.objects.all()
    # payment=Payment.objects.get(pk=id)
    
    # context={
    #     'match':match,
    #     'payment':payment
    
    # }
    return render(request, 'khaltirequest.html')   


       
def paymentplayer(request,id):  
    player=Player.objects.get(pk=id)
    paymentdata=Player.objects.all()

    
    context={
    'player':player,
    'paymentdata':paymentdata
    
    }
    return render(request, 'paymentplayer.html',context)  

def khaltiverify(request):
    token=request.GET.get("token")
    amount=request.GET.get("amount")
    id=request.GET.get("id")
    url = "https://khalti.com/api/v2/payment/verify/"
    payload = {
    "token": token,
    "amount": amount
    }
    headers = {
    "Authorization": "Key test_secret_key_f50cad48221049bd98813a45a2b6c5f6"
    }

    response = request.post(url, payload, headers = headers)
    resp_dict=response.json()
    if resp_dict.get("idx"):
        success=True
    
        payment=Payment(teamname=teamname,address=address,email=email,status=status,payment_method=payment_method,amount=amount)
        save=Payment.save()
    else:
      success=False
    data={
        "success":success
    }
    return JsonResponse(data)





