from rake_nltk import Rake 
from nltk.corpus import stopwords

class KeywordExtractor:
    def __init__(self, language='english'):
        self.model = Rake(stopwords=set(stopwords.words(language)))

    def extractKeyword(self, text):
        self.model.extract_keywords_from_text(text)
        return self.model.get_ranked_phrases()
