import pytest

from case.base.base import Base


class TestDiv(Base):

    @pytest.mark.parametrize("a, b, expect",
                             [[1, 1, 1], [-0.01, -0.02, 0.5], [10, 0.02, 500], [99, 0, "ZeroDivisionError"]],
                             ids=["整数", "小数", "整数小数", "除数为0"])
    @pytest.mark.P0
    def test_div(self, a, b, expect):
        with pytest.raises(eval("ZeroDivisionError")) as e:
            result = self.cal.div(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect",
                             [[99, 0, "ZeroDivisionError"]],
                             ids=["除数为0"])
    @pytest.mark.P0
    def test_div1(self, a, b, expect):
        with pytest.raises(eval(expect)) as e:
            result = self.cal.div(a, b)
        print(e)

    @pytest.mark.parametrize("a, b, expect", [["文", 9.3, "TypeError"], [4, "分", "TypeError"],
                                              ["nu", 0.2, "TypeError"], [30, "t", "TypeError"]])
    @pytest.mark.P1
    def test_div2(self, a, b, expect):
        with pytest.raises(eval(expect)) as e:
            result = self.cal.div(a, b)
        print(e)
