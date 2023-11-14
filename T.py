import tweepy
import csv

# Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def scrape_tweets(username):
    all_tweets = []

    # Using Tweepy Cursor to paginate through the user timeline
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=username, tweet_mode='extended').items():
        tweet_content = tweet.full_text
        profile_link = f"https://twitter.com/{username}"
        tweet_link = f"https://twitter.com/{username}/status/{tweet.id}"
        tweet_date = tweet.created_at

        all_tweets.append([tweet_content, profile_link, tweet_link, tweet_date])

    return all_tweets

def save_to_csv(tweets, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Tweet Content', 'Profile Link', 'Tweet Link', 'Tweet Date'])
        writer.writerows(tweets)

# Replace with the username of the Twitter account you want to scrape
username = 'twitter_username'

# Scrape tweets
tweets = scrape_tweets(username)

# Save to CSV
save_to_csv(tweets, f'{username}_tweets.csv')

print(f"Scraping complete. Data saved to {username}_tweets.csv.")
