import calculator


class TestCalculator:

    def test_add(self):
        assert calculator.add(1, 2) == 3

    def test_subtract(self):
        assert calculator.subtract(2, 2) == 0
