import pytest

from case.base.base import Base
from case.utils.get_data import get_data


class TestDiv(Base):
    DIV_DATA, DIV_IDS = get_data("div", "P0", "ids")

    @pytest.mark.parametrize("a, b, expect",
                             DIV_DATA,
                             ids=DIV_IDS)
    @pytest.mark.P0
    def test_div(self, a, b, expect):
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
