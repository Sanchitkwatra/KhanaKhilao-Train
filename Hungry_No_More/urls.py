from django.urls import  path,include
from django.views.generic import ListView
from .models import FoodDetails
from Hungry_No_More import views
from .views import VendorFoodSubmitView

urlpatterns=[
path('',views.home,name='home'),
path('vendor/foodform/',views.VendorFoodSubmitView.as_view(),name='vendor_food_fill'),
path('vendor/foodform/ngo_list/',views.VendorFoodSubmissionSuccessView.as_view(),name='vendor_food_ngo_list'),
path('vendor/foodhistory/',ListView.as_view(queryset=FoodDetails.objects.all(),template_name='Hungry_No_More/vendor_history.html')),
path('ngo/ngo_home/',views.ngo_home,name='ngo_home'),
]