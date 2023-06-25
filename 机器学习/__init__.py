import xlrd
import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as ts
import warnings

warnings.filterwarnings("ignore")


def excel_to_matrix(path):
    table = xlrd.open_workbook(path).sheets()[0]  # 获取第一个sheet表
    row = table.nrows  # 行数
    col = table.ncols  # 列数
    datamatrix = np.zeros((row, col))  # 生成一个nrows行ncols列，且元素均为0的初始矩阵
    for x in range(col):
        cols = np.matrix(table.col_values(x))  # 把list转换为矩阵进行矩阵操作
        datamatrix[:, x] = cols  # 按列把数据存进矩阵中
    return datamatrix


# 数据处理
def data_iris(I):
    """
    返回类别1和类别2的样本特征X_iris_1,X_iris_2
    以及类别1和类别2的标签数组Y_iris_1,Y_iris_2
    """
    Y_iris = I[:, -1]
    X_iris = I[:, 0:4]
    y_iris_1 = np.where(Y_iris == 1)
    X_iris_1 = X_iris[y_iris_1]
    y_iris_2 = np.where(Y_iris == 2)
    X_iris_2 = X_iris[y_iris_2]
    y_iris_3 = np.where(Y_iris == 3)
    X_iris_3 = X_iris[y_iris_3]
    return X_iris_1, X_iris_2, X_iris_3, X_iris, Y_iris


def data_sonar(S):
    """
    返回类别1和类别2的样本特征X_sonar_1,X_sonar_2
    以及类别1和类别2的标签数组Y_sonar_1,Y_sonar_2
    """
    Y_sonar = S[:, 60]
    X_sonar = S[:, 0:60]
    y_sonar_1 = np.where(Y_sonar == 1)
    X_sonar_1 = X_sonar[y_sonar_1]
    y_sonar_2 = np.where(Y_sonar == 2)
    X_sonar_2 = X_sonar[y_sonar_2]
    return X_sonar_1, X_sonar_2, X_sonar, Y_sonar


def m_S(X):
    d = np.size(X, 1)
    m = np.mean(X, axis=0, keepdims=True)  # 均值向量
    S = np.zeros((d, d))  # 类内离散度矩阵
    for x in X:
        S += np.dot((x - m).T, (x - m))
    return m, S


# fisher判别向量
def fisher(X1, X2, X3):
    X = np.vstack((X1, X2, X3))
    m, _ = m_S(X)
    m1, S1 = m_S(X1)
    m2, S2 = m_S(X2)
    m3, S3 = m_S(X3)
    Sw = S1 + S2 + S3
    # Sw = S1 + S2
    Sb = np.dot((m1 - m).T, (m1 - m)) + np.dot((m2 - m).T, (m2 - m)) + np.dot((m3 - m).T, (m3 - m))
    u, s, v = np.linalg.svd(Sw)  # 奇异值分解
    s_w_inv = np.dot(np.dot(v.T, np.linalg.pinv(np.diag(s))), u.T)
    return s_w_inv, Sb


def fisher(X1, X2):
    X = np.vstack((X1, X2))
    m, _ = m_S(X)
    m1, S1 = m_S(X1)
    m2, S2 = m_S(X2)
    Sw = S1 + S2
    # Sw = S1 + S2
    Sb = np.dot((m1 - m).T,
                (m1 - m)) + np.dot((m2 - m).T,
                                   (m2 - m))
    u, s, v = np.linalg.svd(Sw)  # 奇异值分解
    s_w_inv = np.dot(np.dot(v.T, np.linalg.pinv(np.diag(s))), u.T)
    return s_w_inv, Sb


# 降维
def LDA(X1, X2, X3):
    Sw_inv, Sb = fisher(X1, X2, X3)
    eigen_vals, eigen_vecs = np.linalg.eig(np.dot(Sw_inv, Sb))  # 求特征值及特征向量
    # 将特征值及特征向量配对
    eigen_pairs = [(np.abs(eigen_vals[i]), eigen_vecs[:, i]) for i in range(len(eigen_vals))]
    # 按从小到大的顺序重排特征值
    eigen_pairs = sorted(eigen_pairs, key=lambda k: k[0], reverse=True)
    X0 = np.vstack((X1, X2, X3))
    w = np.hstack((eigen_pairs[0][1].reshape(4, 1), eigen_pairs[1][1].reshape(4, 1)))
    X = np.dot(X0, w)
    return X


def LDA(X1, X2):
    Sw_inv, Sb = fisher(X1, X2)
    eigen_vals, eigen_vecs = np.linalg.eig(np.dot(Sw_inv, Sb))  # 求特征值及特征向量
    # 将特征值及特征向量配对
    eigen_pairs = [(np.abs(eigen_vals[i]), eigen_vecs[:, i]) for i in range(len(eigen_vals))]
    # 按从小到大的顺序重排特征值
    eigen_pairs = sorted(eigen_pairs, key=lambda k: k[0], reverse=True)
    X0 = np.vstack((X1, X2))
    w = np.hstack((eigen_pairs[0][1].reshape(60, 1), eigen_pairs[1][1].reshape(60, 1)))
    X = np.dot(X0, w)
    return X


def main():
    I = excel_to_matrix('iris.xlsx')
    S = excel_to_matrix('sonar.xlsx')

    X_iris_1, X_iris_2, X_iris_3, X_iris, Y_iris = data_iris(I)
    # s_w_inv, Sb = fisher(X_iris_1, X_iris_2, X_iris_3)
    X = LDA(X_iris_1, X_iris_2, X_iris_3)
    X = np.abs(X)
    score_rbf_ave = 0
    print("Iris数据的分类结果:")
    for i in range(10):
        # 10次随机抽样
        X_train, X_test, y_train, y_test = ts(X, Y_iris, test_size=0.2)
        clf_rbf = svm.SVC(kernel='rbf', decision_function_shape='ovo')
        clf_rbf.fit(X_train, y_train)
        score_rbf = clf_rbf.score(X_test, y_test)
        print("第{}次随机抽样的正确率为{}".format(i + 1, score_rbf))
        score_rbf_ave += score_rbf
    print("10次随机抽样的平均正确率为：{}".format(score_rbf_ave / 10))
    print('-' * 50)

    # 画出最后一次分类的超平面
    x_min = X_train[:, 0].min()
    x_max = X_train[:, 0].max()
    y_min = X_train[:, 1].min()
    y_max = X_train[:, 1].max()
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))
    Z = clf_rbf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contour(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
    plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train)
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.show()

    X_sonar_1, X_sonar_2, X_sonar, Y_sonar = data_sonar(S)
    X = LDA(X_sonar_1, X_sonar_2)
    X = np.abs(X)
    score_rbf_ave = 0
    print("Sonar数据的分类结果:")
    for i in range(10):
        X_train, X_test, y_train, y_test = ts(X, Y_sonar, test_size=0.3)
        clf_rbf = svm.SVC(C=0.8, kernel='linear')
        clf_rbf.fit(X_train, y_train)
        score_rbf = clf_rbf.score(X_test, y_test)
        print("第{}次随机抽样的正确率为{}".format(i + 1, score_rbf))
        score_rbf_ave += score_rbf
    print("10次随机抽样的平均正确率为：{}".format(score_rbf_ave / 10))

    # 画出最后一次分类的超平面
    x_min = X_train[:, 0].min()
    x_max = X_train[:, 0].max()
    y_min = X_train[:, 1].min()
    y_max = X_train[:, 1].max()
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))
    Z = clf_rbf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contour(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
    plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train)
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.show()


if __name__ == '__main__':
    main()