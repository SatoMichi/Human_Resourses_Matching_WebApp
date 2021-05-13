from django.http.response import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import *
from .models import *
from .recomend import *
from .utils import *

# Sign-in actions and pages

def sign_up(request):
    params = {
        "form":Create_User_Form()
    }
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        user = User.objects.create_user(username=username,email=email,password=password,\
                                        first_name=f_name,last_name=l_name,is_staff=True)
        user.save()
        messages.success(request,"Successfully Created Account!!")
        return redirect(to="/app/")
    else:
        return render(request,'app/register.html',params)


@login_required(login_url="admin/login")
def set_info(request):
    params = {
        "title":"Enter Information",
        "msg":"Please Enter Your Information.",
        "form":User_Profile_Form(),
    }
    # post entered info
    if request.method == "POST":
        # set profile
        profile = Profile()
        profile.owner = request.user
        profile.age = request.POST.get('age')
        profile.major = request.POST.get("major")
        profile.prog_langs = ", ".join(request.POST.getlist("prog_langs"))
        profile.comment = request.POST.get("comment")
        profile.save()
        # redirect to the profile page
        messages.success(request,"Successfully saved profile information!!")
        return redirect(to="set_image")
    else:
        return render(request,'app/set_profile.html',params)


@ login_required(login_url="/admin/login")
def set_image(request):
    params = {
        "form":Image_Upload_Form(),
    }
    # post entered info
    if request.method == "POST":
        # delete old image
        Image.objects.all().filter(owner=request.user).delete()
        # create new image
        image = Image()
        image.owner = request.user
        image.image = request.FILES.get("image")
        image.save()
        # redirect to the profile page
        messages.success(request,"Successfully Uploaded Image!!")
        return redirect(to="profile/"+str(request.user.id))
    else:
        return render(request,'app/set_image.html',params)


# web pages

@ login_required(login_url="/admin/login/")
def index(request,page=1):
    # if first login the redirect to Edit Profile
    if not Profile.objects.all().filter(owner=request.user):
        return redirect("set_profile")
    # if Edit Profile is already done
    data = [user for user in User.objects.all() if user.id is not request.user.id][1:]
    raw_list = []
    for user in data:
        if is_mutual_friend(request.user,user):
            pass
        elif is_friend(request.user,user):
            pass
        else:
            raw_list.append(user)
    recomended_list = sort_user(raw_list,request.user)
    #recomended_list = raw_list
    page_num = 10
    page_item = Paginator(recomended_list,page_num)
    page = page_item.get_page(page)
    params = {
        "login_user":request.user,
        "title":"Home",
        "msg":"List of people recomended for you listed based on recomendation algorithm.",
        "data":page,
    }
    return render(request,'app/index.html',params)


@ login_required(login_url="/admin/login/")
def profile(request,num=1):
    target = User.objects.all().filter(id=num).first()
    # own profile
    if request.user.id == num:
        email = str(request.user.email)
        edit = True
        add = False
    # mutual friend's profile
    elif is_mutual_friend(request.user,target):
        email = str(target.email)
        edit = False
        add = False
    # just one-direction (user -> target) friend's profile
    elif is_friend(request.user,target):
        email = "You added this person as Friend, BUT, This person did not add you yet."
        edit = False
        add = False
    # just one-direction (target -> user) friend's profile
    elif is_friend(target,request.user):
        email = "This person added you as Friend, BUT, You did not add this person yet."
        edit = False
        add = True
    else:
        email = "You are not Mutual Friend with this person."
        edit= False
        add = True
    params = {
        "login_user":request.user,
        "target_id":target.id,
        "title":"Personel Profile",
        "msg":"This is profile for "+str(target.first_name)+" "+str(target.last_name),
        "name":str(target.first_name)+" "+str(target.last_name),
        "email":email,
        "profile":Profile.objects.all().filter(owner=target).first(),
        "image":Image.objects.all().filter(owner=target).first(),
        "edit":edit,
        "add":add,
    }
    return render(request,'app/profile.html',params)


@ login_required(login_url="/admin/login/")
def friends(request,page=1):
    friends = Friend.objects.all().filter(owner=request.user)
    data = [f.user for f in friends]
    page_num = 10
    page_item = Paginator(data,page_num)
    page = page_item.get_page(page)
    params = {
        "login_user":request.user,
        "title":"Friends List",
        "msg":"Your friends list (people you added as friend).",
        "data":page,
    }
    return render(request,'app/friends.html',params)


@ login_required(login_url="/admin/login/")
def find(request):
    data = [user for user in User.objects.all() if user.id is not request.user.id][1:]
    params = {
        "login_user":request.user,
        "title":"Search Users",
        "msg":"Please input key words.",
        "form":Find_Form(),
        "data":data,
    }
    if request.method == "POST":
        query = request.POST.get("find")
        if query:
            data = list(User.objects.all().filter(first_name__icontains=query))
            data += list(User.objects.all().filter(last_name__icontains=query))
            data += [prof.owner for prof in Profile.objects.all().filter(major__icontains=query)]
            data += [prof.owner for prof in Profile.objects.all().filter(prog_langs__icontains=query)]
            data = [user for user in data if user.id is not request.user.id]
        else:
            pass
        params["data"] = data
        params["form"] = Find_Form(request.POST)
        return render(request,'app/find.html',params)
    else:
        return render(request,'app/find.html',params)


@ login_required(login_url="/admin/login/")
def friends_request(request):
    friends = Friend.objects.all().filter(user=request.user)
    data = []
    for friend in friends:
        if is_mutual_friend(request.user, friend.owner):
            pass
        else:
            data.append(friend.owner)
    params = {
        "login_user":request.user,
        "title":"Friends Request",
        "msg":"List of peope who added you as a friend, but you did not add.",
        "data":data,
    }
    return render(request,'app/friends_request.html',params)


# page actions

@ login_required(login_url="/admin/login/")
def edit(request):
    params = {
        "title":"Update Information",
        "msg":"Please Update Your Information.",
        "form":User_Profile_Form(),
    }
    # post entered info
    if request.method == "POST":
        # delete previous profile
        Profile.objects.all().get(owner= request.user).delete()
        # set profile
        profile = Profile()
        profile.owner = request.user
        profile.age = request.POST.get('age')
        profile.major = request.POST.get("major")
        profile.prog_langs = ", ".join(request.POST.getlist("prog_langs"))
        profile.comment = request.POST.get("comment")
        profile.save()
        # redirect to the profile page
        messages.success(request,"Successfully saved profile information!!")
        return redirect(to="profile/"+str(request.user.id))
    else:
        return render(request,'app/edit_profile.html',params)


@ login_required(login_url="/admin/login")
def add(request,num=1):
    target = User.objects.all().filter(id=num).first()
    friend = Friend()
    friend.owner = request.user
    friend.user = target
    friend.save()
    messages.success(request,"Successfully added Frined!!")
    return redirect(to="friends")


@ login_required(login_url="/admin/login/")
def delete(request,num=1):
    target = User.objects.all().filter(id=num).first()
    Friend.objects.all().filter(owner=request.user).filter(user=target).delete()
    messages.success(request,"Successfully deleted Frined!!")
    return redirect(to="friends")