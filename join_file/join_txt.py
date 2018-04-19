# -*- coding: utf-8 -*- 
import os

#获取目标文件夹的路径
filedir = os.getcwd() + '/file'
#获取当前文件夹中的文件名称列表  
filenames = os.listdir(filedir)
#打开当前目录下的result.txt文件，如果没有则创建
with open('result.txt','w') as f:
    for filename in filenames:
        filepath = filedir + '/' + filename
        #遍历单个文件，读取行数
        for line in open(filepath):
            f.writelines(line)
        f.write('\n')
