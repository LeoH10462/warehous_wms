from tkinter import *
from tkinter import ttk
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from data_bol import Bol

window = Tk()
window.geometry("1920x1080")
window.title("wms")

myBol = Bol()

#创建新提单号，柜号，eta， ----新增
def new_window():

    #新增---创建新窗口
    window = Tk()
    window.geometry("300x600")
    window.title('新增')

    #输入框-货柜客户
    customer_show_label = Label(window, text="输入 客户：",font=("Ink Free", 20))
    customer_show_label.pack()
    cmb_customer = ttk.Combobox(window)
    cmb_customer.pack()
    cmb_customer['value'] = ('委达','整柜','泛美','泛整','彦达','彦整','空运','恒达','飞扬')
    myBol.setCustomer(cmb_customer['value'])

    #输入框-BOL
    bol_show_label = Label(window, text="输入 提单号：",font=("Ink Free", 20))
    bol_show_label.pack()
    text_bol = Text(window, bg = "light yellow", font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    text_bol.pack()
    myBol.setmbl(text_bol)

    #输入框-柜号
    container_show_label = Label(window, text="输入 柜号：",font=("Ink Free", 20))
    container_show_label.pack()
    text_container = Text(window, bg = "light yellow", font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    text_container.pack()
    myBol.setContainer(text_container)

    #输入框-ETA
    eta_show_label = Label(window, text="输入 ETA:",font=("Ink Free", 20))
    eta_show_label.pack()
    text_eta = Text(window, bg = "light yellow", font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    text_eta.pack()
    myBol.setEta(text_eta)

    #输入框-卡车公司
    truck_show_label = Label(window, text="输入 卡车公司：",font=("Ink Free", 20))
    truck_show_label.pack()
    text_truck = Text(window, bg = "light yellow", font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    text_truck.pack()
    myBol.setTruck(text_truck)

    window.mainloop()
    print("new entry")

#对当前货柜单所有货物进行记录，汇总，动向统计，eg： ups 几箱几板； 亚马逊 编号，卡派记录-----编辑
def edit_window():
    print("edit window")

#显示所有货柜记录 -----查看
def view_window():
    myBol.printInfo()
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