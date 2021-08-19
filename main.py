# Simple HTML Parser, coded by Emre Demirbag https://github.com/emre-demirbag
# New York Times Mini Crossword Puzzle,by Joel Fagliano,(https://www.nytimes.com/crosswords/game/mini)
#requests:(http://docs.python-requests.org/en/master/),
#soup:(https://www.crummy.com/software/BeautifulSoup/bs4/doc/)


# Import the required modules
import requests
from bs4 import BeautifulSoup as Soup


#Checking Connection
def check(url):
	chkUrl=requests.get(url)
	if chkUrl.status_code == 200:
		print("HTTP 200 OK: Connection established")
	else:
		print("Oops! Something went wrong")

	return None
#Session Object
session = requests.Session()

def getHTML(url):

# session.get(url) returns a response that is saved
# in a response object called resp.

	resp = session.get(url)

# BeautifulSoup will create a
# parsed tree in soup.

	soup = Soup(resp.content, "lxml")

	return soup

def getColoumns(soup):
	# soup.find_all finds the div's, all having the same
	# class "ClueList-wrapper--3m-kd" that is
	# stored NyTimes Mini Crosswords web site
	# https://www.nytimes.com/crosswords/game

	cluwrap = soup.find_all("div", {"class": "ClueList-wrapper--3m-kd"})

	# Initialise the required variable
	html = "<html><body>"

	# Iterate cluewrap and clutext check for the html tags
	# to get the information of each clues.
	for i in cluwrap:

		title = i.findAll("h3")

		html += "<h3>" + title[0].text.strip() + "</h3><ul>"

		cluetext = i.findAll("li")

		for j in cluetext:
			html += "<li>"
			span = j.findAll("span")
			html += "<span><b>" + span[0].text.strip() + ".</b></span> <span>" + span[1].text.strip() + "</span></li>"
		html += "</ul>"

	html += "</body></html>"
	return html


if __name__ == "__main__":

	url = "https://www.nytimes.com/crosswords/game/mini"
	# Enter the url of website
	check(url)
	s = getHTML(url)

	# Function will return a list of clues
	html = getColoumns(s)

	# export a list of clues to text file
	htmlFile = open("a.html", "w")
	htmlFile.write(html)
	htmlFile.close()
	print("Created html file")