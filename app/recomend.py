import numpy as np
from .models import *

# From Profile extract Vector
def to_vector(profile):
    langs = ["Assembly Language","C","C++","C#","Java","Python","Perl","Ruby","PHP","Swift","Go","Rust","R","JavaScript"
            ,"TypeScript","Haskell","Scaler","Scheme","Elixer","Erlang","Prolog","LISP","SQL","HTML/CSS","Other"]
    vec = np.zeros(len(langs))
    prog_langs = profile.prog_langs.split(", ")
    for i,l in enumerate(langs):
        if l in prog_langs: vec[i] = 1
    return vec

# from profile return dict consist of profile inputed and its vector
# Profile -> dict
def to_vec_pro(profile):
    p = {
        "profile":profile,
        "vec":to_vector(profile),
    }
    return p

# from [Profile] return [dict] consist of profile inputed and its vector
# [Profile] -> [dict]
def to_vec_pros(profiles):
    vps = [to_vec_pro(p) for p in profiles]
    return vps

# from dict consist of vector and profile to profile
# dict -> Profile
def to_pro(d):
    return d["profile"]

# from [dict] consist of vector and profile to [Profile]
# [dict] -> [Profile]
def to_pros(ds):
    ps = [to_pro(d) for d in ds]
    return ps

# Calculate the Cos Similarity between v1 and v2
def cosSimilarity(v1,v2):
    cos = np.dot(v1,v2) / (np.linalg.norm(v1)*np.linalg.norm(v2))
    return cos

# Quick Sort Function
# return sorted [profile_dict]
# this function is recomended for use since it has no side-effects
# [dict] -> dict -> [dict]
def qsortCosSim(ps,user):
    if len(ps) == 0:
        return []
    else:
        sim = cosSimilarity(ps[0]["vec"],user["vec"])
        lessSimilar = qsortCosSim([p for p in ps[1:] if cosSimilarity(p["vec"],user["vec"]) < sim],user)
        moreSimilar = qsortCosSim([p for p in ps[1:] if cosSimilarity(p["vec"],user["vec"]) >= sim],user)
        return moreSimilar+[ps[0]]+lessSimilar

# From given User list and request_user, retrun sorted [User] based on CosSimilarity
# [User] -> User -> [User]
def sort_user(users,request_user):
    request_profile = Profile.objects.all().filter(owner=request_user).first()  # Profile
    user = to_vec_pro(request_profile)                                          # dict

    profiles = [Profile.objects.all().get(owner=u) for u in users]              # [Profile]
    vec_profiles = to_vec_pros(profiles)                                        # [dict]

    vps = qsortCosSim(vec_profiles,user)                                        # [dict]
    ps = to_pros(vps)                                                           # [Profiles]

    users = [p.owner for p in ps]                                               # [User]
    
    return users
