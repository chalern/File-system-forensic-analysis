# _*_coding:utf-8_*_
# Author:Hello world

import os
import time
import hashlib
import sys

filepath = 'C:\\Sandbox'  # 默认沙盘目录

def fileinfo(root, name):  # 获取文件信息
    Name = os.path.join(root, name)  # 获取文件名称
    Time = time.ctime(os.path.getmtime(Name))  # 获取文件时间
    with open(Name, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        Hash = md5obj.hexdigest()  # 获取文件md5
    list = Time + '   ' + Name + '   ' + Hash + '\n'
    return list

def creS(num):  # 创建文件系统状态
    if num == '0':
        S = open('./S0.txt', 'a', encoding='utf-8')
    elif num == '1':
        S = open('./S1.txt', 'a', encoding='utf-8')
    else:
        print('Something wrong happened!')
    for root, dirs, files in os.walk(filepath, topdown=False):
        for name in files:
            print(os.path.join(root, name))
            fileinfo(root, name)
            S.writelines(fileinfo(root, name))
    S.close()

def cfS():  # 对比文件系统状态
    S0 = open('./S0.txt', 'r', encoding='utf-8')
    S1 = open('./S1.txt', 'r', encoding='utf-8')
    S2 = open('./S2.txt', 'w', encoding='utf-8')
    setS = set(S1) - set(S0)
    print('\n分析出文件差异：\n' + str(setS))
    S2.writelines(setS)
    S0.close()
    S1.close()
    S2.close()
    print('\n完成比较，已输出S2.txt')

def main():
    while 1:
        num = input('\n输入(0)获取文件系统初始状态S0\n输入(1)更新文件系统状态S1\n输入(2)比较S0，S1\n输入(3)退出本程序\n')
        if num == '0' or num == '1':
            creS(num)
        elif num == '2':
            cfS()
        else:
            if num == '3':
               sys.exit()
            else:
               print('正经一点,重新输过')

print('\n*** File system forensic analysis tool ***\n\n当前路径为 ' + filepath)
main()
