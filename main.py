from data import coaches, students
from matching_algorithm import match_coaches

def main():
    for student_name, student_vector in students.items():
        print(f"\nผลลัพธ์การจับคู่สำหรับ {student_name}")
        results = match_coaches(student_vector, coaches)

        # แสดงผลลัพธ์ 3 อันดับแรก พร้อมคะแนนรวม
        for i, (coach, similarity, trust, weighted_score) in enumerate(results[:4], start=1):
            print(f"{i}. {coach}: ความคล้ายคลึง = {similarity:.2f}, ความน่าเชื่อถือ = {trust:.2f}, คะแนนรวม = {weighted_score:.2f}")
        
        print(f"**------------------{student_name}------------------**")

if __name__ == "__main__":
    main()
