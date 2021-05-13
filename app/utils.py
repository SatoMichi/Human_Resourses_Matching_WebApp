from django.contrib.auth.models import User
from .models import *

# user <-> target
def is_mutual_friend(user,target):
    user_target = is_friend(user,target)
    target_user = is_friend(target,user)
    return user_target and target_user
    
# user -> target
def is_friend(user,target):
    friend = Friend.objects.all().filter(owner=user).filter(user=target).first()
    if friend is not None: return True
    else: return False