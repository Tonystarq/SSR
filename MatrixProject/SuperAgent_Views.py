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
import csv
import datetime


@login_required(login_url='/')
def Home(request):
    '''This is the Agent Home function.
    In this function when someone open the url of Agent_Home, it will return the AGENT/home.html page.
    The user will be able to see things which are available for agent only.
    The sidebar, footer, header are linked acoording to agent only.'''
    

    
    book_plot_count1 = BookPlot.objects.filter(owner=request.user.id).count
    plot_count1 = AddPlot.objects.all().count
    customer_count1 = Customer.objects.filter(owner=request.user.id).count
    
    agent_count1 = SuperAgent.objects.filter(admin=request.user.id).count
    

    return render(request, 'AGENT/home.html',{'agent_count1':agent_count1,'book_plot_count1':book_plot_count1,'plot_count1':plot_count1,"customer_count1":customer_count1})

@login_required
def AgentADD_USER(request):
    '''
    This is the Agent ADD USER function.
    According to this function when an agent will go through the url of add customer with SSR then Agent will go to the AGENT/add_user.html file.
    In that html the POST function works on a form and save the detail of new customer in database of Customer Table.
    The post method also return the same form of creating new customer if the customer id matches with any previous customer id in database.
    
    '''
    if request.method == "POST":
        cust_id = request.POST.get('cust_id')
        name = request.POST.get('name')
        father_name = request.POST.get('father_name')
        mob_no = request.POST.get('mob_no')

        customer =  Customer(customer_id=cust_id,customer_name=name,cust_father_name=father_name,cust_mobileno=mob_no)
        
        if Customer.objects.filter(customer_id = cust_id).exists():
            messages.warning(request, "Customer Id is already Taken")
            return redirect('agentadd_user')
            
        owner=customer.owner=request.user
        customer.owner = owner
        customer.save()
        messages.success(request, "Customer ID Added Successfully !!")

        print(cust_id)

    return render(request,'AGENT/add_user.html')

@login_required(login_url='/')
def  Agent_bookplot(request):

    '''
    The Agent bookplot function can be used for booking plots by agent.
    According to this function when an agent will go through the url of booking plot for any customer then Agent will go to the AGENT/bookplot.html file.
    In that html the POST function works on form (previously fetched by selecting custid and plot no from database) and save the detail of new booking plot in database of BookPlot Table and in Installment Table with some less details.
    The post method also return the same form of booking a new plot if the plot Number matches with any previous plot id in database of BookPlot.
    '''

    selected_customer_id = None
    selected_plot_no = None
    customer_Id = Customer.objects.all()
    plot_no = AddPlot.objects.all()
    current_user = request.user
    code = current_user.user_id
    rank = current_user.rank
    plot_number = AddPlot.objects.all()
  
    if request.method =="POST":
        if 'newsletter_sub' in request.POST:
        
            selected_customer_id = request.POST.get("user_id")
            customer_Id = customer_Id.filter(customer_id=selected_customer_id)

            selected_plot_no = request.POST.get("plot_no")
            plot_no = plot_no.filter(plot_no=selected_plot_no)
            
        if 'demo' in request.POST:

        
            ref_id = request.POST.get('ref_id')
        
            user_id = request.POST.get('user_id')
        
            plot_number = request.POST.get('plot_number')
            amount = int(request.POST.get('amount'))
            booking_amount = int(request.POST.get('booking_amount'))
            remaining_amount = amount-booking_amount
            name = request.POST.get('name')
            father_name = request.POST.get('father_name')
            mobile_number = request.POST.get('mobile_number')
            payment_mode = request.POST.get('payment_mode')
            remarks = request.POST.get('remarks')
            receipt = request.FILES.get('receipt')
            print(ref_id)

            book_plot = BookPlot(ref_id= ref_id,user_id=user_id,plot_number = plot_number, Payable_amout = amount,payment_amount=booking_amount,remaining_amount=remaining_amount, name = name,father_name = father_name , mobile_no = mobile_number, payment_mode = payment_mode ,remarks=remarks,receipt=receipt )
            owner=book_plot.owner=request.user
           
            
            book_plot.owner = owner


            isntallment = Installment(ref_id= ref_id,user_id=user_id,plot_number = plot_number, Payable_amout = amount,payment_amount = booking_amount,remaining_amount=remaining_amount,name = name, mobile_no = mobile_number, payment_mode = payment_mode ,remarks=remarks,receipt=receipt )
            owner=isntallment.owner=request.user
            isntallment.owner = owner


            if BookPlot.objects.filter(plot_number = plot_number).exists():
                messages.warning(request, "Plot Number is already Taken")
                return redirect('Agent_bookplot')
            
            
            book_plot.save()
            isntallment.save()
            messages.success(request,"Booking Plot Successfully")
            return redirect('Agent_bookplot')
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

    }
    return render(request, 'AGENT/bookplot.html', context)

def  installment_detail(request):

    '''
    The Agent installment_detail function can be used for booking Installment of any plot previously booked by agent or HOD.
    According to this function when an agent will go through the url of booking Installment for any customer of a particular plot then Agent wiil go to the AGENT/installmentdetail.html file.
    In that html the POST function works on form(previously fetched by entering plotno) and save the detail of new booking installment of a plot in database of  Installment Table.
    '''

    selected_customer_id = None
    selected_plot_no = None
    customer_Id = Customer.objects.all()
    plot_no = AddPlot.objects.all()
    current_user = request.user
    code = current_user.user_id
    
    rank = current_user.rank

    plot_number = AddPlot.objects.all()
  
    

    if request.method =="POST":
        if 'newsletter_sub' in request.POST:
        
            selected_customer_id = request.POST.get("user_id")
            customer_Id = customer_Id.filter(customer_id=selected_customer_id)

            selected_plot_no = request.POST.get("plot_no")
            plot_no = plot_no.filter(plot_no=selected_plot_no)
            
        if 'demo' in request.POST:

        
            ref_id = request.POST.get('ref_id')
        
            user_id = request.POST.get('user_id')
        
            plot_number = request.POST.get('plot_number')
            amount = request.POST.get('amount')
           
            name = request.POST.get('name')
            father_name = request.POST.get('father_name')
            mobile_number = request.POST.get('mobile_number')
            payment_mode = request.POST.get('payment_mode')
            remarks = request.POST.get('remarks')
            receipt = request.FILES.get('receipt')
            print(ref_id)

            book_plot = Installment(ref_id= ref_id,user_id=user_id,plot_number = plot_number, Payable_amout = amount, name = name,father_name = father_name , mobile_no = mobile_number, payment_mode = payment_mode ,remarks=remarks,receipt=receipt )
            book_plot.save()
            messages.success(request,"Installment recieved Successfully")
            return render(request, 'AGENT/installmentdetail.html')
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

    }
    return render(request, 'AGENT/installmentdetail.html',context)


def  editagentdata(request):
    return render(request, 'AGENT/editagentdata.html')
def  update_account(request):
    return render(request, 'AGENT/updateaccount.html')
def  update_password(request):
    return render(request, 'AGENT/updatepassword.html')
def  update_bank_details(request):
    return render(request, 'AGENT/update_bank_details.html')
def  income_details(request):
    return render(request, 'AGENT/income_details.html')
def  level_income(request):
    return render(request, 'AGENT/level_income.html')
def  get_in_touch(request):
    return render(request, 'AGENT/get_in_touch.html')

def  agent_profile(request):
    '''
    The agent_profile function will return the profile of a specific agent which is currently logged in on AGENT/agent_profile.html page with all the necessary information.
    '''
    current_user = request.user
    context = {
        'code': current_user
    }
    return render(request, 'AGENT/agent_profile.html', context)


def  agent_approvedplot(request):
    '''
    The agent_approvedplot function will get the requesting of viewing the booked plot by the logged in user and return the Agent/approvedplot.html.
    This function is exporting data from BookPlot according to current user user id.
    '''
    
    booking_data1 = BookPlot.objects.filter(owner=request.user.id)
    current_user = request.user
    
    Agent_code = current_user
    code = Agent_code.user_id

    
    print(booking_data1)

    context = {
        'booking_data1': booking_data1,
        'code' : code

    }  

    return render(request, 'Agent/approvedplot.html', context)
   
def  wallet_history(request):
    Funddetails1 = FundDetails.objects.filter(owner=request.user.id)
    # Funddetails1 = FundDetails.objects.all()
    current_user = request.user
    # id =current_user.id
    # print(id)

    Agent_code = current_user
    code = Agent_code.user_id

    # booking_data1 = BookPlot.objects.all()
    # booking_data1 = BookPlot.objects.filter(ref_id=agent_obj)
    print(Funddetails1)

    context = {
        'Funddetails1': Funddetails1,
        'code' : code

    }  
    return render(request, 'AGENT/wallethistory.html', context)


def customer_view1(request):
    customer = Customer.objects.filter(owner=request.user.id)
    current_user = request.user
    # id =current_user.id
    # print(id)

    Agent_code = current_user
    code = Agent_code.user_id
    context = {
        'customer' : customer,
        'code' : code
    }

    return render(request,'AGENT/customer_view1.html',context)

def customer_export_csv(request):
    response = HttpResponse(content_type = 'text/csv')
    # response['Content-Disposition'] = 'attachment; filename="Approve Po.csv"'
    response['Content-Disposition'] = 'attachment; filename= customerDetails'+ str(datetime.datetime.now())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Customer ID', 'Customer Name', "Father's Name", 'Mobile No'])
    customer = Customer.objects.all()
    for approve in customer:
        print(approve)
    
        writer.writerow(
                    [approve.customer_id, 
				approve.customer_name, 
				approve.cust_father_name, 
				approve.cust_mobileno])
           

    return response



def customer_edit1(request,id):
    
    customer = Customer.objects.filter(id=id)
    
    
    
    context = {
        'customer': customer
    }
    return render(request, 'AGENT/customer_edit1.html', context)
# def UPDATE_CUSTOMER1(request):
#     if request.method == "POST":
        
#         customer_id = request.POST.get('customer_id')
#         cust_id = request.POST.get("cust_id")
#         # cust_id = request.POST.get('cust_id')
#         name = request.POST.get('name')
#         father_name = request.POST.get('father_name')
#         mob_no = request.POST.get('mob_no')

#         # customer =  Customer(customer_id=cust_id,customer_name=name,cust_father_name=father_name,cust_mobileno=mob_no)
#         # customer = Customer.objects.get(id=customer_id)
#         customer = Customer.objects.filter(owner=request.user.id)
#         current_user = request.user
#         customer.customer_id = cust_id
#         customer.customer_name = name
#         customer.cust_father_name = father_name
#         customer.cust_mobileno = mob_no
#         Agent_code = current_user
#         code = Agent_code.user_id
#         customer.save()
#         messages.success(request, "Record Updated Add Successfully")
#         return redirect('customer_view1')
#     return render(request,"AGENT/edit_customer1")


def UPDATE_CUSTOMER1(request):
    if request.method == "POST":
        customer_id = request.POST.get('customer_id')
        cust_id = request.POST.get("cust_id")
        # cust_id = request.POST.get('cust_id')
        name = request.POST.get('name')
        father_name = request.POST.get('father_name')
        mob_no = request.POST.get('mob_no')

        # customer =  Customer(customer_id=cust_id,customer_name=name,cust_father_name=father_name,cust_mobileno=mob_no)
        customer = Customer.objects.get(id=customer_id)
        customer.customer_id = cust_id
        customer.customer_name = name
        customer.cust_father_name = father_name
        customer.cust_mobileno = mob_no
        customer.save()
        messages.success(request, "Record Updated Add Successfully")
        return redirect('customer_view1')
    return render(request,"AGENT/customer_edit1")

def DELETE_CUSTOMER1(request,id):
    
    customer = Customer.objects.get(id=id)
    # customer = CustomUser.objects.get(id=admin)
    customer.delete()
    messages.success(request,"Record are Successfully Deleted")
    return redirect('customer_view1')


def edit_bookplot1(request,id):
    bookplot = BookPlot.objects.filter(id=id)
    cust_id = Customer.objects.all()   
    plot_no = AddPlot.objects.all()  
    context = {
        'bookplot': bookplot,
        'plot_no':plot_no,
        'cust_id':cust_id
        
    }
    return render(request, 'AGENT/editbookplot1.html', context)

def update_bookplot1(request):
    if request.method == "POST":
        bookplot_id = request.POST.get('bookplot_id')
        print(bookplot_id)
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
        # print(f"ref id= {ref_id}, plot_number = {plot_number},  ")
        # print(f"reference Id = {ref_id}, Plot No = {plot_number}, amount = {amount} name = {name}, father name = {father_name}, Mobile No = {mobile_number} payment mode = {payment_mode}, remars = {remarks}, receipt = {receipt} ")  

        # book_plot = BookPlot(ref_id= ref_id,user_id=user_id,plot_number = plot_number, Payable_amout = amount,Mnthly_Installment = Mnthly_Installment, number_of_Installment = no_Installment, name = name,father_name = father_name , mobile_no = mobile_number, payment_mode = payment_mode ,remarks=remarks,receipt=receipt )
        # book_plot.save()
        # messages.success(request,"Booking Plot Successfully")

        bookplot = BookPlot.objects.get(id=bookplot_id)
       
       
        # user.save()

        bookplot.plot_number = plot_number
        bookplot.Payable_amout = amount
        bookplot.Mnthly_Installment = Mnthly_Installment
        bookplot.number_of_Installment = no_Installment
        bookplot.name = name
        bookplot.father_name = father_name
        bookplot.mobile_no = mobile_number
        bookplot.payment_mode = payment_mode
        bookplot.remarks = remarks
        bookplot.receipt = receipt
        bookplot.save()
        messages.success(request, "Record Are Successfully Updated")
        return redirect('agent_approvedplot')

        
    return render(request, 'AGENT/editbookplot1.html')    

def delete_plot1(request,id):

    plot = BookPlot.objects.get(id=id)
    
    # customer = CustomUser.objects.get(id=admin)
    
    plot.delete()
    messages.success(request,"Record are Successfully Deleted")
    return redirect('agent_approvedplot')


def VIEWInstallment1(request):
    isntallment = Installment.objects.filter(owner=request.user.id)
    # customer = Customer.objects.filter(owner=request.user.id)
    current_user = request.user
    # id =current_user.id
    # print(id)

    Agent_code = isntallment
    # code = Agent_code.user_id
    context = {
        'installment' : isntallment,
        # 'code' : code
    }

    return render(request,'AGENT/view_installment1.html',context) 

def VIEWPlotNo1(request):
    plotno = AddPlot.objects.all()
    return render(request,'AGENT/viewplotno1.html',{'plotno':plotno})      


def  ADDInstallment1(request):
    
   # selected_customer_id = None
    # selected_plot_no = None
    # customer_Id = Customer.objects.all()
    # plot_no = Installment.objects.all()
    current_user = request.user
    code = current_user.user_id
    
    rank = current_user.rank
   
    # plot_number = AddPlot.objects.all()

    if request.method =="POST":
        if 'newsletter_sub' in request.POST:
            searched = request.POST['searched']
            venues = Installment.objects.filter(plot_number__contains=searched)
            return render(request, 'AGENT/add_installment1.html',{'searched':searched,'venues':venues})
        

        # else:
        #     return render(request, 'add_installment.html',{})
        
            # selected_customer_id = request.POST.get("user_id")
            # customer_Id = customer_Id.filter(customer_id=selected_customer_id)

            # selected_plot_no = request.POST.get("plot_no")
            # plot_no = plot_no.filter(plot_number=selected_plot_no)
            # return render(request, 'HOD/bookplot.html',context)
            

        
        if 'demo' in request.POST:

        
            ref_id = request.POST.get('ref_id')
        
            user_id = request.POST.get('user_id')
        
            plot_number = request.POST.get('plot_number')
            amount = request.POST.get('amount')
            # booking_amount = int(request.POST.get('booking_amount'))
            remaining_amount = int(request.POST.get('remaining_amt'))
            payment_amt = int(request.POST.get('payment_amount'))
            remaining_amount = remaining_amount-payment_amt
            rem = remaining_amount
            # print("ddddddddddddddddddddddddd",remaining_amount)
            no_Installment = request.POST.get('no_Installment')
            name = request.POST.get('name')
           
            mobile_number = request.POST.get('mobile_number')
            payment_mode = request.POST.get('payment_mode')
            remarks = request.POST.get('remarks')
            receipt = request.FILES.get('receipt')
            # print(ref_id)
            if rem>=0:
                isntallment = Installment(ref_id= ref_id,user_id=user_id,plot_number = plot_number, Payable_amout = amount,remaining_amount=remaining_amount,payment_amount = payment_amt, name = name, mobile_no = mobile_number, payment_mode = payment_mode ,remarks=remarks,receipt=receipt )
                    
                owner=isntallment.owner=request.user
                # print("heloooooo",owner)
                isntallment.owner = owner          
                isntallment.save()
                messages.success(request,"Installment Add Successfully")
                return redirect('add_installment1')
               
               
                
            else:
                messages.warning(request, "No more Remaining Amount")
                return redirect('add_installment1')
                


           
           
        else:
            return render(request, 'AGENT/add_installment1.html',{})
    # cus_id = Customer.objects.order_by('customer_id').values_list('customer_id', flat=True)
    # plot_num = Installment.objects.order_by('plot_number').values_list('plot_number', flat=True)
        

    context = {
    'code':code,
    'rank':rank,
    # 'plot_number':plot_number,
    # 'cus_id':cus_id,
    # 'customer_Id':customer_Id,
    # 'selected_customer_id':selected_customer_id,

    # 'plot_num':plot_num,
    # 'plot_no':plot_no,
    # 'selected_plot_no':selected_plot_no
    
    # 'customer_id':customer_Id,
    

    }
    

    return render(request, 'AGENT/add_installment1.html',context)

def  memberlist1(request):
    all_user = SuperAgent.objects.filter(admin=request.user.id)
    # agent_count1 = SuperAgent.objects.filter(admin=request.user.id).count
    # firstname = all_user.username
    # print(firstname)
    context = {
        'all_user':all_user
    }
    return render(request, 'AGENT/memberlist1.html',context)




def customer_export_csv1(request):
    response = HttpResponse(content_type = 'text/csv')
    # response['Content-Disposition'] = 'attachment; filename="Approve Po.csv"'
    response['Content-Disposition'] = 'attachment; filename= customer Details'+ str(datetime.datetime.now())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Customer ID', 'Customer Name', "Father's Name", 'Mobile No'])
    customer = Customer.objects.filter(owner=request.user.id)
    
    for approve in customer:
        print(approve)
    
        writer.writerow(
                    [approve.customer_id, 
				approve.customer_name, 
				approve.cust_father_name, 
				approve.cust_mobileno])
           

    return response



def approved_export_csv1(request):
    response = HttpResponse(content_type = 'text/csv')
    # response['Content-Disposition'] = 'attachment; filename="Approve Po.csv"'
    response['Content-Disposition'] = 'attachment; filename= Booking Details'+ str(datetime.datetime.now())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Father Name', 'Plot No', 'Amount', 'Payment Mode', 'Mobile No', 'Ref Id', 'Date', 'Remarks'])
    approve_plot = BookPlot.objects.filter(owner=request.user.id)
    for approve in approve_plot:
        print(approve)
    
        writer.writerow(
                    [approve.name, 
				approve.father_name, 
				approve.plot_number, 
				approve.Payable_amout, 
				approve.payment_mode, 
				approve.mobile_no, 
				approve.ref_id, 
				approve.joinig_date, 
				approve.remarks])
           

    return response


def View_installment1_export_csv1(request):
    approve_plot = Installment.objects.filter(owner=request.user.id)
    response = HttpResponse(content_type = 'text/csv')
    # response['Content-Disposition'] = 'attachment; filename="Approve Po.csv"'
    response['Content-Disposition'] = 'attachment; filename= Installment Details'+ str(datetime.datetime.now())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Customer Name','Customer ID', 'Mobile No','Plot No', 'Plot Rate','Payment Amount' "Remaining Amount",'Payment Mode','Remarks','Date','Ref Id' ])
    # installment = Installment.objects.all()
    for approve in approve_plot:
        print(approve)
    
        writer.writerow(
                    [approve.name, 
				approve.user_id, 
				approve.mobile_no, 
				approve.plot_number, 
				approve.Payable_amout, 
				approve.remaining_amount, 
				approve.payment_amount, 
				approve.remarks, 
				approve.joinig_date, 
				approve.ref_id])
           

    return response


def wallet_history_export_csv1(request):
    response = HttpResponse(content_type = 'text/csv')
    # response['Content-Disposition'] = 'attachment; filename="Approve Po.csv"'
    response['Content-Disposition'] = 'attachment; filename= Wallet Details'+ str(datetime.datetime.now())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['User Id', 'Ref ID', 'User Name', 'Amount'])
    approve_plot = FundDetails.objects.filter(owner=request.user.id)
    for approve in approve_plot:
        print(approve)
    
        writer.writerow(
                    [approve.user_id, 
				approve.ref_id, 
				approve.user_name, 
				# approve.amount, 
				# approve.Payable_amout, 
				# approve.payment_amount, 
				# approve.remaining_amount, 
				# approve.payment_mode, 
				# approve.remarks,
                # approve.joinig_date, 
                approve.amount])
           

    return response