class User:
    id = 0
    languages = []
    starCount = 0
    def __init__(self,id):
        self.id = id

    def add_language(self,language):
        self.languages.append(language)

    def add_starCount(self,starCount):
        self.starCount += starCount
         
