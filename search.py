import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
from requests_html import HTMLSession

# Starting info
session = HTMLSession()
uname = input("What is your username? (Required) ")
scrapeNet = input(f"Do you want to search the internet as well and grab relevant results? (Beta) [{Fore.GREEN}Y{Style.RESET_ALL}/{Fore.RED}N{Style.RESET_ALL}] ")
if scrapeNet.lower() not in ['y', 'n']:
    print("Error: please pick Either yes or no.")
    exit()
saveResults = input(f"Do you want to save your results to a separate file? [{Fore.GREEN}Y{Style.RESET_ALL}/{Fore.RED}N{Style.RESET_ALL}] ")
if saveResults.lower() not in ['y', 'n']:
    print("Error: please pick Either yes or no.")
    exit()

# YouTube
print("Searching YouTube...")
youtubeURL = f"https://www.youtube.com/@{uname}"
youtubeResults = BeautifulSoup(requests.get(youtubeURL).content, "html.parser").find(id="container")

# Github
print("Searching Github...")
githubURL = f"https://www.github.com/{uname}"
githubResults = BeautifulSoup(requests.get(githubURL).content, "html.parser").find("main")

# Reddit
print("Searching Reddit...")
redditURL = f"https://www.reddit.com/user/{uname}"
redditResults = BeautifulSoup(requests.get(redditURL).content, "html.parser").find("main")

# Linktree
print("Searching Linktree")
linktreeURL = f"https://www.linktr.ee/{uname}"
linktreeResults = BeautifulSoup(requests.get(linktreeURL).content, "html.parser").find(id="TopBar")

# DuckDuckGo
if scrapeNet.lower() == "y":
    print("Searching internet...")
    links = []
    
    searchURL = f"https://lite.duckduckgo.com/lite/?q={uname}"
    searches = BeautifulSoup(session.get(searchURL).content, "html.parser").find_all("a")
    for i in searches:
        link = i.get("href")
        if "youtube.com" in link or "linktr.ee" in link or "github.com" in link or "gitlab.com" in link or "facebook.com" in link or "instagram.com" in link or "reddit.com" in link or "twitter.com" in link or uname in link:
            links.append(link)

# Results
if youtubeResults:
    print(f"User \"{uname}\" found at {youtubeURL}")
    if saveResults.lower() == "y":
        with open("output.txt","a") as o:
            o.flush() # Clear output.txt
            o.write(f"{youtubeURL}\n")
else:
    print("No results were found at YouTube.")
if githubResults:
    print(f"User \"{uname}\" found at {githubURL}")
    if saveResults.lower() == "y":
        with open("output.txt","a") as o:
            o.write(f"{githubURL}\n")
else:
    print("No results were found at Github.")
if redditResults:
    print(f"User \"{uname}\" found at {redditURL}")
    if saveResults.lower() == "y":
        with open("output.txt","a") as o:
            o.write(f"{redditURL}\n")
else:
    print("No results were found at Reddit.")
if linktreeResults:
    print(f"User \"{uname}\" found at {linktreeURL}")
    if saveResults.lower() == "y":
        with open("output.txt","a") as o:
            o.write(f"{linktreeURL}\n")
else:
    print("No results were found at Linktree.")
if links:
    print("Relevant search results:")
    if saveResults.lower() == "y":
        with open("output.txt","a") as o:
            o.write("Relevant Search Results:\n")
    for x in links:
        print(x)
        if saveResults.lower() == "y":
            with open("output.txt","a") as o:
                o.write(f"{x}\n")
elif scrapeNet.lower() == "y":
    print("Sorry, no relevant results were found.")
if saveResults.lower() == "y":
        print(f"Results saved to {Fore.GREEN}output.txt")
