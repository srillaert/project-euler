from p059 import *

def test_load_file():
	actual = load_file()
	assert actual[0] == 36
	assert len(actual) == 1455
	assert actual[-1] == 94
