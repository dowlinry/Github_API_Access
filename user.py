class User:
    id = 0
    languages = []
    popularity_score = 0
    def __init__(self,id):
        self.id = id

    def add_language(self,language):
        self.languages.append(language)

    def add_popularity_score(self,score):
        self.popularity_score = score
         
