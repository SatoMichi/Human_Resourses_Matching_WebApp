from django import forms
from django.contrib.auth.models import User
from .models import *

# Unused forms
class Profile_Form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["owner","age","major","prog_langs","comment"]

class Friend_Form(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ["owner","user"]

class Image_Form(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["owner","image"]


# Used forms

# for creating new User
class Create_User_Form(forms.Form):
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password",min_length=8,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name",widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name",required=False,widget=forms.TextInput(attrs={"class":"form-control"}))


# for editing (creating) new Profile
class User_Profile_Form(forms.Form):
    age = forms.IntegerField(label="age", widget=forms.NumberInput(attrs={"class":"form-control"}))
        
    professions = [("Not CS Major","Not CS Major")
                  ,("Computer Hardware","Computer Hardware")
                  ,("Computer Architecture","Computer Architecture")
                  ,("Computer Communication","Computer Communication")
                  ,("Computer Security","Computer Security")
                  ,("Computer Graphics","Computer Graphics")
                  ,("Software Engineering","Software Engineering")
                  ,("Data Science","Data Science")
                  ,("Data Base","Data Base")
                  ,("Robot Engineering","Robot Engineering")
                  ,("Machine Lerning","Machine Lerning")
                  ,("Deep Lerning","Deep Lerning")
                  ,("Theoritical Computer Science","Theoritical Computer Science")
                  ,("Others","Others")]
    major = forms.ChoiceField(label="Major area", choices=professions, widget=forms.RadioSelect())

    langs = [("Assembly Language","Assembly Language")
            ,("C","C")
            ,("C++","C++")
            ,("C#","C#")
            ,("Java","Java")
            ,("Python","Python")
            ,("Perl","Perl")
            ,("Ruby","Ruby")
            ,("PHP","PHP")
            ,("Swift","Swift")
            ,("Go","Go")
            ,("Rust","Rust")
            ,("R","R")
            ,("JavaScript","JavaScript")
            ,("TypeScript","TypeScript")
            ,("Haskell","Haskell")
            ,("Scaler","Scaler")
            ,("Scheme","Scheme")
            ,("Elixer","Elixer")
            ,("Erlang","Erlang")
            ,("Prolog","Prolog")
            ,("LISP","LISP")
            ,("SQL","SQL")
            ,("HTML/CSS","HTML/CSS")
            ,("Other","Other")]
    prog_langs = forms.MultipleChoiceField(label="Programing Language Skills", choices=langs, \
        widget=forms.CheckboxSelectMultiple(attrs={"size":len(langs)}))

    comment = forms.CharField(label="Content",max_length=300,widget=forms.Textarea(attrs={"class":"form-control","rows":3}))


# for updating Profile
class Update_Profile_Form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["owner","age","major","prog_langs","comment"]

# for uploading Image
class Image_Upload_Form(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["image"]


# for Search User
class Find_Form(forms.Form):
    find = forms.ChoiceField(label="Find", required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    