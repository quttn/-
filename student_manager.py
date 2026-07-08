import json
import os

DATA_FILE = 'students.json'
students = []

#检查文件是否存在 → 存在则读取 → 解析JSON → 赋值给students → 不存在则students为空列表
def load_data():
    global students
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                students = json.load(f)
            print(f"成功加载 {len(students)} 条学生数据")
        except Exception as e:
            print(f"加载数据失败: {e}")
            students = []
    else:
        students = []

#将学生数据写入JSON文件，实现数据持久化
def save_data():
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(students, f)
        print("数据已保存")
    except Exception as e:
        print(f"保存数据失败: {e}")

#菜单
def show_menu():
    print("\n===== 学生成绩管理系统 =====")
    print("1. 成绩录入")
    print("2. 成绩查询")
    print("3. 成绩统计")
    print("4. 修改成绩")
    print("5. 删除学生")
    print("6. 显示所有学生")
    print("7. 退出系统")
    print("=="*10)

#录入新学生信息，包括学号、姓名和各科成绩
def add_student():
    print("\n------ 成绩录入 ------")
    student_id = input("请输入学号: ")
    
    for student in students:
        if student['id'] == student_id:
            print(f"学号 {student_id} 已存在！")
            return
    
    name = input("请输入姓名: ")
    if not name:
        print("姓名不能为空！")
        return
    
    scores = {}
    subjects = ['语文', '数学', '英语']
    
    for subject in subjects:
        while True:
            try:
                score = float(input(f"请输入{subject}成绩: "))
                if 0 <= score <= 100:
                    scores[subject] = score
                    break
                else:
                    print("成绩必须在 0-100 之间！")
            except ValueError:
                print("请输入有效的数字！")
    
    student = {
        'id': student_id,
        'name': name,
        'scores': scores
    }
    students.append(student)
    save_data()
    print(f"学生 {name} 的成绩录入成功！")

#按学号或姓名查询学生详细信息
def query_student():
    print("\n------ 成绩查询 ------")
    if not students:
        print("暂无学生信息！")
        return
    
    query_type = input("请选择查询方式：1-按学号查询 2-按姓名查询: ")
    
    if query_type == '1':
        student_id = input("请输入学号: ")
        for student in students:
            if student['id'] == student_id:
                display_student_info(student)
                return
        print(f"未找到学号为 {student_id} 的学生！")
    
    elif query_type == '2':
        name = input("请输入姓名: ")
        found = False
        for student in students:
            if student['name'] == name:
                display_student_info(student)
                found = True
        if not found:
            print(f"未找到姓名为 {name} 的学生！")
    
    else:
        print("无效的选择！")

#展示学生信息
def display_student_info(student):
    print(f"\n学号: {student['id']}")
    print(f"姓名: {student['name']}")
    print("成绩:")
    for subject, score in student['scores'].items():
        print(f"  {subject}: {score}")
    total = sum(student['scores'].values())
    average = total / len(student['scores'])
    print(f"总分: {total:.2f}")
    print(f"平均分: {average:.2f}")

#计算各科目统计数据和学生排名
def show_statistics():
    print("\n------ 成绩统计 ------")
    if not students:
        print("暂无学生信息！")
        return
    
    all_scores = {}
    subjects = ['语文', '数学', '英语']
    
    for subject in subjects:
        subject_scores = [student['scores'][subject] for student in students]
        all_scores[subject] = subject_scores
    
    print("\n各科目统计：")
    for subject, scores in all_scores.items():
        avg = sum(scores) / len(scores)
        max_score = max(scores)
        min_score = min(scores)
        print(f"{subject}:")
        print(f"  平均分: {avg:.2f}")
        print(f"  最高分: {max_score}")
        print(f"  最低分: {min_score}")
    
    print("\n所有学生平均分排名：")
    sorted_students = sorted(students, key=lambda s: sum(s['scores'].values()) / len(s['scores']), reverse=True)
    for idx, student in enumerate(sorted_students, 1):
        avg = sum(student['scores'].values()) / len(student['scores'])
        print(f"{idx}. {student['name']} (学号: {student['id']}) - 平均分: {avg:.2f}")

#修改成绩
def modify_score():
    print("\n------ 修改成绩 ------")
    if not students:
        print("暂无学生信息！")
        return
    
    student_id = input("请输入要修改成绩的学生学号: ").strip()
    
    for student in students:
        if student['id'] == student_id:
            display_student_info(student)
            
            subjects = ['语文', '数学', '英语']
            print("\n请选择要修改的科目：")
            for i, subject in enumerate(subjects, 1):
                print(f"{i}. {subject}")
            
            while True:
                try:
                    choice = int(input("请输入科目序号: "))
                    if 1 <= choice <= 3:
                        subject = subjects[choice - 1]
                        break
                    else:
                        print("请输入 1-3 之间的数字！")
                except ValueError:
                    print("请输入有效的数字！")
            
            while True:
                try:
                    new_score = float(input(f"请输入{subject}的新成绩: "))
                    if 0 <= new_score <= 100:
                        student['scores'][subject] = new_score
                        save_data()
                        print(f"{student['name']}的{subject}成绩已更新为 {new_score}！")
                        return
                    else:
                        print("成绩必须在 0-100 之间！")
                except ValueError:
                    print("请输入有效的数字！")
    
    print(f"未找到学号为 {student_id} 的学生！")

#删除学生
def delete_student():
    print("\n------ 删除学生 ------")
    if not students:
        print("暂无学生信息！")
        return
    
    student_id = input("请输入要删除的学生学号: ").strip()
    
    for i, student in enumerate(students):
        if student['id'] == student_id:
            confirm = input(f"确定要删除学生 {student['name']} 吗？(y/n): ").strip().lower()
            if confirm == 'y':
                del students[i]
                save_data()
                print(f"学生 {student['name']} 已删除！")
            else:
                print("取消删除操作")
            return
    
    print(f"未找到学号为 {student_id} 的学生！")

#列出所有学生的简要信息（学号、姓名、平均分）
def show_all_students():
    print("\n------ 所有学生列表 ------")
    if not students:
        print("暂无学生信息！")
        return
    
    print(f"共 {len(students)} 名学生：")
    for i, student in enumerate(students, 1):
        avg = sum(student['scores'].values()) / len(student['scores'])
        print(f"{i}. 学号: {student['id']}, 姓名: {student['name']}, 平均分: {avg:.2f}")

#加载数据 → 显示菜单 → 获取用户选择 → 调用对应函数 → 循环直到选择退出
def main():
    load_data()
    
    while True:
        show_menu()
        choice = input("请输入选择（1-7）: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            query_student()
        elif choice == '3':
            show_statistics()
        elif choice == '4':
            modify_score()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            show_all_students()
        elif choice == '7':
            save_data()
            print("感谢使用学生成绩管理系统！")
            break
        else:
            print("无效的选择，请输入 1-7 之间的数字！")


if __name__ == '__main__':
    main()