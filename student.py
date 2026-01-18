def average_and_grade(marks):
    avg = sum(marks) / len(marks)
    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "D"
    result = f"Marks : {marks}\nAverage : {avg}\nGrade : {grade}"
    return result

if __name__ == "__main__":
    print(average_and_grade([80, 85, 90, 75, 88]))