# 使用KMeans进行聚类
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np
# 数据加载
data = pd.read_csv('Mall_Customers.csv')
train_x = data[["Gender","Age","Annual Income (k$)", "Spending Score (1-100)"]]
# print(train_x)
# 打印出来后发现gender 为字母类型，不能在Kmeans中进行运算
# 常见的有LabelEncoder 和 one-hot两种编码方式转换成数字类型
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
# le.fit_transform = fit + transform
train_x['Gender'] = le.fit_transform(train_x['Gender'])
# print(train_x)
# 规范化到 [0,1] 空间
min_max_scaler=preprocessing.MinMaxScaler()
train_x=min_max_scaler.fit_transform(train_x)
pd.DataFrame(train_x).to_csv('temp.csv', index=False)
print(train_x)
# 使用KMeans聚类，KMeans(n_clusters=8, max_iter=300)
# n_clusters：聚类个数，缺省值为8，max_iter：执行一次k-means算法所进行的最大迭代数，缺省值为300
kmeans = KMeans(n_clusters=3)
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
# predict_y = kmeans.fit_predict(train_x)与上两行的代码等效，输出结果相同
# 合并聚类结果，插入到原数据中
result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类结果'},axis=1,inplace=True)
print(result)
# 将结果导出到CSV文件中
result.to_csv("customer_cluster_result.csv",index=False)
### 使用层次聚类可以实现可视化呈现
from scipy.cluster.hierarchy import dendrogram, ward
from sklearn.cluster import KMeans, AgglomerativeClustering
import matplotlib.pyplot as plt
model = AgglomerativeClustering(linkage='ward', n_clusters=3)
y = model.fit_predict(train_x)
print(y)
# 可视化呈现
linkage_matrix = ward(train_x)
dendrogram(linkage_matrix)
plt.show()


