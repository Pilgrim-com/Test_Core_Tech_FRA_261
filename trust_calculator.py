def calculate_trust(reviews, competition, videos):
    """
    คำนวณคะแนนความน่าเชื่อถือ (Trust) จากรีวิว, ประวัติการแข่งขัน และจำนวนวิดีโอการสอน
    :param reviews: คะแนนรีวิว (1-5) คิดเป็น 60%
    :param competition: ประวัติการแข่งขัน โดยมีรูปแบบเป็นลิสต์ เช่น [("จังหวัด", "เยาวชน"), ("โลก", "มืออาชีพ")] คิดเป็น 40%
    :param videos: จำนวนวิดีโอการสอนที่มี (0 หรือ 1) คะแนนพิเศษ 10%
    :return: คะแนน Trust (0-100)
    """
    
    # น้ำหนักคะแนนของแต่ละระดับการแข่งขัน
    level_weights = {"จังหวัด": 5, "ภาค": 10, "ประเทศ": 20, "โลก": 40}
    group_weights = {"เยาวชน": 0.8, "มืออาชีพ": 1.0}

    # คะแนนรีวิว (60% ของคะแนนทั้งหมด)
    review_score = (reviews / 5)
    review_score_weighted = review_score * 60

    # คะแนนจากประวัติการแข่งขัน (40% ของคะแนนทั้งหมด)
    competition_score = sum(
        level_weights.get(level, 0) * group_weights.get(group, 1)
        for level, group in competition
    )
    competition_score_weighted = competition_score 

    # รวมคะแนนก่อนเพิ่มวิดีโอ
    total_score = review_score_weighted + competition_score_weighted

    # เพิ่มคะแนนโบนัสจากวิดีโอหากคะแนนรวมยังไม่ถึง 90
    if total_score < 90 and videos:
        total_score += 10 
        
    return total_score
