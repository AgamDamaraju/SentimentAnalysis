# List of punctuations
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# Function for removing punctuations from the word
def strip_punctuation(word):
    punct = ",".join(punctuation_chars) 
    for i in word:
        if i in punct:
            word = word.replace(i,"")
    return word

# Function for counting positive words
def get_pos(sentence):
    punctWords = sentence.split()
    pos_wrds = 0
    for i in punctWords:
        words = strip_punctuation(i)
        words_lower = words.lower()
        if words_lower in positive_words:
            pos_wrds += 1
    return pos_wrds

# Function for counting negative words
def get_neg(sentence):
    punctWords = sentence.split()
    neg_wrds = 0
    for i in punctWords:
        words = strip_punctuation(i)
        words_lower = words.lower()
        if words_lower in negative_words:
            neg_wrds += 1
    return neg_wrds

# Function for positive words collection
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

# Function for negative words collection
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

# Collection for tweets, retweets and replies
reT_reP = []
txt = []
with open("project_twitter_data.csv") as data_read:
    for lin in data_read:
        for char in lin:
            if char == "\n":
                lin = lin.replace(char, "")
        lst = lin.split(",")
        reT_reP.append(tuple(lst[-2:]))
        txt.append(tuple(lst[:-2]))
    retrep = reT_reP[1:]  
    text = txt[1:]        
    
retweets = []
replies = []
for tup in retrep:
    retweets.append(tup[0])
    replies.append(tup[1])

# Evaluation of Positive and Negative scores
positive_score = []
negative_score = []
for tup in text: 
    for txt in tup:
        positive_score.append(get_pos(txt))
        negative_score.append(get_neg(txt))

# Evaluation of Net score
net_score = []
for ps, ns in zip(positive_score, negative_score):
    nt = ps-ns
    net_score.append(nt)

# Writing results in csv format            
with open("resulting_data.csv", "w") as data_write:
    data_write.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")
    for rt, rp, ps, ns, nt in zip(retweets, replies, positive_score, negative_score, net_score):
        data_write.write(str(rt)+", "+str(rp)+", "+str(ps)+", "+str(ns)+", "+str(nt)+"\n")