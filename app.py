students = []

def get_students():
    return students

def add_student(name, age, course):
    student = {
        "name": name,
        "age": age,
        "course": course
    }
    students.append(student)
    return student

def update_student(index, data):
    students[index] = data
    return data

def delete_student(index):
    students.pop(index)
    return "Deleted"
