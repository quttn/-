import numpy as np


def array_creation():
    print("=" * 60)
    print("任务1：创建不同维度的数组")
    print("=" * 60)
    
    print("\n1D数组（一维）：")
    arr_1d = np.array([1, 2, 3, 4, 5])
    print(f"  创建: np.array([1, 2, 3, 4, 5])")
    print(f"  数组: {arr_1d}")
    print(f"  形状: {arr_1d.shape}, 维度: {arr_1d.ndim}, 类型: {arr_1d.dtype}")
    
    print("\n2D数组（二维矩阵）：")
    arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"  创建: np.array([[1,2,3],[4,5,6],[7,8,9]])")
    print(f"  数组:\n{arr_2d}")
    print(f"  形状: {arr_2d.shape}, 维度: {arr_2d.ndim}")
    
    print("\n3D数组（三维）：")
    arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print(f"  创建: np.array([[[1,2],[3,4]],[[5,6],[7,8]]])")
    print(f"  数组:\n{arr_3d}")
    print(f"  形状: {arr_3d.shape}, 维度: {arr_3d.ndim}")
    
    print("\n特殊数组创建：")
    print(f"  全零数组: np.zeros((3, 4))\n{np.zeros((3, 4))}")
    print(f"\n  全一数组: np.ones((2, 3))\n{np.ones((2, 3))}")
    print(f"\n  单位矩阵: np.eye(3)\n{np.eye(3)}")
    print(f"\n  等差数列: np.arange(0, 10, 2) = {np.arange(0, 10, 2)}")
    print(f"  等间距数组: np.linspace(0, 1, 5) = {np.linspace(0, 1, 5)}")
    print()


def array_indexing_slicing():
    print("=" * 60)
    print("任务2：数组的索引与切片")
    print("=" * 60)
    
    arr_1d = np.arange(10)
    print(f"\n原始1D数组: {arr_1d}")
    print(f"  arr[0] = {arr_1d[0]}")
    print(f"  arr[-1] = {arr_1d[-1]}")
    print(f"  arr[2:7] = {arr_1d[2:7]}")
    print(f"  arr[::2] = {arr_1d[::2]}")
    print(f"  arr[::-1] = {arr_1d[::-1]}")
    
    arr_2d = np.arange(1, 13).reshape(3, 4)
    print(f"\n原始2D数组:\n{arr_2d}")
    print(f"  arr[0, 0] = {arr_2d[0, 0]}")
    print(f"  arr[1, 2] = {arr_2d[1, 2]}")
    print(f"  arr[:, 0] = {arr_2d[:, 0]}")
    print(f"  arr[0, :] = {arr_2d[0, :]}")
    print(f"  arr[1:3, 1:3] =\n{arr_2d[1:3, 1:3]}")
    
    arr_3d = np.arange(24).reshape(2, 3, 4)
    print(f"\n原始3D数组:\n{arr_3d}")
    print(f"  arr[0, :, :] =\n{arr_3d[0, :, :]}")
    print(f"  arr[:, 0, :] =\n{arr_3d[:, 0, :]}")
    print(f"  arr[:, :, 0] = {arr_3d[:, :, 0]}")
    print()


def shape_operations():
    print("=" * 60)
    print("任务3：形状变换操作")
    print("=" * 60)
    
    arr = np.arange(12)
    print(f"\n原始数组: {arr}, 形状: {arr.shape}")
    
    arr_reshaped = arr.reshape(3, 4)
    print(f"\nreshape(3, 4):\n{arr_reshaped}")
    
    arr_reshaped = arr.reshape(2, 2, 3)
    print(f"\nreshape(2, 2, 3):\n{arr_reshaped}")
    
    arr_2d = np.arange(1, 13).reshape(3, 4)
    print(f"\n原始2D数组:\n{arr_2d}")
    
    arr_transposed = arr_2d.T
    print(f"\n转置 .T:\n{arr_transposed}")
    
    arr_transposed2 = arr_2d.transpose()
    print(f"\n转置 transpose():\n{arr_transposed2}")
    
    arr_flattened = arr_2d.flatten()
    print(f"\nflatten(): {arr_flattened}")
    
    arr_raveled = arr_2d.ravel()
    print(f"ravel(): {arr_raveled}")
    
    print("\n维度扩展：")
    arr_1d = np.array([1, 2, 3])
    print(f"  原始: {arr_1d}, shape: {arr_1d.shape}")
    print(f"  np.expand_dims(arr, axis=0): {np.expand_dims(arr_1d, axis=0).shape}")
    print(f"  np.expand_dims(arr, axis=1): {np.expand_dims(arr_1d, axis=1).shape}")
    print()


def matrix_operations():
    print("=" * 60)
    print("任务4：矩阵基本运算")
    print("=" * 60)
    
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print(f"\n矩阵A:\n{A}")
    print(f"\n矩阵B:\n{B}")
    
    print("\n1. 矩阵加法：")
    C_add = A + B
    print(f"  A + B =\n{C_add}")
    print(f"  np.add(A, B) =\n{np.add(A, B)}")
    
    print("\n2. 矩阵减法：")
    C_sub = A - B
    print(f"  A - B =\n{C_sub}")
    
    print("\n3. 矩阵乘法（元素级）：")
    C_mul = A * B
    print(f"  A * B =\n{C_mul}")
    print(f"  np.multiply(A, B) =\n{np.multiply(A, B)}")
    
    print("\n4. 矩阵乘法（矩阵级）：")
    C_matmul = A @ B
    print(f"  A @ B =\n{C_matmul}")
    print(f"  np.matmul(A, B) =\n{np.matmul(A, B)}")
    print(f"  np.dot(A, B) =\n{np.dot(A, B)}")
    
    print("\n5. 矩阵转置：")
    print(f"  A.T =\n{A.T}")
    print(f"  np.transpose(A) =\n{np.transpose(A)}")
    
    print("\n6. 矩阵求逆（方阵）：")
    A_inv = np.linalg.inv(A)
    print(f"  np.linalg.inv(A) =\n{A_inv}")
    print(f"  A @ A_inv =\n{A @ A_inv}")
    
    print("\n7. 矩阵行列式：")
    det_A = np.linalg.det(A)
    print(f"  np.linalg.det(A) = {det_A:.2f}")
    
    print("\n8. 矩阵迹（对角线元素之和）：")
    trace_A = np.trace(A)
    print(f"  np.trace(A) = {trace_A}")
    print()


def random_data_statistics():
    print("=" * 60)
    print("任务5：随机数据生成与统计分析")
    print("=" * 60)
    
    np.random.seed(42)
    
    print("\n1. 生成随机数据：")
    rand_arr = np.random.rand(5)
    print(f"  np.random.rand(5) = {rand_arr}")
    
    randn_arr = np.random.randn(5)
    print(f"  np.random.randn(5) = {randn_arr}")
    
    randint_arr = np.random.randint(0, 100, 10)
    print(f"  np.random.randint(0, 100, 10) = {randint_arr}")
    
    print("\n2. 统计分析：")
    data = np.random.randn(1000)
    print(f"  数据量: {len(data)}")
    print(f"  均值: {np.mean(data):.4f}")
    print(f"  中位数: {np.median(data):.4f}")
    print(f"  方差: {np.var(data):.4f}")
    print(f"  标准差: {np.std(data):.4f}")
    print(f"  最小值: {np.min(data):.4f}")
    print(f"  最大值: {np.max(data):.4f}")
    print(f"  极差: {np.ptp(data):.4f}")
    print(f"  分位数(25%): {np.percentile(data, 25):.4f}")
    print(f"  分位数(75%): {np.percentile(data, 75):.4f}")
    
    print("\n3. 二维数据统计：")
    data_2d = np.random.randn(100, 3)
    print(f"  数据形状: {data_2d.shape}")
    print(f"  每列均值: {np.mean(data_2d, axis=0).round(4)}")
    print(f"  每行均值: {np.mean(data_2d, axis=1).round(4)[:5]}...")
    print(f"  协方差矩阵:\n{np.cov(data_2d.T).round(4)}")
    print(f"  相关系数矩阵:\n{np.corrcoef(data_2d.T).round(4)}")
    print()


if __name__ == '__main__':
    array_creation()
    array_indexing_slicing()
    shape_operations()
    matrix_operations()
    random_data_statistics()
    
    print("=" * 60)
    print("所有NumPy数组基础操作任务完成！")
    print("=" * 60)