from bs4 import BeautifulSoup
import requests

#url = "https://www.google.com/search?q=python+programming"
url = "https://www.google.com/search?q=python+programming&rlz=1C1CHBF_enIN876IN876&oq=python+programming&aqs=chrome..69i57j0l7.10069j0j7&sourceid=chrome&ie=UTF-8"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())
# print(soup.title)
# print(soup.title.string)
# print(soup.a)
# print(soup.find_all("a"))
# print(soup.find(id="intro"))
# print(soup.select("#intro"))
# print(soup.select(".intro"))
# print(soup.select("p.intro"))
# print(soup.select("p#intro"))
# print(soup.select("p.intro")[0].get_text())
# print(soup.select("p.intro")[0].text) 
