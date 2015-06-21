require('twitteR')
# setup oauth
source('auth.R')

# searchTwitter('mecate', geocode='40.7361,-73.9901,5km',  n=5000, retryOnRateLimit=1)
tweetList <- searchTwitter('mecate',  n=5000, retryOnRateLimit=1)
tweetDataFrame <- twListToDF(tweetList)
dim(tweetDataFrame)
names(tweetDataFrame)


# For reading the stream
library(streamR)
# in case you quit R in between load your authentication again...
# load("credentials.RData")
# filter terms
filterStream(file.name="tweets_keyword.json", track=c("mecate", "LET"), timeout=600, oauth=twitCred)
# parsing tweets into dataframe
tweets_mecate <- parseTweets("tweets_keyword.json", verbose = TRUE)
