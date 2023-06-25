import numpy as np

class NaiveBayes:
    def __init__(self):
        self.X = None  # 训练数据
        self.y = None  # 训练标签
        self.classes = None   # 所有类别
        self.M = None  # 每个类别下每个特征的均值
        self.V = None  # 每个类别下每个特征的方差

    def fit(self, X, y):
        """训练模型
        参数：
        X: 训练数据，形状为 [n_samples, n_features]
        y: 训练标签，形状为 [n_samples]
        """
        self.X = X
        self.y = y
        self.classes = np.unique(y)

        # 初始化均值和方差
        self.M = np.zeros((len(self.classes), X.shape[1]))
        self.V = np.zeros((len(self.classes), X.shape[1]))

        # 求每个类别下每个特征的均值和方差
        for i, c in enumerate(self.classes):
            X_c = X[c == y]
            self.M[i, :] = X_c.mean(axis=0)
            self.V[i, :] = X_c.var(axis=0)

    def predict(self, X):
        """预测标签
        参数：
        X: 测试数据，形状为 [n_samples, n_features]
        返回：
        预测标签，形状为 [n_samples]
        """
        # 求每个类别下样本的概率
        P = np.zeros((len(self.classes), X.shape[0]))
        for i, c in enumerate(self.classes):
            pdf = self.pdf(X, self.M[i], self.V[i])
            P[i, :] = np.log(self.prior(c)) + np.log(pdf).sum(axis=1)

        # 返回概率最大的类别
        return self.classes[np.argmax(P, axis=0)]

    def prior(self, c):
        """计算先验概率
        """
        return (self.y == c).sum() / len(self.y)

    def pdf(self, X, mu, sigma):
        """计算概率密度函数
        """
        exponent = np.exp(-0.5 * ((X - mu) / sigma) ** 2)
        return (1.0 / (np.sqrt(2 * np.pi) * sigma)) * exponent
