import allure
import pytest

from case.base.base import Base
from case.utils.logs_utils import logger


def teardown_module(self):
    print("结束测试")


"""

"""


@allure.feature("相加功能")
class TestAdd(Base):

    #
    # 测试两个整数的用例

    @pytest.mark.P0
    @pytest.mark.parametrize("a,b,expect", [(1, 1, 2), (0.1, 0.9, 1), (-1, -2, -3), (0.9, 1, 1.9)],
                             ids=["int", "float", "fushu", "float_int"])
    def test_add_integer(self, a, b, expect):
        logger.info(f"输入参数a={a}，b={b}，期望结果expect={expect}")
        result = self.cal.add(a, b)
        logger.info(f"实际结果result={result}")
        assert result == expect

    """
        测试小数的测试用例
    """

    @pytest.mark.P1
    def test_add_decimal(self):
        with allure.step("stpe1：相加操作"):
            result = self.cal.add(0.1, 0.9)
        with allure.step("stpe2：断言结果"):
            assert result == 1

    """
           边界值的测试用例
    """

    @pytest.mark.P1
    def test_add_boundary(self):
        result = self.cal.add(99.01, 98.99)
        assert "参数大小超出范围" == "参数大小超出范围"

    """
              负数边界值的测试用例
    """

    @pytest.mark.P2
    def test_add_negative_boundary(self):
        result = self.cal.add(-99.01, -98.99)
        assert "参数大小超出范围" == "参数大小超出范围"

    @pytest.mark.P2
    def test_add_negative_numberandchar(self):
        with pytest.raises(TypeError) as e:
            result = self.cal.add("ff", 1)
        print(e)
