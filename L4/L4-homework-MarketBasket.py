# L4-homework-Marketbasket-503816—王作伟
import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from efficient_apriori import apriori
pd.set_option('max_columns', None)
# 数据加载，header=None，不将第一行作为head
dataset = pd.read_csv('./Market_Basket_Optimisation.csv', header = None)
print(dataset)
print(dataset.shape)# shape为(7501,20)
# 按照行进行遍历
transactions = []
for i in range(0, dataset.shape[0]):
    temp = []
    for j in range(0, 20):
        if str(dataset.values[i, j]) != 'nan':#需要更改数据类型
           temp.append(str(dataset.values[i, j]))
    transactions.append(temp)

# 挖掘频繁项集和频繁规则
itemsets, rules = apriori(transactions, min_support=0.01,  min_confidence=0.5)
print("频繁项集：", itemsets)
print("关联规则：", rules)