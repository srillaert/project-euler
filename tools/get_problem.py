from bs4 import BeautifulSoup
import requests

def parse_html(input_html):
	soup = BeautifulSoup(input_html, 'html.parser')
	
	h2_element = soup.find('h2')
	problem_name = h2_element.get_text()
	sb = ["## " + problem_name + "\n"]

	h3_element = soup.find('h3')
	problem_number = h3_element.get_text()
	sb.append("### " + problem_number + "\n")

	container = soup.find('div', class_='problem_content')
	for child in container.children:
		if child.name == 'p':  # If it's a <p> tag, get its text
			sb.append(child.get_text())
		elif isinstance(child, str):  # If it's a string, check for LaTeX equations
			child_text = child.get_text(strip=True)
			if child_text.startswith("$$"):
				sb.append("```math\n" + child_text[2:-2].strip() + "\n```\n")
	result = "\n".join(sb) + "\n"
	return result

if __name__ == "__main__":
	response = requests.get("https://projecteuler.net/problem=800")
	response.raise_for_status()
	markdown_text = parse_html(response.text)
	print(markdown_text)
