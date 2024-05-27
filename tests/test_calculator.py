from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected
    
    def test_subtract(self):
        a = 4321
        b= 1234
        cal = Calculator()
        result = cal.subtract(a,b)
        expected = 3087
        assert result == expected
    
    def test_multiply(self):
        a = 4321
        b= 1234
        cal = Calculator()
        result = cal.multiply(a,b)
        expected = 5332114
        assert result == expected

    def test_divide(self):
        a = 4321
        b= 1234
        cal = Calculator()
        result = cal.divide(a,b)
        expected = 3.5016207455429496
        assert result == expected

