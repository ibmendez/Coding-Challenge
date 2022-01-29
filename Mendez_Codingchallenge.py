from tkinter import *
from tkinter import ttk


info_dict = {}

class UserInfo():

    id_number = 0
         
    def add_entry():
        # 'data' variable puts user info (name, age, gender) into a dictionary
        # data is assigned an ID inserted into another dictionary, with the ID as the key
        # ID starts from 0 and increments by 1 for every user created
        get_name = name_entry.get()
        get_age = age_entry.get()
        get_gender = age_entry.get()
        
       
        if get_name.strip() == '' or get_age.strip() == '' or get_gender.strip() == '':

            add_label_message.set('ENTRY MUST NOT BE EMPTY')
            add_message.grid(row= '4',column= '0',columnspan= '2')
        else:

            add_label_message.set('SUCCESS')
            add_message.grid(row= '4',column= '1')

            user_data = {'name':get_name, 'age' : get_age, 'gender' : get_gender}  
            info_dict[UserInfo.id_number] = user_data

            # Adds new entry to table

            table.insert(parent='', iid = UserInfo.id_number,index= 'end',values=(UserInfo.id_number, get_name, get_age, get_gender))

            UserInfo.id_number += 1
            
            
            
            name_entry.delete(0,END)
            age_entry.delete(0,END)
            gender_entry.delete(0,END)


        

        

    def delete_entry(user_id):
        # Deletes an object inside an array based on the object's ID
        
        try:
            user_id = int(user_id)
        
            if user_id not in info_dict.keys():
                delete_label_message.set('INVALID ID')
                delete_message.grid(row= '2',column= '1')
            
            else:

                delete_label_message.set('SUCCESS')

                table.delete(user_id)
                delete_message.grid(row= '2', column= '1')  
                info_dict.pop(user_id)
                
                id_entry.delete(0,END)
        except:    
            delete_label_message.set('ERROR')
            delete_message.grid(row= '2',column= '1')

  
## GUI

root = Tk()
root.geometry('800x800')
root.resizable(False,False)

 # Side frame
top_frame = Frame(root, bg= '#e3e6e4')
top_frame.place(rely=0.1, relx=0.5, anchor=CENTER)

## TABLE FEATURE
table_frame = Frame(root)
table_frame.place(relx= '0.5', rely= '0.5', anchor= CENTER)

    # scrollbar
table_scrollbar = Scrollbar(table_frame, orient= 'vertical')
table_scrollbar.grid(row= '1', column= '1', sticky = 'ns')

    #table
user_columns = ('id','name', 'age', 'gender')
table = ttk.Treeview(table_frame, columns= user_columns, show = 'headings', height = '20', yscrollcommand= table_scrollbar.set)
table.grid(row= '1', column = '0',padx = '20',pady= '20')

table_scrollbar.config(command= table.yview)

    # heading config
table.heading('id', text= 'ID')
table.heading('name', text= 'Name')
table.heading('age', text= 'Age')
table.heading('gender', text= 'Gender')

    # column config
table_columnwidth = '150'
table.column('id', anchor=CENTER, width= '80')
table.column('name', anchor=CENTER, width= table_columnwidth)
table.column('age', anchor=CENTER, width= table_columnwidth)
table.column('gender', anchor=CENTER, width= table_columnwidth)

   
## ADD ENTRY FEATURE
add_entry_frame = Frame(top_frame, bg='#e3e6e4',bd='5')
add_entry_frame.grid(row= '0',column = '0',padx= '20',pady= '20')

    # Name
name_label = Label(add_entry_frame, text='Name:',bg= '#e3e6e4')
name_entry = Entry(add_entry_frame,width='20',borderwidth = '2')

name_label.grid(row= '0',column = '0')
name_entry.grid(row= '0',column = '1')

    # Age
age_label = Label(add_entry_frame,text='Age:',bg= '#e3e6e4')
age_entry = Entry(add_entry_frame,width='20',borderwidth = '2' )

age_label.grid(row= '1',column = '0')
age_entry.grid(row= '1',column = '1')

    # Gender
gender_label = Label(add_entry_frame,text='Gender:',bg= '#e3e6e4')
gender_entry = Entry(add_entry_frame,width='20',borderwidth = '2')

gender_label.grid(row= '2',column = '0')
gender_entry.grid(row= '2',column = '1')


    # Add Entry Button
add_entry_button = Button(add_entry_frame,text='Add Entry',width='10',bg= '#2a49a3',fg= 'white', command = UserInfo.add_entry)
add_entry_button.grid(row='3',column = '1',pady = '10')

# Add Entry Message
add_label_message = StringVar()
add_message = Label(add_entry_frame, textvariable= add_label_message)

## DELETE ENTRY FEATURE
delete_entry_frame = Frame(top_frame,bg='#e3e6e4',bd='5')
delete_entry_frame.grid(row = '0', column = '1',padx= '20',pady= '20')

    # ID
id_label = Label(delete_entry_frame, text='ID:',bg= '#e3e6e4')
id_entry = Entry(delete_entry_frame,width='20',borderwidth = '2')

id_label.grid(row= '0',column = '0')
id_entry.grid(row= '0',column = '1')

    # Delete Entry Button
delete_entry_button = Button(delete_entry_frame,text='Delete Entry',width='10',bg= '#2a49a3',fg= 'white',command = lambda: UserInfo.delete_entry(id_entry.get()))
delete_entry_button.grid(row='1',column = '1',padx= '20',pady= '20')

    # Delete Entry Message
delete_label_message = StringVar(delete_entry_frame)
delete_message = Label(delete_entry_frame, textvariable= delete_label_message)

root.mainloop()
