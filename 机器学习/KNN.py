from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

from numpy import genfromtxt
#genfromtxt函数创建数组表格数据
import time
# 开始计时
start = time.perf_counter()

#加载数据
dataPath = r'TrainFile_dis19_feature26.txt'
data = genfromtxt(dataPath,delimiter=',')       #将路径下的文本文件导入并转化成numpy数组格式
dataPath1 = r'TestFile_dis26_feature26.txt'
data1 = genfromtxt(dataPath1,delimiter=',')       #将路径下的文本文件导入并转化成numpy数组格式
# 训练集和测试集（假设已经准备好）
#提取特征值
#x_train,y_train分别是训练集的特征向量和类别标签
#x_test,y_test分别是测试集的特征向量和类别标签
x_train=data[:,:-1]
y_train=data[:,-1]
x_test=data1[:,:-1]
y_test=data1[:,-1]

# 创建KNN分类器
knn_classifier = KNeighborsClassifier(n_neighbors=7)

# 训练KNN模型
knn_classifier.fit(x_train, y_train)

# 进行预测
y_pred = knn_classifier.predict(x_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)

print('预测正确率为: %.2f%%'%(accuracy*100))
# 打印预测结果和准确率
end = time.perf_counter()
print("运行耗时: %.fs" %(end-start))