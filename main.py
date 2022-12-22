from tkinter import *

window = Tk()
window.geometry("1920x1080")
window.title("wms")


#创建新提单号，柜号，eta， ----新增
def new_window():

    #新增---创建新窗口
    window = Tk()
    window.geometry("300x600")
    window.title('新增')

    #输入框
    text_bol = Text(window, 
                    bg = "light yellow",
                    font=("Ink Free", 25),
                    height= 1,
                    width=10,
                    fg = "purple"
                    )
    text_bol.pack()
    window.mainloop()
    print("new entry")

#对当前货柜单所有货物进行记录，汇总，动向统计，eg： ups 几箱几板； 亚马逊 编号，卡派记录-----编辑
def edit_window():
    print("edit window")

#显示所有货柜记录 -----查看
def view_window():
    print("view window")

#对应 new_window 按键-新增
new_button = Button(window, text="NEW",
                    width=50,
                    height=6,
                    command=new_window)
new_button.place(x=100, y=100)

#对应 edit_window 按键-编辑
edit_button = Button(window, text="EDIT",
                    width=50,
                    height=6,
                    command=edit_window)
edit_button.place(x=700, y=100)

#对应 view_window 按键-查看
view_button = Button(window, text="VIEW",
                    width=50,
                    height=6,
                    command=view_window)
view_button.place(x=100, y=400)



window.mainloop()