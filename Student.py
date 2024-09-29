
# Student information management system

def calculate_total_and_grade(scores):
    total_score = sum(scores)
    # Define grading criteria
    if total_score >= 270:
        grade = 'A'
    elif total_score >= 240:
        grade = 'B'
    elif total_score >= 210:
        grade = 'C'
    elif total_score >= 180:
        grade = 'D'
    else:
        grade = 'F'
    return total_score, grade

def display_students(students):
    print("\nStudent Details:")
    print(f"{'Name':<20} {'Student ID':<15} {'Total Score':<15} {'Grade':<10}")
    print("=" * 60)
    for student in students:
        print(f"{student['name']:<20} {student['student_id']:<15} {student['total_score']:<15} {student['grade']:<10}")

def main():
    students = []
    
    while True:
        name = input("Enter student's name: ")
        student_id = input("Enter student ID: ")
        scores = []
        
        for subject in range(1, 4):
            score = int(input(f"Enter score for subject {subject}: "))
            scores.append(score)
        
        total_score, grade = calculate_total_and_grade(scores)
        
        # Store student information in a dictionary
        student_info = {
            'name': name,
            'student_id': student_id,
            'scores': scores,
            'total_score': total_score,
            'grade': grade
        }
        
        students.append(student_info)
        
        another = input("Do you want to enter another student? (yes/no): ").strip().lower()
        if another != 'yes':
            break

    display_students(students)

if __name__ == "__main__":
    main()
