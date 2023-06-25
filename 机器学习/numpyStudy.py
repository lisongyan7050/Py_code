from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from 机器学习.two import NaiveBayes

data = load_iris()
X = data.data
y = data.target
print(X)
print(y)

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建并训练模型
clf = NaiveBayes()
clf.fit(X_train, y_train)

# 预测并计算准确率
y_pred = clf.predict(X_test)
acc = (y_pred == y_test).sum() / len(y_test)
print(f'Accuracy: {acc:.4f}')
