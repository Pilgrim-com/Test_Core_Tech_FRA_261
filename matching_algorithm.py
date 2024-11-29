import numpy as np

def jaccard_similarity(vec1, vec2):
    # Jaccard Similarity = (Intersection / Union)
    intersection = np.sum(np.minimum(vec1, vec2))
    union = np.sum(np.maximum(vec1, vec2))
    return intersection / union if union != 0 else 0

def match_coaches(student_vector, coaches):
    results = []

    for coach_name, coach_data in coaches.items():
        coach_vector = coach_data['style']
        trust_score = coach_data['trust']

        # คำนวณความคล้ายคลึงด้วย Jaccard Similarity
        similarity = jaccard_similarity(student_vector, coach_vector)

        # คำนวณคะแนนรวมตามสูตรที่ถูกต้อง
        weighted_score = (trust_score * 0.6) + (similarity * 40)

        # บันทึกผลลัพธ์
        results.append((coach_name, similarity, trust_score, weighted_score))

    # เรียงลำดับโดยใช้คะแนนรวม
    results = sorted(results, key=lambda x: x[3], reverse=True)

    return results
