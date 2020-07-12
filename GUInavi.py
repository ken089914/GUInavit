import tkinter as tk
import sys
import os
from PIL import Image, ImageTk
def navit():
    os.system("navit")
#def program_2():
    #subprocess.Popen(r'C:\python\program_2.exe')

#def program_3():
    #subprocess.Popen(r'C:\python\program_3.exe')

def finish_menu():
    sys.exit()



#menubox
root = tk.Tk()
root.title(u"menu")
root.geometry("1920x1080")



#program1
labeltitle = tk.Label(root, text=u'menu')
labeltitle.pack()

Label_Blanc = tk.Label(root, text=u'')
Label_Blanc.pack()
program_1_Button = tk.Button(root, text=u'navit', width=70)
program_1_Button["command"] = navit
program_1_Button.pack()
#program_1_Button.place(x=860,y=425)


# program2
#Label_Blanc = tk.Label(root, text=u'')
#Label_Blanc.pack()
#program_2_Button = tk.Button(root, text=u'program3', width=30)
#program_2_Button["command"] = program_2
#program_2_Button.pack()

# program3
#Label_Blanc = tk.Label(root, text=u'')
#Label_Blanc.pack()
#program_3_Button = tk.Button(root, text=u'program3', width=30)
#rogram_3_Button["command"] = program_3
#program_3_Button.pack()

# end
Label_Blanc = tk.Label(root, text=u'')
Label_Blanc.pack()
finish_menu_Button = tk.Button(root, text=u'end')
finish_menu_Button["command"] = finish_menu
finish_menu_Button.pack()


#canvas
canvas = tk.Canvas(root,width=1920,height=1080)
canvas.pack()
img = tk.PhotoImage(file = "/home/pi/.navit/panalogo.png")
canvas.create_image(950 ,300, image=img) 

root.mainloop()
