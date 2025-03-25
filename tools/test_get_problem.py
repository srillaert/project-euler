from get_problem import parse_html
import os

def test_get_problem_108():
	script_dir = os.path.dirname(__file__)
	with open(os.path.join(script_dir, "p108.html")) as input_html_file:
		input_html = input_html_file.read()
	with open(os.path.join(script_dir, "../p108.md")) as expected_file:
		expected = expected_file.read()
	actual = parse_html(input_html)
	assert actual == expected

def test_get_problem_800():
	script_dir = os.path.dirname(__file__)
	with open(os.path.join(script_dir, "p800.html")) as input_html_file:
		input_html = input_html_file.read()
	with open(os.path.join(script_dir, "../p800.md")) as expected_file:
		expected = expected_file.read()
	actual = parse_html(input_html)
	assert actual == expected