#pip install wordcloud
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt


df = pd.read_csv("reviews.csv")
df = df.loc[df.comments.apply(type) != float]

text = " ".join(review for review in df.comments)
print ("There are {} words in the combination of all review.".format(len(text)))

# Generate a word cloud image
wordcloud = WordCloud(width = 3000,
                      heigh = 2000,
                      max_font_size=50, 
                      max_words=100, 
                      background_color="white").generate(text)

wordcloud = WordCloud().generate(text)

# Display the generated image:
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# save it to local
wordcloud.to_file("Comments_WC.png")