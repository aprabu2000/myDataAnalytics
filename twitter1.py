# from twython import Twython
# import pandas as pd
# import jsons
#
# # consumer_key = 'pRBFesJMfPzYxlbMLzWlF32dy'
# # consumer_secret ='EPhjqzoOEl4UbSrUksKqqNMdUKXSVnTOgN50pMuPzL2yf1xojm'
# # access_token = '120034511-yqLgfT4fYW4aj0zEpWWBdbnJDwOgArLv78PhIUjQ'
# # access_token_secret = 'mm4UH70eMtCDneAPgm1GRLHBiK04p6AMEDbQqY3sIAXwW'
#
# # with open("/Users/prabahar/Desktop/twitter.json", "r+") as file:
#     creds = jsons.loads(file)
#
# python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
#
# query = {
#
#     'q' : 'learn Python',
#     'result_type' : 'popular',
#     'count' : 10,
#      'lang' : 'en'
# }

# Import the Twython class
from twython import Twython
import pandas as pd

# # Load credentials from json file
# with open("/Users/prabahar/Desktop/twitter.json", "r") as file:
#     creds = jsons.loads(file)
#
# # Instantiate an object
# python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

APP_KEY = 'x9OAKN9c6aN7P80o3wiMQDBL7'
APP_SECRET ='WMjYvzX4lBGbK7qlHfJ7hECQrOfSomBweYxY8gV6bZKp7dsUph'
ACCESS_TOKEN = '120034511-rKzYCStshE7GRKFHeSTuVXZZINv9bWvargc4vpZT'
ACCESS_TOKEN_SECRET = 'gb9rDAUz822o6k4S6ociMYvZJeREgS8LJk4LsDzV5bxox'

twitter = Twython(APP_KEY, ACCESS_TOKEN)
print(twitter)


# Create our query
# query = {'q': 'learn python',
#         'result_type': 'popular',
#         'count': 10,
#         'lang': 'en',
#         }
#
# print(query)

results = twitter.cursor(twitter.search, q="#Python", result_type='recent', count=25, tweet_mode='extended')


max_str_id = None
for _result in results:
    str_id = _result['id_str']
    if str_id > max_str_id:
        max_str_id = str_id

    # if tweet_mode='extended', use _result['full_text']
    text = _result['text'] if 'text' in _result else _result['full_text']

    # check if is retweet
    is_retweet = True if 'retweeted_status' in _result or 'quoted_status' in _result else False

    # generate tweet url
    user_id = _result['user']['id_str']
    username = _result['user']['screen_name']
    post_id = _result['id_str']
    url = "https://twitter.com/{}/status/{}".format(username, post_id)

    # Mon Sep 24 03:35:21 +0000 2012
    created = datetime.datetime.strptime(_result['created_at'], '%a %b %d %H:%M:%S +0000 %Y')

    # hashtags
    hashtags = [_hashtag['text'].lower() for _hashtag in _result['entities']['hashtags']]

# you might want to save max_str_id if you plan to use since_id in next query.
# df.head(5)




# dict={ 'user' :[], 'date':[], 'text':[],'favorite_count':[] }
# for status in python_tweets.search(**query)['statuses']:
#     dict_['user'].append(status['user']['screen_name'])
#     dict_['date'].append(status['created_at'])
#     dict_['text'].append(status['text'])
#     dict_['favorite_count'].append(status['favorite_count'])
#
# # Structure data in a pandas DataFrame for easier manipulation
# df = pd.DataFrame(dict_)
# df.sort_values(by='favorite_count', inplace=True, ascending=False)
# df.head(5)

