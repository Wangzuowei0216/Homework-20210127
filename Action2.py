import numpy as np
import pandas as pd
arr = np.array([[68, 65, 30], [95, 76, 98], [98, 86, 88], [90, 88, 77], [80, 90, 90]])
df = pd.DataFrame(arr, columns=('语文', '数学', '英语'), index=('张飞', '关羽', '刘备', '典韦', '许诸'))
print(df)
#计算平均成绩
score_ave = np.mean(df)
print('各科的平均成绩：\n', score_ave)
#计算最低成绩
score_min = np.min(df)
print('各科的最低成绩：\n', score_min)
#计算最高成绩
score_max = np.max(df)
print('各科的最高成绩：\n', score_max)
#计算成绩方差
score_var = np.var(df)
print('各科成绩方差：\n', score_var)
#计算总分
df['总分'] = df.apply(lambda x: x.sum(), axis=1)
print('总分计算结果：\n', df)
#排序
df.sort_values(by='总分', ascending=False, inplace=True)
print('总分排序：\n', df)