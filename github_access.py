from github import Github
from user import User
import pandas as pd
import numpy as np


g = Github("6102ec3c086ba008db6d251f6ec91baa09d06e75")
org = g.get_organization("amzn")
members = org.get_members()

df = pd.DataFrame(columns = ['ID', 'Popularity Score'])
#df.insert(0,'69','420')
#df.to_json(results.json)
#print(df)

#member_list = []

count = 0
for member in members:
 #   user = User(member.id)
    popularity_score = member.followers
    repos = member.get_repos()
    for repo in repos:
        if(member.id == repo.owner.id):
            popularity_score = popularity_score + repo.stargazers_count 

            

 #           if((repo.language not in user.languages) & (repo.language != None)):
 #               user.languages.append(repo.language) 
 #   user.add_popularity_score(popularity_score)
 #   member_list.append(user)
    df.loc[count] = [member.id] + [popularity_score]
    count += 1      

print(df)
df.to_json('results.json')




    


    

