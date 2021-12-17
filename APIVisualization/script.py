#import Github from the pyGithub library
from github import Github

# using an access token--create own token to use
g = Github(" ")

#getting basic user data
usr = g.get_user()
print("user:  " + usr.login)
print("fullname:  " + usr.name)

#getting repositories of the user
repos = g.get_user().get_repos()

for repo in repos:
    print(repo.name)



