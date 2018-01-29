import io
def test_one():
        data = io.open("../task2/input.txt")
        s = data.read().strip()
        assert len(s)
