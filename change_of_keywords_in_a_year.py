
import pandas as pd

# This program loads the data frame that was built from the 'InitialDataProcessing' file,
# uses a list of keywords regarding LGBT, and visualize the change of their wordcounts 
# over the 12 months in a given year

year = 2009
df_year = pd.read_csv(f'df_{year}.csv') # load your CSV file


# Get the wordcount of a special word for every month in a year
# (repeat this process for every year and keep track of wordcounts in each year)
df_year['gay'] = df_year['text'].str.count("gay")
df_year['lesbian'] = df_year['text'].str.count("lesbian")
df_year['trans'] = df_year['text'].str.count("trans")
df_year['bisexual'] = df_year['text'].str.count("bisexual")
df_year['woman'] = df_year['text'].str.count("woman")
df_year['man'] = df_year['text'].str.count("man")

# reverse the data frame
df_year = df_year.iloc[::-1]
print(df_year)

df_year.sum(axis=0)


# This is for finding the change of keywords wordcount from 2010 ~ 2015
# Use all the wordcounts collected to build a data frame, where each row represents a year and all the keywords wordcounts 
# d = {'year': [2010, 2011, 2012, 2013, 2015], 
#      'gay': [37210, 70267, 39009, 24146, 17897], 
#      'lesbian': [3681, 6187, 3981, 2597, 1800], 
#      'trans': [9705, 22457, 17292, 10119, 9822], 
#      'bisexual': [3972, 6511, 4459, 2719, 2471], 
#      'woman': [9104, 17193, 10985, 6931, 6561], 
#      'man': [27933, 55400, 36203, 22748, 20072]}
#
# df_year = pd.DataFrame(d)
# df_year



import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')


figure(figsize=(12, 8), dpi=80)
# plt.rcParams['figure.figsize'] = [15, 10]

x = df_year.month

y1 = df_year.gay
y2 = df_year.lesbian
y3 = df_year.trans
y4 = df_year.bisexual
y5 = df_year.man
y6 = df_year.woman



plt.plot(x, y1, label='gay') 
plt.plot(x, y2, label='lesbian')
plt.plot(x, y3, label='trans')
plt.plot(x, y4, label='bisexual')
plt.plot(x, y5, label='man')
plt.plot(x, y6, label='woman') 



plt.xlabel('month')
plt.xticks(rotation=90)
plt.ylabel('wordcount')
plt.ylim(ymin=0, ymax=7000)
plt.title(f"Change of wordcount of keywords over {year}")
plt.legend()


# save the figure
plt.savefig(f"Change of wordcount of keywords over {year}")

