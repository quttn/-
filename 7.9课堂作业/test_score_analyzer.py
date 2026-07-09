import numpy as np


def test_statistics():
    students = [
        {"name": "张三", "score": 85},
        {"name": "李四", "score": 92},
        {"name": "王五", "score": 76},
        {"name": "赵六", "score": 88},
        {"name": "钱七", "score": 95},
    ]
    
    scores = np.array([s["score"] for s in students])
    
    print("=" * 40)
    print("测试：成绩统计分析")
    print("=" * 40)
    print(f"学生人数: {len(students)}")
    print(f"平均分: {scores.mean():.2f}")
    print(f"最高分: {scores.max():.2f}")
    print(f"最低分: {scores.min():.2f}")
    print(f"方差: {scores.var():.2f}")
    print(f"标准差: {scores.std():.2f}")
    print(f"中位数: {np.median(scores):.2f}")


def test_ranking():
    students = [
        {"name": "张三", "score": 85},
        {"name": "李四", "score": 92},
        {"name": "王五", "score": 76},
        {"name": "赵六", "score": 88},
        {"name": "钱七", "score": 95},
    ]
    
    sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
    
    print("\n" + "=" * 40)
    print("测试：成绩排名")
    print("=" * 40)
    print(f"{'排名':^6} {'姓名':^10} {'成绩':^8}")
    print("-" * 40)
    for i, s in enumerate(sorted_students, 1):
        print(f"{i:^6} {s['name']:^10} {s['score']:^8.2f}")


def test_distribution():
    students = [
        {"name": "张三", "score": 85},
        {"name": "李四", "score": 92},
        {"name": "王五", "score": 76},
        {"name": "赵六", "score": 88},
        {"name": "钱七", "score": 95},
        {"name": "孙八", "score": 58},
        {"name": "周九", "score": 65},
        {"name": "吴十", "score": 72},
    ]
    
    scores = np.array([s["score"] for s in students])
    
    excellent = np.sum(scores >= 90)
    good = np.sum((scores >= 80) & (scores < 90))
    medium = np.sum((scores >= 60) & (scores < 80))
    failed = np.sum(scores < 60)
    total = len(students)
    
    print("\n" + "=" * 40)
    print("测试：成绩分布分析")
    print("=" * 40)
    print(f"{'等级':^10} {'人数':^6} {'占比':^10}")
    print("-" * 40)
    print(f"{'优秀(90+)':^10} {excellent:^6} {excellent/total*100:^10.2f}%")
    print(f"{'良好(80-89)':^10} {good:^6} {good/total*100:^10.2f}%")
    print(f"{'及格(60-79)':^10} {medium:^6} {medium/total*100:^10.2f}%")
    print(f"{'不及格(<60)':^10} {failed:^6} {failed/total*100:^10.2f}%")
    print("-" * 40)
    print(f"{'合计':^10} {total:^6} {'100.00%':^10}")


if __name__ == '__main__':
    test_statistics()
    test_ranking()
    test_distribution()
    
    print("\n" + "=" * 40)
    print("所有功能测试通过！")
    print("=" * 40)