from django.test import TestCase
import numpy as np
from .recomend import *

class AlgorithmTests(TestCase):

    def test_to_vec(self):
        langs = ["Assembly Language","C","C++","C#","Java","Python","Perl","Ruby","PHP","Swift","Go","Rust","R","JavaScript"
                ,"TypeScript","Haskell","Scaler","Scheme","Elixer","Erlang","Prolog","LISP","SQL","HTML/CSS","Other"]
        class Profile:
            def __init__(self,prog_langs):
                self.prog_langs = prog_langs

        profile = Profile("Assembly Language, C, C++, Python, PHP, JavaScript, SQL, HTML/CSS")
        vec1 = np.zeros(len(langs))
        vec1[0] = 1
        vec1[1] = 1
        vec1[2] = 1
        vec1[5] = 1
        vec1[8] = 1
        vec1[13] = 1
        vec1[22] = 1
        vec1[23] = 1
        vec2 = to_vector(profile)
        #print(vec1)
        #print(vec2)
        self.assertTrue((vec1==vec2).all())

    def test_cosSimilarity(self):
        vec1 = np.array([1,1,1])
        vec2 = np.array([1,1,1])
        vec3 = np.array([-1,-1,-1])
        val1 = int(cosSimilarity(vec1,vec2))
        self.assertEqual(val1,1)
        val2 = int(cosSimilarity(vec1,vec3))
        self.assertEqual(val2,-1)
