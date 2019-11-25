from github import Github
import pandas as pd



g = Github("0")
orgs = []


def add_organisation(org):
    orgs.append(g.get_organization(org))

add_organisation("amzn")
add_organisation("Facebook")
add_organisation("Apple")
add_organisation("intel")


pop_df = pd.DataFrame(columns = ['Popularity Score', 'Number of Known Languages'])
lang_df = pd.DataFrame(columns = ['Language','Number of Languages Known By User'])
member_count = 0

for org in orgs:
    members = org.get_members()
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
            for lang in languages:
                lang_df.loc[len(lang_df)] = [lang] + [language_count]
            pop_df.loc[member_count] = [popularity_score] + [language_count]
            member_count += 1        
pop_df.to_json('results.json')
lang_df.to_json('languages.json')





    


    

