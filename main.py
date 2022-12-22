from tkinter import *

window = Tk()
window.geometry("1920x1080")
window.title("wms")


#创建新提单号，柜号，eta， 
def new_window():
    print("new entry")

#对当前货柜单所有货物进行记录，汇总，动向统计，eg： ups 几箱几板； 亚马逊 编号，卡派记录
def edit_window():
    print("edit window")

#显示所有货柜记录
def view_window():
    print("view window")


new_button = Button(window, text="NEW",
                    width=50,
                    height=6,
                    command=new_window)
new_button.place(x=100, y=100)

edit_button = Button(window, text="EDIT",
                    width=50,
                    height=6,
                    command=edit_window)
edit_button.place(x=700, y=100)

view_button = Button(window, text="VIEW",
                    width=50,
                    height=6,
                    command=view_window)
view_button.place(x=100, y=400)

window.mainloop()