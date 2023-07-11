#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector as sql_data
mydb = sql_data.connect(host = 'localhost',user = 'root',password = 'rajat123', database = 'school_management')
cur = mydb.cursor() 


# In[2]:


import random
from datetime import date
import pandas as pd
import sqlalchemy 
import pymysql


# In[3]:


try:
    engine=sqlalchemy.create_engine("mysql+pymysql://root:rajat123@localhost/school_management")
except:
    print("Something went wrong- cant use option 19")


# In[ ]:





# In[ ]:





# In[4]:



def randompassword():
    import random
    import string

    password_length = 8
    alpha_count = 4
    num_count = 2
    symbol_count = 2

    alpha = string.ascii_letters
    numb = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_elements = []

    for alphabet in range(0,alpha_count):
        temp1 = random.choice(alpha)
        password_elements.append(temp1)

    for num in range(0,num_count):
        temp2 = random.choice(numb)
        password_elements.append(temp2)

    for sym in range(0,symbol_count):
        temp3 =  random.choice(symbols)
        password_elements.append(temp3)

    random.shuffle(password_elements)

    final_password = ''
    for element in password_elements:
        final_password += element

    return final_password


# In[5]:


#sending Auto message to all registred student
def msg_to_all_stu(msg):
    cmd_gr_msg_100 = "Select s_roll from registration"
    cur.execute(cmd_gr_msg_100)
    all_id_of_group_msg = cur.fetchall()
    #print(all_id_of_group_msg)
    print("Sending message ...")
    
    try:
        for all_id_msg  in all_id_of_group_msg:

            cmd_gr_msg_20 = "Insert into message_table (sender_id,receiver_id,message) value ('1000','{}','{}')".format(all_id_msg[0],msg)
            cur.execute(cmd_gr_msg_20)
        mydb.commit()
        print("*** Message Successfully delivered")
    except:
        mydb.rollback()
        print("*** Error in delivering message")
 


# In[6]:


#gives all avaibleble department
def get_availabe_department():
    cat_sub_cmd_1 = "Select subject1,subject2,subject3,subject4,subject5,subject6 from catagory_selection"
    cur.execute(cat_sub_cmd_1)
    all_sub = cur.fetchall()
    department_available = []
    for _sub in all_sub:
        for subone in _sub:
            if(department_available.count(subone)==0 and subone != None):
                department_available.append(subone)

    return department_available


# In[7]:


#function to delete past student(class 12) message and user id -- part of admin declare end of acedemic year 
def deletemsg_paststudent_and_user_from_securitytable_transfer_to_past_student():
    ex89 = "select s_roll from registration where class = 12"
    cur.execute(ex89)
    past_student_id = cur.fetchall()
    for paststd in past_student_id:	
        ex90 = f"delete from message_table where sender_id = '{paststd[0]}' or receiver_id = '{paststd[0]}'"
        cur.execute(ex90)
        ex92 = f"delete from security_table where user_id = '{paststd[0]}'"
        cur.execute(ex92)
        
        
    ex87 = '''Insert into past_student(student_id,fname,lname,dob,gender,address,email,faculty,catagory,guardian_name,guardian_number)
    Select s_roll,fname,lname,dob,gender,address,email,faculty,catagory,guardian_name,guardian_number from registration where class = 12'''
    cur.execute(ex87)

    
    
    
    
    

    
    
#fuction to update class from 11 to 12 -- -- part of admin declare end of acedemic year 
def update_class_12():
    print("Updating class 11 to class 12...")
    cmd_upclass_1 = "update registration set class = 12 where class = 11"
    cur.execute(cmd_upclass_1)
    
    
    
    
    
#delete all content of form     -- part of admin declare end of acedemic year 
def delete_allcontent_from():
    print("Deleting content of form and entrance marks...")
    cmd_deleteform_1 = "Delete from entrance_marks"
    cur.execute(cmd_deleteform_1)
    cmd_deleteform_2 = "Delete from entrance_form"
    cur.execute(cmd_deleteform_2)
    
    print("Successfully Deleted...")


# In[8]:


#this function fill up technical table with technical data - part of admin declare acedemic season
def get_technical_data():
    cm1 = "select count(*) from entrance_form"
    cm2 = "select count(*) from entrance_form where statuscheck = 'Approved'"
    cm3 = "select max(marks) from entrance_marks"
    cm4 ="select min(marks) from entrance_marks natural join entrance_form where statuscheck = 'Approved'"
    cm5 ="select avg(marks) from entrance_marks natural join entrance_form where statuscheck = 'Approved'"
    cm6 ="select avg(marks) from entrance_marks"
    cm7 ="select count(*) from message_table"
    cm8 ="select count(*) from message_table where sender_id like 'S%' and receiver_id like 'T%'"
    cm9 ="select count(*) from message_table where sender_id like 'T%' and receiver_id like 'S%'"
    cm10 ="select count(*) from message_table where sender_id like '1%' and receiver_id like 'T%'"
    cm11 ="select count(*) from message_table where sender_id like 'T%' and receiver_id like '1%'"
    cm12 ="select count(*) from message_table where sender_id like '1%' and receiver_id like 'S%'"
    cm13 ="select count(*) from message_table where sender_id like 'S%' and receiver_id like '1%'"

    cur.execute(cm1)
    _val_1 = cur.fetchall()


    cur.execute(cm2)
    _val_2 = cur.fetchall()

    cur.execute(cm3)
    _val_3 = cur.fetchall()

    cur.execute(cm4)
    _val_4 = cur.fetchall()

    cur.execute(cm5)
    _val_5 = cur.fetchall()

    cur.execute(cm6)
    _val_6 = cur.fetchall()

    cur.execute(cm7)
    _val_7 = cur.fetchall()

    cur.execute(cm8)
    _val_8 = cur.fetchall()

    cur.execute(cm9)
    _val_9 = cur.fetchall()

    cur.execute(cm10)
    _val_10 = cur.fetchall()

    cur.execute(cm11)
    _val_11 = cur.fetchall()

    cur.execute(cm12)
    _val_12 = cur.fetchall()

    cur.execute(cm13)
    _val_13 = cur.fetchall()


    cmd_to_ins_1 ="insert into technical_data(entrance_appear_stu,approved_in_entrance_stu,max_marks_in_entrance,cutoff_marks_in_entrance,avg_marks_in_entrance_of_approved_stu, avg_marks_in_entrance,total_msg,total_msg_stuTotec,total_msg_tecTostu,total_msg_adminTotec,total_msg_tecToadmin,total_msg_adminTosec,total_msg_stuToadmin) values({},{},{},{},{},{},{},{},{},{},{},{},{})".format(_val_1[0][0],_val_2[0][0],_val_3[0][0],_val_4[0][0],_val_5[0][0],_val_6[0][0],_val_7[0][0],_val_8[0][0],_val_9[0][0],_val_10[0][0],_val_11[0][0],_val_12[0][0],_val_13[0][0])
    #print(cmd_to_ins_1)
    cur.execute(cmd_to_ins_1)
    


# In[9]:


#delete marksheet at each end of acedemic yaer - ---------------
def delete_marksheet_store_in_backup():
    cmd_catall_1 = "select catagory from catagory_selection"
    cur.execute(cmd_catall_1)
    cat_all_are = cur.fetchall()
    for cat_all in cat_all_are:
        cmd_marksheet_backup = "insert into marksheet_backup(year_of_exam,student_roll_number,terminal,total_marks_obtained,percentage,remarks) Select year_of_exam,student_roll_number,terminal,total_marks_obtained,percentage,remarks from marksheet_calculation_{} ".format(cat_all[0])
        cur.execute(cmd_marksheet_backup)
        cur.execute("Delete from marksheet_catagory_{}".format(cat_all[0]))


# In[10]:


#admin declare acedemic year -------------- func
def admin_declare_end_of_acedemic_year():
    try:
        
        print("Process 1:Transfering all information to technical data table..  ")

        get_technical_data()
        print("Process 1 COMPLETED!!!")





        print("\nPROCESS 2: Deleting messages of 12 and user id of 12 and tranfering class 12 to past student table...")

        deletemsg_paststudent_and_user_from_securitytable_transfer_to_past_student()
        print("Process 2 COMPLETED!!!")
        
        

        print("\n PROCESS 3:CLEARING MARKSHEET")
        delete_marksheet_store_in_backup()
        print("Process 3 COMPLETED!!!")
        
        print("\n PROCESS 4:DELETING REGISTERED STUDENT")
        ex88 = "delete from registration where class = 12"
        cur.execute(ex88)
        print("Process 4 COMPLETED!!!")



        print("\nPROCESS 5: Clearing Entrance form and entrance marks...")

        delete_allcontent_from()
        print("Process 5 COMPLETED!!!")
        
       




        print("\nPROCESS 6: Updating Class 11 student to 12 ...")

        update_class_12()
        print("Process 6 COMPLETED!!!")






        print("\nPROCESS 7: Granting student to fill entrance from")

        cur.execute("grant insert on school_management.entrance_form TO 'student';")
        print("Process 7 COMPLETED!!!")
        
       
        
        #----------------------------recording activity
        
        activity_msg = "Declaring end of acedemic year"
        activity_status = "success"
        cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
        cur.execute(cmd_activity_1)
        mydb.commit()
        print("All process completed")
        
          
        #----------------------------------------------------------
        
        
        
        
        
        
        

    except:
        print("!!!Error occured !!! all process cancelled ")
        mydb.rollback()
        
        #----------------------------recording activity------------------

        try:
            activity_msg = "Declaring end of acedemic year"
            activity_status = "failed"
            cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
            cur.execute(cmd_activity_1)
            mydb.commit()
        except:
            print("!!!Error in recording activity")
        #----------------------------------------------------------
        
        
        
        
        

        
        
    print("Sending message to students regarding new season.")
    msg_acd = '''Dear student, \nNew acedemic session has started\nWe would like to wish for your great session ahead.'''
    msg_to_all_stu(msg_acd)
        
    



# In[ ]:





# In[11]:


def change_statuscheck_of_candidate():
    print("\n----------------------------------CHANGE STATUS OF CANDIDATE ----------------------------------")
    e_roll_extract = input("Enter Entance_roll: ").upper()
    cmd_chgstatus_1 = "Select entrance_roll,fname,lname from entrance_form where entrance_roll = '{}'".format(e_roll_extract)
    cur.execute(cmd_chgstatus_1)
    e_roll_found = cur.fetchall()

    
    if(e_roll_found != []):
        print("\nEntance roll: {}      Name: {} {}".format(e_roll_found[0][0],e_roll_found[0][1],e_roll_found[0][2]))
        print("Type\n1 for changing to Approved\n2 for changing to Rejected\n3 for changing to Waiting\n any other to exit ")
        option_to_change_status = input("Enter your choice: ")
        if(option_to_change_status == '1'):
            statuscheck_to="Approved" 
            
        elif(option_to_change_status == '2'):
            statuscheck_to="Rejected"
        elif(option_to_change_status == '3'):
            statuscheck_to="Waiting"
        else:
            return
        try:
            cmd_chgstatus = "Update entrance_form set statuscheck = '{}' where entrance_roll = '{}'".format(statuscheck_to,e_roll_found[0][0])
            cur.execute(cmd_chgstatus)
            
            
            #----------------------------recording activity

            activity_msg = "Updating status of {} to {}".format(e_roll_found[0][0],statuscheck_to)
            activity_status = "success"
            cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
            cur.execute(cmd_activity_1)
            mydb.commit()
      
            #-------------------------------------------------------

            print("All process completed")

        
            
            
            print("Sucessfully Updated")
        except:
            mydb.rollback()
            print("!!!Error occured")
            
            
            
            #----------------------------recording activity
            try:
                activity_msg = "Updating status of {} to {}".format(e_roll_found[0][0],statuscheck_to)
                activity_status = "failed"
                cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
                cur.execute(cmd_activity_1)
                mydb.commit()
            except:
                print("!!!Error in recording activity")
            #-------------------------------------------------------

    else:
        print("!!!! No ID found")


# In[12]:



def transfer_students_into_registration():
    print("Transfering Student To registratin table ... Please wait")
    ex123 = "Select s_roll from registration"
    cur.execute(ex123)
    all_roll = cur.fetchall()
    if(len(all_roll) == 0):
        today = str(date.today())
        #print(today)
        date_only = int(today[1:4])
        #print(date_only)
        date_nepali = str(date_only + 57).zfill(3)
    else:
        today = all_roll[-1][0]
        date_only = int(today[1:4])
        #print(today)
        date_only +=1
        #print(date_only)
        date_nepali = str(date_only).zfill(3)


    roll_num = 0
    ex8 = "SELECT entrance_roll from entrance_form where statuscheck = 'Approved'"
    cur.execute(ex8)
    selective_roll = cur.fetchall()
    section = ['T1','T2']
    
    try:
        for selroll in selective_roll:

            random_section = random.choice(section)
            roll_num += 1
            roll = "S" + date_nepali + "-" + str(roll_num).zfill(3)		
            tup5 = (roll,random_section)
            ex9 = f'''INSERT INTO registration(fname,lname,dob,gender,address,email,faculty,catagory,gpa,guardian_name,guardian_number)  
            Select fname,lname,dob,gender,address,email,faculty,catagory,gpa,guardian_name,guardian_number from  entrance_form where entrance_roll = "{selroll[0]}" '''
            cur.execute(ex9)
            ex10 = 'Update registration set s_roll = %s , section = %s where s_roll = "xxxxxx"'
            cur.execute(ex10,tup5)

            password_stu_rand = randompassword()
            ex11 = "insert into security_table values('{}','{}')".format(roll,password_stu_rand)
            cur.execute(ex11)

      
        

        #----------------------------recording activity
       
        activity_msg = "Transfering selected student to registration table"
        activity_status = "success"
        cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
        cur.execute(cmd_activity_1)
        mydb.commit()

        #-------------------------------------------------------

        
        print("Transferred successsfully")
    except:
        mydb.rollback()
        print("!!!Error occured while transfering")

        #----------------------------recording activity
        try:
            activity_msg = "Transfering selected student to registration table"
            activity_status = "failed"
            cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
            cur.execute(cmd_activity_1)
            mydb.commit()
        except:
            print("!!!Error in recording activity")
        #-------------------------------------------------------
    

    


# In[13]:


def admin_declare_entrance_exam():
    print("\n\n-------------------------------ADMIN DECLARE ENTRANCE EXAM -----------------------------------")
    
    print("\nPROCESS 1: Disabling entrance form table ...")
    try:
        cur.execute("revoke insert on school_management.entrance_form from 'student'")
        print("Process 1 COMPLETED!!!")
        
    except:
        print("!!!! Error in process one\nprocess TERMINATED!!!")
        return
    
 
    
    
    print("\nPROCESS 2: Filling entrance marks table with roll number ...")
    try:
        entrance_roll_cmd = "Select entrance_roll from entrance_form"
        cur.execute(entrance_roll_cmd)
        entrance_roll_all = cur.fetchall()



        entrance_roll_cmd_markstable = "Select entrance_roll from entrance_marks"
        cur.execute(entrance_roll_cmd_markstable)
        entrance_roll_all_markstable = cur.fetchall()
        entrance_roll_all_markstable_list = [] #variable to store exixted eroll in emarkstable
        check_anyother_eroll = 0

        #getting eroll in entrance marks table to avoid dupicate entry
        for entrance_roll_markstable in entrance_roll_all_markstable:
            entrance_roll_all_markstable_list.append(entrance_roll_markstable[0])

        #print(entrance_roll_all_markstable)
        
        #inser eroll in entrance marks
        for entrance_roll_ in entrance_roll_all:
            if(entrance_roll_all_markstable_list.count(entrance_roll_[0])==0):
                cmd_insert_entrance_marks_tb_1 = "insert into entrance_marks values('{}',{})".format(entrance_roll_[0],0)
                cur.execute(cmd_insert_entrance_marks_tb_1)
                check_anyother_eroll = 1

        if(check_anyother_eroll ==1):
            
            

            #----------------------------recording activity
            
            activity_msg = "Declaring entrance exam."
            activity_status = "success"
            cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
            cur.execute(cmd_activity_1)
            mydb.commit()
           
            #-------------------------------------------------------
            print("Process 2 COMPLETED!!!")
    except:
        mydb.rollback()
        print("!!!! Error in process one\nprocess TERMINATED!!!")
                    

        #----------------------------recording activity
        try:
            activity_msg = "Declaring entrance exam"
            activity_status = "failed"
            cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
            cur.execute(cmd_activity_1)
            mydb.commit()
        except:
            print("!!!Error in recording activity")
        #-------------------------------------------------------
        return
    
    print("\n All processes are completed sucessfully")
    
    


# In[14]:


def admin_declare_entrance_result():
        

    while True:
        total_intake = input("Enter total student to be selected: ")
        if(total_intake.isnumeric()):
            break
        else:
            print('!!!! Invaid value')
    
    print("Process 2: Giving status...")
    entrance_toper =  "Select * from entrance_marks order by marks desc limit  {}".format(total_intake)
    cur.execute(entrance_toper)
    get_topper_stu = cur.fetchall()
    topper_stu_list = []
    
    for get_topper_ in get_topper_stu:
        topper_stu_list.append(get_topper_[0])
        
    
    
    entrance_stu =  "Select entrance_roll from entrance_form"
    cur.execute(entrance_stu)
    get_entrance_stu = cur.fetchall()
    
    
    try:
        for _entrance_stu in get_entrance_stu:
            if(topper_stu_list.count(_entrance_stu[0]) == 1):
                statuscheck_ = "Approved"
            else:
                statuscheck_ = "Rejected"

            cmd_entrance_stu = "update entrance_form set statuscheck = '{}' where entrance_roll = '{}'".format(statuscheck_,_entrance_stu[0])
            cur.execute(cmd_entrance_stu)
        
        
            

        #----------------------------recording activity
       
        activity_msg = "Declaring entrance result"
        activity_status = "success"
        cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
        cur.execute(cmd_activity_1)
        mydb.commit()
    
        #-------------------------------------------------------

    except:
        mydb.rollback()
        print("!!!Error occured")
        #----------------------------recording activity
        try:
            activity_msg = "Declaring entrance result"
            activity_status = "failed"
            cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
            cur.execute(cmd_activity_1)
            mydb.commit()
        except:
            print("!!!Error in recording activity")
        #-------------------------------------------------------
        
        return
            
        
    
    print("\n All processes are completed sucessfully")
    


# In[15]:


#MESSAGING SYSTEM------------------------------------


def get_my_message_status(login_user,all_msg):
    msg_by = []
    
    #collect all message sender
    for msg_read_for_status in all_msg:
        if(msg_read_for_status[2]==login_user and msg_read_for_status[5] == 'U'):
            msg_by.append(msg_read_for_status[1])

    
    #fillterarion of message sender to know how many message bu whom
    c_msg_status =[] #give all sender id
    d_msg_status = [] # give total message
    #name_for_msg_status = [] #give name of sender
    if(msg_by != []):
        while True:
            e_msg_status = msg_by[0]
            c_msg_status.append(e_msg_status)
            b_msg_status = msg_by.count(e_msg_status)
            d_msg_status.append(b_msg_status)
            while True:

                for i in range(0,b_msg_status):
                    msg_by.remove(e_msg_status)

                if(msg_by.count(e_msg_status) == 0 ):
                    break
            if(msg_by == [] ):
                break       
            
    
    
    
    
            
    print("INBOX MESSAGE")
    if(c_msg_status == []):
        print("No unseen message")
    for i in range(0,len(c_msg_status)):
        print(i+1,". ",c_msg_status[i],"(",d_msg_status[i],")")
    if(c_msg_status.count('1000') != 0):
        print("*** NEW MESSAGE FROM ADMIN (1000) ***")
    else:
        pass























#this define single message box with particular person
def message_box(login_user,receiver_id,receiver_fname,receiver_lname,id_all_msg):
    
    

    chat_with = "{} {}({})".format(receiver_fname,receiver_lname,receiver_id)
    print("\n\n-----------------MESSAGE BOX WITH {}---------------------------------------------------------------\n\n".format(chat_with ))
    if(id_all_msg==[]):
        print("No message till now")
        
    
    for msg_with_id in id_all_msg:


        if(msg_with_id[1]== receiver_id):
            print("from {} {}".format(chat_with,msg_with_id[3]))
            print("Message: ",msg_with_id[4])
            

        elif(msg_with_id[2]== receiver_id):
            
            staTus_msg = 'UNSEEN'
            
            print("To {} {}".format(chat_with,msg_with_id[3]))
            print("Message: ",msg_with_id[4])
            if(msg_with_id[5] == 'S'): # for checking status
                staTus_msg = 'SEEN'
            print("Status: ",staTus_msg)
        print("-------------------------------------------------")
        
    #change status from unseen to seen
    msg_cmd_status_change = "Update message_table set msg_status = 'S' where sender_id = '{}' and receiver_id = '{}'".format(receiver_id,login_user)
    cur.execute(msg_cmd_status_change)
    mydb.commit()
        
        
    while True:
        print("To {} ".format(chat_with))
        message_ = input("Message: ")
        
        if(message_ == '#' or message_ == '#'):
            print("-------------------------------------------------Message box close----------------------------\n\n")
            break
        else:
            print("Status: ",'UNSEEN')
            
        msg_cmd_5 = "Insert into message_table (sender_id,receiver_id,message) value ('{}','{}','{}')".format(login_user,receiver_id,message_)
        cur.execute(msg_cmd_5)
        mydb.commit()
        print("------------------------------------------------------")
        
    











# --------------------------- admin message handelling -----------------------------
def admin_login_(login_user,login_type):
        
    while True:
        get_to_whome =[] #variable to store all stu or teacher id

        print("\n\n--------------------------------MESSAGE SECTION ------------------------------------")
        msg_cmd_1 = "Select * from message_table where sender_id = '{}' or receiver_id ='{}'".format(login_user,login_user) #select all message by login_user
        cur.execute(msg_cmd_1)   
        all_msg = cur.fetchall()
        
        
        #to display all message status
        get_my_message_status(login_user,all_msg)
        
        
        
        id_all_msg = [] # for storing message with sepcific user
        
        print("Type #6 for sending message to group")
        
        #select id to message
        
        select_id_for_msg = input("Select id to message: ").upper()
        
        if(select_id_for_msg =='#'):
            print("Exited...")
            break
            
        #--------------------------- SEction to handle message to group---------------    
        if(select_id_for_msg =='#6'):
            print("type 1 to send message to students according to class.")
            print("type 2 to send message to teachers according to department.")
            print("type 3 to send message to students according to catagory.")
            print("type 4 to send message to all students.")
            print("type 5 to send message to all teachers.")
            
            
            
            
            op_grp_msg = input("Enter your option: ") 
            
            if(op_grp_msg == '1'):
                class_input_stu = input("Enter class: ")
                if(class_input_stu == '11' or class_input_stu == '12'):
                    cmd_gr_msg_1 = "Select s_roll from registration where class = {}".format(class_input_stu)
                    cur.execute(cmd_gr_msg_1)
                    all_id_of_group = cur.fetchall()
                else:
                    print("Invalid input !!!")
                    continue
            elif(op_grp_msg == '2'):
                dept_input_tec = input("Enter Department: ")
                cmd_gr_msg_1 = "Select teacher_id from teacher_details where department = '{}'".format(dept_input_tec)
                cur.execute(cmd_gr_msg_1)
                all_id_of_group = cur.fetchall()
            elif(op_grp_msg == '3'):
                cat_input_stu = input("Enter Catagory: ").upper()
                cmd_gr_msg_1 = "Select s_roll from registration where catagory = '{}'".format(cat_input_stu)
                cur.execute(cmd_gr_msg_1)
                all_id_of_group = cur.fetchall()
            elif(op_grp_msg == '4'):
                cmd_gr_msg_1 = "Select s_roll from registration"
                cur.execute(cmd_gr_msg_1)
                all_id_of_group = cur.fetchall()
            elif(op_grp_msg == '5'):
                cmd_gr_msg_1 = "Select teacher_id from teacher_details"
                cur.execute(cmd_gr_msg_1)
                all_id_of_group = cur.fetchall() 
           
                
                
            else:
                print("******************invalid input *************************")
                all_id_of_group = []
                continue
                
                
            msg_grp_ = input("MESSAGE: ") # enter message for group
            
                
            #inseerting  group message to security table    
            for all_id_  in all_id_of_group:
                
                cmd_gr_msg_2 = "Insert into message_table (sender_id,receiver_id,message) value ('1000','{}','{}')".format(all_id_[0],msg_grp_)
                cur.execute(cmd_gr_msg_2)
            mydb.commit()
            print("*** Message Successfully delivered")
            continue
                
                
            
            
            
        #----------------------------end of above section ------------------------    
        # develop condition for stu-teacher and teacher to stu msg only    
        if(select_id_for_msg[0] == 'T'):   
            #select detail of id entered from teacher details
            msg_cmd_2 = "select teacher_id,fname,lname from teacher_details where teacher_id = '{}'".format(select_id_for_msg)
            cur.execute(msg_cmd_2)
            get_to_whome = cur.fetchall()
        if(select_id_for_msg[0] == 'S'):
            msg_cmd_2 = "select s_roll,fname,lname from registration where s_roll = '{}'".format(select_id_for_msg)
            cur.execute(msg_cmd_2)
            get_to_whome = cur.fetchall()
            
        
        #check type of id called
        
        
        if(get_to_whome == []):
            print(" NO ID found!!!!")
        elif(select_id_for_msg == get_to_whome[0][0]):
            receiver_id = get_to_whome[0][0]
            receiver_fname = get_to_whome[0][1]
            receiver_lname = get_to_whome[0][2]
            for all_msg_ in all_msg:
                
                if (all_msg_[1] == receiver_id or all_msg_[2] == receiver_id):
                    id_all_msg.append(all_msg_)
            message_box(login_user,receiver_id,receiver_fname,receiver_lname,id_all_msg)
            
        






# In[16]:


#Teacher ----------------------registration
def get_teacher_id():    
    while True:
        rand_num_t_1 ='T'+str(random.randint(10000,99999))
        cmd_tinr_3 = "Select teacher_id from teacher_details where teacher_id = '{}'".format(rand_num_t_1)
        cur.execute(cmd_tinr_3)
        all_teach_detail_list = cur.fetchall()
        cmd_tinr_4 = "Select teacher_id from old_teacher_details where teacher_id = '{}'".format(rand_num_t_1)
        cur.execute(cmd_tinr_4)
        all_old_teach_detail_list = cur.fetchall()

        if(all_teach_detail_list == [] and all_old_teach_detail_list == []):
            break
    return rand_num_t_1


def teacher_detail_registration_by_admin():
    print("-----------------------------------TEACHER DETAIL INSERTION------------------------------------------")
    department_available = get_availabe_department() #store all subject vailable
    
    #teacher detail fill up ----------------------------------------------------------------------------------
    #teacher fname -------------------------------
    while True:
        teacher_fname = input("Enter teacher FNAME: ").upper()
        f_name_split_list = teacher_fname.split()
        teacher_fname = ""
        check_isalp = 0
        for f_name_split in f_name_split_list:
            if(f_name_split.isalpha()==False):
                check_isalp = 1
        #check string is alphabet or not        
        if(check_isalp == 1):
            print("Invalid String!!!")
            continue
        #put string in proper format    
        if(len(f_name_split_list) == 1):
            teacher_fname = f_name_split_list[0]
            break
        elif(len(f_name_split_list) == 2):
            teacher_fname = f_name_split_list[0]+" "+f_name_split_list[1]
            break     
        else:
            print("Invalid String!!!!!!")
            
    #--------------------------------teacher lname-        
    while True:
        teacher_lname = input("Enter teacher LNAME: ").upper()
        l_name_split_list = teacher_lname.split()
        teacher_lname = ""
        check_isalp = 0
        for l_name_split in l_name_split_list:
            if(l_name_split.isalpha()==False):
                check_isalp = 1
        #check string is alphabet or not        
        if(check_isalp == 1):
            print("Invalid String!!!!!!")
            continue
        #put string in proper format    
        if(len(l_name_split_list) == 1):
            teacher_lname = l_name_split_list[0]
            break     
        else:
            print("Invalid String!!!!!!")
    
    #----------------------contact number -----------
    while True:
        teacher_contact = input("Enter teacher contact number: ")
        if((len(teacher_contact) == 10) and (teacher_contact.isnumeric() == True) ):
            break
        print("Invalid phone number!!!")
    #---------------------------- email-------------------
    while True:
        teacher_email = input("Enter teacher mail: ").lower()
        if((teacher_email.count('@')==1) and (teacher_email.count('.com')==1) and (len(teacher_email)>6)):
            break
        print("INVALID EMAIL")
           
    #-----------------------------------------department------------------------
    while True:
        print("Available Department are:- {}".format(department_available))
        teacher_dept = input("Enter teacher department: ").capitalize()
        if(department_available.count(teacher_dept)!=0):
            break
        print("Invalid Department")
        
        
    
    #check detail are correct or not
    corr_check = input("Are details correct?(Y/N)").upper()
    if(corr_check != 'Y'):
        print("Process Terminated !!!!!!")
        return
        
       
    #inserting intoo databse--------------------
    try:
        teacher_id = get_teacher_id() #get teacher id
        cmd_tiner_1 = "insert into teacher_details values('{}','{}','{}',{},'{}','{}')".format(teacher_id,teacher_fname,teacher_lname,teacher_contact,teacher_email,teacher_dept)
        cur.execute(cmd_tiner_1)
        get_rand_pwd = randompassword() #get random password
        sec_cmd_1 = "insert into security_table values('{}','{}')".format(teacher_id,get_rand_pwd)
        cur.execute(sec_cmd_1)
        
        
        #----------------------------recording activity
        
        activity_msg = "Registering new teacher ({})".format(teacher_id)
        activity_status = "success"
        cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
        cur.execute(cmd_activity_1)
        mydb.commit()
        print("Successfully inserted")
        
        #-------------------------------------------------------
        
    except:
        mydb.rollback()
        print("Error occur while inserting")
        #----------------------------recording activity
        try:
            activity_msg = "Registering new teacher"
            activity_status = "failed"
            cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
            cur.execute(cmd_activity_1)
            mydb.commit()
            

        except:
            print("!!!Error in recording activity")
        #-------------------------------------------------------

  

    print("---------------------------------------------------------------------------------------")
               
           
           
                 
            


# In[17]:


#update student teacher---------------
def delete_student_from_registration():
    print("-----------------------------------STUDENT DELETE SECTION---------------------------------")
    stu_up_roll = input("Enter id to delete: ").upper()
    cmd_up_1 = "Select * from registration where s_roll='{}'".format(stu_up_roll)
    cur.execute(cmd_up_1)
    list_up_stu = cur.fetchall() 
    if(list_up_stu != []):
        tup_up_stu = list_up_stu[0]
        print("NAME: ",tup_up_stu[1]+" "+tup_up_stu[2])
        
        try:  
            catagory_of_stu = tup_up_stu[8]
            #print(catagory_of_stu)
            cmd_del_stu_1 = "Delete from message_table where ( sender_id = '{}' or receiver_id = '{}')".format(stu_up_roll,stu_up_roll)

            cur.execute(cmd_del_stu_1)

            cmd_del_stu_2 = "Delete from security_table where user_id = '{}'".format(stu_up_roll)
            cur.execute(cmd_del_stu_2)


        
            cmd_marksheet_backup = "insert into marksheet_backup(year_of_exam,student_roll_number,terminal,total_marks_obtained,percentage,remarks) Select year_of_exam,student_roll_number,terminal,total_marks_obtained,percentage,remarks from marksheet_calculation_{} where student_roll_number = '{}'".format(catagory_of_stu,stu_up_roll)
            cur.execute(cmd_marksheet_backup)
            cur.execute("Delete from marksheet_catagory_{} where student_roll_number = '{}'".format(catagory_of_stu,stu_up_roll))
            
            
            cmd_del_stu_3 = """Insert into past_student(student_id,fname,lname,dob,gender,address,email,faculty,catagory,guardian_name,guardian_number,statuscheck)
            Select s_roll,fname,lname,dob,gender,address,email,faculty,catagory,guardian_name,guardian_number,'Drop Out' from registration where s_roll = '{}'""".format(stu_up_roll)
            #print(cmd_del_stu_3)
            cur.execute(cmd_del_stu_3)

            cmd_del_stu_4 = "Delete from registration where s_roll = '{}'".format(stu_up_roll)
            cur.execute(cmd_del_stu_4)

            
            
            #----------------------------recording activity

            activity_msg = "Deleting student ({})".format(stu_up_roll)
            activity_status = "success"
            cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
            cur.execute(cmd_activity_1)
            mydb.commit()
            print("Succesfuly deleted!!!!")
            
            #-------------------------------------------------------

        except:
            mydb.rollback()
            print("!!! Error occur")
            #----------------------------recording activity
            try:
                activity_msg = "Deleting student ({})".format(stu_up_roll)
                activity_status = "failed"
                cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
                cur.execute(cmd_activity_1)
                mydb.commit()
            except:
                print("!!!Error in recording activity")
            #-------------------------------------------------------
    
    else:
        print("No ID found!!!!\nProcess Terminaled")
        return


    
#delete teacher-------------------- update teacher student
#update student teacher---------------
def delete_teacher_from_teacher_details():
    print("-----------------------------------TEACHER DELETE SECTION---------------------------------")
    tech_up_roll = input("Enter id to delete: ").upper()
    cmd_up_1 = "Select * from teacher_details where teacher_id ='{}'".format(tech_up_roll)
    cur.execute(cmd_up_1)
    list_up_tech = cur.fetchall() 
    if(list_up_tech != []):
        tup_up_tech = list_up_tech[0]
        print("NAME: ",tup_up_tech[1]+" "+tup_up_tech[2])
        
        try:  
            
            cur.execute("Delete from section_teacher where teacher_id = '{}'".format(tech_up_roll))
            
            cmd_del_tech_1 = "Delete from message_table where ( sender_id = '{}' or receiver_id = '{}')".format(tech_up_roll,tech_up_roll)

            cur.execute(cmd_del_tech_1)

            cmd_del_tech_2 = "Delete from security_table where user_id = '{}'".format(tech_up_roll)
            cur.execute(cmd_del_tech_2)


            
            cmd_del_tech_3 = """Insert into old_teacher_details(teacher_id,fname,lname,contact_number,email,department)
            Select teacher_id,fname,lname,contact_number,email,department from teacher_details where teacher_id = '{}'""".format(tech_up_roll)
            #print(cmd_del_tech_3)
            cur.execute(cmd_del_tech_3)

            cmd_del_tech_4 = "Delete from teacher_details where teacher_id = '{}'".format(tech_up_roll)
            cur.execute(cmd_del_tech_4)

            
            
            #----------------------------recording activity

            activity_msg = "Deleting teacher ({})".format(tech_up_roll)
            activity_status = "success"
            cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
            cur.execute(cmd_activity_1)
            mydb.commit()
            print("Succesfuly deleted!!!!")
            
            #-------------------------------------------------------

        except:
            mydb.rollback()
            print("!!! Error occur")
            #----------------------------recording activity
            try:
                activity_msg = "Deleting teacher ({})".format(tech_up_roll)
                activity_status = "failed"
                cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
                cur.execute(cmd_activity_1)
                mydb.commit()
            except:
                print("!!!Error in recording activity")
            #-------------------------------------------------------
    
    else:
        print("No ID found!!!!\nProcess Terminaled")
        return


#----------------------------------------------------------------


def update_student_record():
    print("-----------------------------------STUDENT UPDATE SECTION---------------------------------")
    print('enter # to exit')
    stu_up_roll = input("Enter id to update: ").upper()
    if(stu_up_roll=='#'):
        return
    cmd_up_1 = "Select * from registration where s_roll='{}'".format(stu_up_roll)
    cur.execute(cmd_up_1)
    list_up_stu = cur.fetchall() 
    if(list_up_stu != []):
        tup_up_stu = list_up_stu[0]
        print("NAME: ",tup_up_stu[1]+" "+tup_up_stu[2])

        print("Type:\n1 for updating Address\n2 for updating Mail\n3 for updating Gaurdain name\n4 for updating Gaurdain Number\n5 for updating Catagory\nany other to exit")
        op_stu_update = input("Enter option: ")
        #update address
        if(op_stu_update == '1'):
            up_add_to_update= input("Enter Address To update:")
            if(len(up_add_to_update) < 3):
                print("Invalid input!!!\nProcess terminated")
                return
            else:
                try:
                    cmd_up_2 = "update registration set address = '{}' where s_roll = '{}'".format(up_add_to_update,stu_up_roll)
                    cur.execute(cmd_up_2)
                    mydb.commit()
                    print("Updated successfully")
                except:
                    mydb.rollback()
                    print("Error in updating")
            
        #update  email
        elif(op_stu_update == '2'):
            up_email_to_update= input("Enter Mail To update:")
            if((up_email_to_update.count('@')==1) and (up_email_to_update.count('.com')==1) and (len(up_email_to_update)>6)):
                try:
                    cmd_up_2 = "update registration set  email= '{}' where s_roll = '{}'".format(up_email_to_update,stu_up_roll)
                    cur.execute(cmd_up_2)
                    mydb.commit()
                    print("Updated successfully")
                except:
                    mydb.rollback()
                    print("Error in updating")
            else:
                print("Invalid input!!!\nProcess terminated")
                return
            
        #update  gaurden name
        elif(op_stu_update == '3'):
            up_gname_to_update= input("Enter Gaurdain Name To update:")
            up_gname_to_update_list = up_gname_to_update.split()
            up_gname_to_update = ""
            check_isalp = 0
            for up_gname_to_update_split in up_gname_to_update_list:
                if(up_gname_to_update_split.isalpha()==False):
                    check_isalp = 1
            #check string is alphabet or not        
            if(check_isalp == 1):
                print("Invalid String!!!\nProcess terminated")
                return
            #put string in proper format    
            if(len(up_gname_to_update_list) == 2):
                up_gname_to_update = up_gname_to_update_list[0]+" "+up_gname_to_update_list[1]
                
            elif(len(up_gname_to_update_list) == 3):
                up_gname_to_update = up_gname_to_update_list[0]+" "+up_gname_to_update_list[1]+" "+up_gname_to_update_list[2]
                    
            else:
                print("Invalid String!!!!!!\nProcess terminated")
                return
            try:
                cmd_up_3 = "update registration set   guardian_name= '{}' where s_roll = '{}'".format(up_gname_to_update,stu_up_roll)
                cur.execute(cmd_up_3)
                mydb.commit()
                print("Updated successfully")
            except:
                mydb.rollback()
                print("Error in updating")


        #update gaurdain phone number
        elif(op_stu_update == '4'):
            up_gphone_to_update= input("Enter Phone Number To update:")
            if((len(up_gphone_to_update) == 10) and (up_gphone_to_update.isnumeric() == True) ):
                try:
                    cmd_up_7 = "update registration set  guardian_number= {} where s_roll = '{}'".format(up_gphone_to_update,stu_up_roll)
                    cur.execute(cmd_up_7)
                    mydb.commit()
                    print("Updated successfully")
                except:
                    mydb.rollback()
                    print("error in updating")
            else:
                print("Invalid input!!!\nProcess terminated")
                return
            
        
        elif(op_stu_update == '5'):
            
    
            up_catagory_to_update= input("Enter Catagory To update:").upper()
            #fetching available catagory
            cmd_up_9 = "Select catagory from catagory_selection"
            cur.execute(cmd_up_9)
            all_cat_available = cur.fetchall()

            all_cat_available_list = []
            for all_cat_ in all_cat_available:
                all_cat_available_list.append(all_cat_[0])
            all_cat_available_list        

            if(all_cat_available_list.count(up_catagory_to_update) != 0):

                try:
                    cmd_up_6 = "update registration set  catagory= '{}' where s_roll = '{}'".format(up_catagory_to_update,stu_up_roll)
                    cur.execute(cmd_up_6)
                    mydb.commit()
                    print("Updated successfully")
                    update_student_record()
                except:
                    mydb.rollback()
                    print("Error in updating")
            else:
                print("Invalid input!!!\nProcess terminated")
                return
                
            
        
            
    else:
        print("No ID found!!!!\nProcess Terminaled")
        return

    
    
    
    
#update student    
def update_teacher_record():
    print("-----------------------------------TEACHER UPDATE SECTION---------------------------------")
    tech_up_roll = input("Enter id to update: ").upper()
    cmd_up_1 = "Select * from teacher_details where teacher_id='{}'".format(tech_up_roll)
    cur.execute(cmd_up_1)
    list_up_tech = cur.fetchall() 
    if(list_up_tech != []):
        tup_up_tech = list_up_tech[0]
        print("NAME: ",tup_up_tech[1]+" "+tup_up_tech[2])

        print("Type:\n1 for updating Contact Number\n2 for updating Mail")
        op_tech_update = input("Enter option: ")
        #update address
        #update  phone number
        if(op_tech_update == '1'):
            up_tphone_to_update= input("Enter Phone Number To update:")
            if((len(up_tphone_to_update) == 10) and (up_tphone_to_update.isnumeric() == True) ):
                try:
                    cmd_up_2 = "update teacher_details set  contact_number= {} where teacher_id = '{}'".format(up_tphone_to_update,tech_up_roll)
                    cur.execute(cmd_up_2)
                    mydb.commit()
                    print("Updated successfully")
                except:
                    mydb.rollback()
                    print("Error in updating")
            else:
                print("Invalid input!!!\nProcess terminated")
                return

            
        #update  email
        elif(op_tech_update == '2'):
            up_temail_to_update= input("Enter Mail To update:")
            if((up_temail_to_update.count('@')==1) and (up_temail_to_update.count('.com')==1) and (len(up_temail_to_update)>6)):
                try:
                    cmd_up_2 = "update teacher_details set  email= '{}' where teacher_id = '{}'".format(up_temail_to_update,tech_up_roll)
                    cur.execute(cmd_up_2)
                    mydb.commit()
                    print("Updated successfully")
                except:
                    mydb.rollback()
                    print("Error in updating")
            else:
                print("Invalid input!!!\nProcess terminated")
                return



        
            
    else:
        print("No ID found!!!!\nProcess Terminaled")
        return


# In[18]:


#update past student ---------------



def update_past_student_record():
    print("-----------------------------------PAST STUDENT UPDATE SECTION---------------------------------")
    stu_up_roll = input("Enter id to update: ").upper()
    cmd_up_1 = "Select * from past_student where student_id='{}'".format(stu_up_roll)
    cur.execute(cmd_up_1)
    list_up_stu = cur.fetchall() 
    if(list_up_stu != []):
        tup_up_stu = list_up_stu[0]
        print("NAME: ",tup_up_stu[1]+" "+tup_up_stu[2])

        print("Type:\n1 for updating Address\n2 for updating Mail\n3 for updating Gaurdain name\n4 for updating Gaurdain Number\n5 for updating Remark for futher study\n6 for updating aggregrated GPA\nany other to exit")
        op_stu_update = input("Enter option: ")
        #update address
        if(op_stu_update == '1'):
            up_add_to_update= input("Enter Address To update:")
            if(len(up_add_to_update) < 3):
                print("Invalid input!!!\nProcess terminated")
                return
            else:
                try:
                    cmd_up_2 = "update past_student set address = '{}' where student_id = '{}'".format(up_add_to_update,stu_up_roll)
                    cur.execute(cmd_up_2)
                    mydb.commit()
                    print("Updated successfully")
                except:
                    mydb.rollback()
                    print("error in updatating")
            
        #update  email
        elif(op_stu_update == '2'):
            up_email_to_update= input("Enter Mail To update:")
            if((up_email_to_update.count('@')==1) and (up_email_to_update.count('.com')==1) and (len(up_email_to_update)>6)):
                try:
                    cmd_up_2 = "update past_student set  email= '{}' where student_id = '{}'".format(up_email_to_update,stu_up_roll)
                    cur.execute(cmd_up_2)
                    mydb.commit()
                    print("Updated successfully")
                except:
                    mydb.rollback()
                    print("Error in updating")
            else:
                print("Invalid input!!!\nProcess terminated")
                return
            
        #update  gaurden name
        elif(op_stu_update == '3'):
            up_gname_to_update= input("Enter Gaurdain Name To update:")
            up_gname_to_update_list = up_gname_to_update.split()
            up_gname_to_update = ""
            check_isalp = 0
            for up_gname_to_update_split in up_gname_to_update_list:
                if(up_gname_to_update_split.isalpha()==False):
                    check_isalp = 1
            #check string is alphabet or not        
            if(check_isalp == 1):
                print("Invalid String!!!\nProcess terminated")
                return
            #put string in proper format    
            if(len(up_gname_to_update_list) == 2):
                up_gname_to_update = up_gname_to_update_list[0]+" "+up_gname_to_update_list[1]
                
            elif(len(up_gname_to_update_list) == 3):
                up_gname_to_update = up_gname_to_update_list[0]+" "+up_gname_to_update_list[1]+" "+up_gname_to_update_list[2]
                    
            else:
                print("Invalid String!!!!!!\nProcess terminated")
                return
            try:
                cmd_up_3 = "update past_student set   guardian_name= '{}' where student_id = '{}'".format(up_gname_to_update,stu_up_roll)
                cur.execute(cmd_up_3)
                mydb.commit()
                print("Updated successfully")
            except:
                mydb.rollback()
                print("Error in updating")


        #update gaurdain phone number
        elif(op_stu_update == '4'):
            up_gphone_to_update= input("Enter Phone Number To update:")
            if((len(up_gphone_to_update) == 10) and (up_gphone_to_update.isnumeric() == True) ):
                try:
                    cmd_up_7 = "update past_student set  guardian_number= {} where student_id = '{}'".format(up_gphone_to_update,stu_up_roll)
                    cur.execute(cmd_up_7)
                    mydb.commit()
                    print("Updated successfully")
                except:
                    mydb.rollback()
                    print("Error in updating")
            else:
                print("Invalid input!!!\nProcess terminated")
                return
            
        #update remark for futher study
        elif(op_stu_update == '5'):
            
    
            up_remark_to_update= input("Enter Remark: ")
            

            try:
                cmd_up_6 = "update past_student set remarks_further_study = '{}' where student_id = '{}'".format(up_remark_to_update,stu_up_roll)
                cur.execute(cmd_up_6)
                mydb.commit()
                print("Updated successfully")
            except:
                mydb.rollback()
                print("Error in updating")
                
        #update agregated GPA        
        elif(op_stu_update == '6'):
            
            
            up_gpa_to_update= input("Enter aggregate gpa: ")
            
            up_gpa_to_update_test_float = up_gpa_to_update.replace('.','0',1) #to check float or not
            
            if(up_gpa_to_update_test_float.isnumeric() == True):
                
                
                if((float(up_gpa_to_update)>=0.0) and (float(up_gpa_to_update)<=4.0)):
                    try:
                        cmd_up_6 = "update past_student set aggregate_gpa = {} where student_id = '{}'".format(up_gpa_to_update,stu_up_roll)
                        cur.execute(cmd_up_6)
                        mydb.commit()
                        print("Updated successfully")
                    except:
                        mydb.rollback()
                        print("Error in updating")
                else:
                    print("Invalid input!!!\nProcess terminated")
                    return
            else:
                print("Invalid input!!!\nProcess terminated")
                return




            
        
            
    else:
        print("No ID found!!!!\nProcess Terminaled")
        return

    
    
    


# In[19]:


#admin part one ------------------------------------------------



def catagory_creation():
    ex56 = "SELECT * from Catagory_selection"
    cur.execute(ex56)
    all_cat = cur.fetchall()
    listxyz = []
    for i in all_cat:
        listxyz.append(i[0])
    listxyz = tuple(listxyz)
    if(all_cat == []):
        print("No Catagories offered by school. Add a catagory.")
    else:
        print("Catagories offered by school are: ")
        for i in all_cat:
            print(i)

    catagory_addition = input("Enter the new catagory: ").upper()
    if catagory_addition in listxyz:
        print("Catagory Already Exists. Try Again!")
        return
    try:
        class_cat = int(input("Catagory offered to class: "))
    except:
        print("Class can either be 11 or 12. Try Again!")
        return
    faculty = input("Faculty of catagory(Science, Management or.....): ").capitalize()
    sub1 = input(f"Enter subject1 for catagory {catagory_addition}: ").capitalize()
    sub2 = input(f"Enter subject2 for catagory {catagory_addition}: ").capitalize()
    sub3 = input(f"Enter subject3 for catagory {catagory_addition}: ").capitalize()
    sub4 = input(f"Enter subject4 for catagory {catagory_addition}: ").capitalize()
    sub5 = input(f"Enter subject5 for catagory {catagory_addition}: ").capitalize()
    sub6 = input(f"Enter subject6 for catagory {catagory_addition} (Type 'No' If No Additional Subject): ").capitalize()
    
    try:
        if(sub6 == "No"):
            ex67= f"INSERT INTO Catagory_selection(catagory,class,faculty,subject1,subject2,subject3,subject4,subject5) values ('{catagory_addition}',{class_cat},'{faculty}','{sub1}','{sub2}','{sub3}','{sub4}','{sub5}')"
            ex2 = f'''Create table Marksheet_Catagory_{catagory_addition}(
            terminal varchar(1), year_of_exam int, student_roll_number varchar(20) not null, 
            {sub1} int default 0,{sub2} int default 0, {sub3} int default 0,
            {sub4} int default 0, {sub5} int default 0,status varchar(20) default "Unpublished", primary key(terminal, year_of_exam , student_roll_number),
            foreign key(student_roll_number) references registration(s_roll))'''
            ex33 = f'''create view marksheet_calculation_{catagory_addition} as
            select year_of_exam,student_roll_number,terminal, ({sub1} + {sub2} + {sub3} + {sub4} + {sub5}) as total_marks_obtained,
            ((({sub1} + {sub2} + {sub3} + {sub4} + {sub5})/500) * 100) as percentage, case when {sub1} >= 40 and {sub2} >= 40 and {sub3} >= 40 and {sub4} >=40 and {sub5} >=40  
            then "Pass" else "Fail" end as remarks    from marksheet_catagory_{catagory_addition}  where status = "Published" '''
        else:
            ex67= f"INSERT INTO Catagory_selection values ('{catagory_addition}','{class_cat}','{faculty}','{sub1}','{sub2}','{sub3}','{sub4}','{sub5}','{sub6}')"
            ex2 = f'''Create table Marksheet_Catagory_{catagory_addition}(
            terminal varchar(1), year_of_exam int, student_roll_number varchar(20) not null, 
            {sub1} int default 0,{sub2} int default 0, {sub3} int default 0,
            {sub4} int default 0, {sub5} int default 0, {sub6} int default 0, status varchar(20) default "Unpublished", primary key(terminal, year_of_exam , student_roll_number),
            foreign key(student_roll_number) references registration(s_roll))'''
            ex33 = f'''create view marksheet_calculation_{catagory_addition} as
            select year_of_exam,student_roll_number,terminal, {sub6}, ({sub1} + {sub2} + {sub3} + {sub4} + {sub5}) as total_marks_obtained,
            ((({sub1} + {sub2} + {sub3} + {sub4} + {sub5})/500) * 100) as percentage, case when {sub1} >= 40 and {sub2} >= 40 and {sub3} >= 40 and {sub4} >=40 and {sub5} >=40  
            then "Pass" else "Fail" end as remarks    from marksheet_catagory_{catagory_addition}  where status = "Published" '''
        
        print("\nProcess 1: Inserting in catagory in catagory_selection table ...")
        cur.execute(ex67)
        print("Process 1 Completed ")
        print("\nProcess 2: Creating Marksheet catagory table ...")
        cur.execute(ex2)
        print("Process 3: Inserting in Marksheet calculation view ...")
        cur.execute(ex33)
        run4 = f"grant select on school_management.Marksheet_Catagory_{catagory_addition} to 'student'"
        run10 = f"grant select on school_management.marksheet_calculation_{catagory_addition} to 'student'"

        cur.execute(run4)
        cur.execute(run10)


        run13 = f"grant select on school_management.marksheet_calculation_{catagory_addition} to 'teacher'"
        cur.execute(run13)
        run33 = f"grant select on school_management.Marksheet_Catagory_{catagory_addition} to 'teacher'"
        cur.execute(run33)

        
        
        
        #----------------------------recording activity

        activity_msg = "Adding new catagory ({}({},{},{},{},{},{}))".format(catagory_addition,sub1,sub2,sub3,sub4,sub5,sub6)
        activity_status = "success"
        cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
        cur.execute(cmd_activity_1)
        mydb.commit()
        print("\nCatagory Successfully added !!!")
      
        #-------------------------------------------------------
    except:
        mydb.rollback()
        print("Error in adding catagory\n no space allowed in subject")
        #----------------------------recording activity
        try:
            activity_msg = "Adding new catagory"
            activity_status = "failed"
            cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
            cur.execute(cmd_activity_1)
            mydb.commit()
        except:
            print("!!!Error in recording activity")
        #-------------------------------------------------------



def update_marks_by_admin():
    subject = input("Enter the subject you want to update marks on: ").capitalize()
    # print(subject)
    student_roll = input("Enter student's roll no: ").upper()
    ex12 = f"Select catagory from registration where s_roll = '{student_roll}'"
    cur.execute(ex12)
    catagory_student= cur.fetchone()
    if(catagory_student == None):
        print("No Such Roll No. Try Again!")
        return
    catagory = catagory_student[0]
    # print(catagory)
    ex13 = f"Select subject1,subject2,subject3,subject4,subject5,subject6 from catagory_selection where catagory = '{catagory}'"
    cur.execute(ex13)
    all_subject_in_catagory = cur.fetchone()
    if (all_subject_in_catagory[-1] == None):
        all_subject_in_catagory = all_subject_in_catagory[:-1]
    # print(all_subject_in_catagory)
    
    if subject in all_subject_in_catagory:
        terminal = input("Which Terminal Exam Marks You Wanna Update? '1' For First Teminal, '2' For Second Terminal, '3' For Third Terminal And 'F' For Final Exam: ").upper()
        if(terminal != '1' and terminal != '2' and terminal != '3'and terminal != 'F'):
            print("No Such Terminal Option. Try Again!")
            return
        ex16 = f"SELECT class from registration where s_roll = '{student_roll}'"
        cur.execute(ex16)
        class_of_student = cur.fetchone()
        if(class_of_student[0] == 11):
            year_of_exam = "2" + student_roll[1:4]
            # print(year_of_exam)
        elif(class_of_student[0] == 12):
            temp_year = str(int(student_roll[1:4]) + 1).zfill(3)
            year_of_exam = "2" + temp_year
            # print(year_of_exam)


        tup1 = (terminal, int(year_of_exam), student_roll)
        ex14 = f"Select terminal,year_of_exam,student_roll_number from Marksheet_Catagory_{catagory} where terminal = '{terminal}' and year_of_exam = {year_of_exam} and student_roll_number = '{student_roll}'"
        cur.execute(ex14)
        fetched = cur.fetchone()
        marks = int(input(f"Enter the {subject} marks: "))
        if(marks>100 or marks < 0):
            print("Marks must be between 0 to 100")
            return
        # print(fetched)
        # print(tup1)
        try:

            if (tup1 == fetched):
                # print("Entry Already Exists!")
                ex15= f"Update Marksheet_Catagory_{catagory} set {subject} = {marks} where student_roll_number = '{student_roll}' and terminal = '{terminal}' and year_of_exam = {year_of_exam} "
                cur.execute(ex15)
            else:
                ex3 = f"INSERT into Marksheet_Catagory_{catagory}(terminal,year_of_exam, student_roll_number) values (%s,%s,%s)"
                cur.execute(ex3,tup1)
                ex15= f"Update Marksheet_Catagory_{catagory} set {subject} = {marks} where student_roll_number = '{student_roll}' and terminal = '{terminal}' and year_of_exam = {year_of_exam} "
                cur.execute(ex15)

            
           
            #----------------------------recording activity
           
            activity_msg = "Updating marks (of {} in {} on {} {} terminal)".format(student_roll,subject,year_of_exam,terminal)
            activity_status = "success"
            cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
            cur.execute(cmd_activity_1)
            mydb.commit()
            print("Marks Updated Successfully")

            #-------------------------------------------------------
        except:
            mydb.rollback()
            print("!!!Error occured while updating ...")
            try:
                activity_msg = "Updating marks (of {} in {} on {} {} terminal)".format(student_roll,subject,year_of_exam,terminal)
                activity_status = "failed"
                cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
                cur.execute(cmd_activity_1)
                mydb.commit()
            except:
                print("!!!Error in recording activity")
            #-------------------------------------------------------
            
    else:
        print("You Donot Have Enough Privilege To Update Marksheet For This Student.\nReason: Student's Catagory Doesnot Have The Subject You Teach.")


def delete_catagory():
    print("The current catagory that our college provides are:")
    print("-----------------------------------------------------")
    run1 = "SELECT * from Catagory_selection"
    cur.execute(run1)
    all_cat = cur.fetchall()
    for cat in all_cat:
        print(cat)
    try:
        catagory = input("Enter the catagory you want to remove from your college: ").upper()
        print("\nProcess 1: Deleting Markscheet table ...")
        run2 = f"Drop table Marksheet_Catagory_{catagory}"
        cur.execute(run2)
        print("Process 1 Completed")
        
        print("\nProcess 2: Deleting Markscheet View ...")
        run2 = f"Drop view Marksheet_Calculation_{catagory}"
        cur.execute(run2)
        print("Process 2 Completed ")
        
        print("\nDeleting Catagory from catagory selection table ...")
        run3 = f"delete from catagory_selection where catagory = '{catagory}'"

        cur.execute(run3),{}
        print("Process 3 Completed ")
     
            
        #----------------------------recording activity
        
        activity_msg = "Deleting catagory ({})".format(catagory)
        activity_status = "success"
        cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
        cur.execute(cmd_activity_1)
        mydb.commit()
        print("\n!!!Catagory Deleted succesfully")
        
        #-------------------------------------------------------
    except:
        mydb.rollback()
        print("Error in Deleting catagory")
                    
        #----------------------------recording activity
        try:
            activity_msg = "Deleting catagory ({})".format(catagory)
            activity_status = "failed"
            cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
            cur.execute(cmd_activity_1)
            mydb.commit()
        except:
            print("!!!Error in recording activity")
        #-------------------------------------------------------


# In[20]:


#assigning and deleting section to teacher ----------------------------------
def assign_section_to_teacher():
    print("------------------------------ASSIGNING SECTION TO TEACHER --------------------------------")
    while True:
        print("enter # to exit")
        id_to_assgn_sec = input("Enter id: ").upper()
        if(id_to_assgn_sec == '#'):
            break
        cmd_assgn_sec_1 = "Select * from teacher_details where teacher_id ='{}'".format(id_to_assgn_sec)
        cur.execute(cmd_assgn_sec_1)
        id_teacher = cur.fetchall() 
        if(id_teacher != []):
            class_assgn_sec = input("Enter Class: ")
            if(class_assgn_sec!='11' and class_assgn_sec != '12'):
                print("Invalid class")
                continue
            faculty_assgn_sec = input("Enter faculty(Science/Management): ").capitalize()
            
            if(faculty_assgn_sec != 'Science' and faculty_assgn_sec != 'Management'):
                print("Invalid faculty")
                continue
            sec_assgn_sec = input("Enter Section: ").upper()
            # if(sec_assgn_sec.isalpha() == False or len(sec_assgn_sec) != 1 ):
            if(sec_assgn_sec != "T1" and sec_assgn_sec != "T2"):
                print("Invalid Section")
                continue
            
            try:
                cmd_asgn_ = "insert into section_teacher values('{}',{},'{}','{}')".format(id_to_assgn_sec,class_assgn_sec,faculty_assgn_sec,sec_assgn_sec)
                cur.execute(cmd_asgn_)
                

                #----------------------------recording activity

                activity_msg = "Assigning section {} of {}({}) to {}".format(sec_assgn_sec,faculty_assgn_sec,class_assgn_sec,id_to_assgn_sec)
                activity_status = "success"
                cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
                cur.execute(cmd_activity_1)
                mydb.commit()
                print("Assigned sucessfully")


                #----------------------------------------------------------
            except:
                print("Error while assigning")
                mydb.rollback()
                #----------------------------recording activity------------------

                try:
                    activity_msg = "Assigning section {} of {}({}) to {}".format(sec_assgn_sec,faculty_assgn_sec,class_assgn_sec,id_to_assgn_sec)
                    activity_status = "failed"
                    cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
                    cur.execute(cmd_activity_1)
                    mydb.commit()
                except:
                    print("!!!Error in recording activity")
                #----------------------------------------------------------


        
            
            
        else:
            print("!!!No id found")
            
def delete_teacher_section_():
    print("Enter\n#$1 to delete all section_teacher record\n2 to delete particular record")
    op_del_assign = input("Enter option: ")
    if(op_del_assign == '#$1'):
        try:
            cur.execute("Delete from section_teacher")
            #----------------------------recording activity

            activity_msg = "Deleting all record section_teacher"
            activity_status = "success"
            cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
            cur.execute(cmd_activity_1)
            mydb.commit()
            print("All record deleted successfully")


            #----------------------------------------------------------
        except:
            print("error while deleting")
            mydb.rollback()
            #----------------------------recording activity------------------

            try:
                activity_msg = "Deleting all record from section_teacher"
                activity_status = "failed"
                cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
                cur.execute(cmd_activity_1)
                mydb.commit()
            except:
                print("!!!Error in recording activity")
             #----------------------------------------------------------


    elif(op_del_assign == '2'):
        while True:
            print("enter # to exit")
            id_to_del_sec = input("Enter id: ").upper()
            if(id_to_del_sec == '#'):
                break
            cmd_del_sec_1 = "Select * from teacher_details where teacher_id ='{}'".format(id_to_del_sec)
            cur.execute(cmd_del_sec_1)
            id_teacher = cur.fetchall() 
            if(id_teacher != []):
                class_del_sec = input("Enter Class: ")
                if(class_del_sec!='11' and class_del_sec != '12'):
                    print("Invalid class")
                    continue
                faculty_del_sec = input("Enter faculty(Science/Management): ").capitalize()

                if(faculty_del_sec != 'Science' and faculty_del_sec != 'Management'):
                    print("Invalid faculty")
                    continue
                sec_del_sec = input("Enter Section: ").upper()
                if(len(sec_del_sec) != 2 ):
                    print("Invalid Section")
                    continue

                try:
                    cmd_asgn_ = "delete from section_teacher where (teacher_id = '{}'and class = {} and faculty = '{}' and assigned_section = '{}')".format(id_to_del_sec,class_del_sec,faculty_del_sec,sec_del_sec)
                    cur.execute(cmd_asgn_)


                    #----------------------------recording activity

                    activity_msg = "Deleting section {} of {}({}) from {}".format(sec_del_sec,faculty_del_sec,class_del_sec,id_to_del_sec)
                    activity_status = "success"
                    cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
                    cur.execute(cmd_activity_1)
                    mydb.commit()
                    print("Deleted successfully")


                    #----------------------------------------------------------
                except:
                    print("!!error while deleting")
                    mydb.rollback()
                    #----------------------------recording activity------------------

                    try:
                        activity_msg = "Deleting section {} of {}({}) from {}".format(sec_del_sec,faculty_del_sec,class_del_sec,id_to_del_sec)
                        activity_status = "failed"
                        cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
                        cur.execute(cmd_activity_1)
                        mydb.commit()
                    except:
                        print("!!!Error in recording activity")
                    #----------------------------------------------------------





            else:
                print("!!!No id found")

    else:
        print("Invalid input")


# In[21]:


#entrance marks insert and updatae
def fill_entranceMarks(data):
    cmd_1 = "update entrance_marks set marks=%s where entrance_roll=%s"
    cur.execute(cmd_1,data)
    mydb.commit()

def enter_entrance_marks():
    
    
    cmd_3 = "Select * from entrance_marks"
    cur.execute(cmd_3)
    roll= cur.fetchall()
    #print(roll)
    try:
        print("enter # to exit")
        for x in roll:

            if x[1]==0:
                while 1:
                    marks_obtained = input("enter marks_obtained by entrance_roll "+str(x[0])+" ")
                    if(marks_obtained == '#'):
                        return
                    if(marks_obtained.isnumeric()):
                        if 0<=int(marks_obtained) and int(marks_obtained)<=100:        
                            break
                    print("Please enter value between 0 and 100 ")
                fill_entranceMarks((marks_obtained,)+(x[0],)) # data is in tupple inside list
                print("successfull inserted")
    except:
        print("Error in inserting entrance marks")
            

            
            
            
            
            
def update_entrance_marks():
    e_roll=input("Enter the roll you want to update: ").upper()
    cmd_3 = "Select entrance_roll from entrance_marks where entrance_roll=%s"
    cur.execute(cmd_3,(e_roll,))
    already_entered= cur.fetchall()
    try:
        if already_entered:
            cmd_4="update entrance_marks set marks = %s where entrance_roll = %s"
            while 1:
                marks_obtained = input("enter marks_obtained by entrance_roll "+str(already_entered[0])+" ")
                if(marks_obtained == '#'):
                    return
                if(marks_obtained.isnumeric()):
                    if 0<=int(marks_obtained) and int(marks_obtained)<=100:        
                        break

                print("Please enter value between 0 and 100 ")
            cur.execute(cmd_4,(marks_obtained,e_roll))
             #----------------------------recording activity

            activity_msg = "Updating entrance marks of {} to {}".format(e_roll,marks_obtained)
            activity_status = "success"
            cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
            cur.execute(cmd_activity_1)
            mydb.commit()
            print("Updated successfully")


            #----------------------------------------------------------


        else:
            print("Roll not found")
    except:
        mydb.rollback()
        
        #----------------------------recording activity------------------

        try:
            activity_msg = "Updating entrance marks of {} to {}".format(e_roll,marks_obtained)
            activity_status = "failed"
            cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
            cur.execute(cmd_activity_1)
            mydb.commit()
        except:
            print("!!!Error in recording activity")
         #----------------------------------------------------------

        


# In[22]:



def show_regis():
    registration_df= pd.read_sql_table("registration",engine)
    print(registration_df)
def show_avail_catagory():
    cat_df= pd.read_sql_table("catagory_selection",engine)
    print(cat_df)
def show_entrance():
    entrance_df= pd.read_sql_table("entrance_form",engine)
    print(entrance_df)
def show_entrance_marks():
    entrance_marks_df= pd.read_sql_table("entrance_marks",engine)
    print(entrance_marks_df)
def show_past_student():
    past_student_df= pd.read_sql_table("past_student",engine)
    print(past_student_df)
def show_teach():
    teach_df= pd.read_sql_table("teacher_details",engine)
    print(teach_df)
def show_marksheet():
    marksheet_df= pd.read_sql_table("marksheet_backup",engine)
    print(marksheet_df)
def recent_activity():
    recent_activity_df= pd.read_sql_query("Select * From activity_record Order By activity_on Desc limit 20",engine)
    print(recent_activity_df)
def marksheet_percentage(cat):
    marksheet_percentage_df= pd.read_sql_query("select * from marksheet_calculation_"+cat+" natural join marksheet_catagory_"+cat,engine)
    print(marksheet_percentage_df)
def section_teach_details():
    section_teacher_details_df= pd.read_sql_table("section_teacher_details",engine)
    print(section_teacher_details_df)    
def old_teach_details():
    old_teach_details_df= pd.read_sql_table("old_teacher_details",engine)
    print(old_teach_details_df)  
    
def show_old_marksheet_analysis():
    old_marksheet_analysis_df= pd.read_sql_table("marksheet_backup_analysis",engine)
    print(old_marksheet_analysis_df)  
    


# In[23]:


def show_info():

    print("Please enter the option from the following items:")
    print("1 to view current student details")
    print("2 to view available catagory")
    print("3 to view entrance form data")
    print("4 to view entrance marks")
    print("5 to view past student data")
    print("6 to view teacher details")
    print("7 to view all past marksheet")
    print("8 to view recent activity done")
    print("9 to view marksheet with marks in each subject")
    print("10 to view section teacher details")
    print("11 to view past teacher details")
    print("12 to view past marksheet analysis")
    print("any other to go back to main menu")



    while 1:
        try:
            option=input()
            selected_option=int(option)
            break;
        except ValueError:
                print("please enter values between 1 to 12")

    if selected_option==1:
        show_regis()
    elif selected_option==2:
        show_avail_catagory()
    elif selected_option==3:
        show_entrance()
    elif selected_option==4:
        show_entrance_marks()
    elif selected_option==5:
        show_past_student()
    elif selected_option==6:
        show_teach()
    elif selected_option==7:
        show_marksheet()
    elif selected_option==8:
        recent_activity()
    elif selected_option==9:
        cmd_see_catagory = "select catagory from catagory_selection"

        cur.execute(cmd_see_catagory)
        all_avai_catagory = cur.fetchall()
        all_cat_list = []
        for avai_catagory in all_avai_catagory:
            all_cat_list.append(avai_catagory[0])

        print("Please enter the marksheet category",all_cat_list)
        cat=input().upper()
        if(all_cat_list.count(cat) == 1):
            marksheet_percentage(cat)
        else:
            print("The selected catagory does not exist or marksheet has not been entered yet")
    elif selected_option==10:
        section_teach_details()
    elif selected_option==11:
        old_teach_details()      
    elif selected_option==12:
        show_old_marksheet_analysis()
    else:
        return
    


# In[24]:



print("----------------------------------------WELCOME TO ADMIN SECTION-----------------------------------------------")
print("!!!Authorized person only. Your every activity is being recorded!!!")
ad_password = input("Enter password: ")
admin_login_cmd = "Select user_id from security_table where user_id='1000' and passwordhash = '{}'".format(ad_password)
cur.execute(admin_login_cmd)
is_pw_right = cur.fetchall()
if(is_pw_right!=[]):
    
    try:
        activity_msg = "Successfully Logged In"
        activity_status = "-"
        cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
        cur.execute(cmd_activity_1)
        mydb.commit()
    except:
        print("!!!Error in recording activity")
    
    
    
    while True:
        print("----------------------------WELCOME TO ADMIN SECTION-------------------------------------------")
        print('''\nEnter
        -----------------------SECTION 1 -----------------------
        1 for declaring end of academic year
        2 for declaring entrance exam
        3 for declaring entrance result
        4 for changing status of any candidate
        5 for transfering all approved student to table
        -----------------------SECTION 2 -----------------------
        6 for messaging
        7 for registering Teacher
        8 to update student teacher detail
        9 to update past student detail
        10 to add catagory
        11 to delete a catagory
        -----------------------SECTION 3 -----------------------
        12 to declare terminal exam
        13 to update terminal marks
        14 to announce terminal result
        ---------------------------------------------------------
        15 to assign section to teacher
        16 to delete assigned section
        ---------------------------------------------------------
        17 insert entance marks
        18 update entrance marks
        ---------------------------------------------------------
        19 view 
        ---------------------------------------------------------
        20 to logout''')

        option_for_admin_ch = '20'
        while True:
            option_for_admin_ch = input("Enter option: ")
            if(option_for_admin_ch == '20' or option_for_admin_ch == '19' or option_for_admin_ch == '6'):
                break

            suring_option = input("Are you sure you want to proceed(Y/N)").upper()
            if(suring_option == 'Y'):
                break


        try:
            if(option_for_admin_ch =='1'):
                admin_declare_end_of_acedemic_year()
                pass
            elif(option_for_admin_ch =='2'):
                admin_declare_entrance_exam()

            elif(option_for_admin_ch =='3'):
                admin_declare_entrance_result()
            elif(option_for_admin_ch =='4'):
                change_statuscheck_of_candidate()
            elif(option_for_admin_ch =='5'):
                print("\n-----------------------TRANSFER APPROVED STUDENT TO REGISTRATION TABLE -----------------------------")

                print("tranfering...")
                try:
                    transfer_students_into_registration()
                    print("Transformation completed successfully")
                except:
                    print("!!!!Error occur")

            elif(option_for_admin_ch =='6'):

                admin_login_('1000','A')

            elif(option_for_admin_ch =='7'):
                teacher_detail_registration_by_admin()

            elif(option_for_admin_ch =='8'):
                #admin update student teacher plus delete
                print("Type:\n3 to update student record\n4 to update teacher record\n5 to delete student record\n6 to delete teacher record\nany other to exit")
                up_stu_tch = input("enter option: ")
                if(up_stu_tch == '3'):
                    update_student_record()
                elif(up_stu_tch == '4'):
                    update_teacher_record()
                elif(up_stu_tch == '5'):
                    delete_student_from_registration()
                elif(up_stu_tch == '6'):
                    delete_teacher_from_teacher_details()
            elif(option_for_admin_ch =='9'):
                update_past_student_record()
            elif(option_for_admin_ch =='10'):
                catagory_creation()

            elif(option_for_admin_ch =='11'):
                delete_catagory()

            elif(option_for_admin_ch =='12'):
                print("---------------------")
                print("Delaring Exam.......")
                print("---------------------")


                #Grant the permission to teacher to update on marksheet
                print("-------------------------------------------------")
                print("Granting Permission To Teacher To Update Marks")
                print("-------------------------------------------------")

                ex1001 = "SELECT catagory from Catagory_selection"
                cur.execute(ex1001)
                catagories = cur.fetchall()
                try:

                    for catagory in catagories:
                        run3 = f"grant select,insert,update on school_management.Marksheet_Catagory_{catagory[0]} to 'teacher'"
                        cur.execute(run3)

                    print("Granting Select, Insert And Update On Teacher, Succeed.")
                    #----------------------------recording activity
                    try:
                        activity_msg = "Declaring Terminal Exam"
                        activity_status = "success"
                        cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
                        cur.execute(cmd_activity_1)
                        mydb.commit()
                    except:
                        print("!!!Error in recording activity")
                    #-------------------------------------------------------
                    print("Sending message to students regarding exam.")
                    msg_dec = '''Dear student, \n We would like to inform you that your exam routine has been published.\nBest of luck  '''
                    msg_to_all_stu(msg_dec)
                except:

                    print("Granting Failed.")
                    #----------------------------recording activity
                    try:
                        activity_msg = "Declaring Terminal Exam"
                        activity_status = "failed"
                        cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
                        cur.execute(cmd_activity_1)
                        mydb.commit()
                    except:
                        print("!!!Error in recording activity")
                    #-------------------------------------------------------






            elif(option_for_admin_ch =='13'):
                update_marks_by_admin()

            elif(option_for_admin_ch =='14'):
                print("----------------------")
                print("RESULT ANNOUNCED!")
                print("----------------------")

                print("Revoking The Permission To Update...")
                ex1001 = "SELECT catagory from Catagory_selection"
                cur.execute(ex1001)
                catagories = cur.fetchall()
                try:

                    for catagory in catagories:
                        # print(catagory[0])
                        run3 = f"revoke insert,update on school_management.Marksheet_Catagory_{catagory[0]} from 'teacher'"
                        cur.execute(run3)


                    print("Permission to revoke update on student's Marksheet Success.")
                except:
                    mydb.rollback()
                    try:
                        activity_msg = "Declaring Terminal Exam Result"
                        activity_status = "failed"
                        cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
                        cur.execute(cmd_activity_1)
                        mydb.commit()
                    except:
                        print("!!!Error in recording activity")
                    print("Revoke Failed!")
                    continue
                    



                try:

                    for catagory in catagories:

                        run12 = f"update marksheet_catagory_{catagory[0]} set status = 'Published'"
                        cur.execute(run12)





                    #----------------------------recording activity

                    activity_msg = "Declaring Terminal Exam Result"
                    activity_status = "success"
                    cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
                    cur.execute(cmd_activity_1)
                    mydb.commit()
                    print("Now Students Can View Their Marksheet.")

                    #-------------------------------------------------------


                    print("Sending message to students regarding result.")
                    msg_rel = '''Dear student, \n We would like to inform you that your exam result has been published.\nCheck your marksheet on your account.'''
                    msg_to_all_stu(msg_rel)

                except:
                    print("Granting Permission To Student To View Marksheet Failed.")
                    mydb.rollback()
                    #----------------------------recording activity
                    try:
                        activity_msg = "Declaring Terminal Exam Result"
                        activity_status = "failed"
                        cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
                        cur.execute(cmd_activity_1)
                        mydb.commit()
                    except:
                        print("!!!Error in recording activity")
                    #-------------------------------------------------------



            elif(option_for_admin_ch =='15'):
                assign_section_to_teacher()


            elif(option_for_admin_ch =='16'):
                delete_teacher_section_()
            
            elif(option_for_admin_ch =='17'):
                enter_entrance_marks()
            
            elif(option_for_admin_ch =='18'):
                update_entrance_marks()
            
            elif(option_for_admin_ch =='19'):
                show_info()



            elif(option_for_admin_ch =='20'):
                print("exited ...")
                try:
                    activity_msg = "Logged out"
                    activity_status = "-"
                    cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
                    cur.execute(cmd_activity_1)
                    mydb.commit()
                except:
                    print("!!!Error in recording activity")
                break
            else:
                print("Invalid Entry")
                
            any_no_use_jst_____12334 = input("Press enter to continue... ")
        except:
            print("Unexpected Error occured!!! Contact Database Administrator")
            #----------------------------recording activity
            try:
                activity_msg = "Unexpected Error !!!"
                activity_status = "failed"
                cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
                cur.execute(cmd_activity_1)
                mydb.commit()
            except:
                print("!!!Error in recording activity")
            #-------------------------------------------------------
        
else:
    print("Incorrect Password")
        
    try:
        activity_msg = "Wrong Password Entered"
        activity_status = "-"
        cmd_activity_1 = "insert into activity_record(activity_by,activity,activity_status) values ('admin','{}','{}')".format(activity_msg,activity_status)
        cur.execute(cmd_activity_1)
        mydb.commit()
    except:
        print("!!!Error in recording activity")
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




