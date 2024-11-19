password = "Python is awesome"
#รับข้อมูลจากผู้ใช้
user_input = input("Enter the password: ")
#ตรวจสอบความถูกต้องของรหัส
if user_input == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
