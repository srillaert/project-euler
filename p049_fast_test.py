from p049_fast import get_arithmetic_sequences

def test_get_arithmetic_sequences():
    sequences = list(get_arithmetic_sequences())
    assert len(sequences) == 2
    assert (1487, 4817, 8147) in sequences