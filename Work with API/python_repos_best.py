import requests

"""creating API request and saving the response"""
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code: ", r.status_code)

"""Saving API response in variable"""
response_dict = r.json()
print("Total repositories: ", response_dict["total_count"])

"""Analysis of information about repositories"""
repo_dicts = response_dict["items"]
print("Repositories returned: ", len(repo_dicts))

"""Analysis of 1st repository"""
repo_dict = repo_dicts[0]


print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print("Name:", repo_dict["name"])
    print("Owner:", repo_dict["owner"]["login"])
    print("Stars:", repo_dict["stargazers_count"])
    print("Repository:", repo_dict["html_url"])
    print("Created:", repo_dict["created_at"])
    print("Updated:", repo_dict["updated_at"])
    print("Description:", repo_dict["description"])

""" print("\nKeys: ", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key) """

"""Processing the results"""
print(response_dict.keys())


"""PAGE 369"""
