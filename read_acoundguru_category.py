import requests
from bs4 import BeautifulSoup
import os
import json

sourcedir = 'C:/Users/username/Downloads/'
htmlfiles = os.listdir(sourcedir)
htmlfiles = [eachfile for eachfile in htmlfiles if eachfile.startswith('Search Results - A Cloud')]
all_entries = []
for counter, each_htmlfile in enumerate(htmlfiles):
	with open(sourcedir+each_htmlfile, 'r', encoding='utf-8') as f:
		readhtml = f.read()

	parsesoup = BeautifulSoup(readhtml, 'lxml')
	all_Title_divs = parsesoup.find_all('div', class_='SearchResult__Right-mz6q0o-2 dhAfEj')
	for each_title in all_Title_divs:
		title = each_title.div.text
		url = each_title.div.a.attrs['href']
		description = each_title.p.span.text
		footer = each_title.find_all('div', class_='Metadata__Item-acy1r8-1 kaKbzl')

		all_entries.append({
			'title': title,
			'url': url,
			'description': description,
			'details': ', '.join([eachfooter.get_text(strip=True) for eachfooter in footer])
		})
		print(counter, title)
		#if title=='AWS Certified DevOps Engineer - Professional 2020':
		#	break

with open('all_acoundguru_course_entries.json', 'w', encoding='utf-8-sig') as f:
	json.dump(all_entries, f, ensure_ascii=False, indent=4)
