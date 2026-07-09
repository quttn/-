import numpy as np


students = []


def show_menu():
    print("=" * 40)
    print("成绩分析系统")
    print("=" * 40)
    print("1. 输入成绩数据")
    print("2. 查看成绩统计")
    print("3. 查看成绩排名")
    print("4. 查看成绩分布")
    print("5. 查询学生成绩")
    print("6. 退出系统")
    print("=" * 40)


def input_scores():
    global students
    students = []
    
    while True:
        try:
            num = int(input("请输入学生人数: "))
            if num > 0:
                break
            else:
                print("请输入正整数！")
        except ValueError:
            print("请输入有效的数字！")
    
    for i in range(num):
        print(f"\n请输入第{i+1}个学生信息:")
        name = input("请输入学生姓名: ").strip()
        while not name:
            name = input("姓名不能为空，请重新输入: ").strip()
        
        while True:
            try:
                score = float(input("请输入成绩: "))
                if 0 <= score <= 100:
                    break
                else:
                    print("成绩必须在0-100之间！")
            except ValueError:
                print("请输入有效的成绩！")
        
        students.append({"name": name, "score": score})
    
    print(f"\n成功录入{num}个学生的成绩数据！")


def show_statistics():
    if not students:
        print("请先输入成绩数据！")
        return
    
    scores = np.array([s["score"] for s in students])
    
    print("\n" + "=" * 40)
    print("成绩统计分析")
    print("=" * 40)
    print(f"学生人数: {len(students)}")
    print(f"平均分: {scores.mean():.2f}")
    print(f"最高分: {scores.max():.2f}")
    print(f"最低分: {scores.min():.2f}")
    print(f"方差: {scores.var():.2f}")
    print(f"标准差: {scores.std():.2f}")
    print(f"中位数: {np.median(scores):.2f}")
    print("=" * 40)


def show_ranking():
    if not students:
        print("请先输入成绩数据！")
        return
    
    sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
    
    print("\n" + "=" * 40)
    print("成绩排名")
    print("=" * 40)
    print(f"{'排名':^6} {'姓名':^10} {'成绩':^8}")
    print("-" * 40)
    
    for i, s in enumerate(sorted_students, 1):
        print(f"{i:^6} {s['name']:^10} {s['score']:^8.2f}")
    
    print("=" * 40)


def show_distribution():
    if not students:
        print("请先输入成绩数据！")
        return
    
    scores = np.array([s["score"] for s in students])
    
    excellent = np.sum(scores >= 90)
    good = np.sum((scores >= 80) & (scores < 90))
    medium = np.sum((scores >= 60) & (scores < 80))
    failed = np.sum(scores < 60)
    
    total = len(students)
    
    print("\n" + "=" * 40)
    print("成绩分布分析")
    print("=" * 40)
    print(f"{'等级':^10} {'人数':^6} {'占比':^10}")
    print("-" * 40)
    print(f"{'优秀(90+)':^10} {excellent:^6} {excellent/total*100:^10.2f}%")
    print(f"{'良好(80-89)':^10} {good:^6} {good/total*100:^10.2f}%")
    print(f"{'及格(60-79)':^10} {medium:^6} {medium/total*100:^10.2f}%")
    print(f"{'不及格(<60)':^10} {failed:^6} {failed/total*100:^10.2f}%")
    print("-" * 40)
    print(f"{'合计':^10} {total:^6} {'100.00%':^10}")
    print("=" * 40)
    
    print("\n成绩分布直方图：")
    bins = [0, 60, 70, 80, 90, 100]
    counts, _ = np.histogram(scores, bins=bins)
    labels = ["0-59", "60-69", "70-79", "80-89", "90-100"]
    
    max_count = counts.max()
    for i, (label, count) in enumerate(zip(labels, counts)):
        bar = "█" * int(count / max_count * 20) if max_count > 0 else ""
        print(f"{label:^10} | {bar} {count}人")


def query_student():
    if not students:
        print("请先输入成绩数据！")
        return
    
    name = input("\n请输入要查询的学生姓名: ").strip()
    
    found = [s for s in students if s["name"] == name]
    
    if found:
        print("\n查询结果：")
        for s in found:
            print(f"姓名: {s['name']}, 成绩: {s['score']:.2f}")
    else:
        print(f"未找到姓名为'{name}'的学生！")


def main():
    print("欢迎使用成绩分析系统！")
    
    while True:
        show_menu()
        
        try:
            choice = int(input("请选择: "))
            
            if choice == 1:
                input_scores()
            elif choice == 2:
                show_statistics()
            elif choice == 3:
                show_ranking()
            elif choice == 4:
                show_distribution()
            elif choice == 5:
                query_student()
            elif choice == 6:
                print("感谢使用成绩分析系统，再见！")
                break
            else:
                print("请输入1-6之间的数字！")
        
        except ValueError:
            print("请输入有效的数字！")
        
        input("\n按回车键继续...")
        print()


if __name__ == '__main__':
    main()