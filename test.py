import tkinter as tk




root = tk.Tk()
root.title("Minion Drawing")

canvas = tk.Canvas(root, width=800, height=800, bg="white")
canvas.pack()
# ขนาด Canvas และช่อง
width = 800
height = 800
grid_size = 50  # ขนาดช่องตาราง


# วาดเส้นแนวตั้ง (แกน X)
for x in range(0, width, grid_size):
    canvas.create_line(x, 0, x, height, fill="gray")
    canvas.create_text(x + 15, 10, text=f"{x}", fill="blue", anchor="nw")

# วาดเส้นแนวนอน (แกน Y)
for y in range(0, height, grid_size):
    canvas.create_line(0, y, width, y, fill="gray")
    canvas.create_text(5, y + 5, text=f"{y}", fill="red", anchor="nw")

# วาดแกน X และ Y ตรงกลาง (เส้นหนา)
canvas.create_line(width//2, 0, width//2, height, fill="black", width=2)  # แกน Y
canvas.create_line(0, height//2, width, height//2, fill="black", width=2)  # แกน X




def draw_minion(canvas):
    # ตัว
    canvas.create_arc(250, 100, 550, 400, start=0, extent=180,  style=tk.CHORD,fill="yellow", outline="yellow", width=4)
    canvas.create_rectangle(250, 250, 550, 400, fill="yellow", outline="yellow")  
    canvas.create_rectangle(250, 250, 550, 550, fill="yellow", outline="yellow")

    # #ผม
    canvas.create_line(390,105,350,105,300,140,smooth=True,width=3)
    canvas.create_line(390,108,350,110,300,150,smooth=True,width=3)
    canvas.create_line(390,110,350,120,300,160,smooth=True,width=3)#left

    canvas.create_line(410,105,470,110,490,140,smooth=True,width=3)
    canvas.create_line(410,108,470,120,490,150,smooth=True,width=3)
    canvas.create_line(410,110,470,130,490,160,smooth=True,width=3)
    
    
    

    
    # # ตาแว่น
    canvas.create_oval(315, 160, 470, 340, fill="yellow", outline="silver", width=10)

    # ตาขาว
    canvas.create_arc(320, 165, 465, 340,start=0, extent=180, style=tk.CHORD,fill="yellow",outline="yellow", width=2)#eye top
    canvas.create_arc(320, 165, 465, 335,start=180, extent=180, style=tk.CHORD,fill="white",outline="white", width=2)#eye bottom
    
    #ตาดำ
    canvas.create_arc(340, 210, 400, 290,start=180, extent=180, style=tk.CHORD,fill="brown",outline="brown", width=2)
    canvas.create_arc(350, 220, 390, 280,start=180, extent=180, style=tk.CHORD,fill="black",outline="black", width=2)

    # # แว่นตาคาด
    canvas.create_rectangle(250, 220, 300, 270, fill="black", width=0)
    canvas.create_rectangle(300, 220, 320, 270, fill="silver", width=0)#left

    canvas.create_rectangle(470, 220, 500, 270, fill="silver", width=0)#right
    canvas.create_rectangle(500, 220, 550, 270, fill="black", width=0)

    # # ปาก
    canvas.create_line(290, 330, 360,380,390,380,smooth=True,width=2)

    # # ชุดเอี๊ยม
    canvas.create_polygon(
                            250,390,#
                            250,430,
                            280,460,
                            280,500,
                            250,500,
                            250,550,#
                            550,550,#
                            550,500,
                            520,500,
                            520,460,
                            550,430,
                            550,390,#
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
    # canvas.create_line(100, 250, 50, 300, width=15, fill="yellow")
    # canvas.create_line(300, 250, 350, 300, width=15, fill="yellow")

    # # ขา
    canvas.create_polygon(340, 580,  350, 600,  350,640,  405,630, 405,610,  405,580,  340,580 ,fill='#6281b0' ,smooth=True)
    # canvas.create_polygon(230, 400, 230, 450, width=15, fill="black")


draw_minion(canvas)

root.mainloop()
