from twython import Twython
APP_KEY = '90d8VHEd9DjuloZSIzQxBUyk7'
APP_SECRET ='5lujhMJKtet1m2JDs5bCsVFw9COEtQybbRYefAvzb79gc7GArs'


twitter = Twython(APP_KEY, APP_SECRET)
auth = twitter.get_authentication_tokens()

OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
print (auth['auth_url'])


# I manually open this url in the browers and
# set oaut_verifier to the value like seen below.

oauth_verifier = 1136867

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

final_step = twitter.get_authorized_tokens(oauth_verifier)

FINAL_OAUTH_TOKEN = final_step['oauth_token']
FINAL_OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']

twitter = Twython(APP_KEY, APP_SECRET,
                  FINAL_OAUTH_TOKEN, FINAL_OAUTH_TOKEN_SECRET)

print (twitter.verify_credentials())
