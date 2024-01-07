from tkinter import *
from tkinter import ttk
import sys
from pathlib import Path
from tkinter import messagebox
from tkcalendar import DateEntry

from data_bol import Bol
from data_bol import Item
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime    # Import datetime
import mongoDB as mdb
#import mysql.connector

window = Tk()
window.geometry("1200x900")
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
    cmb_customer['value'] = ('委达','委整','彦达','彦整','ZTT',
                             '九猫','猫整','空运','恒达','飞扬')


    #输入框-BOL
    bol_show_label = Label(window, text="输入 提单号：",font=("Ink Free", 20))
    bol_show_label.pack()
    text_bol = Text(window, bg = "light yellow", 
                    font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    text_bol.pack()


    #输入框-柜号
    container_show_label = Label(window, text="输入 柜号：",font=("Ink Free", 20))
    container_show_label.pack()
    text_container = Text(window, bg = "light yellow", 
                          font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    text_container.pack()


    #输入框-ETA 
    eta_show_label = Label(window, text="输入 ETA:",font=("Arial", 20))
    eta_show_label.pack()
    date_eta = DateEntry(window, bg="light yellow", fg="purple", font=("Arial", 25))
    date_eta.pack()


    #输入框-卡车公司
    truck_show_label = Label(window, text="输入 卡车公司：",font=("Ink Free", 20))
    truck_show_label.pack()

    cmb_truck = ttk.Combobox(window)
    cmb_truck.pack()
    cmb_truck['value'] = ('FAE', 'Ocean epic', 'DHC', 'Hung Source Inc')


    #输入框-备注
    note_show_label = Label(window, text="输入 备注：",font=("Ink Free", 20))
    note_show_label.pack()
    text_note = Text(window, bg = "light yellow", 
                     font=("Ink Free", 15), height= 4, width=35, fg = "purple")
    text_note.pack()


    #输入框-amazon 数量
    amanum_show_label = Label(window, text="输入  Amazon数量: ",font=("Ink Free", 20))
    amanum_show_label.pack()
    text_amanum = Text(window, bg = "light yellow", 
                       font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    text_amanum.pack()

    #输入框-ups 数量
    upsnum_show_label = Label(window, text="输入 UPS数量: ",font=("Ink Free", 20))
    upsnum_show_label.pack()
    text_upsnum = Text(window, bg = "light yellow", 
                       font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    text_upsnum.pack()


    #输入框-other 数量
    othnum_show_label = Label(window, text="输入 其他数量：",font=("Ink Free", 20))
    othnum_show_label.pack()
    text_othnum = Text(window, bg = "light yellow", 
                       font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    text_othnum.pack()


    #创建save 按键将上述输入内容保存
    def save_close():
        myBol.setCustomer(cmb_customer.get())
        myBol.setMbl(text_bol.get("1.0", END).strip().upper())
        myBol.setContainer(text_container.get("1.0", END).strip().upper())
        myBol.setEta(date_eta.get())
        myBol.setTruck(cmb_truck.get())
        myBol.setNote(text_note.get("1.0", END).strip())
        myBol.setAma_num(safe_int(text_amanum.get("1.0", END).strip()))
        myBol.setUps_num(safe_int(text_upsnum.get("1.0", END).strip()))
        myBol.setOth_num(safe_int(text_othnum.get("1.0", END).strip()))
        
        myBol_list.append(myBol)

        # add to database at mongoDB 
        mdb.insert_bol(myBol)

        print(type(date_eta.get()))
        window.destroy()


    save_button = Button(window, text="Save", command= save_close, font=("Ink Free", 20))
    save_button.pack()

    window.mainloop()


# Helper function to safely convert text to int, defaulting to 0
# 如果ama, ups, other 为空，则默认为0
def safe_int(text):
    try:
        return int(text) if text else 0
    except ValueError:
        return 0
    

#对当前货柜单所有货物进行记录，汇总，动向统计，eg： ups 几箱几板； 亚马逊 编号，卡派记录-----编辑
def search_window():
    
    window = Tk()
    window.geometry("600x600")
    window.title('搜索')

    # Container label
    search_label = Label(window, text="输入 Container: ",font=("Ink Free", 20))
    search_label.pack()

    # Container 输入框
    container_search = Text(window, bg = "light yellow", 
                            font=("Ink Free", 25), height= 1, width=15, fg = "purple")
    container_search.pack()

    # Bol label
    search_label = Label(window, text="输入 BOL: ", font=("Ink Free", 20))
    search_label.pack()

    # Bol 输入框
    bol_search = Text(window, bg = "light yellow", 
                      font=("Ink Free", 25), height= 1, width=20, fg = "purple")
    bol_search.pack()

    def search_button():
        bol = bol_search.get("1.0", END).strip().upper()
        container = container_search.get("1.0", END).strip().upper()

        #搜索 bol和柜号
        #found = mdb.search_bol_container(bol, container)  

        #测试用，仅搜bol
        found = mdb.search_bol(bol)

        if found:
            #messagebox.showinfo("Success", "BOL found")
            edit_add_window(bol, container)
        else:
            messagebox.showerror("Error", "BOL or Container incorrect!")

    Button(window, text="Search", command=search_button, font=("Ink Free", 20)).pack()
    window.mainloop()


# after search success, add or edit info in new window
def edit_add_window(bol, container):
    window = Tk()
    window.geometry("1200x600")
    window.title('编辑')

    # Create a frame to hold the buttons
    button_frame = Frame(window)
    button_frame.pack(anchor='n', pady=20)

    # 设置两按键，分别对搜索的bol document进行编辑和添加info
    Button(button_frame, text="Add new", command=lambda: add_new_info(bol, container),
           font=("Ink Free", 20)).grid(row=0, column=0, padx=10, pady=10)
    Button(button_frame, text="Edit exist", command=lambda: edit_exist_info(bol, container),
           font=("Ink Free", 20)).grid(row=0, column=1, padx=10, pady=10)

    # Create Treeview显示title
    tree = ttk.Treeview(window, columns=("Customer", "Bol", "Container", 
                                         "ETA", "Truck", "Note"), show='headings')
    tree.heading('Customer', text='Customer')
    tree.heading('Bol', text='MBL')
    tree.heading('Container', text='Container')
    tree.heading('ETA', text='ETA')
    tree.heading('Note', text='Note')
    tree.heading('Truck', text='Truck')
    

    #tree.column('#0', stretch=YES, minwidth=30, width=50)
    tree.column('Customer', stretch=YES, minwidth=50, width=100)
    tree.column('Bol', stretch=YES, minwidth=50, width=100)
    tree.column('Container', stretch=YES, minwidth=50, width=100)
    tree.column('ETA', stretch=YES, minwidth=50, width=100)
    tree.column('Note', stretch=YES, minwidth=50, width=100)
    tree.column('Truck', stretch=YES, minwidth=50, width=100)

    #获取document 内容
    bol_data = mdb.get_bol(bol)
    print(bol_data)

    #显示内容
    if bol_data:
        tree.insert("", END, values=(
            bol_data.get('Customer', ''), 
            bol_data.get('Bol', ''), 
            bol_data.get('Container', ''), 
            bol_data.get('ETA', ''), 
            bol_data.get('Truck', ''), 
            bol_data.get('Note', '')))
        
        # Check if there are items and insert them as children of the main document
        if 'Items' in bol_data and isinstance(bol_data['Items'], list):
            for item in bol_data['Items']:
                tree.insert("", END, values=(
                    'Item: ' + item.get('name', ''),
                    'Count: ' + str(item.get('count', 0)),
                    'Pallet: ' + str(item.get('pallet', 0)),
                    # Add other item details as needed
                ))

    tree.pack(expand=YES, fill=BOTH)

    window.mainloop()

#添加新info到ocument，eg： ups 几箱几板； 亚马逊 编号，卡派记录-----添加
def add_new_info(bol, container):
    window = Toplevel()
    window.geometry("600x800")
    window.title('添加信息')
  
    #find the input bol from mongodb
    document_data = mdb.get_bol(bol)
    
    #显示添加的container信息
    if document_data:
        Label(window, text=f"Customer: {document_data.get('Customer', 'N/A')}",
              font=("Ink Free", 20)).grid(row=0, column=0, sticky=W)
        Label(window, text=f"Bol: {document_data.get('Bol', 'N/A')}",
              font=("Ink Free", 20)).grid(row=1, column=0, sticky=W)
        Label(window, text=f"Container: {document_data.get('Container', 'N/A')}",
              font=("Ink Free", 20)).grid(row=2, column=0, sticky=W)
        Label(window, text=f"ETA: {document_data.get('ETA', 'N/A')}",
              font=("Ink Free", 20)).grid(row=3, column=0, sticky=W)
    
    #添加item到该container
    Label(window, text="Name", font=("Ink Free", 20)).grid(row=4, column=0, sticky=W)
    item_name = Text(window, bg = "light yellow", 
                    font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    item_name.grid(row=4, column=1, sticky=W)
    
    Label(window, text="Count", font=("Ink Free", 20)).grid(row=5, column=0, sticky=W)
    item_count = Text(window, bg = "light yellow", 
                    font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    item_count.grid(row=5, column=1, sticky=W)

    Label(window, text="Pallet", font=("Ink Free", 20)).grid(row=6, column=0, sticky=W)
    item_pallet = Text(window, bg = "light yellow", 
                    font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    item_pallet.grid(row=6, column=1, sticky=W)

    Label(window, text="Note", font=("Ink Free", 20)).grid(row=7, column=0, sticky=W)
    item_note = Text(window, bg = "light yellow", 
                    font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    item_note.grid(row=7, column=1, sticky=W)

    Label(window, text="Price", font=("Ink Free", 20)).grid(row=8, column=0, sticky=W)
    item_price = Text(window, bg = "light yellow", 
                    font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    item_price.grid(row=8, column=1, sticky=W)

    Label(window, text="Cost", font=("Ink Free", 20)).grid(row=9, column=0, sticky=W)
    item_cost = Text(window, bg = "light yellow", 
                    font=("Ink Free", 25), height= 1, width=10, fg = "purple")
    item_cost.grid(row=9, column=1, sticky=W)

    Label(window, text="Status", font=("Ink Free", 20)).grid(row=10, column=0, sticky=W)
    item_status = ttk.Combobox(window, values=["暂扣", "自提","已派送","改UPS", "改Ama", "客户下单"],)
    item_status.grid(row=10, column=1, sticky=W)


    item = Item()

    def save_add():
        item.setName(item_name.get("1.0", "end-1c"))
        item.setCount(item_count.get("1.0", "end-1c"))
        item.setPallet(item_pallet.get("1.0", "end-1c"))
        item.setNote(item_note.get("1.0", "end-1c"))
        item.setSale(item_price.get("1.0", "end-1c"))
        item.setCost(item_cost.get("1.0", "end-1c"))
        item.setStatus(item_status.get())
        item_dict = item.to_dict()
        mdb.insert_item_to_bol(bol, item_dict)
        window.destroy()
        
    save_add_btn = Button(window, text="Save", command= save_add, font=("Ink Free", 20))
    save_add_btn.grid(row=11, column=0, columnspan=2, pady=10)


    window.mainloop()
    print("add new")

#编辑现有document
def edit_exist_info(bol, container):
    window = Toplevel()
    window.geometry("600x600")
    window.title('编辑现有')

    window.mainloop()
    print("edit exist")

#显示所有货柜记录 -----客户，MBL，柜，期，，备注，亚，UPS，其他
def display_BOL(window):

    # Create Treeview
    tree = ttk.Treeview(window, columns=("Customer", "Bol", "Container", 
                                         "ETA", "Truck", "Note"), show='headings')

    # Configure Treeview
    #tree.heading('#0', text='ID')
    tree.heading('Customer', text='Customer')
    tree.heading('Bol', text='MBL')
    tree.heading('Container', text='Container')
    tree.heading('ETA', text='ETA')
    tree.heading('Note', text='Note')
    tree.heading('Truck', text='Truck')
    

    #tree.column('#0', stretch=YES, minwidth=30, width=50)
    tree.column('Customer', stretch=YES, minwidth=50, width=100)
    tree.column('Bol', stretch=YES, minwidth=50, width=100)
    tree.column('Container', stretch=YES, minwidth=50, width=100)
    tree.column('ETA', stretch=YES, minwidth=50, width=100)
    tree.column('Note', stretch=YES, minwidth=50, width=100)
    tree.column('Truck', stretch=YES, minwidth=50, width=100)
    
    tree.pack(expand=YES, fill=BOTH)


#预览：显示所有货柜记录 -----查看pre_table, 客户，MBL，柜，期，，备注，亚，UPS，其他
def pre_view_window():

    pre_view_windo = Tk()
    pre_view_windo.title("Pre-Table View")
    pre_view_windo.geometry("1000x600")


    # Customize the Treeview Style
    style = ttk.Style()
    style.configure("Treeview", background="white", fieldbackground="white")

    # Create Treeview
    tree = ttk.Treeview(pre_view_windo, columns=("Customer", "Bol", "Container", 
                                                 "ETA", "Truck", "Note"), show='headings')

    # Configure Treeview columns
    tree.heading('Customer', text='Customer')
    tree.heading('Bol', text='MBL')
    tree.heading('Container', text='Container')
    tree.heading('ETA', text='ETA')
    tree.heading('Note', text='Note')
    tree.heading('Truck', text='Truck')

    tree.column('Customer', stretch=YES, minwidth=50, width=100)
    tree.column('Bol', stretch=YES, minwidth=50, width=100)
    tree.column('Container', stretch=YES, minwidth=50, width=100)
    tree.column('ETA', stretch=YES, minwidth=50, width=100)
    tree.column('Note', stretch=YES, minwidth=50, width=100)
    tree.column('Truck', stretch=YES, minwidth=50, width=100)

    # Insert data into Treeview
    bol_data = mdb.get_all_bols_by_eta()
    for bol in bol_data:
        tree.insert("", END, values=(
            bol.get('Customer', ''), 
            bol.get('Bol', ''), 
            bol.get('Container', ''), 
            bol.get('ETA', ''), 
            bol.get('Truck', ''), 
            bol.get('Note', '')))

    # Add a scrollbar
    scrollbar = ttk.Scrollbar(pre_view_windo, orient="vertical", command=tree.yview)
    scrollbar.pack(side='right', fill='y')
    tree.configure(yscrollcommand=scrollbar.set)

    tree.pack(expand=YES, fill=BOTH)
    pre_view_windo.mainloop()


# 详细：显示所有货柜记录 -----查看pos_table, 客户，MBL，柜，备注，每个item明细，数量，几板
def pos_view_window():

    pos_view_window = Tk()
    pos_view_window.title("Post-Table View")
    pos_view_window.geometry("1000x600")

    # Customize the Treeview Style
    style = ttk.Style()
    style.configure("Treeview", background="white", fieldbackground="white")

    # Create Treeview
    tree = ttk.Treeview(pos_view_window, columns=("Customer", "Bol", "Container", 
                                                 "ItemName", "ItemPallet" ), show='headings')

    # Configure Treeview columns
    tree.heading('Customer', text='Customer')
    tree.heading('Bol', text='MBL')
    tree.heading('Container', text='Container')
    tree.heading('ItemName', text='Item Name')
    tree.heading('ItemPallet', text='Item Pallet')


    tree.column('Customer', stretch=YES, minwidth=50, width=100)
    tree.column('Bol', stretch=YES, minwidth=50, width=100)
    tree.column('Container', stretch=YES, minwidth=50, width=100)
    tree.column('ItemName', stretch=YES, minwidth=50, width=100)
    tree.column('ItemPallet', stretch=YES, minwidth=50, width=100)

    

    #get all data from MongoDB
    bol_data = mdb.get_all_bols()
    
    # Insert data into Treeview
    for bol in bol_data:
        bol_id = tree.insert("", 'end', values=(str(bol.get('Customer', '')), 
                                                str(bol.get('Bol', '')), 
                                                str(bol.get('Container', '')), 
                                                "", ""))
        for item in bol.get('Items', []):
            tree.insert(bol_id, 'end', values=("", "", "", 
                                               str(item.get('ItemName', '')), 
                                               str(item.get('ItemPallet', ''))))
        tree.item(bol_id, open=True)  # Expand the parent row

    # Add a scrollbar
    scrollbar = ttk.Scrollbar(pos_view_window, orient="vertical", command=tree.yview)
    scrollbar.pack(side='right', fill='y')
    tree.configure(yscrollcommand=scrollbar.set)

    tree.pack(expand=YES, fill=BOTH)
    pos_view_window.mainloop()
    

#对应 new_window 按键-新增
new_button = Button(window, text="NEW",
                    width=50,
                    height=6,
                    command=new_window)
new_button.place(x=100, y=100)

#对应 search_window 按键-编辑
edit_button = Button(window, text="EDIT",
                    width=50,
                    height=6,
                    command=search_window)
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