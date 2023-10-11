import threading

# สร้างตัวแปรแชร์
shared_variable = 0
lock = threading.Lock()

# ฟังก์ันที่จะรันในแต่ละ thread
def update_shared_variable():
    global shared_variable
    for _ in range(1000000):
        with lock:  # เข้าถึงตัวแปรแชร์ในบริเวณนี้จะใช้ Lock
            shared_variable += 1

# สร้าง threads
thread1 = threading.Thread(target=update_shared_variable)
thread2 = threading.Thread(target=update_shared_variable)

# เริ่มการทำงานของ threads
thread1.start()
thread2.start()

# รอให้ทุก thread ทำงานเสร็จ
thread1.join()
thread2.join()

# แสดงค่าของตัวแปรแชร์
print("Shared Variable:", shared_variable)


# เรานำเข้าคลัง threading เพื่อใช้ในการจัดการ threads.

# เราสร้างตัวแปร shared_variable เพื่อเป็นตัวแปรที่ถูกแชร์ระหว่าง threads และสร้าง Lock ด้วย threading.Lock() เพื่อใช้ในการควบคุมการเข้าถึง shared_variable.

# เรานิยามฟังก์ชัน update_shared_variable ซึ่งจะรันในแต่ละ thread. ฟังก์ชันนี้จะเข้าไปในลูปที่ทำการเพิ่มค่าของ shared_variable 1,000,000 ครั้ง แต่จะใช้ Lock เพื่อป้องกัน race condition.

# เราสร้างสอง thread (thread1 และ thread2) และกำหนดให้ทั้งสอง thread รันฟังก์ชัน update_shared_variable.

# เริ่มการทำงานของทั้งสอง thread ด้วย thread1.start() และ thread2.start().

# รอให้ทั้งสอง thread ทำงานเสร็จด้วย thread1.join() และ thread2.join().

# แสดงค่าของ shared_variable ที่ถูกเพิ่มขึ้นจากการทำงานของทั้งสอง thread และไม่มี race condition ที่เกิดขึ้น.

# การใช้ Lock ในที่นี้ทำให้ทุก thread รอการควบคุมก่อนที่จะเข้าถึง shared_variable, ทำให้ไม่มีการแชร์ข้อมูลที่ไม่ปลอดภัยระหว่าง threads และผลลัพธ์ถูกต้องตามที่คาดหวัง.