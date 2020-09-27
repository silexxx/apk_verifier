from __future__ import unicode_literals, print_function
import os

try:
    from .apkverify.check_apk import is_apk_file
    from .apkverify import ApkSignature
except (ValueError, ImportError):
    from apkverify.check_apk import is_apk_file
    from apkverify import ApkSignature


import streamlit as st

import awesome_streamlit as ast
import pyrebase
import os

#enter the firebase config here
config=" "


username_text = st.text_input('Enter username:') 
password_text = st.text_input('Enter password:')
st.write("Enter the name of the file need to publish ")

name = st.text_input('App Name')

st.write("Enter the version name ")

version = st.text_input('App version')


file_bytes = st.file_uploader("Upload a file", type=("apk"))
print(file_bytes)

def write():

    fireabse=pyrebase.initialize_app(config)

    storage =fireabse.storage()

    if (username_text!=0 and password_text!=0):

        path_on_cloud=f"{username_text}{password_text}/{name}/{version}/apk/{name}.apk"

        path_local=file_bytes

        a=storage.child(path_on_cloud).put(path_local)
        print(a)
        st.write("successfully uploaded")
    
    else:
        st.write("usename or password is empty")


def check_default():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    apk_path = os.path.join(base_dir, 'valid/input.apk')
    apk = ApkSignature(apk_path)
    print('    File: {}'.format(apk.apkpath))
    signature_version = apk.is_sigv2()
    v_auto = apk.verify()  # auto check version
    v_ver1 = apk.verify(1)  # force check version 1
    v_ver2 = apk.verify(2)  # force check version 2
    print('    Verify: {}, {}, {}, {}'.format(signature_version, v_auto, v_ver1, v_ver2))
    if signature_version==False and v_auto==True and  v_ver1==True and v_ver2 == False:

        
        write()
        st.write("apk verfication success")
    else:
        print("False")
        st.write("apk verfication failed")

    
if st.button("upload"):
    try:
        check_default()
    except:
        st.write("apk verfication failed")








    




