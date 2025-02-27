from models import *

def get_token_by_key(key_string):
    token = Token.objects.filter(key=key_string).first()
    if token and token.is_expired():
        token.delete()  # Delete expired token immediately
        return None
    return token


