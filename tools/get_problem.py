from bs4 import BeautifulSoup

def parse_html(input_html):
	soup = BeautifulSoup(input_html, 'html.parser')
	
	h2_element = soup.find('h2')
	h2_text = h2_element.get_text(strip=True)
	sb = ["## " + h2_text + "\n"]

	container = soup.find('div', class_='problem_content')
	for child in container.children:
		if child.name == 'p':  # If it's a <p> tag, get its text
			sb.append("\n" + child.get_text())
		elif isinstance(child, str):  # If it's a string, check for LaTeX equations
			child_text = child.get_text(strip=True)
			if child_text.startswith("$$"):
				sb.append("\n```math\n" + child_text[2:-2].strip() + "\n```\n")
	result = "".join(sb) + "\n"
	return result

if __name__ == "__main__":
	with open("p108.html") as input_html_file:
		input_html = input_html_file.read()
	markdown_text = parse_html(input_html)
	print(markdown_text)
