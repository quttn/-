import math

# 1. 写入计算记录到文件
def write_history(expr, result):
    try:
        with open("calc_history.txt", "a") as f:
            f.write(f"{expr} = {result}\n")
    except IOError as e:
        print(f"文件写入失败：{e}")

# 2. 读取并打印全部历史记录
def read_history():
    print("\n===== 计算历史记录 =====")
    try:
        with open("calc_history.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                print("暂无计算记录")
                return
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("历史文件不存在，还没有计算记录")
    except IOError as e:
        print(f"读取文件出错：{e}")

# 3. 获取合法数字输入（异常处理）
def get_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("输入错误！请输入有效数字")

# 4. 计算核心运算逻辑
def calculate(op, n1, n2):
    expr = ""
    res = 0
    if op == "+":
        expr = f"{n1} + {n2}"
        res = n1 + n2
    elif op == "-":
        expr = f"{n1} - {n2}"
        res = n1 - n2
    elif op == "*":
        expr = f"{n1} * {n2}"
        res = n1 * n2
    elif op == "/":
        if n2 == 0:
            raise ZeroDivisionError("除数不能为0")
        expr = f"{n1} / {n2}"
        res = n1 / n2
    elif op == "**":
        expr = f"{n1} ** {n2}"
        res = n1 ** n2
    elif op == "sqrt":
        if n1 < 0:
            raise ValueError("负数无法开平方根")
        expr = f"sqrt({n1})"
        res = math.sqrt(n1)
    elif op == "square":
        expr = f"{n1} ^ 2"
        res = n1 ** 2
    else:
        raise ValueError("无效运算符")
    return expr, res

# 5. 单次计算交互入口
def single_calc():
    print("\n可选运算：+ - * / **(幂) square(平方) sqrt(开方)")
    op = input("请输入运算符：").strip()
    # 单目运算（开方、平方只需要一个数）
    if op in ["sqrt", "square"]:
        num1 = get_number("请输入数字：")
        num2 = 0
    else:
        num1 = get_number("请输入第一个数：")
        num2 = get_number("请输入第二个数：")
    try:
        expr, result = calculate(op, num1, num2)
        print(f"计算结果：{expr} = {result}")
        write_history(expr, result)
    except (ZeroDivisionError, ValueError) as err:
        print(f"计算失败：{err}")

# 6. 主菜单函数（程序入口）
def main_menu():
    while True:
        print("\n===== 数学计算器 =====")
        print("1. 进行计算")
        print("2. 查看历史记录")
        print("3. 退出程序")
        choice = input("请选择功能(1/2/3)：").strip()
        if choice == "1":
            single_calc()
        elif choice == "2":
            read_history()
        elif choice == "3":
            print("程序已退出")
            break
        else:
            print("输入无效，请选择1、2、3")

# 程序启动
if __name__ == "__main__":
    main_menu()