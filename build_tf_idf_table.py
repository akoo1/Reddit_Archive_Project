
import pandas as pd
import numpy as np

# This program loads the data frame that was built from the 'InitialDataProcessing' file,
# and build a tf-idf table with the top distinctive words in that year.

year = 2009

df_year = pd.read_csv('df_{year}.csv') # load your CSV file 

print(df_year)



# The tf-idf table shows the most distinctive words on reddit under sub-reddit r/lgbt in each month


# df['text'][0:1]  # 2015_05
# df['text'][1:2]  # 2015_04

def build_tf_idf_table(df, df_one_month, month_idx):
    
    # Term Frequency => Raw Count Definition
    tf1 = (df_one_month).apply(lambda x: pd.value_counts(x.split(" "))).sum(axis = 0).reset_index()

    tf1.columns = ['words','tf']
    tf1['month'] = df['month'].loc[month_idx]    # This adds the month column  
    tf1.sort_values(by='tf', ascending=False)[:10]
    
    # Inverse Document Frequency
    for i,word in enumerate(tf1['words']):
        tf1.loc[i, 'idf'] = np.log(df.shape[0]/(len(df[df['text'].str.contains(word)])))

    tf1.sort_values(by='idf', ascending=False)[:10]
    
    
    # tf-idf
    tf1['tfidf'] = tf1['tf'] * tf1['idf']
    tf1.sort_values(by='tf', ascending=False)[:10]
    
    return tf1



tf_idf_arr_year = []

for i in range(12):
    tf_idf_table = build_tf_idf_table(df_year, df_year['text'][i:i+1], i)
    tf_idf_arr_year.append(tf_idf_table)
    



# An empty master DF will get appended all the sub-tf-idf-Dfs
master_df_year = pd.DataFrame()

for i in range(len(tf_idf_arr_year)):
    master_df_year = master_df_year.append(tf_idf_arr_year[i])


# maybe sort the master df again by tf-idf score
master_df_year = master_df_year.sort_values(by='tfidf', ascending=False)
master_df_year.head(20)


# saving the data frame as a CSV file on disk
master_df_year.to_csv(f'tf-idf_{year}.csv') 