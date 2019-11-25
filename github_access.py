from github import Github
import pandas as pd


g = Github("")
org = g.get_organization("amzn")
members = org.get_members()

df = pd.DataFrame(columns = ['ID', 'Popularity Score','Known Languages', 'Number of Known Languages'])

member_count = 0

for member in members:
    popularity_score = member.followers
    repos = member.get_repos()
    languages = []
    language_count = 0
    for repo in repos:
        if(member.id == repo.owner.id):
            popularity_score = popularity_score + repo.stargazers_count
            if((repo.language not in languages) & (repo.language is not None) & (repo.language != "Makefile")):
                languages.append(repo.language) 
                language_count += 1
    if(language_count != 0):
        known_languages = '|'.join(str(x) for x in languages)
        df.loc[member_count] = [member.id] + [popularity_score] + [known_languages] + [language_count]
        member_count += 1      
    
df.to_json('results.json')




    


    

