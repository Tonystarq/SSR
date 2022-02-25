from matrixapp.seriealzers import AddPlotSerliazer,CustomerSerliazer,BookPlotSerliazer,KycSerliazer,CustomUserSerliazer,SuperAgentSerliazer#,HODSerliazer
from rest_framework.viewsets import ViewSet,ModelViewSet
from .models import HOD, Customer,AddPlot,BookPlot,Kyc,SuperAgent,CustomUser
from rest_framework.response import Response


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()     
    serializer_class  = CustomerSerliazer
     

class PlotViewSet(ModelViewSet):
    queryset = AddPlot.objects.all()     
    serializer_class  = AddPlotSerliazer
     

class BookPlotViewSet(ModelViewSet):
    queryset = BookPlot.objects.all()     
    serializer_class  = BookPlotSerliazer
     

class KYCViewSet(ModelViewSet):
    queryset = Kyc.objects.all()     
    serializer_class  = KycSerliazer
     

# class HODViewSet(ModelViewSet):
#     queryset = HOD.objects.all()     
#     serializer_class  = HODSerliazer
     

class CustomUserViewSet(ModelViewSet):
    # queryset = CustomUser.objects.all()     
    # serializer_class  = CustomUserSerliazer
    serializer_class = CustomUserSerliazer
    def get_queryset(self):
        posts = CustomUser.objects.all()
        return posts
     
    def create(self,request,*args, **kwargs):
        post_data = request.data

        new_rate = CustomUser.objects.create(username=post_data["username"],email=post_data["email"],first_name=post_data["first_name"],last_name=post_data["last_name"],user_type=post_data['user_type'],user_id=post_data['user_id'],rank=post_data["rank"],password=post_data["password"])
        # new_rate = CustomUser.objects.create(user_type=post_data["admin"]["user_type"],profile_pic=post_data["admin"]["profile_pic"],user_id=post_data["admin"]["user_id"],rank=post_data["admin"]["rank"])
        new_rate.set_password('password')
        new_rate.save()

        new_post = SuperAgent.objects.create(admin=new_rate)
        new_post.save()
        serializer = SuperAgentSerliazer(new_post)
        return Response(serializer.data)

    
     

class AgentViewSet(ModelViewSet):
    serializer_class = SuperAgentSerliazer
    def get_queryset(self):
        posts = SuperAgent.objects.all()
        return posts
     
    def create(self,request,*args, **kwargs):
        post_data = request.data

        new_rate = CustomUser.objects.create(user_type=post_data["admin"]["user_type"],profile_pic=post_data["admin"]["profile_pic"],user_id=post_data["admin"]["user_id"],rank=post_data["admin"]["rank"])
        new_rate.save()

        new_post = SuperAgent.objects.create(reference_id=post_data["reference_id"],first_name=post_data["first_name"],created_at=post_data["created_at"],updated_at=post_data["updated_at"],admin=new_rate)
        new_post.save()
        serializer = SuperAgentSerliazer(new_post)
        return Response(serializer.data)

     