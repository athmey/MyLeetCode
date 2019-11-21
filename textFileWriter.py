import os,sys
import json

with open('./input.txt', 'w', encoding='UTF-8') as f:
    for i in range(1, 101):
        prefix = 'Byton Vehicle Sys Log '
        line = prefix + 'Line Num ' + str(i) + '   拜腾系统日志第 ' + str(i) + ' 行\n'

        f.write(line)