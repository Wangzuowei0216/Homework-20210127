import pandas as pd
df = pd.read_csv('car_complain.csv')
df = df.drop('problem', 1).join(df.problem.str.get_dummies(','))
print(df)
#存在别名，需要对数据进行清洗
def f(x):
    x = x.replace('一汽-大众', '一汽大众')
    return x
df['brand'] = df['brand'].apply(f)
result = df.groupby(['brand'])['id'].agg(['count'])
#查看columns对应问题标签，从第7个索引开始
print(df.columns)
tips = df.columns[7:]
print('展示问题标签\n', tips)
#不同问题的种数
result2 = df.groupby(['brand'])[tips].agg(['sum'])
print(result2)
result2 = result.merge(result2, left_index=True, right_index=True, how='left')
result2.reset_index(inplace=True)
result2.to_csv("./result.csv")
#投诉数量排序
result2.sort_values('count', ascending=False, inplace=True)
print(result2)
result3 = df.groupby(['car_model'])['id'].agg(['count'])
result3.sort_values('count', ascending=False, inplace=True)
print(result3)