from get_problem import parse_html
import os

def get_problem(problem_number):
	script_dir = os.path.dirname(__file__)
	with open(os.path.join(script_dir, f"p{problem_number}.html")) as input_html_file:
		input_html = input_html_file.read()
	actual = parse_html(input_html)
	with open(os.path.join(script_dir, f"../p{problem_number}.md")) as expected_file:
		expected = expected_file.read()
	assert actual == expected

def test_get_problem_108():
	get_problem(108)

def test_get_problem_800():
	get_problem(800)