from data import coaches, students
from matching_algorithm import match_coaches

ground_truth = {
    "Student 1": "Coach A",
    "Student 2": "Coach B",
    "Student 3": "Coach C",
    "Student 4": "Coach D"
}


def calculate_accuracy(students, coaches, ground_truth):
    correct_matches = 0
    total_students = len(students)

    for student_name, student_vector in students.items():
        # เรียกใช้ matching_algorithm
        results = match_coaches(student_vector, coaches)

        # ตรวจสอบว่าโค้ชอันดับหนึ่งตรงกับ ground truth หรือไม่
        best_match = results[0][0]  # ชื่อโค้ชที่ดีที่สุด
        if best_match == ground_truth[student_name]:
            correct_matches += 1
        print(f"{results[0][0]}")

    # คำนวณ Accuracy
    accuracy = (correct_matches / total_students) * 100
    return accuracy

accuracy = calculate_accuracy(students, coaches, ground_truth)
print(f"Accuracy ของ Matching Algorithm คือ: {accuracy:.2f}%")
