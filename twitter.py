from twython import Twython
from pywordcloud import pywordcloud

TWITTER_APP_KEY = 'r5G7F451BPcsC2n4pk2hnXbDL'
TWITTER_APP_KEY_SECRET = '6TURsBrRrn3QPFNkkj2Mzpye9KcF2OgeICktXwm1duKdFHWHtS'
TWITTER_ACCESS_TOKEN = '90354135-YGxOwOqDZlz8htRC8gIXtjZTUn3s2IA9pIzbZcIM6'
TWITTER_ACCESS_TOKEN_SECRET = 'zk3EmCRNsi3cDGubq8EBUhw6bt5w6ZBwUYytARHCZKC4C'

t = Twython(app_key=TWITTER_APP_KEY,
            app_secret=TWITTER_APP_KEY_SECRET,
            oauth_token=TWITTER_ACCESS_TOKEN,
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q='#MECATE',
                  count=1000)

tweets = search['statuses']
text = ""
for tweet in tweets:
  # print tweet['user']['screen_name'], '\n', tweet['text'], '\n'
  text +=  tweet['text']

create(text,
    outfile="output.html",
    uppercase=False,
    showfreq=True,
    frequency=100,
    removepunct = False,
    minfont = 1.5,
    maxfont = 6,
    hovercolor="green",
    showborder=False,
    fontfamily='calibri',
    width="1000px",
    height="400px",
    #colorlist = ["red","blue","yellow","black","green"]
    )
