room = 1
while room < 4:
    sum = 0
    student_id = 1
    while student_id < 6:
        grade = int(input(f"Class #{room} Enter {student_id}'s grade: "))
        sum += grade
        student_id += 1
    print(f"{room}'s average is: {sum / student_id}.")
    room += 1