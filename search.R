source('auth.R')
# searchTwitter('mecate', geocode='40.7361,-73.9901,5km',  n=5000, retryOnRateLimit=1)
head(searchTwitter('mecate',  n=5000, retryOnRateLimit=1))
