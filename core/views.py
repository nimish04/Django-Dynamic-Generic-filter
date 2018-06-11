from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.http import HttpResponse
from .forms import SignUpForm, ForgotPasswordForm, ChangePasswordForm
from .tokens import account_activation_token
# from product.filters import ProductFilter
from core.forms1 import Att
from core.forms2 import Att2
# from .forms import Productip
from .filters import PackageFilter
from django.db.models import Q
from .forms import Packageip
from ast import literal_eval
from functools import reduce
from .models import *
from operator import or_
import ast


@login_required
def home(request):
    return render(request, 'core/home.html')

# def login(request):


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # current_site = get_current_site(request)
            # subject = 'Activate Your MySite Account'
            # message = render_to_string('core/account_activation_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': account_activation_token.make_token(user),
            # })
            # user.email_user(subject, message)
            #
            # return redirect('account_activation_sent')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})

# def account_activation_sent(request):
#     return render(request,'core/account_activation_sent.html')
#
# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.profile.email_confirmed = True
#         user.save()
#         login(request, user)
#         return redirect('home')
#     else:
#         return render(request, 'core/account_activation_invalid.html')

def forgot(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            return redirect('core/login')
    else:
        form=ForgotPasswordForm()
    return render(request,'core/forgot.html',{'form':form})

def change(request):
    if request.method=='POST':
        form= ChangePasswordForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_active=False
            user.save()
            return redirect ('core/login')
    else :
        form=ForgotPasswordForm()
    return render(request,'core/change.html',{'form':form})

def search(request):
    if request.GET:
        q1=request.GET
        print(q1)
        print()

        package=PackageAttribute.objects.all()
        d={}
        for obj in package:
            op1={obj.name:{'op':obj.op}}
            d.update(op1)
        # print(d)
        # print()
        # method={'price':'range','tour_type':'in','number_of_people':'range'}
        qu=dict(request.GET)

        # result=Package.objects.all()

        for key,value in qu.items():
            qu[key]={'attri':value}
        dict3={n:{**qu[n],**d[n]} for n in qu }
        print(dict3)
        result=Package.objects.all()
        print()
        print(result)
        print()


        for key, value in dict3.items():
            vls = value['attri']
            print(vls)
            print()
            if value['op'] == 'range':
                vls = [ literal_eval(vl) for vl in vls ]
                print(vls)
                print()
                cond_name = 'attributes__{}__{}'.format(key, value['op'])
                conditions = reduce(or_, [Q(**{cond_name: vl}) for vl in vls], Q())
                result = result.filter(conditions)
                print(cond_name)
                print()
                print(conditions)
                print()
                result = result.filter(conditions)
                print(result)
                print()
            else:
                result = result.filter(**{'attributes__{}__{}'.format(key, value['op']): value['attri']})
        #print(result)

        #     if method[key] == 'range':
        #         result = result.filter(**{'attributes__{}__{}'.format(key,method[key]):ast.literal_eval(value)})
        #     else :
        #         result = result.filter(**{'attributes__{}__{}'.format(key, method[key]): value})

        #     print({'attributes__{}__{}'.format(key,method[key])})
        #     print(key,value)

        # print("scscs",result)


        # data=Att2()
        package_filter=PackageFilter(request.GET,queryset=result)
        print(package_filter)
        print()
        return render(request,'core/package_list.html',{'package1': package_filter, 'filter1': Att()})

    else :
        package_list=Package.objects.all()
        package_filter=PackageFilter(request.GET,queryset=package_list)
        return render(request,'core/package_list.html',{'package1': package_filter, 'filter1': Att()})

#
# def inp(request):
#     form=request.POST
#     if request.method=='POST':
#         print(form)
#         nm=form["name"]
#         ds=form["desciption"]
#         at=form["attributes"]
#         p=Package(name=nm,desciption=ds,attributes=at)
#         print(p)
#         p.save()
#         return render(request,'core/package_list.html')
#     form1=Packageip()
#     return render(request,'core/packageip.html',{'form':form1})
