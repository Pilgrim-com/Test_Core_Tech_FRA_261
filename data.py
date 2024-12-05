from trust_calculator import calculate_trust

# ข้อมูลโค้ช
coaches = {
    'Coach A': {
        'style': [1, 0, 1, 0],  # เข้มงวด, ใจดี, จริงจัง, เฮฮา
        'trust': calculate_trust(
            reviews=4.5,
            competition=[("จังหวัด", "มืออาชีพ"), ("ภาค", "เยาวชน")],
            videos=1,
            distance=10  # ระยะทาง 10 กิโลเมตร
        )
    },
    'Coach B': {
        'style': [0, 1, 1, 1],  # ใจดี, จริงจัง, เฮฮา
        'trust': calculate_trust(
            reviews=0,  # ไม่มีรีวิว
            competition=[("โลก", "มืออาชีพ")],
            videos=0,
            distance=50  # ระยะทาง 50 กิโลเมตร
        )
    },
    'Coach C': {
        'style': [1, 1, 0, 0],  # เข้มงวด, ใจดี
        'trust': calculate_trust(
            reviews=0,
            competition=[("ประเทศ", "เยาวชน"), ("โลก", "มืออาชีพ")],
            videos=1,
            distance=5  # ระยะทาง 5 กิโลเมตร
        )
    },
    'Coach D': {
        'style': [0, 0, 1, 1],  # จริงจัง, เฮฮา
        'trust': calculate_trust(
            reviews=0,  # ไม่มีรีวิว
            competition=[("ประเทศ", "มืออาชีพ")],
            videos=0,
            distance=3  # ไม่มีข้อมูลระยะทาง
        )
    }
}

# ข้อมูลผู้เรียน
students = {
    'Student 1': [1, 0, 1, 0],  # ชอบ: เข้มงวด, จริงจัง
    'Student 2': [0, 1, 1, 1],  # ชอบ: ใจดี, จริงจัง, เฮฮา
    'Student 3': [1, 1, 0, 0],  # ชอบ: เข้มงวด, ใจดี
    'Student 4': [0, 0, 1, 1]   # ชอบ: จริงจัง, เฮฮา
}