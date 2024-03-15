from wordcloud import WordCloud 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/wordCloud/cleaned_hm.csv') 
print(df.columns) # Printing the column names to verify the data


# Concatenate all text items into a single string. 
text = ' '.join(df['cleaned_hm'].dropna())

#Generate the word cloud
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = None,  # You can add a set of words to ignore here
                min_font_size = 10).generate(text)

#Display the word cloud
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0) 

#Save the word cloud
plt.savefig('images/general/wordcloud.png')
plt.show()







