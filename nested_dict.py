#nested dictionary program
student_data=[
    {"name":"anjali",
     "age": 19
    },
    { "name":"riya",
      "age":15
    }
]
print(student_data)
def add_new_student(name,age):
    student_data.append({"name":name,"age":age})

add_new_student("shivi",23)
print(student_data)
