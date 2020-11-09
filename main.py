# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
from datetime import date, timedelta


def miner_log():
    # 获取当前日期的前一天日期，并格式化输出
    yesterday = (date.today() + timedelta(days=-1)).strftime("%Y-%m-%d")

    # 获取前一天的日志到临时文件中
    val = os.system("sed -n /{}T00:00:00/,/{}T23:59:59/p ./miner.log >./miner-log.tmp".format(yesterday, yesterday))
    print(val)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    miner_log()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
