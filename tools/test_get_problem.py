from bs4 import BeautifulSoup
from get_problem import parse_html, parse_paragraph
import os

def get_problem(problem_number):
	script_dir = os.path.dirname(__file__)
	with open(os.path.join(script_dir, f"p{problem_number}.html")) as input_html_file:
		input_html = input_html_file.read()
	actual = parse_html(input_html)
	with open(os.path.join(script_dir, f"../p{problem_number}.md")) as expected_file:
		expected = expected_file.read()
	assert actual == expected

#def test_get_problem_108():
#	get_problem(108)

#def test_get_problem_800():
#	get_problem(800)

def test_parse_paragraph_strong():
	input_html = r"<p>This period is called the <strong>Pisano period</strong> for $n$, often shortened to $\pi(n)$.</p>"
	soup = BeautifulSoup(input_html, 'html.parser')
	actual = parse_paragraph(soup)
	expected = r"This period is called the **Pisano period** for $n$, often shortened to $\pi(n)$."
	assert actual == expected

def test_parse_paragraph_newlines():
	input_html = r"""<p>
For every positive integer $n$ the Fibonacci sequence modulo 
$n$ is periodic. The period depends on the value of $n$.
<p>"""
	soup = BeautifulSoup(input_html, 'html.parser')
	actual = parse_paragraph(soup)
	expected = r"For every positive integer $n$ the Fibonacci sequence modulo $n$ is periodic. The period depends on the value of $n$."
	assert actual == expected
