import sys
import json
def hw():

    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)    # Convert the score to an integer.
    i=0
    for line in tweet_file:
        dec_line = json.loads(line)    # Decoding each line: parsing json data and returning a dictionary

        if "text" in dec_line and dec_line["lang"] == "en":    # Test if the line is a tweet, if it is written in English,
            tweet = dec_line["text"]
            enc_tweet = tweet.encode('utf-8')
            words = enc_tweet.split(" ")
            score_tw = 0
            for word in words:
                word=word.strip('.,"[]\'\n?!_-()$%^+*&/').lower()
                if word in scores:
                    #print word + " : " + str(scores[word])
                    score_tw += scores[word]
            print score_tw

def lines(fp):
    print str(len(fp.readlines()))

def main():
    global sent_file
    sent_file = open(sys.argv[1])
    global tweet_file
    tweet_file = open(sys.argv[2])
    hw()
    sent_file.seek(0)
    tweet_file.seek(0)
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
