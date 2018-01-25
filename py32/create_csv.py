import win32com.client
import pandas as pd

instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
stockNum = instCpStockCode.GetCount()
codeList = instCpCodeMgr.GetStockListByMarket(1)

kospi = []

for i in range(stockNum):
    if instCpStockCode.GetData(1, i) == '유한양행':
         kospi = [instCpStockCode.GetData(0,i)]

for i in range(stockNum):
    if instCpStockCode.GetData(1, i) == '종근당':
        kospi.append(instCpStockCode.GetData(0, i))

for i in range(stockNum):
    if instCpStockCode.GetData(1, i) == '한미약품':
        kospi.append(instCpStockCode.GetData(0, i))

for i in range(stockNum):
    if instCpStockCode.GetData(1, i) == '조아제약':
        kospi.append(instCpStockCode.GetData(0, i))

for i in range(stockNum):
    if instCpStockCode.GetData(1, i) == '셀트리온':
        kospi.append(instCpStockCode.GetData(0, i))

f = open('kospi.csv', 'w')
f.write(",")
for i in kospi:
    f.write("%s," % (i))
f.close()




