import sys

try:
    salary = int(sys.argv[1])
except:
    print("请输入正确的工资金额！")

if (salary <= 3500):
    print("0")
else:
    ts = salary - 3500
    sl = 0
    if (ts <= 1500):
        sl = ts * 0.03
    elif (ts > 1500 and ts <= 4500):
        sl = ts * 0.1 - 105
    elif (ts > 4500 and ts <= 9000):
        sl = ts * 0.2 - 555
    elif (ts > 9000 and ts <= 35000):
        sl = ts * 0.25 - 1005
    elif (ts > 35000 and ts <= 55000):
        sl = ts * 0.3 - 2755
    elif (ts > 55000 and ts <= 80000):
        sl = ts * 0.35 - 5505
    else:
        sl = ts * 0.45 - 13505


    print("the tax rate is: " + format(sl, ".2f"))
