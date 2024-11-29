# FRA261 INNOVATION TEST

Repositories เป็นการทดสอบ Core Technology เป็นกลุ่มของพวกเรา ซึ่งเกี่ยวข้องกับการจับคู่ระหว่างนักเรียนและโค้ชตามความคล้ายคลึงในสไตล์และคะแนนความน่าเชื่อถือของโค้ช

## Structure

- **Main**   
    - **ไฟล์**: `main.py`
    - **คำอธิบาย**:  
    ไฟล์นี้มีหลักการทำงาน โดยจะทำการวนลูปผ่านรายชื่อของผู้เรียนและจับคู่พวกเขากับโค้ชตามความชอบ (สไตล์) และคะแนนความน่าเชื่อถือของโค้ช ผลลัพธ์จะแสดงในลำดับจากมากไปหาน้อย โดยแสดงโค้ชที่เหมาะสมที่สุด 3 คนสำหรับแต่ละผู้เรียน

- **Data**
    - **ไฟล์**: `data.py`
    - **คำอธิบาย**:  
    ไฟล์นี้ประกอบไปด้วยข้อมูลที่กำหนดไว้ล่วงหน้าสำหรับโค้ชและผู้เรียน โดยแต่ละโค้ชมีชุดของสไตล์การสอน และคะแนนความน่าเชื่อถือที่คำนวณจากการรีวิว, ประวัติการแข่งขัน และการมีวิดีโอการสอน นักเรียนแต่ละคนก็มีชุดความชอบเช่นกัน ซึ่งจะถูกเปรียบเทียบกับความชอบของโค้ชเพื่อหาคู่ที่เหมาะสมที่สุด

- **Trust Calculate**
    - **ไฟล์**: `trust_calculator.py`
    - **คำอธิบาย**:  
    ไฟล์นี้ประกอบไปด้วยการคำนวณคะแนนความน่าเชื่อถือสำหรับแต่ละโค้ช คะแนนความน่าเชื่อถือคำนวณจากสามปัจจัย ได้แก่ คะแนนรีวิว (60%), ประวัติการแข่งขัน (40%) และการมีวิดีโอการสอน (ซึ่งจะให้คะแนนเพิ่มถ้ามี) และคะแนนความน่าเชื่อถือที่คำนวณได้จะนำไปใช้ในการตัดสินใจในการจับคู่

- **Matching Algorithm**   
    - **ไฟล์**: `matching_algorithm.py`
    - **คำอธิบาย**:  
    ไฟล์นี้จะมีการจับคู่ระหว่างนักเรียนและโค้ชโดย **Content-Based Filtering Algorythm** ซึ่งอิงจากข้อมูลที่เกี่ยวข้องกับความชอบและลักษณะสไตล์ของผู้เรียนและโค้ช โดยจะใช้วิธีการคำนวณ **Jaccard Similarity** เพื่อเปรียบเทียบความคล้ายคลึงระหว่างสไตล์ของนักเรียนกับโค้ช และใช้คะแนนความน่าเชื่อถือ (Trust Score) และหาคะแนนรวมระหว่างทั้งสองโดยมีน้ำหนัก 40:60 และจัดอับดับโค้ชตามผลคะแนนรวมที่ได้

## การใช้งาน/ตัวอย่าง
ใช้โปรแกรมในไฟล์ `main.py` เพื่อเริ่มโปรแกรม! 🚀

1. รันไฟล์ `main.py` เพื่อเริ่มโปรแกรม
2. โปรแกรมจะแสดงโค้ชที่เหมาะสมที่สุด 3 คนสำหรับแต่ละนักเรียน โดยเรียงตามความคล้ายคลึงและความน่าเชื่อถือ
3. ผลลัพธ์จะแสดงคะแนนความคล้ายคลึง คะแนนความน่าเชื่อถือ และคะแนนที่มีน้ำหนักสำหรับแต่ละโค้ช

