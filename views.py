from django.shortcuts import render
from django.http import HttpResponse
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import string
from nltk.corpus import stopwords
from digifest.models import Reviews
from digifest import dictonary

def result(request):
    sr1 = []
    final_pos = []
    final_neg = []

    # Fetching reviews from database
    for review in Reviews.objects.all():
        sr1.append(review.reviews)

    for rev in sr1:
        pos = 0
        neg = 0
        rev1 = [j for j in rev if j not in string.punctuation]
        rev1 = ''.join(rev1)
        rev1 = rev1.split()
        rev2 = [word for word in rev1 if word not in stopwords.words('english')]
        
        for h in rev2:
            h = h.lower()
            l1 = h[0]
            
            # Checking positive and negative dictionaries
            if l1 in dictonary.positive_dict:
                if h in dictonary.positive_dict[l1]:
                    pos += 1
                elif h in dictonary.negative_dict[l1]:
                    neg += 1
        
        if pos > neg:
            final_pos.append(rev)
        else:
            final_neg.append(rev)

    # Generating WordCloud for positive reviews
    comm_words = ' '.join(final_pos)
    wordcloud = WordCloud(width=500, height=400, min_font_size=10).generate(comm_words)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig('digifest/static/img/pos_plot.jpg')

    # Generating WordCloud for negative reviews
    comm_words1 = ' '.join(final_neg)
    wordcloud = WordCloud(width=500, height=400, min_font_size=10).generate(comm_words1)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig('digifest/static/img/neg_plot.jpg')

    context = {
        'review': sr1,
        'pos': final_pos,
        'neg': final_neg,
    }

    return render(request, 'result.html', context)
