
import pandas as pd
import nltk
from nltk.corpus import stopwords
from textblob import Word


# This program loads the data, the Reddit Archive from 2009-01 to 2015-05, stored on ManeFrame II, 
# a shared high-performance computing environment implemented by Southern Methodist University. 
# It then filters the data, cleans up the data, convert each year of data into a Panda dataFrame, 
# and save them on disk (for quick data loading in the future). 


# A long list of stop words
stopwords = [
    "i",
    "me",
    "my",
    "myself",
    "we",
    "our",
    "ours",
    "ourselves",
    "you",
    "your",
    "yours",
    "yourself",
    "yourselves",
    "he",
    "him",
    "his",
    "himself",
    "she",
    "her",
    "hers",
    "herself",
    "it",
    "its",
    "itself",
    "they",
    "them",
    "their",
    "theirs",
    "themselves",
    "what",
    "which",
    "who",
    "whom",
    "this",
    "that",
    "these",
    "those",
    "am",
    "is",
    "are",
    "was",
    "were",
    "be",
    "been",
    "being",
    "have",
    "has",
    "had",
    "having",
    "do",
    "does",
    "did",
    "doing",
    "a",
    "an",
    "the",
    "and",
    "but",
    "if",
    "or",
    "because",
    "as",
    "until",
    "while",
    "of",
    "at",
    "by",
    "for",
    "with",
    "about",
    "against",
    "between",
    "into",
    "through",
    "during",
    "before",
    "after",
    "above",
    "below",
    "to",
    "from",
    "up",
    "down",
    "in",
    "out",
    "on",
    "off",
    "over",
    "under",
    "again",
    "further",
    "then",
    "once",
    "here",
    "there",
    "when",
    "where",
    "why",
    "how",
    "all",
    "any",
    "both",
    "each",
    "few",
    "more",
    "most",
    "other",
    "some",
    "such",
    "no",
    "nor",
    "not",
    "only",
    "own",
    "same",
    "so",
    "than",
    "too",
    "very",
    "s",
    "t",
    "can",
    "will",
    "just",
    "don't",
    "should",
    "now"
]


# This function will extract all the body texts in a specific month return them as one huge string
def get_all_body_text_in_a_month(filename):
    
    data = pd.read_csv(filename, sep='\t') 
    # data.head()
    # 2015-03 total posts: 54455873
    # len(data)
    

    # FILTERING data for r/lgbt from a whole month of reddit data

    # The subreddit dataset shows all the posts under r/lgbt in 2015-03. Total posts: 9382
    # I can create a graph for this dataset for the most recent 10 months, and list them in chronological order.
    subreddit=data[data['subreddit'].str.contains('lgbt')]
 
    
    # If some of our data is missing, this will replace the blank entries. This is only necessary in some cases
    subreddit = subreddit.fillna("No Information Provided")
   

    # CLEANING UP text

    # Lowercase
    data['body'] = data['body'].apply(lambda x: " ".join(x.lower() for x in x.split()))
    subreddit['body'] = subreddit['body'].apply(lambda x: " ".join(w.lower() for w in x.split()) if type(x) != float else x)
    
    # Remove punctuations
    subreddit['body'] = subreddit['body'].str.replace('[^\w\s]','')

    # Remove stopwords
    stop = stopwords.words('english')

    subreddit['body'] = subreddit['body'].apply(lambda x: " ".join(x for x in x.split() if x not in stopwords))
    
    # Lemmetization
    nltk.download('wordnet')
    subreddit['body'] = subreddit['body'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))

    
    # concatenate the body text in each row into a huge string
    text_sum = ''
    for i in range(len(subreddit['body'])):
    
        body = subreddit['body'].iloc[i] 
        text_sum += body
    
    print(f'{filename} done.')

    return text_sum
    
    # Contextualization - This block of code is used to filter for posts that contain certain words
    # special_word = 'leelah'
    # special_word_arr = []
    # for i in range(len(subreddit['body'])):
    #     body = subreddit['body'].iloc[i]
    #     if special_word in body:
    #          special_word_arr.append(body)
    
    # return special_word_arr


                   
year = 2009

# filenames of 12 months from 2009_12 ~ 2009_01 (repeat the process for 2009~2015)
filename_year_12 = f'/scratch/group/oit_research_data/reddit/RC_{year}-12.tsv'
filename_year_11 = f'/scratch/group/oit_research_data/reddit/RC_{year}-11.tsv'
filename_year_10 = f'/scratch/group/oit_research_data/reddit/RC_{year}-10.tsv'
filename_year_09 = f'/scratch/group/oit_research_data/reddit/RC_{year}-09.tsv'
filename_year_08 = f'/scratch/group/oit_research_data/reddit/RC_{year}-08.tsv'
filename_year_07 = f'/scratch/group/oit_research_data/reddit/RC_{year}-07.tsv'
filename_year_06 = f'/scratch/group/oit_research_data/reddit/RC_{year}-06.tsv'
filename_year_05 = f'/scratch/group/oit_research_data/reddit/RC_{year}-05.tsv'
filename_year_04 = f'/scratch/group/oit_research_data/reddit/RC_{year}-04.tsv'
filename_year_03 = f'/scratch/group/oit_research_data/reddit/RC_{year}-03.tsv'
filename_year_02 = f'/scratch/group/oit_research_data/reddit/RC_{year}-02.tsv'
filename_year_01 = f'/scratch/group/oit_research_data/reddit/RC_{year}-01.tsv'

body_text_year_12 = get_all_body_text_in_a_month(filename_year_12)
body_text_year_11 = get_all_body_text_in_a_month(filename_year_11)
body_text_year_10 = get_all_body_text_in_a_month(filename_year_10)
body_text_year_09 = get_all_body_text_in_a_month(filename_year_09)
body_text_year_08 = get_all_body_text_in_a_month(filename_year_08)
body_text_year_07 = get_all_body_text_in_a_month(filename_year_07)
body_text_year_06 = get_all_body_text_in_a_month(filename_year_06)
body_text_year_05 = get_all_body_text_in_a_month(filename_year_05)
body_text_year_04 = get_all_body_text_in_a_month(filename_year_04)
body_text_year_03 = get_all_body_text_in_a_month(filename_year_03)
body_text_year_02 = get_all_body_text_in_a_month(filename_year_02)
body_text_year_01 = get_all_body_text_in_a_month(filename_year_01)



# Creating the dataframe for 12 months of r/lgbt data (2009_12 ~ 2009_01) 
d = {"month":[f"{year}_12", f"{year}_11", f"{year}_10", f"{year}_09", f"{year}_08",
              f"{year}_07", f"{year}_06", f"{year}_05", f"{year}_04", f"{year}_03", f"{year}_02", f"{year}_01"],
     "text":[body_text_year_12, body_text_year_11, body_text_year_10, body_text_year_09, body_text_year_08, 
             body_text_year_07, body_text_year_06, body_text_year_05, body_text_year_04, body_text_year_03, body_text_year_02, body_text_year_01]
    }


# Reddit data grouped by month
df_year = pd.DataFrame(d)
print(df_year)

df_year.to_csv(f'df_{year}.csv') # saving the data frame as a CSV file on disk
