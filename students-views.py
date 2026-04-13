students = []

def get_students():
    return students

def add_student(data):
    students.append(data)
    return data

def update_student(index, data):
    students[index] = data
    return data

def delete_student(index):
    students.pop(index)
    return "Deleted"
