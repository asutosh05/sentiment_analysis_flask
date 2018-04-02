import os
from flask import Flask, request, render_template, jsonify
import tweepy
from textblob import TextBlob
import json
from twitter import TwitterClient
app = Flask(__name__)

api = TwitterClient("@Sirjology")

def strtobool(v):
	return v.lower() in ["yes","true","t","1"]


@app.route('/')
def index():
    return render_template('index.html')
    
# @app.route('/tweets')
# def tweets():
#     query = request.args.get('query')
#     print(query)
#     public_tweets = [d._json for d in api.search(query)]
#     tweets=json.dumps(public_tweets)
#     count=len(public_tweets)
#     print(count)
#     return jsonify({'data': public_tweets, 'count':count})
@app.route('/tweets')
def tweets():
	retweets_only = request.args.get('retweets_only')
	api.set_retweet_checking(strtobool(retweets_only.lower()))
	with_sentiment = request.args.get('with_sentiment')
	api.set_with_sentiment(strtobool(with_sentiment.lower()))
	query = request.args.get('query')
	api.set_query(query)
	tweets = api.get_tweets()
	return jsonify({'data':tweets,'count':len(tweets)})


        
if __name__ == '__main__':
   app.run()