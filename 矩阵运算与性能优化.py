import numpy as np
import time


def matrix_multiplication_benchmark():
    print("=" * 60)
    print("任务1：矩阵乘法优化")
    print("=" * 60)
    
    np.random.seed(42)
    A = np.random.rand(1000, 2000)
    B = np.random.rand(2000, 3000)
    
    print(f"矩阵 A: {A.shape}")
    print(f"矩阵 B: {B.shape}")
    print(f"结果矩阵: (1000, 3000)")
    print()
    
    methods = [
        ('np.dot(A, B)', lambda: np.dot(A, B)),
        ('A @ B', lambda: A @ B),
        ('np.matmul(A, B)', lambda: np.matmul(A, B)),
    ]
    
    results = []
    for name, func in methods:
        start = time.perf_counter()
        for _ in range(5):
            result = func()
        end = time.perf_counter()
        avg_time = (end - start) / 5 * 1000
        results.append((name, avg_time))
        print(f"{name:25s} 平均耗时: {avg_time:.2f} ms")
    
    min_time = min(r[1] for r in results)
    print("\n性能对比：")
    for name, avg_time in results:
        ratio = avg_time / min_time
        print(f"{name:25s} 耗时: {avg_time:.2f} ms  相对速度: {ratio:.2f}x")
    
    print("\n结论：三种方法在现代NumPy中底层实现相同，性能差异很小")
    print("np.dot适用于向量点积和矩阵乘法，@和np.matmul更明确用于矩阵乘法")
    print()


def memory_layout_benchmark():
    print("=" * 60)
    print("任务2：内存布局影响")
    print("=" * 60)
    
    np.random.seed(42)
    
    c_order = np.random.rand(1000, 1000).astype(np.float64, order='C')
    f_order = np.random.rand(1000, 1000).astype(np.float64, order='F')
    
    print(f"C顺序(行优先)数组: flags.c_contiguous = {c_order.flags.c_contiguous}")
    print(f"F顺序(列优先)数组: flags.f_contiguous = {f_order.flags.f_contiguous}")
    print()
    
    print("按行求和（沿axis=1）：")
    start = time.perf_counter()
    for _ in range(100):
        c_row_sum = np.sum(c_order, axis=1)
    c_row_time = (time.perf_counter() - start) / 100 * 1000
    
    start = time.perf_counter()
    for _ in range(100):
        f_row_sum = np.sum(f_order, axis=1)
    f_row_time = (time.perf_counter() - start) / 100 * 1000
    
    print(f"  C顺序数组: {c_row_time:.4f} ms")
    print(f"  F顺序数组: {f_row_time:.4f} ms")
    print(f"  差异: C顺序快 {f_row_time/c_row_time:.2f}x")
    print()
    
    print("按列求和（沿axis=0）：")
    start = time.perf_counter()
    for _ in range(100):
        c_col_sum = np.sum(c_order, axis=0)
    c_col_time = (time.perf_counter() - start) / 100 * 1000
    
    start = time.perf_counter()
    for _ in range(100):
        f_col_sum = np.sum(f_order, axis=0)
    f_col_time = (time.perf_counter() - start) / 100 * 1000
    
    print(f"  C顺序数组: {c_col_time:.4f} ms")
    print(f"  F顺序数组: {f_col_time:.4f} ms")
    print(f"  差异: F顺序快 {c_col_time/f_col_time:.2f}x")
    print()
    
    print("结论：按存储顺序方向访问数据（C顺序按行，F顺序按列）性能更好")
    print("这是因为连续内存访问可以更好地利用CPU缓存")
    print()


def avoid_temporary_allocation():
    print("=" * 60)
    print("任务3：避免临时内存分配")
    print("=" * 60)
    
    np.random.seed(42)
    A = np.random.rand(500, 500)
    
    print(f"矩阵 A: {A.shape}")
    print("计算: A^2 + 2*A + 1")
    print()
    
    print("方法1：普通写法（产生中间变量）")
    start = time.perf_counter()
    for _ in range(100):
        result1 = A * A + 2 * A + 1
    method1_time = (time.perf_counter() - start) / 100 * 1000
    print(f"  耗时: {method1_time:.4f} ms")
    print(f"  中间数组数量: 3个 (A*A, 2*A, A*A+2*A)")
    print()
    
    print("方法2：使用out参数链式调用（避免中间分配）")
    start = time.perf_counter()
    for _ in range(100):
        result = np.empty_like(A)
        np.multiply(A, A, out=result)
        np.multiply(2, A, out=A)
        np.add(result, A, out=result)
        np.add(result, 1, out=result)
    method2_time = (time.perf_counter() - start) / 100 * 1000
    print(f"  耗时: {method2_time:.4f} ms")
    print(f"  中间数组数量: 0个（仅使用result）")
    print()
    
    print("方法3：使用np.add链式调用（保留原始A）")
    start = time.perf_counter()
    for _ in range(100):
        result = np.empty_like(A)
        np.multiply(A, A, out=result)
        temp = np.empty_like(A)
        np.multiply(2, A, out=temp)
        np.add(result, temp, out=result)
        np.add(result, 1, out=result)
    method3_time = (time.perf_counter() - start) / 100 * 1000
    print(f"  耗时: {method3_time:.4f} ms")
    print(f"  中间数组数量: 1个（temp）")
    print()
    
    print("性能对比：")
    min_time = min(method1_time, method2_time, method3_time)
    print(f"方法1(普通写法): {method1_time/min_time:.2f}x")
    print(f"方法2(out参数,修改A): {method2_time/min_time:.2f}x")
    print(f"方法3(out参数,保留A): {method3_time/min_time:.2f}x")
    print()
    
    print("结论：使用out参数可以减少内存分配次数，提高性能")
    print("对于大规模计算，内存分配和释放的开销非常显著")
    print("注意：方法2修改了原始数组A，实际使用时需注意")
    print()


if __name__ == '__main__':
    matrix_multiplication_benchmark()
    memory_layout_benchmark()
    avoid_temporary_allocation()
    
    print("=" * 60)
    print("所有测试完成！")
    print("=" * 60)