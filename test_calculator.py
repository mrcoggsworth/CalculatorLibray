import calculator


class TestCalculator:

    def test_add(self):
        assert calculator.add(1, 2) == 3

    def test_subtract(self):
        assert calculator.subtract(2, 2) == 0

    def test_multiply(self):
        assert calculator.multiply(10, 10) == 100

    def test_divide(self):
        assert calculator.divide(25, 5) == 5
