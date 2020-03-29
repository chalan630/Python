#coding:utf-8
import base64,base36,base58,base91,base92,base62
import binascii
import re


def base_decode(n):
    m=''
    flag=False

    try:
        if re.search('[a-e]',n):
            m=base64.b16decode(n,True)
        else:
            m=base64.b16decode(n)
    except binascii.Error:
        pass
    else:
        flag=True
        print("base16deocde:",m)
        return flag
    #'''''''''''''''''''''''''''''''''
    try:        
        m=base64.b32decode(n)
    except binascii.Error:
                pass
    else:
        flag=True
        print("base32deocde:",m)
        return flag
    #'''''''''''''''''''''''''''''''''    
    try:
        m=base58.b58decode(n)
    except    ValueError:
        pass
    else:
        m=str(m)[2:-1]
        if '\\x' in m:
            pass
        else:
            flag=True
            print("base58deocde:",m)
            mm=str(base91.decode(n))
            if '\\x' not in mm:
                print("maybe base91decode:",mm)
            return flag
    #'''''''''''''''''''''''''''''''''
    try:
        m=base62.decodebytes(n)
    except    ValueError:
        pass
    else:
        m=str(m)
        if '\\x' in m:
            pass
        else:        
            flag=True
            print("base62deocde:",m)
            return flag
    #'''''''''''''''''''''''''''''''''    
    try:
        m=base64.b64decode(n)
    except binascii.Error:
        pass
    else:
        m=str(m)
        if '\\x' in m:
            pass
        else:
            flag=True
            print("base64deocde:",m)
            return flag
    #'''''''''''''''''''''''''''''''''
    try:
        m=base64.b85decode(n)
    except ValueError:
        pass
    else:
        m=str(m)
        if '\\x' in m:
            pass
        else:    
            print("base_b85deocde:",m)
            flag=True
            return flag
    #'''''''''''''''''''''''''''''''''
    try:
        m=base64.a85decode(n)
    except ValueError:
        pass
    else:
        m=str(m)
        if '\\x' in m:
            pass
        else:
            print("base_a85deocde:",m)
            flag=True
            return flag
    #'''''''''''''''''''''''''''''''''
    try:
        m=base91.decode(n)    
    except ValueError:
        pass
    else:
        m=str(m)
        if '\\x' in m:
            pass
        else:
            print("base91deocde:",m)
            flag=True
            return flag
    #'''''''''''''''''''''''''''''''''
    try:
        m=base92.decode(n)
    except ValueError:
        pass
    else:
        flag=True
        print("base92deocde:",m)
        with open('1.txt','w',encoding='utf-8') as f:
            f.write(m)
        return flag
    return flag
    #'''''''''''''''''''''''''''''''''


if __name__=='__main__':
    print("******There are no base36 and base128******")
    while(1):
        x=input("input the string(q to quit):")

        if x=='q':
            break
        a=base_decode(x)
        if a==True:
            print('\n')
        else:
            print("Fail")
