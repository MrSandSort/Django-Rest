from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.hashers import make_password 

def verify_access_token(token):
    if not token:
        return False or None
    try:
        accessToken= AccessToken(token=token)
        accessToken.verify()
        payload_data= accessToken.payload
        return True, payload_data

    except Exception as e:
        return False, None 
    
def hashPassword(password):
    return make_password(password=password,'' )


