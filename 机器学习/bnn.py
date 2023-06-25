from pgmpy.models import BayesianNetwork

# 创建贝叶斯网络模型，并定义节点之间的依赖关系
letter_bn = BayesianNetwork([
    ('D', 'G'), ('I', 'G'), ('I', 'S'), ('G', 'L')  # 指向关系 D->I
])

from pgmpy.factors.discrete import TabularCPD

# 定义变量 D 的条件概率分布
d_cpd = TabularCPD(variable='D', variable_card=2, values=[[0.6], [0.4]])

# 定义变量 I 的条件概率分布
i_cpd = TabularCPD(variable='I', variable_card=2, values=[[0.7], [0.3]])

# 定义变量 G 的条件概率分布，其中 evidence 表示 G 依赖的变量为 I 和 D
g_cpd = TabularCPD(variable='G', variable_card=3,
                   values=[[0.3, 0.05, 0.9, 0.5], [0.4, 0.25, 0.08, 0.3], [0.3, 0.7, 0.02, 0.2]],
                   evidence=['I', 'D'], evidence_card=[2, 2])

# 定义变量 S 的条件概率分布，其中 evidence 表示 S 依赖的变量为 I
s_cpd = TabularCPD(variable='S', variable_card=2, values=[[0.95, 0.2], [0.05, 0.8]],
                   evidence=['I'], evidence_card=[2])

# 定义变量 L 的条件概率分布，其中 evidence 表示 L 依赖的变量为 G
l_cpd = TabularCPD(variable='L', variable_card=2, values=[[0.1, 0.4, 0.99], [0.9, 0.6, 0.01]],
                   evidence=['G'], evidence_card=[3])

# 将定义好的条件概率分布加入到贝叶斯网络模型中
letter_bn.add_cpds(d_cpd, i_cpd, g_cpd, s_cpd, l_cpd)

# 检查构建的模型是否合理
letter_bn.check_model()

# 获取网络中的条件概率依赖关系
letter_bn.get_cpds()

from pgmpy.inference import VariableElimination

# 创建变量消除推断的对象
letter_infer = VariableElimination(letter_bn)

# 进行推断，计算变量 L 的后验概率，给定 I=1 和 D=1 的观测值
prob_I1 = letter_infer.query(variables=['L'], evidence={'I': 0, 'D': 1}) # 智商普通并且题比较难 获取推荐信的概率
prob_I2 = letter_infer.query(variables=['L'], evidence={'I': 1, 'D': 1}) # 智商高并且题比较难 获取推荐信的概率
prob_I3 = letter_infer.query(variables=['L'], evidence={'I': 0, 'D': 0}) # 智商普通并且题比较难 获取推荐信的概率
prob_I4 = letter_infer.query(variables=['L'], evidence={'I': 1, 'D': 0}) # 智商高并且题比较简单 获取推荐信的概率


prob_G = letter_infer.query(variables=['G'], evidence={'I': 1, 'D': 0, 'L': 1, 'S': 1})# 智商高,题简单,已经获取推荐信,并且SAT 的分数比较高的学生,获得比较好的成绩的概率


print("学生智商普通并且题比较难 获取推荐信的概率")
print(f"{prob_I1}")
print("学生智商高并且题比较难 获取推荐信的概率")
print(f"{prob_I2}")
print("学生智商普通并且题比较简单 获取推荐信的概率")
print(f"{prob_I3}")
print("学生智商高并且题比较简单 获取推荐信的概率")
print(f"{prob_I4}")
print("智商高,题简单,已经获取推荐信,并且高考的分数比较高的学生,获得比较好的成绩的概率")
print(f"{prob_G}")