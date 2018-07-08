import sys
from collections import namedtuple

income_tax_item = namedtuple(
    'income_tax_item',
    ['start_point', 'tax_rate', 'quick_subtractor']
)

INCOME_TAX_START_POINT = 3500

income_tax_table = [
    income_tax_item(80000, 0.45, 13505),
    income_tax_item(55000, 0.35, 5505),
    income_tax_item(35000, 0.3, 2755),
    income_tax_item(9000, 0.25, 1005),
    income_tax_item(4500, 0.2, 555),
    income_tax_item(1500, 0.1, 105),
    income_tax_item(0, 0.03, 0)
]

SOCIAL_MONEY_RATE = {
    'yanglao': 0.08,
    'yiliao': 0.02,
    'shiye': 0.005,
    'gongshang': 0,
    'shengyu': 0,
    'gongjijin': 0.06
}


def calculator_sl(s):
    pay1 = s * sum(SOCIAL_MONEY_RATE.values())
    pay2 = s - pay1 - INCOME_TAX_START_POINT
    if pay2 < 0:
        return s - pay1
    for in_tax in income_tax_table:
        if pay2 >= in_tax.start_point:
            _salary = s - pay1 - (pay2 * in_tax.tax_rate - in_tax.quick_subtractor)
            print(_salary)
            return _salary


def main():
    for item in sys.argv[1:]:
        em_id, em_sy = item.split(':')
        try:
            salary = int(em_sy)
        except:
            print("请输入正确的工资金额！" + em_id)
        salary = calculator_sl(salary)
        print("the " + em_id + " of salary is: " + format(salary, ".2f"))


if __name__ == '__main__':
    main()


