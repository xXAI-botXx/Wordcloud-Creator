import os


def create_wordcloud():
    # load data from file
    dir_path = './input.txt'

    data = ""
    with open(dir_path, 'r') as readed:
        data = readed.read()
    
    ##############################################
    # text analysis
    import spacy
    
    nlp = spacy.load("de_core_news_sm")
    doc = nlp(data)
    
    # remove stopwords
    span_without_stopwords = []
    
    for token in doc:
        if not token.is_stop:
            span_without_stopwords += [token.text] 
    
    ##############################################
    # create wordcloud
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    
    wordcloud = WordCloud(width = 2000, height = 2000, background_color = "white").generate(''.join(span_without_stopwords))
    
    plt.figure(figsize = (10,10))
    plt.imshow(wordcloud, interpolation = "bilinear")
    
    # for testing
    from random import randint
    plt.savefig("./output,png"+randint(0, 1000)+".png")
