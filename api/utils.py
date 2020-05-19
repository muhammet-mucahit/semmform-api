from django.contrib.auth import authenticate
from account.models import User
import json
import requests
import jwt


def jwt_get_username_from_payload_handler(payload):
    auth0_id = payload.get('sub').replace("|", ".")
    authenticate(remote_user=auth0_id)
    if len(User.objects.filter(username=auth0_id).all()) < 1:
        user = User()
        user.username = auth0_id
        user.save()
    return auth0_id


def jwt_decode_token(token):
    header = jwt.get_unverified_header(token)
    jwks = requests.get('https://{}/.well-known/jwks.json'.format(
        'dev-uu11qs8p.auth0.com')).json()
    public_key = None
    for jwk in jwks['keys']:
        if jwk['kid'] == header['kid']:
            public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))

    if public_key is None:
        raise Exception('Public key not found.')

    issuer = 'https://{}/'.format('dev-uu11qs8p.auth0.com')
    return jwt.decode(token, public_key, audience='https://api.semmform.com',
                      issuer=issuer, algorithms=['RS256'])