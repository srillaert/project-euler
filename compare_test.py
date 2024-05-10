from compare import *
from unittest.mock import patch, MagicMock

@patch('subprocess.run')
def test_get_output(run_mock):
    mock_result = MagicMock()
    mock_result.stdout = "123\n"
    run_mock.return_value = mock_result

    (output, elapsed_time) = get_output("p013.py")

    assert output == "123"
    assert elapsed_time > 0