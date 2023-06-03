import numpy as np

# 输入数据
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# 目标输出
y = np.array([[0], [1], [1], [0]])

# 定义神经网络结构
input_size = 2
hidden_size = 2
output_size = 1

# 随机初始化权重
W1 = np.random.randn(input_size, hidden_size)
W2 = np.random.randn(hidden_size, output_size)

# 定义激活函数（sigmoid）
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 前向传播
def forward(X):
    # 第一层
    z1 = np.dot(X, W1)
    a1 = sigmoid(z1)
    # 第二层
    z2 = np.dot(a1, W2)
    a2 = sigmoid(z2)
    return a2

# 计算预测结果
predictions = forward(X)
print(predictions)