from tkinter import *
from tkinter import ttk
import sys
from pathlib import Path
from tkinter import messagebox
from tkcalendar import DateEntry

from data_bol import Bol
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime    # Import datetime
import mongoDB as mdb
#import mysql.connector

window = Tk()
window.geometry("1560x1080")
window.title("wms")

#所有bol 保存到同一个list
myBol_list = []

#创建新提单号，柜号，eta， ----新增
def new_window():

    # 连接到mongoDB, wms为
    client = mdb.get_client()
    db = client['wms']
    bol_collection = db['bol']

    #新增---创建新窗口
    window = Tk()
    window.geometry("600x800")
    window.title('新增')

    #新增--每个bol代表每条货柜
    myBol = Bol()

    #输入框-货柜客户
    customer_show_label = Label(window, text="输入 客户：",font=("Ink Free", 20))
    customer_show_label.pack()
    cmb_customer = ttk.Combobox(window)
    cmb_customer.pack()
    cmb_customer['value'] = ('委达','委整','彦达','彦整','ZTT','九猫','猫整','空运','恒达','飞扬')


    #输入框-BOL
    bol_show_label = Label(window, text="输入 提单号：",font=("Ink Free", 20))
    bol_show_label.pack()
    text_bol = Text(window, bg = "light yellow", font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    text_bol.pack()


    #输入框-柜号
    container_show_label = Label(window, text="输入 柜号：",font=("Ink Free", 20))
    container_show_label.pack()
    text_container = Text(window, bg = "light yellow", font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    text_container.pack()


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


    #输入框-卡车公司
    truck_show_label = Label(window, text="输入 卡车公司：",font=("Ink Free", 20))
    truck_show_label.pack()
    # text_truck = Text(window, bg = "light yellow", font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    # text_truck.pack()
    cmb_truck = ttk.Combobox(window)
    cmb_truck.pack()
    cmb_truck['value'] = ('FAE', 'Ocean epic', 'DHC', 'Hung Source Inc')


    #输入框-备注
    note_show_label = Label(window, text="输入 备注：",font=("Ink Free", 20))
    note_show_label.pack()
    text_note = Text(window, bg = "light yellow", font=("Ink Free", 15), height= 4, width=35, fg = "purple")
    text_note.pack()


    #输入框-amazon 数量
    amanum_show_label = Label(window, text="输入  Amazon数量: ",font=("Ink Free", 20))
    amanum_show_label.pack()
    text_amanum = Text(window, bg = "light yellow", font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    text_amanum.pack()

    #输入框-ups 数量
    upsnum_show_label = Label(window, text="输入 UPS数量: ",font=("Ink Free", 20))
    upsnum_show_label.pack()
    text_upsnum = Text(window, bg = "light yellow", font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    text_upsnum.pack()


    #输入框-other 数量
    othnum_show_label = Label(window, text="输入 其他数量：",font=("Ink Free", 20))
    othnum_show_label.pack()
    text_othnum = Text(window, bg = "light yellow", font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    text_othnum.pack()


    #创建save 按键将上述输入内容保存
    def save_close():
        myBol.setCustomer(cmb_customer.get())
        myBol.setMbl(text_bol.get("1.0", END).strip())
        myBol.setContainer(text_container.get("1.0", END).strip())
        myBol.setEta(date_eta.get())
        myBol.setTruck(cmb_truck.get())
        myBol.setNote(text_note.get("1.0", END).strip())
        myBol.setAma_num(int(text_amanum.get("1.0", END).strip()))
        myBol.setUps_num(int(text_upsnum.get("1.0", END).strip()))
        myBol.setOth_num(int(text_othnum.get("1.0", END).strip()))
        myBol_list.append(myBol)

        # add to database at mongoDB 
        mdb.insert_bol(myBol)
        window.destroy()


    save_button = Button(window, text="Save", command= save_close, font=("Ink Free", 20))
    save_button.pack()

    window.mainloop()



#对当前货柜单所有货物进行记录，汇总，动向统计，eg： ups 几箱几板； 亚马逊 编号，卡派记录-----编辑
def edit_window():
    print("edit window")
    window = Tk()
    window.geometry("600x800")
    window.title('编辑')

    # Container label
    search_label = Label(window, text="输入 Container: ",font=("Ink Free", 20))
    search_label.pack()

    # Container 输入框
    text_search = Text(window, bg = "light yellow", font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    text_search.pack()

    # Bol label
    search_label = Label(window, text="输入 BOL: ",font=("Ink Free", 20))
    search_label.pack()

    # Bol 输入框
    text_search = Text(window, bg = "light yellow", font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    text_search.pack()

    window.mainloop()

# def display_BOL():
#     if not myBol_list:
#         messagebox.showerror("Error", "No BOLs to display")
#         return

#     # Create Treeview
#     tree = ttk.Treeview(window, columns=("Customer", "ETA", "MBL", "Container", "Truck"))

#     # Configure Treeview
#     tree.heading('#0', text='ID')
#     tree.heading('Customer', text='Customer')
#     tree.heading('ETA', text='ETA')
#     tree.heading('MBL', text='MBL')
#     tree.heading('Container', text='Container')
#     tree.heading('Truck', text='Truck')

#     tree.column('#0', stretch=YES, minwidth=30, width=50)
#     tree.column('Customer', stretch=YES, minwidth=50, width=100)
#     tree.column('ETA', stretch=YES, minwidth=50, width=100)
#     tree.column('MBL', stretch=YES, minwidth=50, width=100)
#     tree.column('Container', stretch=YES, minwidth=50, width=100)
#     tree.column('Truck', stretch=YES, minwidth=50, width=100)

#     # Insert data into Treeview
#     for index, eah in enumerate(myBol_list):
#         tree.insert("", index, text=str(index + 1), values=(eah.Customer, eah.ETA, eah.MBL, eah.Container, eah.Truck))

#     tree.pack(expand=YES, fill=BOTH)


#预览：显示所有货柜记录 -----查看pre_table, 客户，MBL，柜，期，，备注，亚，UPS，其他
def pre_view_window():

    pre_view_windo = Tk()
    pre_view_windo.title("Pre-Table View")
    # Create Treeview
    tree = ttk.Treeview(pre_view_windo, columns=("Bol", "Container", "ETA", "Note", "Truck", "Customer"), show='headings')

    # Configure Treeview
    #tree.heading('#0', text='ID')
    
    tree.heading('Bol', text='MBL')
    tree.heading('Container', text='Container')
    tree.heading('ETA', text='ETA')
    tree.heading('Note', text='Note')
    tree.heading('Truck', text='Truck')
    tree.heading('Customer', text='Customer')

    #tree.column('#0', stretch=YES, minwidth=30, width=50)
    tree.column('Bol', stretch=YES, minwidth=50, width=100)
    tree.column('Container', stretch=YES, minwidth=50, width=100)
    tree.column('ETA', stretch=YES, minwidth=50, width=100)
    tree.column('Note', stretch=YES, minwidth=50, width=100)
    tree.column('Truck', stretch=YES, minwidth=50, width=100)
    tree.column('Customer', stretch=YES, minwidth=50, width=100)



    # Insert data into Treeview, 显示 myBol_list 中所有货柜记录的信息，包括客户，MBL，柜，备注，每个item明细，数量，几板
    # for index, eah in enumerate(myBol_list):
    #     total_num = eah.Ama_num + eah.Ups_num + eah.Oth_num
    #     tree.insert("", index, text=str(index + 1), values=(eah.Customer, eah.MBL, eah.Container, eah.Note, eah.ETA, eah.Truck, eah.Ama_num, eah.Ups_num, eah.Oth_num, total_num))

    bol_data = mdb.get_all_bols_by_eta()

    # Insert data into Treeview, 显示mongoDB 中所有货柜记录的信息，包括客户，MBL，柜，备注，每个item明细，数量，几�
    for bol in bol_data:
        #total_num = bol['Ama_num'] + bol['Ups_num'] + bol['Oth_num']
        tree.insert("", END, text=str(bol['_id']), values=(bol.get('Customer', ''), bol.get('MBL', ''), bol.get('Container',''), bol.get('Note',''), bol.get('ETA',''), bol.get('Truck',''), bol.get('Ama_num',''), bol.get('Ups_num',''), bol.get('Oth_num',""), bol.get('total_num','')))
    
    tree.pack(expand=YES, fill=BOTH)
    pre_view_windo.mainloop()
    print("view window")


# 详细：显示所有货柜记录 -----查看pos_table, 客户，MBL，柜，备注，每个item明细，数量，几板
# 需要经过edit window才能查看!!
def pos_view_window():

    pre_view_windo = Tk()
    pre_view_windo.title("Post-Table View")
    print("post view")

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



#对应 pre_view_window 按键-查看
view_button = Button(window, text="PRE VIEW",
                    width=50,
                    height=6,
                    command=pre_view_window)
view_button.place(x=100, y=400)

#对应 pos_view_window 按键-查看
view_button = Button(window, text="POST VIEW",
                    width=50,
                    height=6,
                    command=pos_view_window)
view_button.place(x=700, y=400)

window.mainloop()