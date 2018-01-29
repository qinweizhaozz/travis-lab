def test_one():
        data = open('input.txt')
        s = data.read().strip()
        assert len(s)==6
