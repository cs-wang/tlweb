#_*_ coding: utf8 _*_ 
import hashlib

MD5Fac = hashlib.md5()

def str_to_mdb5(string):
    global MD5Fac;
    MD5Fac.update(string)
    return MD5Fac.hexdigest()