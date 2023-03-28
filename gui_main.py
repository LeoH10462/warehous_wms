from tkinter import *
from tkinter import ttk
import sys
from pathlib import Path
from tkinter import messagebox
from tkcalendar import DateEntry


from data_bol import Bol

window = Tk()
window.geometry("1920x1080")
window.title("wms")

#所有bol 保存到同一个list
myBol_list = []

#创建新提单号，柜号，eta， ----新增
def new_window():

    #新增---创建新窗口
    window = Tk()
    window.geometry("600x1000")
    window.title('新增')

    #新增--每个bol代表每条货柜
    myBol = Bol()

    #输入框-货柜客户
    customer_show_label = Label(window, text="输入 客户：",font=("Ink Free", 20))
    customer_show_label.pack()
    cmb_customer = ttk.Combobox(window)
    cmb_customer.pack()
    cmb_customer['value'] = ('委达','整柜','彦达','彦整','泛美','泛整','空运','恒达','飞扬')
    #myBol.setCustomer(cmb_customer.get())

    #输入框-BOL
    bol_show_label = Label(window, text="输入 提单号：",font=("Ink Free", 20))
    bol_show_label.pack()
    text_bol = Text(window, bg = "light yellow", font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    text_bol.pack()
    # myBol.setmbl(text_bol)

    #输入框-柜号
    container_show_label = Label(window, text="输入 柜号：",font=("Ink Free", 20))
    container_show_label.pack()
    text_container = Text(window, bg = "light yellow", font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    text_container.pack()
    # myBol.setContainer(text_container)

    #输入框-ETA 
    '''
    # eta_show_label = Label(window, text="输入 ETA:",font=("Ink Free", 20))
    # eta_show_label.pack()
    # text_eta = Text(window, bg = "light yellow", font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    # text_eta.pack()
    # myBol.setEta(text_eta)'''
    eta_show_label = Label(window, text="输入 ETA:",font=("Arial", 20))
    eta_show_label.pack()
    date_eta = DateEntry(window, bg="light yellow", fg="purple", font=("Arial", 25))
    date_eta.pack()
    # myBol.setEta(date_eta.get())

    #输入框-卡车公司
    truck_show_label = Label(window, text="输入 卡车公司：",font=("Ink Free", 20))
    truck_show_label.pack()
    # text_truck = Text(window, bg = "light yellow", font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    # text_truck.pack()
    cmb_truck = ttk.Combobox(window)
    cmb_truck.pack()
    cmb_truck['value'] = ('FAE', 'Ocean epic', 'DHC')

    # myBol.setTruck(text_truck)

    #输入框-备注
    note_show_label = Label(window, text="输入 备注：",font=("Ink Free", 20))
    note_show_label.pack()
    text_note = Text(window, bg = "light yellow", font=("Ink Free", 15), height= 4, width=35, fg = "purple")
    text_note.pack()
    # myBol.setNote(text_note)

    #输入框-amazon 数量
    amanum_show_label = Label(window, text="输入  Amazon数量：",font=("Ink Free", 20))
    amanum_show_label.pack()
    text_amanum = Text(window, bg = "light yellow", font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    text_amanum.pack()
    # myBol.setAma_num(text_amanum)

    #输入框-ups 数量
    upsnum_show_label = Label(window, text="输入 UPS数量：",font=("Ink Free", 20))
    upsnum_show_label.pack()
    text_upsnum = Text(window, bg = "light yellow", font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    text_upsnum.pack()
    # myBol.setUps_num(text_upsnum)

    #输入框-other 数量
    othnum_show_label = Label(window, text="输入 其他数量：",font=("Ink Free", 20))
    othnum_show_label.pack()
    text_othnum = Text(window, bg = "light yellow", font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    text_othnum.pack()
    # myBol.setOth_num(text_othnum)


    #创建save 按键将上述输入内容保存
    def save_close():
        myBol.setCustomer(cmb_customer.get())
        myBol.setmbl(text_bol.get())
        myBol.setContainer(text_container.get())
        myBol.setEta(date_eta.get())
        myBol.setTruck(cmb_truck.get())
        myBol.setNote(text_note.get())
        myBol.setAma_num(text_amanum.get())
        myBol.setUps_num(text_upsnum.get())
        myBol.setOth_num(text_othnum.get())
        myBol_list.append(myBol)
        window.destroy()

    save_button = Button(window, text="Save", command= save_close, font=("Ink Free", 20))
    save_button.pack()

    window.mainloop()


#对当前货柜单所有货物进行记录，汇总，动向统计，eg： ups 几箱几板； 亚马逊 编号，卡派记录-----编辑
def edit_window():
    print("edit window")
    window = Tk()
    window.geometry("600x600")
    window.title('编辑')

    # 文字label
    search_label = Label(window, text="输入 货柜号：",font=("Ink Free", 20))
    search_label.pack()

    # 输入框
    text_search = Text(window, bg = "light yellow", font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    text_search.pack()

    display_BOL()

    window.mainloop()

def display_BOL():
    if not myBol_list:
        messagebox.showerror("Error", "No BOLs to display")
        return

    # Create Treeview
    tree = ttk.Treeview(window, columns=("Customer", "ETA", "MBL", "Container", "Truck"))

    # Configure Treeview
    tree.heading('#0', text='ID')
    tree.heading('Customer', text='Customer')
    tree.heading('ETA', text='ETA')
    tree.heading('MBL', text='MBL')
    tree.heading('Container', text='Container')
    tree.heading('Truck', text='Truck')

    tree.column('#0', stretch=YES, minwidth=30, width=50)
    tree.column('Customer', stretch=YES, minwidth=50, width=100)
    tree.column('ETA', stretch=YES, minwidth=50, width=100)
    tree.column('MBL', stretch=YES, minwidth=50, width=100)
    tree.column('Container', stretch=YES, minwidth=50, width=100)
    tree.column('Truck', stretch=YES, minwidth=50, width=100)

    # Insert data into Treeview
    for index, eah in enumerate(myBol_list):
        tree.insert("", index, text=str(index + 1), values=(eah.Customer, eah.ETA, eah.MBL, eah.Container, eah.Truck))

    tree.pack(expand=YES, fill=BOTH)


#显示所有货柜记录 -----查看
def view_window():

    for eah in myBol_list:
        eah.printInfo()

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