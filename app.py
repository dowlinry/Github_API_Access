from github import Github
from user import User
g = Github("")

org = g.get_organization("amzn")
members = org.get_members()
member_list = []
for member in members:
    user = User(member.id)
    popularity_score = member.followers
    repos = member.get_repos()
    for repo in repos:
        if(member.id == repo.owner.id):
            popularity_score = popularity_score + repo.stargazers_count 
            if((repo.language not in user.languages) & (repo.language != None)):
                user.languages.append(repo.language) 
    user.add_popularity_score(popularity_score)
    member_list.append(user)
print("Done")



    


    

