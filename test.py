import tkinter as tk
import tkinter.font as tkFont 




root = tk.Tk()
root.title("Minion Drawing")

canvas = tk.Canvas(root, width=800, height=660, bg="#78a5e9")
canvas.pack()


blink_state = [False]  # ใช้ list เพื่อให้เปลี่ยนค่าภายในฟังก์ชันได้
eye_cover_id = [None]    # เก็บ ID ของเปลือกตาเพื่อจะได้ลบภายหลัง

def blink_eye():
    if blink_state[0]:
        # ลืมตา: ลบเปลือกตาที่ปิดไว้
        if eye_cover_id[0]:
            canvas.delete(eye_cover_id[0])
            eye_cover_id[0] = None
        blink_state[0] = False
        canvas.after(3000, blink_eye)  # รอกระพริบอีกใน 3 วินาที
    else:
        # หลับตา: วาดทับตาทั้งดวงด้วยสีผิว (เหลือง)
        eye_cover_id[0] = canvas.create_oval(320, 165, 465, 340,
                                             fill="#ffe941", outline="#ffe941")
        blink_state[0] = True
        canvas.after(150, blink_eye)  # หลับแค่ 150 มิลลิวินาที

button_frame = tk.Frame(root)
button_frame.pack(pady=20)  # วางไว้ด้านขวาของ root window
btn_font = tkFont.Font(family="Tahoma", size=20, weight="bold")



def draw_bored():
    canvas.delete("face")  # ลบเฉพาะหน้าก่อนวาดใหม่
    canvas.delete("mouth")
    # ตาขาว
    canvas.create_arc(320, 165, 465, 340,start=0, extent=180, style=tk.CHORD,fill="#ffe941",outline="#ffe941", width=2)#eye top
    canvas.create_arc(320, 165, 465, 335,start=180, extent=180, style=tk.CHORD,fill="white",outline="white", width=2)#eye bottom
    #ตาดำ
    canvas.create_arc(340, 210, 400, 290,start=180, extent=180, style=tk.CHORD,fill="brown",outline="brown", width=2)
    canvas.create_arc(350, 220, 390, 280,start=180, extent=180, style=tk.CHORD,fill="black",outline="black", width=2)
    # ปาก
    canvas.create_line(290, 330, 360,380,390,380,smooth=True,width=2)

# สร้างปุ่ม
def show_bored_then_back():
    draw_bored()
    canvas.after(10000, lambda: draw_minion(canvas)) 

btn_bored = tk.Button(button_frame, text="bored face",font=btn_font, command=show_bored_then_back, width=15, height=2)
btn_bored.pack(side="left", padx=10)

btn_crazy = tk.Button(button_frame, text="crazy face",font=btn_font, command=lambda: print("Happy"), width=15, height=2)
btn_crazy.pack(side="left", padx=10)#

btn_love = tk.Button(button_frame, text="in love Face",font=btn_font, command=lambda: print("Happy"), width=15, height=2)
btn_love.pack(side="left", padx=10)


def draw_minion(canvas):
    # ตัว
    canvas.create_arc(250, 100, 550, 400, start=0, extent=180,  style=tk.CHORD,fill="#ffe941", outline="#ffe941", width=4)
    canvas.create_rectangle(250, 250, 550, 400, fill="#ffe941", outline="#ffe941")  
    canvas.create_rectangle(250, 250, 550, 550, fill="#ffe941", outline="#ffe941")

    # #ผม
    canvas.create_line(390,105,350,105,300,140,smooth=True,width=3)
    canvas.create_line(390,108,350,110,300,150,smooth=True,width=3)
    canvas.create_line(390,110,350,120,300,160,smooth=True,width=3)#left

    canvas.create_line(410,105,470,110,490,140,smooth=True,width=3)
    canvas.create_line(410,108,470,120,490,150,smooth=True,width=3)
    canvas.create_line(410,110,470,130,490,160,smooth=True,width=3)

    # # ตาแว่น
    canvas.create_oval(315, 160, 470, 340, fill="#ffe941", outline="silver", width=10)

    # ตาขาว
    canvas.create_oval(320, 165, 465, 335, fill="white", outline="white")
    
    #ตาดำ
    canvas.create_oval(360, 210, 425, 290, fill="brown", outline="brown")  # ตาสีน้ำตาลใหญ่
    canvas.create_oval(378, 230, 410, 270, fill="black", outline="black")  # ตาดำกลาง

    # # แว่นตาคาด
    canvas.create_rectangle(249, 220, 300, 270, fill="black", width=0)
    canvas.create_rectangle(300, 220, 320, 270, fill="silver", width=0)#left

    canvas.create_rectangle(470, 220, 500, 270, fill="silver", width=0)#right
    canvas.create_rectangle(500, 220, 552, 270, fill="black", width=0)

    
    
    # ปากยิ้ม
    canvas.create_arc(340, 320, 450, 400, start=180, extent=180, style=tk.CHORD ,fill="#dd6f6e",outline="#ffe941", width=3,tag="face")
    

    # # ชุดเอี๊ยม
    canvas.create_polygon(
                            250,390,
                            250,430,
                            280,460,
                            280,500,
                            250,500,
                            250,550,
                            550,550,
                            550,500,
                            520,500,
                            520,460,
                            550,430,
                            550,390,
                            500,440,
                            300,440,
                            outline='#6281b0', fill='#6281b0')
    # ดีเทลชุด
    canvas.create_polygon(
                        350,455,
                        350,455,
                        450,455,
                        450,455,
                        450,500,
                        450,500,
                        400,525,
                        350,500,
                        350,500,
                        350,455,
                        
                        outline='#3b5572',fill='#6281b0' ,smooth=True,width=1)
    
    canvas.create_oval(380,465,420,505, fill="#6281b0", outline="#313131", width=10)

    canvas.create_oval(290,450,310,470, fill="gray", outline="#313131", width=2)
    canvas.create_oval(490,450,510,470, fill="gray", outline="#313131", width=2)

    canvas.create_line( 520,500,
                        535,512,
                        550,525, fill="gray", width=1,smooth=True)
    canvas.create_arc(250, 510, 550, 590,start=180, extent=180, style=tk.CHORD,fill="#6281b0", outline="#6281b0")

    

    # # แขน
    canvas.create_polygon(250, 423, 
                          220,480,
                          215,510,
                          212,530,
                          210,540,
                          209,551,

                          231,551,
                          231,530,
                          234,510,
                          240,485,
                          254,478,
                          250,443
                          ,fill='#ffe941' ,smooth=True)#แขนซ้าย
    
    canvas.create_polygon(549,480,
                          558,475,
                          568,510,
                          568,530,
                          565,551,

                          586,552,
                          586,540,
                          586,530,
                          586,510,
                          587,480,
                          548,415,
                          fill='#ffe941',smooth=True)#แขนขวา
    
    #มือ
    canvas.create_polygon(202,551,
                            209,570,
                            202,590,
                            209,615,
                            213,610,
                            215,620,
                            226,627,
                            235,617,
                            233,615,
                            244,610,
                            # 224,610,
                            235,590,
                            225,578,
                            240,549,
                            221,551,
                            205,551,
                            fill='#313131',smooth=True)#มือซ้าย
    canvas.create_polygon(592,551,
                          587,570,
                          595,590,
                          587,610,
                          583,608,
                          585,620,
                          569,627,
                          560,617,
                          562,615,
                          551,610,
                          560,590,
                          570,578,
                          555,549,
                          574,551,
                          590,551,
                          fill='#313131', smooth=True)  # มือขวา

    # # ขา

    canvas.create_polygon(330, 580,  340, 600,  340,640,  395,630, 395,610,  395,580,  330,580 ,fill='#6281b0' ,smooth=True)
    canvas.create_polygon(408, 580,  408, 600,  408,630,  460,630, 460,615,  460,600,  475,570 ,fill='#6281b0' ,smooth=True)

    # รองเท้า (ด้านซ้าย)
    canvas.create_polygon(340, 620, 
                          310, 630, 
                          305, 645, 
                          340, 650, 
                          355, 650, 
                          393, 648, 
                          393, 632,
                          393, 624,
                          370,625, 
                          350, 623,
                          fill='#313131', smooth=True)

    # รองเท้า (ด้านขวา)
    canvas.create_polygon(408, 620,
                          408, 630,
                          408, 645, 
                          450, 655,
                          470, 658, 
                          465, 658, 
                          478, 655, 
                          470, 630, 
                          465, 625,
                          460, 620,
                          440, 630,  
                          fill='#313131', smooth=True)



draw_minion(canvas)
blink_eye()



root.mainloop()
