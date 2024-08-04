import firebase_admin 
from firebase_admin import credentials, firestore, storage

cred = credentials.Certificate('firebase-adminsdk.json')
default_app = firebase_admin.initialize_app(cred,{
    'storageBucket': 'societymanagementsystem-ead0a.appspot.com'
})

db = firestore.client()

bucket = storage.bucket()
