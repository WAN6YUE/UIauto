db_file = 'student_register_data.txt'

def register_api():
    stu_data={}#初始化空字典 存学院数据
    print("欢迎注册 请完成学籍注册")
    name= input("姓名:").strip()
    age = input("年龄:").strip()
    phone = input("手机号:").strip()
    if phone in phone_list:
        exit('手机号已存在')
    id_card = input("身份证:").strip()
    if id_card in id_card_list:
        exit('身份证已存在')

    course_list=["测试",'前端','后端','运维']
    for index,course in enumerate(course_list):
        print(f"{index}.{course}")

    select_course_index=input("请选择你想选择的课程:")
    if select_course_index.isdigit():
        select_course_index=int(select_course_index)
        if 0<=select_course_index<=len(course_list):
            select_course=course_list[select_course_index]
        else:
            exit("不合法选项")
    else:
        exit("不合法选项")

    stu_data['name']=name
    stu_data['age'] = age
    stu_data['phone'] = phone
    stu_data['id_card'] = id_card
    stu_data['course'] = select_course

    return stu_data

def commit_to_db(filename,stu_data):
    f=open(filename,'a')
    row = f"{stu_data['name']},{stu_data['age']},{stu_data['phone']},{stu_data['id_card']},{stu_data['course']}"
    f.write(row)
    f.close()

def validates_data(filename):
    f =open(filename) #默认只读模式
    phone_list=[]
    id_card_list=[]
    for line in f:
        line = line.split(",")
        phone=line[2]
        id_card=line[3]
        phone_list.append(phone)
        id_card_list.append(id_card)

        return phone_list,id_card_list


phone_list,id_card_list = validates_data(db_file)

student_data=register_api()
print(student_data)

commit_to_db(db_file,student_data)