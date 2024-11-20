while True:
    # รับข้อความจากคีบอร์ด
    user_input = input("What you gotta say? : ")
    # ตรวจสอบว่าป้อน "STOP" หรือไม่
    if user_input == "STOP":
        break  # ออกจากลูปเมื่อพิมพ์ STOP
    # แสดงข้อความตอบกลับเมื่อใส่คำที่ไม่ใช่stop
    print(f"I got that! Anything else? : {user_input}")
