import argparse
from bs4 import BeautifulSoup
import re
import requests

def parse_paragraph(soup):
	# Replace <strong> tags with markdown bold **text**
	for strong_tag in soup.find_all('strong'):
		strong_tag.replace_with(f"**{strong_tag.text}**")
	result = soup.get_text().replace("\n", "").strip()
	return result

def parse_html(input_html):
	soup = BeautifulSoup(input_html, 'html.parser')
	
	h2_element = soup.find('h2')
	problem_name = h2_element.get_text()
	sb = ["## " + problem_name + "\n\n"]

	h3_element = soup.find('h3')
	problem_number = h3_element.get_text()
	sb.append("### " + problem_number + "\n")

	container = soup.find('div', class_='problem_content')
	for child in container.children:
		if child.name == 'p':  # If it's a <p> tag, get its text
			sb.append("\n" + parse_paragraph(child) + "\n")
		elif isinstance(child, str):  # If it's a string, check for LaTeX equations
			child_text = child.get_text(strip=True)
			if child_text.startswith("$$"):
				sb.append("```math\n" + child_text[2:-2].strip() + "\n```\n")
	result = "".join(sb)
	return result

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Fetch a Project Euler problem description by number and convert it to markdown.')
	parser.add_argument('problem_number', type=int, help='the number of the problem to fetch')
	args = parser.parse_args()

	url = f"https://projecteuler.net/problem={args.problem_number}"
	response = requests.get(url)
	response.raise_for_status()
	markdown_text = parse_html(response.text)
	print(markdown_text)
