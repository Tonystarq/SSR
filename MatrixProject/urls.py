
from email.mime import base
from django.contrib import admin
from django.db import router
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from matrixapp import views
from matrixapp import API_Views
from .import views , HOD_Views,SuperAgent_Views
router = DefaultRouter()
router.register('Customer', API_Views.CustomerViewSet,basename="Customer")
router.register('Plot', API_Views.PlotViewSet,basename="Plot")
router.register('BookPlot', API_Views.BookPlotViewSet,basename="BookPlot")
router.register('Kyc', API_Views.KYCViewSet,basename="Kyc")
# router.register('HOD', API_Views.HODViewSet,basename="HOD")
router.register('User', API_Views.CustomUserViewSet,basename="User")
router.register('Agent', API_Views.AgentViewSet,basename="Agent")
# from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

# from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    
    # path('api/',API_View.Plot_list),
    # path('api/BookPlotList/',API_View.BookPlotList),
    # path('api/KYCList/',API_View.KYCList),
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('base', views.BASE, name='base') ,
    path('base1', views.BASE1, name='base1') ,
   
    #Login Path

    # path('', views.LOGIN, name='login') ,
    path('', views.pagelogin, name='login') ,
    path('doLogin', views.doLogin, name='doLogin'),
    path('Logout', views.doLogout,name="logout"),

    #profile update 

    path('profile/', views.profile,name="profile"),
    path('profile/update', views.Profile_Update,name="profile_update"),
    path('registeruser/', views.registeruser,name="registeruser"),
    path('registeruserr/', views.registeruserr,name="registeruserr"),
    path('do_superAgent_signup',views.dosuperAgent,name="do_superAgent_signup"),
    path('do_Agent_signup',views.doAgent,name="do_Agent_signup"),


    ################################## ADDING USER ######################
    path('HOD/add_user/',HOD_Views.ADD_USER,name="add_user"),
    path('HOD/customer_view/',HOD_Views.CUSTOMER_VIEW,name="customer_view"),
    path('HOD/customer_view/export_csv/',HOD_Views.customer_export_csv,name="customer_export-csv"),
    path('HOD/customer/Edit/<str:id>', HOD_Views.EDIT_CUSTOMER,name="edit_customer"),
    path('HOD/customer/Update/', HOD_Views.UPDATE_CUSTOMER,name="update_customer"),
    path('HOD/customer/Delete/<str:id>',HOD_Views.DELETE_CUSTOMER,name="delete_customer"),
    

    # path('HOD/add_user',HodViews.ADD_USER,name="add_user")

    
    # path('approvedplote/', views.approvedplote,name="approvedplote"),
    # path('edit_approvedplote/<str:staff_id>', HodViews.edit_staff,name="edit_staff"),
    # path('editApprovePlote/<int:id>/', views.editApprovePlote.as_view(), name='editApprovePlote'),

    path('cancelledplote/',HOD_Views.cancelledplote,name="cancelledplote"),
    path('bookingdetails/', HOD_Views.bookingdetails,name="bookingdetails"),
    
    path('agrrement/', HOD_Views.agrrement,name="agrrement"),
    path('fundtransfer/', HOD_Views.fundtransfer,name="fundtransfer"),
    path('viewfunds/<str:id>', HOD_Views.viewfunds,name="viewfunds"),
    path('previewfunds/', HOD_Views.previewfunds,name="previewfunds"),


    
    path('kyc/', HOD_Views.kyc,name="kyc"),
    path('approvedkyc/', HOD_Views.approvedkyc,name="approvedkyc"),
    path('approvedkyc/export_csv/',HOD_Views.KYC_export_csv,name="kyc_export-csv"),
    path('HOD/kyc/Edit/<str:id>', HOD_Views.EDIT_KYC,name="edit_kyc"),
    path('HOD/kyc/Update/', HOD_Views.UPDATE_KYC,name="update_kyc"),
    path('HOD/kyc/Delete/<str:id>',HOD_Views.DELETE_KYC,name="delete_kyc"),
     

    
    path('pendingkyc/', HOD_Views.pendingkyc,name="pendingkyc"),
    path('rejectedkyc/', HOD_Views.rejectedkyc,name="rejectedkyc"),
    path('memberlist/', HOD_Views.memberlist,name="memberlist"),
    path('memberlist/export_csv/',HOD_Views.memberList_export_csv,name="memberlist_export-csv"),
    
    path('payplotinstallment/', HOD_Views.payplotinstallment,name="payplotinstallment"),
    path('updateplotinstallment/', HOD_Views.updateplotinstallment,name="updateplotinstallment"),
    path('updatebookingdate/', HOD_Views.updatebookingdate,name="updatebookingdate"),
    
    path('deleteplotinstallment/', HOD_Views.deleteplotinstallment,name="deleteplotinstallment"),
    path('updateplotrate/', HOD_Views.updateplotrate,name="updateplotrate"),
    
    path('blockassociate/', HOD_Views.blockassociate,name="blockassociate"),
    
    path('blockassociatelist/', views.blockassociatelist,name="blockassociatelist"),
    path('tokenslip/', views.tokenslip,name="tokenslip"),
    path('pendingPlot/', views.pendingPlot,name="pendingPlot"),
    path('updatekyc/', views.updatekyc,name="updatekyc"),
    path('installmentdetail/', views.installmentdetail,name="installmentdetail"),
    path('supportsystem/', views.supportsystem,name="supportsystem"),

    # Plot Path 

    path('HOD/bookplot/', HOD_Views.bookplot,name="bookplot"),
    path('addplot/', HOD_Views.addplot,name="addplot"),
    path('plotno/View-plotno', HOD_Views.VIEWPlotNo,name="view_plotno"),
    path('HOD/View-plotno/export_csv/',HOD_Views.PLOTDETAILS_export_csv,name="plot_export-csv"),
    path('plotno/Edit<str:id>', HOD_Views.EDIT_PlotNo,name="edit_plotno"),
    path('plotno/UPDATE', HOD_Views.UPDATE_PlotNo,name="update_plotno"),
    path('plotno/DELETE<str:id>', HOD_Views.DELETE_PlotNo,name="delete_plotno"),
   
    
    
   
    path('HOD/approvedplote/', HOD_Views.approvedplote,name="approvedplote"),
    path('HOD/bookplot/Edit/<str:id>', HOD_Views.EDIT_BOOKPLOT,name="edit_bookplot"),
    path('HOD/bookplot/Update/', HOD_Views.UPDATE_BOOKPLOT,name="update_bookplot"),
    path('HOD/bookplot/Delete/<str:id>',HOD_Views.DELETE_PLOT,name="delete_plot"),
    path('HOD/searchbar/',HOD_Views.SEARCH_BAR,name="searchbar"),
   

    path('export_csv/', views.export_csv,name="export-csv"),
    path('pendingPlot/', views.pendingPlot,name="pendingPlot"),
    

    # Hod Panel 
    path('signup_admin/',views.signup_admin,name="signup_admin"),
    path('do_admin_signup',views.do_admin_signup,name="do_admin_signup"),
    path('HOD/Home', HOD_Views.HOME, name='admin_home'),


    
    # path("signup/", views.signup_view,name="signup-view"),
    
    


     ########################## define for user url ############################

     path('Agent/Home', SuperAgent_Views.Home, name='Agent_Home') ,
     path('Agent/Agent_bookplot', SuperAgent_Views.Agent_bookplot, name='Agent_bookplot') ,
     path('Agent/installment_detail', SuperAgent_Views.installment_detail, name='installment_detail') ,
     path('Agent/update_account', SuperAgent_Views.update_account, name='update_account') ,
     path('Agent/editagentdata', SuperAgent_Views.editagentdata, name='editagentdata') ,
     path('Agent/update_password', SuperAgent_Views.update_password, name='update_password') ,
     path('Agent/update_bank_details', SuperAgent_Views.update_bank_details, name='update_bank_details') ,
     path('Agent/wallet_history', SuperAgent_Views.wallet_history, name='wallet_history') ,
     path('Agent/income_details', SuperAgent_Views.income_details, name='income_details') ,
     path('Agent/level_income', SuperAgent_Views.level_income, name='level_income') ,
     path('Agent/get_in_touch', SuperAgent_Views.get_in_touch, name='get_in_touch') ,
     path('Agent/agent_profile', SuperAgent_Views.agent_profile, name='agent_profile') ,
     path('Agent/approvedplot', SuperAgent_Views.agent_approvedplot, name='agent_approvedplot') ,
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)



if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
         path('__debug__/', include('debug_toolbar.urls')),

    ]+urlpatterns

# urlpatterns += staticfiles_urlpatterns()
   