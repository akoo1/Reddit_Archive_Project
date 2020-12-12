
# This program uses Natural Language Processing with the spaCy library for finding the 
# top grammatical gendered adjective-noun pairs and LGBT adjective-noun pairs for the purpose 
# of looking for language trends. This process is done by using spaCy to extract 
# grammatical parts-of-speech in a given year of data and filter for adjective-noun pairs.
# For the “noun” in the adjective-noun pairs, the words “woman”, “man”, “lesbian”, and “gay are used.
# Visualizations are created for all the top grammatical adjective-noun pairs with these 4 different nouns
 
import pandas as pd, spacy, warnings; warnings.simplefilter('ignore')
nlp = spacy.load('en_core_web_sm')


year = 2009

df_year = pd.read_csv(f'df_{year}.csv') 

# Extracting Parts-of-Speech 

# This pipeline returns a parsed Doc object
df_year['parsed_text'] = list(nlp.pipe(df_year['text'], disable = ["ent"], batch_size=100))


# Filtering for Gendered Adjective-Noun Pairs.
# Create visualizations to compare male/gay adjective-noun pairs and female/lesbian adjective-noun pairs
# for a given year
from spacy.symbols import amod, acomp, NOUN

# woman, man, gay, lesbian
my_noun = "gay"

def extractAdjNounPairs(spacy_doc_object):
    pairs = []
    for doc in spacy_doc_object['parsed_text']:
        for adjective in doc:
            if adjective.dep == amod or adjective.dep == acomp and adjective.head.pos == NOUN: # or adjective.dep == ccomp or adjective.dep == conj 
                extracted_pairs = adjective.text, adjective.head.lemma_
                concat_extracted_pairs = ' '.join(extracted_pairs)
                pairs.append(str(concat_extracted_pairs))
    return pairs

adjective_noun_pairs = extractAdjNounPairs(df_year)


import re

def extract_adj_noun_pairs(adjective_noun_pairs):
    regex = re.compile(f' {my_noun}')
    female = [word for word in adjective_noun_pairs if regex.search(word)]
    return female

adj_noun_pairs = extract_adj_noun_pairs(adjective_noun_pairs)



stopwords = ['']
def remove_stop_words(pairs):
    keep_pairs = []
    for pair in pairs:
        tokens = pair.split(" ")
        tokens_filtered = [word for word in tokens if not word in stopwords]
        joined_tokens = " ".join(tokens_filtered)
        if len(tokens_filtered) == 2: # if string is length of two, keep the string
            keep_pairs.append(str(joined_tokens)) 
    return keep_pairs

# adj_noun_pairs = remove_stop_words(adj_noun_pairs)

# create a dictionary with each unique pair and its frequency
adj_noun_dictionary = countWords(adj_noun_pairs)

# create a data frame from our dictionary of grammatical pairs
adj_noun_df = pd.DataFrame(adj_noun_dictionary.items(),columns = ['Pair','Count'])

# arrange in ascending order
adj_noun_df.sort_values(by=['Count'], inplace=True, ascending=False)

# take a subset of the data (top 40 words)
top_adj_noun_df = female_adj_noun_df[:40].copy()
top_adj_noun_df = top.iloc[::-1]



# VISUALIZATION
import matplotlib.pyplot as plt

# set the parameters of the visualization
matplotlib.rcParams['figure.figsize'] = [15, 10]
# sort the pairs for visualization
top_adj_noun_df.sort_values(by=['Count'], inplace=True, ascending=True)
# render visualization
top_adj_noun_df.plot.barh(x = "Pair", y = "Count",
            title = f"Top Grammatical Adjective-Noun Pairs with {my_noun}: Searching Sub-Reddit r/lgbt {year}")
# save the figure
plt.savefig(f'adjective_noun_counts_bar-chart-{year}-{my_noun}.png')



# Scatter graph
plt.scatter(top.Pair, top.Count, color='red')
plt.xlabel("Pairs")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.title(f"Top Grammatical Adjective-Noun Pairs with {my_noun}: Searching Sub-Reddit r/lgbt {year}")
# save the figure
plt.savefig(f"adjective_noun_counts_scatter-{year}-{my_noun}.png")
plt.show()

