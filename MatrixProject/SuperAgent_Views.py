from django.shortcuts import render,redirect,HttpResponse
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# from django.views.generic import TemplateView
from matrixapp import views
from MatrixProject import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .import views , HOD_Views,SuperAgent_Views
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from matrixapp.models import *
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
# from django.contrib.auth.decorators import login_required

# @login_required(login_url='/')
def Home(request):
    return render(request, 'AGENT/home.html')

@login_required(login_url='/')
def  Agent_bookplot(request):
    selected_customer_id = None
    selected_plot_no = None
    customer_Id = Customer.objects.all()
    plot_no = AddPlot.objects.all()
    current_user = request.user
    code = current_user.user_id
    
    rank = current_user.rank
   
    # context = {
    #     'code': code,
    #     'rank':rank,
    # }
    
    plot_number = AddPlot.objects.all()
   
    # print(customer_Id)
    

    
    # user_profile = HOD.objects.all()
  

  
  
    

    if request.method =="POST":
        if 'newsletter_sub' in request.POST:
        
            selected_customer_id = request.POST.get("user_id")
            customer_Id = customer_Id.filter(customer_id=selected_customer_id)

            selected_plot_no = request.POST.get("plot_no")
            plot_no = plot_no.filter(plot_no=selected_plot_no)
            # return render(request, 'HOD/bookplot.html',context)
            

        
        
        # context = {

        #     'cus_id':cus_id,
        #     'customer_Id':customer_Id,
        #     'selected_customer_id':selected_customer_id  
        # }
        # return render(request, 'HOD/bookplot.html',context)
        if 'demo' in request.POST:

        
            ref_id = request.POST.get('ref_id')
        
            user_id = request.POST.get('user_id')
        
            plot_number = request.POST.get('plot_number')
            amount = request.POST.get('amount')
            Mnthly_Installment = request.POST.get('Mnthly_installment')
            no_Installment = request.POST.get('no_Installment')
            name = request.POST.get('name')
            father_name = request.POST.get('father_name')
            mobile_number = request.POST.get('mobile_number')
            payment_mode = request.POST.get('payment_mode')
            remarks = request.POST.get('remarks')
            receipt = request.FILES.get('receipt')
            print(ref_id)

            book_plot = BookPlot(ref_id= ref_id,user_id=user_id,plot_number = plot_number, Payable_amout = amount,Mnthly_Installment = Mnthly_Installment, number_of_Installment = no_Installment, name = name,father_name = father_name , mobile_no = mobile_number, payment_mode = payment_mode ,remarks=remarks,receipt=receipt )
            book_plot.save()
            messages.success(request,"Booking Plot Successfully")
            return render(request, 'AGENT/bookplot.html')
    cus_id = Customer.objects.order_by('customer_id').values_list('customer_id', flat=True)
    plot_num = AddPlot.objects.order_by('plot_no').values_list('plot_no', flat=True)
        

    context = {
    'code':code,
    'rank':rank,
    'plot_number':plot_number,
    'cus_id':cus_id,
    'customer_Id':customer_Id,
    'selected_customer_id':selected_customer_id,
    'plot_num':plot_num,
    'plot_no':plot_no,
    'selected_plot_no':selected_plot_no
    
    # 'customer_id':customer_Id,
    

    }
    
        
    return render(request, 'AGENT/bookplot.html', context)
def  installment_detail(request):
    return render(request, 'AGENT/installmentdetail.html')
def  editagentdata(request):
    return render(request, 'AGENT/editagentdata.html')
def  update_account(request):
    return render(request, 'AGENT/updateaccount.html')
def  update_password(request):
    return render(request, 'AGENT/updatepassword.html')
def  update_bank_details(request):
    return render(request, 'AGENT/update_bank_details.html')
def  wallet_history(request):
    selected_customer_id = None
    selected_plot_no = None
    customer_Id = Customer.objects.all()
    plot_no = AddPlot.objects.all()
    current_user = request.user
    code = current_user.user_id
    
    rank = current_user.rank
   

    Funddetails1 = FundDetails.objects.all()

    context = {
        'Funddetails1': Funddetails1,
        'code' : code,
        'rank':rank,
        # 'plot_number':plot_number,
        # 'cus_id':cus_id,
        'customer_Id':customer_Id,
        'selected_customer_id':selected_customer_id,
        # 'plot_num':plot_num,
        'plot_no':plot_no,
        'selected_plot_no':selected_plot_no

    }
    return render(request, 'AGENT/wallethistory.html', context)
def  income_details(request):
    return render(request, 'AGENT/income_details.html')
def  level_income(request):
    return render(request, 'AGENT/level_income.html')
def  get_in_touch(request):
    return render(request, 'AGENT/get_in_touch.html')

def  agent_profile(request):
    # customuser = SuperAgent.objects.get()
    current_user = request.user
    context = {
        'code': current_user
    }
    return render(request, 'AGENT/agent_profile.html', context)


def  agent_approvedplot(self,request):
    # user_profile = SuperAgent.objects.get()
    # user_profile = HOD.objects.get()
    # user = self.request.user
    # adaccount_list = BookPlot.objects.filter(user=user)\
    #                      .values_list('adaccounts', flat=True)
    current_user = request.user

    Agent_code = current_user
    code = Agent_code.user_id
    # print(code)
   

    booking_data1 = BookPlot.objects.all()

    context = {
        'booking_data1': booking_data1,
        'code' : code

    }
    # approval = BookPlot.objects.all()#.order_by('uname')
    # return render(request,'show.html',)
    

    return render(request, 'Agent/approvedplot.html', context)
    # return render(request,'SuperAgent/home.html')
    