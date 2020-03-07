import tweepy
import time

print('This is my twitter bot')

CONSUMER_KEY = '50F1C1BGp0wfw9k2SRKWtiP28'
CONSUMER_SECRECT='yFDSWxP7IWT9v6gmICEnF8r3NE2Hb060orZimjqbtSSw21qBF3'
ACCESS_KEY='1232879253059973120-tstOXKgbYSHeo0XTq00cb6F9poS9b7'
ACCESS_SECRECT='bPULLppaRAErpE0267tlPxc9YCeCZ9lXvOWYZfBXkja1q'

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRECT)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRECT)
api = tweepy.API(auth)

mentions = api.mentions_timeline()


		
		
		
FILE_NAME = 'last_seen_id.txt'

#this function retrieve the last seen id from the last_seen_id.txt file
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id
	
#this function stores the last seen id in the file
def store_last_seen_id(last_seen_id, file_name):
	f_write = open(file_name, 'w')
	f_write.write(str(last_seen_id))
	f_write.close()
	return
	
#mentions is a list, so we can iterate through it
#converting the integer into string 
#if #helloworld is found we respond with output messages
# testing id : 1233728202050281479

def reply_to_tweets():
	print('retrieving and replying to tweets....')
last_seen_id = retrieve_last_seen_id(FILE_NAME)
mentions = api.mentions_timeline(last_seen_id,tweet_mode = 'extended')

for mention in reversed(mentions):
	print(str(mention.id) + ' _ ' + mention.full_text)
	last_seen_id = mention.id
	store_last_seen_id(last_seen_id, FILE_NAME)
	if '#helloworld' in mention.full_text.lower():
		print('found #helloworld')
		api.update_status('@' + mention.user.screen_name + 
			 '#Hello world back to you.',mention.id)

while True:
	reply_to_tweets()
	time.sleep(10)

