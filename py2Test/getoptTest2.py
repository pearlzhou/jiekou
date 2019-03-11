# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 15:57
# @Author  : zhouzz
# @FileName: getoptTest2.py


"""
args: 要解析的命令行参数列表。

options: 以列表的格式定义，options后的冒号(:)表示该选项必须有附加的参数，不带冒号表示该选项不附加参数。

long_options: 以字符串的格式定义，long_options 后的等号(=)表示如果设置该选项，必须有附加的参数，否则就不附加参数。

该方法返回值由两个元素组成: 第一个是 (option, value) 元组的列表。 第二个是参数列表，包含那些没有'-'或'--'的参数。"""
import sys, getopt
from selenium import webdriver
import time

def main(argv):
    '''
    命令行传参
    '''
    name = "firefox" # 给个默认值

    try:
        # 这里的 h 就表示该选项无参数，n:表示 n 选项后需要有参数
        opts, args = getopt.getopt(argv, "hn:", ["name="])
    except getopt.GetoptError:
        print('Error: getoptTest2.py -n <browsername>')
        print('   or: getoptTest2.py --name=<browsername>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print('getoptTest2.py -n <browsername>')
            print('or: getoptTest2.py --name=<browsername>')
            sys.exit()
        elif opt in ("-n", "--name"):
            name = arg

    print('run browser name : %s' % name)
    return name

def browser(n=None):
    '''
    启动浏览器, n是浏览器名称，支持浏览器：chrome ,firefox
    https://www.cnblogs.com/yoyoketang/
    '''
    if n == None:
        name = main(sys.argv[1:])
    else:
        name = n
    if name == "firefox":
        print("当前执行浏览器：%s" % name)
        return webdriver.Firefox()
    elif name == "chrome":
        print("当前执行浏览器：%s" % name)
        return webdriver.Chrome()
    else:
        print("支持浏览器：chrome,firefox")

if __name__ == "__main__":
    driver = browser()
    driver.get("https://www.cnblogs.com/yoyoketang/")
    t = driver.title
    print(t)
    time.sleep(10)
    driver.quit()