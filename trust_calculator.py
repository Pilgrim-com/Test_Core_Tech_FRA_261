def calculate_trust(reviews, competition, videos, distance=None):
    """
    คำนวณคะแนนความน่าเชื่อถือ (Trust) จากรีวิว, ประวัติการแข่งขัน, และระยะทาง
    :param reviews: คะแนนรีวิว (1-5)
    :param competition: ประวัติการแข่งขันในรูปแบบลิสต์ เช่น [("จังหวัด", "เยาวชน"), ("โลก", "มืออาชีพ")]
    :param videos: จำนวนวิดีโอการสอนที่มี (0 หรือ 1)
    :param distance: ระยะทางจากโค้ชถึงผู้เรียน (กิโลเมตร)
    :return: คะแนน Trust (0-100)
    """
    
    # น้ำหนักคะแนนของแต่ละระดับการแข่งขัน
    level_weights = {"จังหวัด": 5, "ภาค": 10, "ประเทศ": 20, "โลก": 40}
    group_weights = {"เยาวชน": 0.8, "มืออาชีพ": 1.0}  # น้ำหนักตามกลุ่ม
    
    if reviews > 0:  # กรณีมีรีวิว
        # คะแนนรีวิว (60% ของคะแนนทั้งหมด)
        review_score = reviews / 5
        review_weighted = review_score * 60

        # คะแนนจากประวัติการแข่งขัน (40% ของคะแนนทั้งหมด)
        if competition:
            competition_score = max(
                level_weights.get(level, 0) * group_weights.get(group, 1)
                for level, group in competition
            )
            competition_weighted = competition_score * 40  # น้ำหนักการแข่งขัน (40%)
        else:
            competition_weighted = 0
        
        # คะแนนวิดีโอ (เพิ่มคะแนน 10 คะแนนในกรณีไม่เต็ม 100 เท่านั้น)
        video_bonus = 10 if videos and (review_weighted + competition_weighted < 90) else 0

        # รวมคะแนน
        total_score = review_weighted + competition_weighted + video_bonus
    else:  # กรณีไม่มีรีวิว
        # คะแนนจากประวัติการแข่งขัน (70% ของคะแนนทั้งหมด)
        if competition:
            competition_score = max(
                level_weights.get(level, 0) * group_weights.get(group, 1)
                for level, group in competition
            )
            competition_weighted = (competition_score / 40) * 70  # น้ำหนักการแข่งขัน (70%)
        else:
            competition_weighted = 0
        
        # คะแนนจากระยะทาง (30% ของคะแนนทั้งหมด) หากไม่มีรีวิว
        distance_score = 0
        max_distance = 100 #ระยะไกลที่สุด 100 กิโลเมตร ที่รองรับในการคำนวณ
        if not reviews and distance is not None:
            normalized_distance = 1 - (distance / max_distance)
            distance_score = normalized_distance * 30  # คะแนนระยะทาง (0-100)
        
        # คะแนนจากวิดีโอการสอน (เพิ่มคะแนน 10 ถ้ามีวิดีโอ)
        video_score = 10 if videos and distance_score + competition_weighted < 90 else 0
        
        # รวมคะแนน
        total_score = competition_weighted + distance_score + video_score

    return total_score

