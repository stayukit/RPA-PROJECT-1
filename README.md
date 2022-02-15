# RPA-PROJECT-1
  โปรเจคนี้เป็นการรวบรวมความรู้ที่ได้เรียนจากคอร์ส Python Bootcamp 2021 โดยเพจ Uncleengineer และการศึกษาเพิ่มเติมจากแหล่งต่างๆในอินเตอร์เนต เพื่อให้ได้ Trick ที่ต้องการ แล้วนำหลักการ RPA มาประติดประต่อเข้าด้วยกัน ทั้งยังปรับประสิทธิภาพของโปรแกรมให้ทำงานได้ไวจนสำเร็จ  *ใช้ได้เฉพาะโปรแกรม T9
  
  Module หลักที่ใช้  tkinter-pyautogui-pynput-cv2-PIL-pytesseract-pyperclip

Problem - งานหน้าร้านปกติ
  เนื่องจากหน้างานจะใช้โปรแกรม POS ของบริษัทแม่ โปรเจคนี้นำมาปรับใช้ในงานส่งรูปสลิป และค่าบรืการทางไลน์ให้กับลูกค้าเครดิต จุดที่ล่าช้า
  1. ที่หน้าใบเสร็จจะต้องใช้การ crop หน้าสลิปแล้วไปวางช่องแชท ถ้ายิ่งมีรายการยาวๆ ต้อง crop หลายรอบ ทำให้รูปไม่ต่อเนื่อง **copy-paste รูปโดยตรง จะได้รูปสีเทา ต้องการพื้นสีขาว
  2. ต้องย้อนกลับไปดูราคาเพื่อพิมพ์สรุปลงในช่องแชท
  
ลำดับการทำงานของโปรแกรมโดยสังเขป
  1. run Main.py เริ่มต้นโปรแกรมจะให้ไปคลิกที่ลูกศร เพื่อบันทึกรูปลูกศร แล้วนำไปอ้างอิงจุดเปลี่ยนหน้า และช่วยในการ Copy ภาพ
  2. เมื่อเสร็จขั้นตอนที่ 1 แล้ว จะเข้าสู่การใช้งานหน้างานได้แล้ว
  3. คลิ๊กปุ่ม 
    3.1 ปุ่ม "Slip ใหม่" โปรแกรมจะใช้รูปลูกศร (ข้อ 1) อ้างอิงโดยถูกกำหนดตำแหน่งขึ้นไปเล็กน้อย เป็นตำแหน่งรูปที่สามารถ copy ได้ แล้วเลื่อนเมาส์ทำการ copy ภาพโดยอัตโนมัติ
        โปรแกรมทำการแสดงยอดที่ดึงมาได้
    3.2 ปุ่ม "หน้า 2" โปรแกรมจะเลื่อนเมาส์ไปกดลูกศรเพื่อเปลี่ยนไปหน้า 2 แล้ว copy slip โดยอัตโนมัติ
        โปรแกรมทำการแสดงยอดที่ดึงมาได้ล่าสุด + กับยอดหน้าที่แล้ว = ยอดรวม บาท
  4. เบื้องหลังโปรแกรมจะ save รูปแล้วดำเนินกระบวนการต่าง ๆ เป็นลำดับ
    4.1 ดึงข้อมูลไฟล์รูป-ปรับพื้นหลังเป็นสีขาว-copy ลง clipboard *สามารถนำไปวาง ได้รูปพื้นสีขาวตัวอักษรชัดเจน
    4.2 จากข้อมูลไฟล์รูป-ถอดข้อความ-เลือกเอาเฉพาะยอดสรุป-แสดงบนโปรแกรม *copy ไปวางในช่องแชทได้
    

วิดีโอสอนวิธีใช้: https://youtu.be/9KSal3XjvKg

ดาวโหลดไฟล์โปรแกรม (Zip): 
* แตกไฟล์แล้วสามารถ run as administrator ไฟล์ RPA.exe 
