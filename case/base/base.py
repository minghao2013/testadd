from calculator.calculator import Calculator
from case.utils.logs_utils import logger


class Base:
    def setup(self):
        logger.info("实例化Cal类")
        self.cal = Calculator()

    """
    """
    def tearup(self):
        logger.info("开始计算")

    """
    """
    def teardown(self):
        logger.info("结束计算")

    def teardown_class(self):
        logger.info("结束测试")
