
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from Computers.models import Items,ItemDetails
#from .forms import CreateUserForm,LoginUserForm 
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from phone.models import Cart

# Create your views here.
def showcomputers(request):
    template = loader.get_template('showcomputers.html')
    Computer=ItemDetails.objects.select_related('itemsid')
    print(Computer.query)
    return HttpResponse(template.render({'Computer':Computer,'request':request}))


def detail(request , id):
   template = loader.get_template('detail.html')
   Computer=ItemDetails.objects.select_related('itemsid').filter(id=id)
   print(Computer.query)
   context={
       'Computer':Computer,
       'request':request
   }
   return HttpResponse(template.render(context)) 


@login_required(login_url='/auth_login/')
def checkoutt(request,id):
       template=loader.get_template('checkoutt.html')
       current_user = request.user
       print(current_user.id)
       cart=ItemDetails.objects.select_related('itemsid').filter(id=id)
       #product=Items.objects.get(id=cart.Id_prudect)
       context={
            'cart':cart,
            #'productname':product,
             'request':request
            
       }
       return HttpResponse(template.render(context=context))


def addcart(requset,id):
     currentuser=requset.user
     discount=2
     state=False
     Computer=ItemDetails.objects.select_related('itemsid').filter(id=id)
     count=0
     for item in Computer:
           net=item.total-discount
           count=count+1
     cart = Cart(
      Id_prudect=item.id,
      Id_user=currentuser.id,
      price=item.price,
      qty=item.qty,
      tax=item.tax,
      total=item.total,
      discount=discount,
      net=net,
      status=state
)
     

     currentuser=requset.user.id
     count=Cart.objects.filter(Id_user=currentuser).count()
     print(count)
     cart.save()
     requset.session['countcart']=count
     return redirect("/showcomputers")
  