import pytest

from calculator.calculator import Calculator


def teardown_module(self):
    print("结束测试")


"""

"""


class TestAdd:

    def setup_class(self):
        self.cal = Calculator()

    """
    """

    def tearup(self):
        print("开始计算")

    """
    """

    def teardown(self):
        print("结束计算")

    def teardown_class(self):
        print("结束测试")

    #
    # 测试两个整数的用例

    @pytest.mark.P0
    def test_add_integer(self):
        result = self.cal.add(1, 1)
        assert result == 2

    """
        测试小数的测试用例
    """

    @pytest.mark.P1
    def test_add_decimal(self):
        result = self.cal.add(0.1, 0.9)
        assert result == 1

    """
           边界值的测试用例
    """

    @pytest.mark.P1
    def test_add_boundary(self):
        result = self.cal.add(99, 98.99)
        assert result == 99 + 98.99

    """
              负数边界值的测试用例
    """

    @pytest.mark.P2
    def test_add_negative_boundary(self):
        result = self.cal.add(-99, -98.99)
        assert result == (-99 + -98.99)
