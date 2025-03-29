import argparse
from bs4 import BeautifulSoup
import re
import requests

def parse_paragraph(soup):
	for break_tag in soup.find_all('br'):
		break_tag.replace_with("br_placeholder")
	for dfn_tag in soup.find_all('dfn'):
		dfn_tag.replace_with(f"_{dfn_tag.text}_")
	for strong_tag in soup.find_all('strong'):
		strong_tag.replace_with(f"**{strong_tag.text}**")
	result = soup.get_text().replace("\n", "").replace("br_placeholder", "\n").strip()
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

def get_input_from_http(problem_number):
	url = f"https://projecteuler.net/problem={problem_number}"
	response = requests.get(url)
	response.raise_for_status()
	return response.text

def get_input_from_file(filepath):
	with open(filepath, 'r') as file:
		return file.read()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Fetch a Project Euler problem description and convert it to markdown.')
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('--http', type=int, help='Number of the problem to fetch from projecteuler.net')
	group.add_argument('--file', type=str, help='File containing the HTML description')
	args = parser.parse_args()

	if args.http:
		html = get_input_from_http(args.http)
	elif args.file:
		html = get_input_from_file(args.file)
	markdown_text = parse_html(html)
	print(markdown_text)
