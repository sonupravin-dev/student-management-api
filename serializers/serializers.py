class StudentSerializer:
    def serialize(self, student):
        return {
            "name": student.name,
            "age": student.age,
            "course": student.course
        }
