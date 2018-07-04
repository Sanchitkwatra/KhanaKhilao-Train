from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import TemplateView

from Hungry_No_More.forms import VendorSignUpForm,NGOSignUpForm,VendorFoodSubmitForm
from Hungry_No_More.models import User,FoodDetails


class SignUpView(TemplateView):
    template_name='registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_vendor:
            return redirect('vendor_food_fill')
        else:
            return redirect('ngo_home')
    return render(request,'Hungry_No_More/home.html')

def ngo_home(request):
    if request.user.is_authenticated:
        if request.user.is_ngo:
            ngo_station=request.user.station
            food_list=FoodDetails.objects.filter(station=ngo_station)
            return render(request,"Hungry_No_More/ngo_home.html",{'food_list':food_list})
        else:
            return redirect('vendor_food_fill')
    return render(request, 'Hungry_No_More/home.html')
class VendorSignUpView(CreateView):
    model=User
    form_class =VendorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type']='vendor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        #form.instance.user=self.request.user
        user=form.save()
        login(self.request,user)
        return redirect('vendor_food_fill')

class NGOSignUpView(CreateView):
    model=User
    form_class=NGOSignUpForm
    template_name='registration/signup_form.html'

    def get_context_data(self,**kwargs):
        kwargs['user_type']='ngo'
        return super().get_context_data(**kwargs)

    def form_valid(self,form):
        user=form.save()
        login(self.request,user)
        return redirect('signup')

class VendorFoodSubmitView(CreateView):
    model = FoodDetails
    form_class = VendorFoodSubmitForm
    template_name = "Hungry_No_More/fooddetails_form.html"
    success_url = reverse_lazy('vendor_food_ngo_list')

    def get(self,request,*args,**kwargs):
        form=super(VendorFoodSubmitView, self).get_form()
        return render(request,self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form=self.get_form()
        if self.form_valid(form):
            if self.request.user.is_authenticated:
                food_station=form.cleaned_data['station']
                print("station: ", form.cleaned_data['station'])
                print("user: ", request.user.id)
                ngo_list=User.objects.filter(is_ngo=True )
            return render(request,"Hungry_No_More/messaged_ngolist.html",{'ngos':ngo_list,'Fstation':food_station})
        return self.form_invalid(form)

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.vendor=self.request.user
            print("station: ",self.request.POST.get('station'))
            print("user: ",self.request.user)
        return super(VendorFoodSubmitView, self).form_valid(form)
    # # def get_form_kwargs(self):
    # #     kwargs=super(VendorFoodSubmitView, self).get_form_kwargs()
    # #     kwargs.update({'current_user':self.request.user})
    # #     return kwargs

class VendorFoodSubmissionSuccessView(TemplateView):
    template_name = 'Hungry_No_More/messaged_ngolist.html'

    def __init__(self):
        super(VendorFoodSubmissionSuccessView, self).__init__()
        users=User.objects.filter(is_ngo='True')
       # print(self.request.POST.get('station'))
        for user in users:
            print(user.name)
            print(user.station)
            if user.station=='NDLS':
                print("special: ",user.name)

