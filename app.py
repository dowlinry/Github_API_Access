import json
from github import Github
from user import User
g = Github("")

org = g.get_organization("Facebook")
members = org.get_members()
memberList = []
for member in members:
    user = User(member.id)
    repos = member.get_repos()
    

