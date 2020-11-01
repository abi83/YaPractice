import unittest


class Calculator:
    """Производит различные арифметические действия."""
    def divider(self, num1, num2):
        """Возвращает результат деления num1 / num2."""
        return num1/num2

    def summ(self, *args):
        """Возвращает сумму принятых аргументов."""
        if len(args) <2:
            return None
        sum = 0
        for i in args:
            sum += i
        return sum


class TestCalc(unittest.TestCase):
    """Тестируем Calculator."""
    # Подготовьте данные для теста
    @classmethod
    def setUpClass(cls) -> None:
        cls.calc = Calculator()

    def test_divider(self):
        act = TestCalc.calc.divider(8,4)  # вызовите метод divider с аргументом
        self.assertEqual(act, 2, 'текст, если проверка провалена')

    def test_divider_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
           TestCalc.calc.divider(8, 0)

    def test_summ(self):
        act = TestCalc.calc.summ(3, -3, 5)
        self.assertEqual(act, 5, 'summ работает неправильно')

    def test_summ_no_argument(self):
        act = TestCalc.calc.summ()
        self.assertIsNone(act, 'None не возращает, если аргументов нет')

    def test_summ_one_argument(self):
        act = TestCalc.calc.summ(5)
        self.assertIsNone(act, 'None не возращает, если аргумент один')
