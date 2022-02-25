import json
# import requests
from multiprocessing import context

from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from matrixapp.models import SuperAgent, AddPlot,HOD,BookPlot, CustomUser, Customer,Kyc,Fundtransfer,FundDetails
from django.contrib import messages
# from django.http import HttpResponse, HttpResponseRedirect
import csv
import datetime


import MySQLdb

# import requests

# import sqlite3 as sql
# from tkinter import *
# from tkinter import ttk
# from tabulate import tabulate


     
 


@login_required(login_url='/')
def HOME(request):
    agent_count1=SuperAgent.objects.all().count()
    customer_count1 = Customer.objects.all().count()
    plot_count1 = AddPlot.objects.all().count
    book_plot_count1 = BookPlot.objects.all().count
    return render(request, 'HOD/home.html',{"agent_count":agent_count1,"customer_count1":customer_count1,'plot_count1':plot_count1,"book_plot_count1":book_plot_count1})

def  cancelledplote(request):
    return render(request, 'HOD/cancelledplote.html')

def  bookingdetails(request):
    return render(request, 'HOD/bookingdetail.html')

def  agrrement(request):
    return render(request, 'HOD/agreement.html')


def ADD_USER(request):
    if request.method == "POST":
        cust_id = request.POST.get('cust_id')
        name = request.POST.get('name')
        father_name = request.POST.get('father_name')
        mob_no = request.POST.get('mob_no')

        customer =  Customer(customer_id=cust_id,customer_name=name,cust_father_name=father_name,cust_mobileno=mob_no)
        # customer =  Customer(customer_id=cust_id)
        if Customer.objects.filter(customer_id = cust_id).exists():
            messages.warning(request, "Customer Id is already Taken")
            return redirect('add_user')
        customer.save()
        messages.success(request, "Customer ID Added Successfully !!")

        print(cust_id)

    return render(request,'HOD/add_user.html')

def CUSTOMER_VIEW(request):
    customer = Customer.objects.all()
    context = {
        'customer' : customer
    }

    return render(request,'HOD/view_customer.html',context)


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



def EDIT_CUSTOMER(request,id):
    
    customer = Customer.objects.filter(id=id)
    
    
    
    context = {
        'customer': customer
    }
    return render(request, 'HOD/customer_edit.html', context)



def  addplot(request):
    if request.method == "POST":
        plot_no = request.POST.get("plot_no")
        plot_size = request.POST.get("plot_size")
        plc_rate = request.POST.get("plc_rate")
        plc = request.POST.get("plc")
        plot_rate = request.POST.get("plot_rate")
        discount = request.POST.get("discount")
        print("plotttttt", plot_no, "plot size:", plot_size)
        # add_plot = AddPlot(plot_no= plot_no)
        # add_plot = {'plot_no':plot_no,'plot_size':plot_size, 'plc_rate':plc_rate,'plc':plc, 'plot_rate':plot_rate, 'discount': discount}
        add_plot = AddPlot(plot_no= plot_no,plot_size = plot_size, plc_rate = plc_rate,plc = plc, plot_rate = plot_rate, discount = discount)
        # headers={'Content-Type: application/json'}
       
        
        if AddPlot.objects.filter(plot_no = plot_no).exists():
            messages.warning(request, "Plot No. is already Taken")
            return redirect('addplot')
        # read = requests.post('http://127.0.0.1:8000/api/plot/',json=add_plot,headers=headers)
        
        add_plot.save()

        
    return render(request, 'HOD/addplot.html')

def VIEWPlotNo(request):
    plotno = AddPlot.objects.all()
    return render(request,'HOD/viewplotno.html',{'plotno':plotno})    


def PLOTDETAILS_export_csv(request):
    response = HttpResponse(content_type = 'text/csv')
    # response['Content-Disposition'] = 'attachment; filename="Approve Po.csv"'
    response['Content-Disposition'] = 'attachment; filename= PLOTDetails'+ str(datetime.datetime.now())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Plot No', 'Plot Size', "Plc Rate", 'Plc', 'Plot Rate', 'Discount'])
    plot = AddPlot.objects.all()
    for approve in plot:
        print(approve)
    
        writer.writerow(
                    [approve.plot_no, 
				approve.plot_size, 
				approve.plc_rate, 
				approve.plc,
				approve.plot_rate,
				approve.discount])
           

    return response



def EDIT_PlotNo(request,id): 
    plot_no = AddPlot.objects.filter(id=id)
    context = {
        'plot_no':plot_no

        
    }
    return render(request, 'HOD/edit_plotno.html', context)    
   





def UPDATE_PlotNo(request):
    if request.method == "POST":
        plot_id = request.POST.get("plot_id")
        plot_no = request.POST.get('plot_no')
        plot_size = request.POST.get('plot_size')
        plcrate = request.POST.get('plc_rate')
        plc = request.POST.get('plc')
        plot_rate = request.POST.get('plot_rate')
        discount = request.POST.get('discount')
       
        plot = AddPlot.objects.get(id=plot_id)
        plot.plot_no = plot_no
        plot.plot_size = plot_size
        plot.plc_rate = plcrate
        plot.plc = plc
        plot.plot_rate = plot_rate
        plot.discount = discount
        
       
        plot.save()
        messages.success(request, "Record Updated Add Successfully")
        return redirect('view_plotno')
    return render(request,"HOD/edit_plotno.html")


def DELETE_PlotNo(request,id):

    plot = AddPlot.objects.get(id=id)
    
    # customer = CustomUser.objects.get(id=admin)
    
    plot.delete()
    messages.success(request,"Record are Successfully Deleted")
    return redirect('view_plotno')
         

@login_required(login_url='/')
def  bookplot(request):
    # try:
    #     if request.method =="POST":

    #         searched = request.POST['searched']
    #         print(searched)
    #         venues = Customer.objects.filter(customer_id__contains=searched)
    #         return render(request, 'HOD/bookplot.html',{'searched':searched,'venues':venues})
    #     else:
    #         return render(request, 'HOD/bookplot.html',{})


    # except MultiValueDictKeyError:
    #     is_private = False
    
        
       

        
    # else:
    #     return render(request, 'HOD/bookplot.html',{})

    
   
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
            return render(request, 'HOD/bookplot.html')
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
    return render(request, 'HOD/bookplot.html', context)


def  approvedplote(request):
    # user_profile = HOD.objects.get()
    # # user_profile = HOD.objects.get()
    # hod_code = user_profile
    # code = hod_code.user_id
    # print(code)
   

    booking_data = BookPlot.objects.all()
   

    context = {
        'booking_data': booking_data,
        
        
        # 'code' : code

    }
    # approval = BookPlot.objects.all()#.order_by('uname')
    # return render(request,'show.html',)
    

    return render(request, 'HOD/approvedplote.html', context)


def EDIT_BOOKPLOT(request,id):
    bookplot = BookPlot.objects.filter(id=id)
    cust_id = Customer.objects.all()   
    plot_no = AddPlot.objects.all()  
    context = {
        'bookplot': bookplot,
        'plot_no':plot_no,
        'cust_id':cust_id
        
    }
    return render(request, 'HOD/editbookplot.html', context)


def UPDATE_CUSTOMER(request):
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
        return redirect('customer_view')
    return render(request,"HOD/edit_customer")



def DELETE_CUSTOMER(request,id):
    
    customer = Customer.objects.get(id=id)
    # customer = CustomUser.objects.get(id=admin)
    customer.delete()
    messages.success(request,"Record are Successfully Deleted")
    return redirect('customer_view')



def DELETE_PLOT(request,id):

    plot = BookPlot.objects.get(id=id)
    
    # customer = CustomUser.objects.get(id=admin)
    
    plot.delete()
    messages.success(request,"Record are Successfully Deleted")
    return redirect('approvedplote')


def SEARCH_BAR(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Customer.objects.filter(customer_id__contains=searched)

        return render(request, 'search.html',{'searched':searched,'venues':venues})
    else:
        return render(request, 'search.html',{})




def UPDATE_BOOKPLOT(request):
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
        return redirect('approvedplote')

        
    return render(request, 'HOD/edit_student.html')    



    

def  fundtransfer(request):
    return render(request, 'HOD/fundtransfer.html')

def previewfunds(request):
    booking_data = BookPlot.objects.all()
   

    context = {
        'booking_data': booking_data,
        
        
        # 'code' : code

    }
    # approval = BookPlot.objects.all()#.order_by('uname')
    # return render(request,'show.html',)
    

    

    return render(request, 'HOD/previewfunds.html',context)

def  viewfunds(request,id):
    

    ref_id = BookPlot.objects.filter(id=id)
    # print("ref id")
    # print(ref_id)
    k=(str(ref_id))
    m=(k.rfind('BookPlot:'))
    f=(m+10)
    l=(k.rfind(' '))
    useriddd=(k[f:l])
    # print("useriddd is")
    # print(useriddd)
    amounttt=(k[l+1:-3])
    # print(amounttt)
    conn = MySQLdb.connect  (user='root', password='root',
                              host='127.0.0.1',
                              database='ssrbrokerProject')

    
    useridd=useriddd
    
    amount=int(amounttt)
    if useridd==1:
        pass
    else:
        def getuserid():
            cur = conn.cursor()
            cur.execute('''SELECT user_id FROM matrixapp_customuser''')
            User_ID = cur.fetchall()
            
            i = 0
            j = 0
            l = []
            for index in User_ID:
                b = User_ID[i]
                k = (b[j])
                i += 1
                l.append(k)
            return l 

            
        userid = getuserid()
        # print("userid is")
        # print(userid)
        useridd1=useridd
        # print("useridd1 is")
        # print(useridd1)
        i=0
        p = [useridd1]
        # print("p is")
        # print(p)
        
        while i<len(userid) :

            if str(useridd1) == userid[i]:
                cur = conn.cursor()
                cur.execute(f'''SELECT matrixapp_superagent.reference_id FROM matrixapp_superagent JOIN matrixapp_customuser ON matrixapp_superagent.admin_id=matrixapp_customuser.id WHERE user_id=%s''',(useridd1,))
                refID = cur.fetchall()
                print("ref id is")
                print(refID)
                if refID==():
                    messages.success(request,"This booking is done by admin and all fund register into his account")
                    i=i+1
                else:
                    i = 0
                    j = 0
                    l = []
                    for index in refID:
                        b = refID[i]
                        k = (b[j])
                        i += 1
                        l.append(k)
                    # print("l is")
                    # print(l)
                    refidd= l[0]
                    # print(refidd)
                    useridd1=refidd
                    i=i+1
                    p.append(useridd1)
            else:
                pass
                i=i+1
            useridd = useridd1
        # print("p is")
        # print(p)
        j=0
        myTable1=[(('User_ID', 'Name', 'Rank', 'Ref_ID'),)]
        # print(myTable1)
        while j<len(p) :
            useridd2=p[j]
            # print(useridd2)
            #print(useridd2)
            cur = conn.cursor()
            cur.execute(f'''SELECT matrixapp_customuser.user_id,matrixapp_customuser.username,matrixapp_customuser.rank, matrixapp_superagent.reference_id FROM matrixapp_superagent JOIN matrixapp_customuser ON matrixapp_superagent.admin_id=matrixapp_customuser.id WHERE user_id=%s''',{useridd2})
            # cur.execute(f'''SELECT o.user_id, o.rank FROM matrixapp_customuser i.created_at, i.reference_id FROM matrixapp_superagent FROM matrixapp_customuser o LEFT JOIN matrixapp_superagent i on o.id = i.admin_id where user_id=%s''',{useridd2})            
            Data = cur.fetchall()
            # print(Data)
            myTable1.append(Data)
            
            j=j+1
        # print("my table is")
        # print(myTable1)
        myTablex=sum(myTable1,())
        myTable=list(myTablex)
        # print((myTable))
        
        i = 1
        namelist = []
        while i < len(myTable):
            z = (myTable[i])
            # print("z is")
            # print(z)
            list1 = list(z)
            # print(list1)
            c = (list1[1])
            namelist.append(c)

            i += 1
        # print("namelist is")
        # print(namelist)
        i = 1
        UserIdList = []
        while i < len(myTable):
            z = (myTable[i])
            # print(z)
            list1 = list(z)
            c = (list1[0])
            UserIdList.append(c)

            i += 1
        # print(UserIdList)

        i = 1
        RefIdlist = []
        while i < len(myTable):
            z = (myTable[i])
            # print(z)
            list1 = list(z)
            c = (list1[3])
            RefIdlist.append(c)

            i += 1
        # print(RefIdlist)


        j = 1
        ranklist1 = []
        while j < len(myTable):
            z = (myTable[j])
            list1 = list(z)
            c = (list1[2])
            ranklist1.append(c)
            j += 1
        # print(ranklist1)
        ranklist=list(reversed(ranklist1))

        k = 0
        l = 1
        finalpercentage1 = []
        while k < len(ranklist):
            if k != (len(ranklist) - 1):
                m = int(int(ranklist[k]) - int(ranklist[l]))
                finalpercentage1.append(abs(m))
                k += 1
                l += 1
            else:
                n = (int(ranklist[k]))
                finalpercentage1.append(abs(n))
                k += 1
        finalpercentage=list(reversed(finalpercentage1))
        # print(finalpercentage)


        a = 0
        while a < len(finalpercentage):
            distamount = str((finalpercentage[a] * amount) / 100)
            bina=(namelist[a] + ' whose User ID is '+UserIdList[a] + ' and Reference ID is '+RefIdlist[a] + ' will get ' + "Rs." + distamount)
            messages.success(request,bina)
            
            # fundetail = FundDetails.objects.get(id=user_id)
            fundetail = FundDetails.objects.all()
       
       
            # user.save()
            fundetail = FundDetails(user_id= UserIdList[a],ref_id=RefIdlist[a],amount = distamount, user_name = namelist[a]  )
            # book_plot.save()
            fundetail.save()
            a += 1

    context={
        "user_id":useriddd
    }

    return render(request, 'HOD/viewfunds.html',context)

def  approvedkyc(request):
   
    kycdetails = Kyc.objects.all()
    context = {
        'kycdetails' : kycdetails
    }

    return render(request,'HOD/approvedkyc.html',context)
def  approvedkyc(request):
   
    kycdetails = Kyc.objects.all()
    context = {
        'kycdetails' : kycdetails
    }

    return render(request,'HOD/approvedkyc.html',context)

def  approvedkyc(request):
   
    kycdetails = Kyc.objects.all()
    context = {
        'kycdetails' : kycdetails
    }

    return render(request,'HOD/approvedkyc.html',context)

    
def  kyc(request):
    
    customer_id = Customer.objects.all()

    context = {
        'cust_id':customer_id, 

    }
    if request.method =="POST":
        cust_id = request.POST.get('cust_id')
        accountname = request.POST.get('accountname')
        accountno=request.POST.get('accountno')
        IFSCno = request.POST.get('IFSCno')
        Pancardno = request.POST.get('Pancardno')
        print(Pancardno)
        
        kyc = Kyc(cust_id=cust_id, accountname=accountname,accountno=accountno,IFSCno=IFSCno, Pancardno=Pancardno)
        kyc.save()
        messages.success(request,"KYC Updated Successfully")  

    return render(request, 'HOD/kyc.html', context)

def EDIT_KYC(request,id):

    kyc = Kyc.objects.filter(id=id)
    cust_id = Customer.objects.all()   
    plot_no = AddPlot.objects.all()  
    context = {
        'bookplot': bookplot,
        'plot_no':plot_no,
        'cust_id':cust_id,
        'kyc':kyc
        
    }
    return render(request, 'HOD/editkyc.html', context)

def UPDATE_KYC(request):

    if request.method =="POST":
        kyc_id = request.POST.get('kyc_id')
        cust_id = request.POST.get('cust_id')
        accountname = request.POST.get('accountname')
        accountno=request.POST.get('accountno')
        IFSCno = request.POST.get('IFSCno')
        Pancardno = request.POST.get('Pancardno')
        # print(Pancardno)
        kyc = Kyc.objects.get(id=kyc_id)
        kyc.cust_id = cust_id
        kyc.accountname = accountname
        kyc.accountno = accountno
        kyc.IFSCno = IFSCno
        kyc.Pancardno = Pancardno
        
        # kyc = Kyc(cust_id=cust_id, accountname=accountname,accountno=accountno,IFSCno=IFSCno, Pancardno=Pancardno)
        kyc.save()
        messages.success(request,"KYC Updated Successfully")  
        return redirect('approvedkyc')
    return render(request,'edit_kyc')


def DELETE_KYC(request,id):

    kyc = Kyc.objects.get(id=id)
    
    # customer = CustomUser.objects.get(id=admin)
    
    kyc.delete()
    messages.success(request,"Record are Successfully Deleted")
    return redirect('approvedkyc')


def KYC_export_csv(request):
    response = HttpResponse(content_type = 'text/csv')
    # response['Content-Disposition'] = 'attachment; filename="Approve Po.csv"'
    response['Content-Disposition'] = 'attachment; filename= ALL KYC DETAILS' + str(datetime.datetime.now())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Customer ID', 'Account Name', "Account No", 'IFSC Code','Pan Card No'])
    kyc = Kyc.objects.all()
    for approve in kyc:
        print(approve)
    
        writer.writerow(
                    [approve.cust_id, 
				approve.accountname, 
				approve.accountno, 
				approve.IFSCno,
                approve.Pancardno])
           

    return response



    
def  pendingkyc(request):
    return render(request, 'HOD/pendingkyc.html')
def  rejectedkyc(request):
    return render(request, 'HOD/rejectedkyc.html')
def  memberlist(request):
    all_user = SuperAgent.objects.all()
    # firstname = all_user.username
    # print(firstname)
    context = {
        'all_user':all_user
    }
    return render(request, 'HOD/memberlist.html',context)


def memberList_export_csv(request):
    response = HttpResponse(content_type = 'text/csv')
    # response['Content-Disposition'] = 'attachment; filename="Approve Po.csv"'
    response['Content-Disposition'] = 'attachment; filename= memberlist'+ str(datetime.datetime.now())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['User Id', 'User Name', 'Mobile No', 'Email', 'Sponsor ID', 'Rank'])
    member_list = SuperAgent.objects.all()
    for approve in member_list:
        print(approve)
        writer.writerow(
            [approve.admin.user_id,
            approve.admin.username,
            '',         
            approve.admin.email,
            approve.reference_id,
            approve.admin.rank],
        )
    
        # writer.writerow(
        #             [approve.name, 
		# 		approve.father_name, 
		# 		approve.plot_number, 
		# 		approve.Payable_amout, 
		# 		approve.payment_mode, 
		# 		approve.mobile_no, 
		# 		approve.ref_id, 
		# 		approve.joinig_date, 
		# 		approve.remarks])
           

    return response


def  payplotinstallment(request):
    return render(request, 'HOD\payplotinstallment.html')
def  updateplotinstallment(request):
    return render(request, 'HOD/updateplotinstallment.html')
def  updatebookingdate(request):
    return render(request, 'HOD/updatebookingdate.html')
def  deleteplotinstallment(request):
    return render(request, 'HOD/deleteplotinstallment.html')
def  updateplotrate(request):
    return render(request, 'HOD/updateplotrate.html')
def  blockassociate(request):
    return render(request, 'HOD/blockassociate.html')
def  blockassociatelist(request):
    return render(request, 'HOD/blockassociatelist.html')
def  tokenslip(request):
    return render(request, 'HOD/tokenslip.html')
def  pendingPlot(request):
    return render(request, 'HOD/pendingplot.html')
def  updatekyc(request):
    return render(request, 'HOD/updatekyc.html')

def  installmentdetail(request):
    # Installment_data = BookPlot.objects.all()
    # context = {
    #     'Installment' : Installment_data
    # }
    return render(request, 'HOD\installmentdetail.html')
def  supportsystem(request):
    return render(request, 'HOD/supportsystem.html')
# def  userdashboard(request):
#     return render(request, 'HOD/installmentdetail.html')    

