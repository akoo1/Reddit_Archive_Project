
import pandas as pd

# This program loads the data frame that was built from the 'InitialDataProcessing' file,
# takes the top 5 distinctive words found from the 'build_tf_idf_table' file, and visualize 
# the change of their wordcounts over the 12 months in a given year

year = 2009

df_year = pd.read_csv(f'df_{year}.csv') # load your CSV file

word1 = "leelah"
word2 = "gencon"
word3 = "immortality"
word4 = "embassy"
word5 = "grenade"



# Get the wordcount of a special word for every month in 2010
df_year[f'{word1}_wordcount'] = df_year['text'].str.count(word1)
df_year[f'{word2}_wordcount'] = df_year['text'].str.count(f"{word2}")
df_year[f'{word3}_wordcount'] = df_year['text'].str.count(f"{word3}")
df_year[f'{word4}_wordcount'] = df_year['text'].str.count(f"{word4}")
df_year[f'{word5}_wordcount'] = df_year['text'].str.count(f"{word5}")

df_year = df_year.iloc[::-1]
print(df_year)


# Visualize the change of wordcount of a list of special words (high tf-idf score) over the 5 months
import matplotlib
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


plt.scatter(df_year.month, df_year.leelah_wordcount, color='red')
plt.xlabel("month")
plt.ylabel("wordcount")
plt.xticks(rotation=90)
plt.title(f"[ {word1} ] Change of wordcount by month")
# save the figure
plt.savefig(f"special_word_{word1}")
plt.show()


plt.scatter(df_year.month, df_year.gencon_wordcount, color='red')
plt.xlabel("month")
plt.ylabel("wordcount")
plt.xticks(rotation=90)
plt.title(f"[ {word2} ] Change of wordcount by month")
# save the figure
plt.savefig(f"special_word_{word2}")
plt.show()

plt.scatter(df_year.month, df_year.immortality_wordcount, color='red')
plt.xlabel("month")
plt.ylabel("wordcount")
plt.xticks(rotation=90)
plt.title(f"[ {word3} ] Change of wordcount by month")
# save the figure
plt.savefig(f"special_word_{word3}")
plt.show()

plt.scatter(df_year.month, df_year.embassy_wordcount, color='red')
plt.xlabel("month")
plt.ylabel("wordcount")
plt.xticks(rotation=90)
plt.title(f"[ {word4} ] Change of wordcount by month")
# save the figure
plt.savefig(f"special_word_{word4}")
plt.show()

plt.scatter(df_year.month, df_year.grenade_wordcount, color='red')
plt.xlabel("month")
plt.ylabel("wordcount")
plt.xticks(rotation=90)
plt.title(f"[ {word5} ] Change of wordcount by month")
# save the figure
plt.savefig(f"special_word_{word5}")
plt.show()


