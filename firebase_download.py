import pyrebase

username="danesh_gobbani"
password="danesh"

config= {
    "apiKey": "AIzaSyC6by4x4FQREB54071ovTPxN62t8hIhk6c",
    "authDomain": "pubg-14691.firebaseapp.com",
    "databaseURL": "https://pubg-14691.firebaseio.com",
    "projectId": "pubg-14691",
    "storageBucket": "pubg-14691.appspot.com",
    "messagingSenderId": "188677800701",
    "appId": "1:188677800701:web:837c150e09f56e8abcf494"
  }
fireabse=pyrebase.initialize_app(config)

storage =fireabse.storage()

path_on_cloud=f"{username}{password}/pickle/filename.pickle"

path_local="filename.pickle"



a=storage.child(path_on_cloud).download("danesh.pickle")
print(a)
print("download complete")