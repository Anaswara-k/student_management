from functools import partial
from tkinter import *
from tkinter import messagebox
import pymysql
import custom as cs
import credentials as cr




class Management:
    def __init__(self, root):
        self.window = root
        self.window.title("Student Management System")
        self.window.geometry("780x480")
        self.window.config(bg = "white")

        # Customization
        self.color_1 = cs.color_1
        self.color_2 = cs.color_2
        self.color_3 = cs.color_3
        self.color_4 = cs.color_4
        self.font_1 = cs.font_1
        self.font_2 = cs.font_2

        # User Credentials
        self.host = cr.host
        self.user = cr.user
        self.password = cr.password
        self.database = cr.database

        # Left Frame
        self.frame_1 = Frame(self.window, bg=self.color_1)
        self.frame_1.place(x=0, y=0, width=540, relheight = 1)

        # Right Frame
        self.frame_2 = Frame(self.window, bg = self.color_2)
        self.frame_2.place(x=540,y=0,relwidth=1, relheight=1)

        # Buttons
        self.add_bt = Button(self.frame_2, text='Add New', font=(self.font_1, 12), bd=2, command=self.AddStudent, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=40,width=100)
        self.view_bt = Button(self.frame_2, text='View Details', font=(self.font_1, 12), bd=2, command=self.GetName_View, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=100,width=100)
        self.update_bt = Button(self.frame_2, text='Update', font=(self.font_1, 12), bd=2, command=self.GetName_Update, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=160,width=100)
        self.delete_bt = Button(self.frame_2, text='Delete', font=(self.font_1, 12), bd=2, command=self.GetName_Delete,cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=220,width=100)
        self.clear_bt = Button(self.frame_2, text='Clear', font=(self.font_1, 12), bd=2, command=self.ClearScreen, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=280,width=100)
        self.exit_bt = Button(self.frame_2, text='Exit', font=(self.font_1, 12), bd=2, command=self.Exit, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=340,width=100)



    def AddStudent(self):
        self.ClearScreen()

        self.name = Label(self.frame_1, text="Student Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=30)
        self.name_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.name_entry.place(x=40, y=60, width=200)

        self.clas = Label(self.frame_1, text="Class", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300, y=30)
        self.class_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.class_entry.place(x=300, y=60, width=200)

        self.roll_num = Label(self.frame_1, text="Roll Number", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=100)

        self.roll_num_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.roll_num_entry.place(x=40, y=130, width=200)

        self.guardian_name = Label(self.frame_1, text="Guardian Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=100)

        self.guardian_name_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.guardian_name_entry.place(x=300, y=130, width=200)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(self.font_1, 12), bd=2, command=self.Submit, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=200,y=389,width=100)




    def GetName_View(self):
        self.ClearScreen()

        self.getInfo = Label(self.frame_1, text="Enter Student Name", font=(self.font_2, 18, "bold"),bg=self.color_1).place(x=140, y=70)

        self.getInfo_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_1, text='Submit', font=(self.font_1, 10), bd=2,command=self.CheckName_View, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=220, y=150, width=80)



    def GetName_Update(self):
        self.ClearScreen()

        self.getInfo = Label(self.frame_1, text="Enter Student Name", font=(self.font_2, 18, "bold"),bg=self.color_1).place(x=140, y=70)

        self.getInfo_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_1, text='Submit', font=(self.font_1, 10), bd=2,command=self.CheckName_Update, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=220, y=150, width=80)



    def GetName_Delete(self):
        self.ClearScreen()

        self.getInfo = Label(self.frame_1, text="Enter Student Name", font=(self.font_2, 18, "bold"),bg=self.color_1).place(x=140, y=70)

        self.getInfo_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_1, text='Submit', font=(self.font_1, 10), bd=2, command=self.DeleteData,cursor="hand2", bg=self.color_2, fg=self.color_3).place(x=220, y=150, width=80)



    def ClearScreen(self):
        for widget in self.frame_1.winfo_children():
            widget.destroy()



    def Exit(self):
        self.window.destroy()

    def CheckName_View(self):
        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter student name", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password,database=self.database)

                curs = connection.cursor()
                curs.execute("select * from student_register where name=%s", self.getInfo_entry.get())
                row = curs.fetchone()

                if row == None:
                    messagebox.showerror("Error!", "student name doesn't exists", parent=self.window)
                else:
                    self.ShowDetails(row)
                    connection.close()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def CheckName_Update(self):
        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter student name", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password,database=self.database)

                curs = connection.cursor()
                curs.execute("select * from student_register where name=%s", self.getInfo_entry.get())
                row = curs.fetchone()

                if row == None:
                    messagebox.showerror("Error!", "student name doesn't exists", parent=self.window)
                else:
                    self.GetUpdateDetails(row)
                    connection.close()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def DeleteData(self):
        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter student name", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password,database=self.database)

                curs = connection.cursor()
                curs.execute("select * from student_register where name=%s", self.getInfo_entry.get())
                row = curs.fetchone()

                if row == None:
                    messagebox.showerror("Error!", "student name doesn't exists", parent=self.window)
                else:
                    curs.execute("delete from student_register where name=%s", self.getInfo_entry.get())
                    connection.commit()
                    messagebox.showinfo('Done!', "The data has been deleted")
                    connection.close()
                    self.ClearScreen()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)


    def GetUpdateDetails(self,row):
        self.ClearScreen()

        self.name = Label(self.frame_1, text="Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=30)
        self.name_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.name_entry.insert(0, row[0])
        self.name_entry.place(x=40,y=60, width=200)

        self.clas = Label(self.frame_1, text="Class", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=30)
        self.class_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.class_entry.insert(0, row[1])
        self.class_entry.place(x=300,y=60, width=200)

        self.roll_num = Label(self.frame_1, text="Roll Number", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=100)
        self.roll_num_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.roll_num_entry.insert(0, row[2])
        self.roll_num_entry.place(x=40,y=130, width=200)

        self.guardian_name = Label(self.frame_1, text="Guardian Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=100)
        self.guardian_name_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.guardian_name_entry.insert(0, row[3])
        self.guardian_name_entry.place(x=300,y=130, width=200)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(self.font_1, 12), bd=2,command=partial(self.UpdateDetails,row), cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=160, y=389, width=100)

        self.cancel_bt = Button(self.frame_1, text='Cancel', font=(self.font_1, 12), bd=2, command=self.ClearScreen,cursor="hand2", bg=self.color_2, fg=self.color_3).place(x=280, y=389, width=100)

    def ShowDetails(self, row):
        self.ClearScreen()
        name = Label(self.frame_1, text="Student Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40, y=30)
        name_data = Label(self.frame_1, text=row[0], font=(self.font_1, 10)).place(x=40, y=60)

        clas = Label(self.frame_1, text="Class", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=30)

        class_data = Label(self.frame_1, text=row[1], font=(self.font_1, 10)).place(x=300, y=60)

        roll_num = Label(self.frame_1, text="Roll Number", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40, y=100)
        roll_num_data = Label(self.frame_1, text=row[2], font=(self.font_1, 10)).place(x=40, y=130)

        guardian_name = Label(self.frame_1, text="Guardian Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=100)

        guardian_name_data = Label(self.frame_1, text=row[3], font=(self.font_1, 10)).place(x=300, y=130)

    def UpdateDetails(self,row):
        if self.name_entry.get() == "" or self.class_entry.get() == "" or self.roll_num_entry.get() == "" or self.guardian_name_entry.get() == "":
            messagebox.showerror("Error!", "Sorry!, All fields are required", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)

                curs = connection.cursor()
                curs.execute("select * from student_register where name=%s", row[0])
                row = curs.fetchone()

                if row==None:
                    messagebox.showerror("Error!", "The student name doesn't exists----", parent=self.window)
                else:
                    curs.execute(
                        "update student_register set class=%s,roll_num=%s,guardian_name=%s where name=%s",
                        (

                            self.class_entry.get(),
                            self.roll_num_entry.get(),
                            self.guardian_name_entry.get(),
                            row[0]
                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Done!',"The data has been updated")
                    self.ClearScreen()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)


    def Submit(self):
        if self.name_entry.get() == "" or self.name_entry.get() == "" or self.class_entry.get() == "" or self.roll_num_entry.get() == "" or self.guardian_name_entry.get() == "":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from student_register where name=%s", self.name_entry.get())
                row=curs.fetchone()

                if row!=None:
                    messagebox.showerror("Error!","The student name is already exists, please try again with another name",parent=self.window)
                else:
                    curs.execute("insert into student_register (name,class,roll_num,guardian_name) values(%s,%s,%s,%s)",
                                        (
                                            self.name_entry.get(),
                                            self.class_entry.get(),
                                            self.roll_num_entry.get(),
                                            self.guardian_name_entry.get(),

                                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Done!', "The data has been submitted")
                    self.reset_fields()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    def reset_fields(self):
        self.name_entry.delete(0, END)
        self.class_entry.delete(0, END)
        self.roll_num_entry.delete(0, END)
        self.guardian_name_entry.delete(0, END)


if __name__ == "__main__":
    root = Tk()
    obj = Management(root)
    root.mainloop()