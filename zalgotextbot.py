# zalgo text bot
# author /u/Rhiknow

# praw is a library that limits the # of requests made (30 a minute),
# and makes parsing json easier
import praw
import os.path
import zalgoscraper as scraper

reddit = praw.Reddit(client_id="JxB62100dt8Fxw",
                     client_secret="wJpALkG2ueqOz_0V_m-KWZEiEMs",
                     username="zalgo-text",
                     password="zalgo-bot",
                     user_agent="zalgo-text by /u/Rhiknow")

# The subreddits the bot will live on. Can be array
subreddits = []
subreddits.append(reddit.subreddit('test'))

# How to use the bot
keyphrase = "!zalgo"

# Keep track of messages replied to, as to not have duplicates
comments_replied_to = []

def runBot():
	print("Zalgo Bot running")
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		# with command handles opening and closing of files without error handling needing to be done
		# "r" indicates reading from file
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			# Gets rid of any empty message ids. Also list() converts the filter object to a list
			comments_replied_to = list(filter(None, comments_replied_to))

	for subreddit in subreddits:
	    for comment in subreddit.stream.comments():
	    	if comment.id in comments_replied_to:
	    		continue

	    	if keyphrase == comment.body:

		        message = comment.parent().body
		        try:
		        	output = scraper.scrapeWebsite(message)
		        	print("Bot zalgo-ing: " + message)
		        	comment.reply(output)
		        	print("Successfully")
		        	comments_replied_to.append(comment.id)

		        	# Writing to file
		        	with open("comments_replied_to.txt", "w") as f:
		        		for commentId in comments_replied_to:
		        			f.write(commentId + "\n")

		        except:
		        	print("Exception thrown.")

        
runBot()


                
