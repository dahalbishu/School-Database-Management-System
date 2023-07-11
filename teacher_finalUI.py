#!/usr/bin/env python
# coding: utf-8

# <h1>Setup and login func</h1>

# In[3]:


import mysql.connector as sql_data
import random
import smtplib
import pandas as pd
import sqlalchemy

mydb = sql_data.connect(host="localhost", user="teacher", password="teacher", database="school_management")
cur = mydb.cursor()

def login_user(username,password):
    runcode = f"select * from security_table where user_id= '{username}' and passwordhash= '{password}'"
    cur.execute(runcode)
    results = cur.fetchall()
    # if results:
    if (len(results) != 0):
        print("Login success!!")
        return True

    else:
        print("Incorrect user id or password. Try Again!")
        return False


# <h1>Forget Password</h1>

# In[3]:


def send_otp_to_mail(otp_send_str,email_to):
    #establis connection 1st part and send mail 2nd part
    
    mail_to = '''subject: School Login Verification \n\nDear Sir/Madam,\n
        Please do not reply to this email.This mailbox is not monitored and you will not receive a response.
        Note: Donot share this code with anyone else. 
        Your verificaton OTP is :{}'''.format(otp_send_str)
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('sthaaakash111@gmail.com','fbqgwjlvnuefpous')
        #securesally@gmail.com
        
        #send mail
        try:
            server.sendmail('dahalbishwambhar@gmail.com',email_to,mail_to)
            print("Check your mail.")
        except:
            print("failed to send email")
        
    except: 
        print("No connection establish")
        
        
def forget_password_acc(logintype):
    check_id_type = 0
    login_id_fpw = input("Enter ID: ").upper()
    #check id available
    if(logintype=='T'):
        cmd_fpwd_1 = "Select teacher_id,email from teacher_details where teacher_id = '{}'".format(login_id_fpw)
        cur.execute(cmd_fpwd_1)
        id_found = cur.fetchall()
        if(id_found == []):
            print("No such id found!!!")
            return
        else:
            check_id_type = 1
    if(logintype=='S'):
        cmd_fpwd_2 = "Select s_roll,email from registration where s_roll = '{}'".format(login_id_fpw)
        cur.execute(cmd_fpwd_2)
        id_found = cur.fetchall()
        if(id_found == []):
            print("No such id found")
            return
        else:
            check_id_type = 1
    #generate otp and change section        
    if(check_id_type==1):
        otp_send_int = random.randint(100000,999999)
        otp_send_str = str(otp_send_int)
        
        print("Sending to mail ... ")
        send_otp_to_mail(otp_send_str,id_found[0][1])#send opt
        
        otp_receive = input("Enter otp: ")
        
        if(otp_send_str == otp_receive):
            while True:
                password_change = input("Enter new password: ")
                if(len(password_change) > 5 and len(password_change)<=8 and password_change.count(' ') == 0): 
                    password_change_re = input("ReEnter password: ")
                    if(password_change_re == password_change):
                        try:
                            cmd_chngpw_1="update security_table set passwordhash = '{}' where user_id = '{}'".format(password_change,login_id_fpw)
                            cur.execute(cmd_chngpw_1)
                            mydb.commit()
                            print("Password updated successfully")
                        except:
                            print("Unexpected Error occur!!! Please Try latter")
                        return
                        
                            
                    else:
                        print("Donot match with new entered password")
                        continue
                    
                else:
                    print("!!!password should between length of 5 and  8")
                    continue
                
        else:
            print("Wrong OTP!!!")
            return
        


# <h1>Insert into marksheet</h1>

# In[4]:





def insert_marks_by_teacher(loginid_tech):
        
    ex11 = f"SELECT department from teacher_details where teacher_id = '{loginid_tech}'"
    cur.execute(ex11)
    teacher_subject = cur.fetchone()
    subject = teacher_subject[0]
    # print(subject)
    
    cmd__21 = "Select catagory,subject1,subject2,subject3,subject4,subject5,subject6 from catagory_selection"
    cur.execute(cmd__21)
    cat_of_cat = cur.fetchall()
    cat_where_dept_lies = []
    #print(cat_of_cat)
    #store all catagory where department lies
    for cat_of_ in cat_of_cat:
        if(cat_of_.count(subject) == 1):
            cat_where_dept_lies.append(cat_of_[0])
    #list to tuple   

    if(len(cat_where_dept_lies)==1):
        cat_where_dept_lies_tup = "('"+cat_where_dept_lies[0]+"')"
    else:

        cat_where_dept_lies_tup = tuple(cat_where_dept_lies)
    #print(cat_where_dept_lies_tup)



    
    
    
    
    get_terminal = input("Which Terminal Exam Marks You Wanna Update? '1' For First Teminal, '2' For Second Terminal, '3' For Third Terminal And 'F' For Final Exam: ").upper()
    
    ex100 = "Select s_roll from registration where catagory in{}".format(cat_where_dept_lies_tup)
    cur.execute(ex100)
    allstu = cur.fetchall()   
    #print(allstu)
    
    
    start_stu = input("Enter starting roll no to update marks: ").upper()
    print("Enter # to stop entering marks")
    start_stu_check = 0
    for stu_one_by_one in allstu:
        
        
        student_roll = stu_one_by_one[0]
        if(student_roll==start_stu):
            start_stu_check = 1
        if(start_stu_check == 0):
            continue
        
        print("\nRoll no: ",student_roll)
        
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
            terminal = get_terminal
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
            ex14 = f"Select terminal,year_of_exam,student_roll_number,{subject} from Marksheet_Catagory_{catagory} where terminal = '{terminal}' and year_of_exam = {year_of_exam} and student_roll_number = '{student_roll}'"
            cur.execute(ex14)
            fetched = cur.fetchall()
            while True:
                marks = input(f"Enter the {subject} marks: ")
                if(marks == '#'):
                    print("Inserting marks completed...")
                    return
                if(marks.isnumeric() == True):
                    marks = int(marks)
                    if(marks>=0 and marks<=100):
                        marks = int(marks)
                        break
                    else:
                        print("Invaid value")
                else:
                    print("Invaid value")
                    
            #print(fetched)
            #print(tup1)

            if (fetched == []):
                ex3 = f"INSERT into Marksheet_Catagory_{catagory}(terminal,year_of_exam, student_roll_number) values (%s,%s,%s)"
                cur.execute(ex3,tup1)
                ex15= f"Update Marksheet_Catagory_{catagory} set {subject} = {marks} where student_roll_number = '{student_roll}' and terminal = '{terminal}' and year_of_exam = {year_of_exam} "
                cur.execute(ex15)
            elif(fetched[0][3] == 0):
                #print("im this")
                ex15= f"Update Marksheet_Catagory_{catagory} set {subject} = {marks} where student_roll_number = '{student_roll}' and terminal = '{terminal}' and year_of_exam = {year_of_exam} "
                cur.execute(ex15)
                
            else:
                print("Already Entered Perviously")

            mydb.commit()
        else:
            print("You Donot Have Enough Privilege To Update Marksheet For This Student.\nReason: Student's Catagory Doesnot Have The Subject You Teach.")

    print("Inserting marks Section Ended...")






# <h1>Message</h1>

# In[5]:


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
        

        
    


# In[6]:


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
        
            


# In[7]:


# Messaging section  for teacher and student
def message_send_receive(login_user,login_type):
    #including catagory
    if(login_type == 'S'):
        cmd_msg_10 = "Select catagory from registration where s_roll = '{}'".format(login_user)
        cur.execute(cmd_msg_10)
        cat_of_stu = cur.fetchall()
        cat_of_student = cat_of_stu[0][0]
        #print(cat_of_student)
        #commnad to select all subject
        cmd_msg_11 = "Select subject1,subject2,subject3,subject4,subject5,subject6 from catagory_selection where catagory = '{}'".format(cat_of_student)
        cur.execute(cmd_msg_11)
        cat_sub = cur.fetchall()
        cat_subject = cat_sub[0]
        #print(cat_subject)
        #tup to list
        cat_subject_list = list(cat_subject)
        #remove none
        for count_i in range(0,cat_subject_list.count(None)):
            cat_subject_list.remove(None)
        #list to tuple    
        cat_subject_tup = tuple(cat_subject_list)
        # print(cat_subject_tup)
        
    
    
    
    elif(login_type == 'T'):
        cat_where_dept_lies = [] #variable to story catagory where department lies
        cmd_msg_20 = "Select department from teacher_details where teacher_id = '{}'".format(login_user)
        cur.execute(cmd_msg_20)
        dept_of_teach = cur.fetchall()
        dept_of_teacher = dept_of_teach[0][0]
        #print(dept_of_teacher)
        #select all catagory
        cmd_msg_21 = "Select catagory,subject1,subject2,subject3,subject4,subject5,subject6 from catagory_selection".format(login_user)
        cur.execute(cmd_msg_21)
        cat_of_cat = cur.fetchall()
        #print(cat_of_cat)
        #store all catagory where department lies
        for cat_of_ in cat_of_cat:
            if(cat_of_.count(dept_of_teacher) == 1):
                cat_where_dept_lies.append(cat_of_[0])
        #print(cat_where_dept_lies)
        #list to tuple
        if(len(cat_where_dept_lies)==1):
            cat_where_dept_lies_tup = "('"+cat_where_dept_lies[0]+"')"
        else:
            
            cat_where_dept_lies_tup = tuple(cat_where_dept_lies)
        #print(cat_where_dept_lies_tup)
            
            
                
        
        
        

        #---------------------------------------------------------------------------------------------------------
        
    
    
    
    while True:
        get_to_whome =[] #variable to store all stu or teacher id

        print("\n\n--------------------------------MESSAGE SECTION ------------------------------------")
        msg_cmd_1 = "Select * from message_table where sender_id = '{}' or receiver_id ='{}'".format(login_user,login_user) #select all message by login_user
        cur.execute(msg_cmd_1)   
        all_msg = cur.fetchall()
        
        
        #to display all message status
        get_my_message_status(login_user,all_msg)
        
        
        
        id_all_msg = [] # for storing message with sepcific user
        
        
        #input id/name
        
        select_id_for_msg = input("Select id for messaging and other keyword for geting id: ").upper()
        
        
        # exiting by # 
        if(select_id_for_msg =='#'):
            print("Exited...")
            break
        
        
        #develop susgesting name and id
        
        
        if(select_id_for_msg.isalpha() and login_type== 'S' ):
            msg_cmd_8 = "select teacher_id,fname,lname,department from teacher_details where (fname like '{}%' or lname like '{}%'or department = '{}') and (department in{})".format(select_id_for_msg,select_id_for_msg,select_id_for_msg,cat_subject_tup)
            
            #print(msg_cmd_8)
            cur.execute(msg_cmd_8)
            get_sug_id = cur.fetchall()
            
            print("\n")
            
            if(get_sug_id == []):
                print("No person with such name found")
            else:
                print("Name and id are:")
            
            for sugg_id in get_sug_id:
                
                print("{} {} ({}) ({})".format(sugg_id[1],sugg_id[2],sugg_id[0],sugg_id[3]))
            continue
            
        if(select_id_for_msg.isalpha() and login_type== 'T' ):
            msg_cmd_8 = "select s_roll,fname,lname,class from registration where (fname like '{}%' or lname like '{}%') and (catagory IN{})".format(select_id_for_msg,select_id_for_msg,cat_where_dept_lies_tup)
            #print(msg_cmd_8)
            cur.execute(msg_cmd_8)
            get_sug_id = cur.fetchall()
            print("\n")
            
            if(get_sug_id == []):
                print("No person with such name found")
            else:
                print("Name and id are:")            
            
            for sugg_id in get_sug_id:
                
                print("{} {} ({}) class:{}".format(sugg_id[1],sugg_id[2],sugg_id[0],sugg_id[3]))
            continue

        
        
        
            
        # develop condition for stu-teacher and teacher to stu msg only    
        if(login_type == 'S'):   
            #select detail of id entered from teacher details
            msg_cmd_2 = "select teacher_id,fname,lname from teacher_details where teacher_id = '{}' and department IN{}".format(select_id_for_msg,cat_subject_tup)
            #print(msg_cmd_2)
            cur.execute(msg_cmd_2)
            get_to_whome = cur.fetchall()
        if(login_type == 'T'):
            msg_cmd_2 = "select s_roll,fname,lname from registration where s_roll = '{}' and catagory IN{}".format(select_id_for_msg,cat_where_dept_lies_tup)
            #print(msg_cmd_2)
            cur.execute(msg_cmd_2)
            get_to_whome = cur.fetchall()
            
        
        #check type of id called
        if(select_id_for_msg == '1000'):
            receiver_id = '1000'
            receiver_fname = 'admin'
            receiver_lname = ' '
            
            for all_msg_ in all_msg:
                if (all_msg_[1] == receiver_id or all_msg_[2] == receiver_id):
                    id_all_msg.append(all_msg_)
                    
            
            message_box(login_user,receiver_id,receiver_fname,receiver_lname,id_all_msg) # send detail and call msg box
        
        elif(get_to_whome == []):
            print("No ID found!!!!")
        elif(select_id_for_msg == get_to_whome[0][0]):
            receiver_id = get_to_whome[0][0]
            receiver_fname = get_to_whome[0][1]
            receiver_lname = get_to_whome[0][2]
            for all_msg_ in all_msg:
                
                if (all_msg_[1] == receiver_id or all_msg_[2] == receiver_id):
                    id_all_msg.append(all_msg_)
            message_box(login_user,receiver_id,receiver_fname,receiver_lname,id_all_msg)
            
        

#Change password
def change_password_acc(login_id):
    cur_pw = input("Enter current password: ")
    
    cmd_chgpw_1 = "Select passwordhash from security_table where user_id = '{}'".format(login_id)
    cur.execute(cmd_chgpw_1)
    curpass = cur.fetchall()
    if("bytearray(b'{}')".format(cur_pw) == str(curpass[0][0])):
        
        while True:
            password_change = input("Enter new password: ")
            if(len(password_change) > 5 and len(password_change)<=8 and password_change.count(' ') == 0): 
                password_change_re = input("Re-enter password: ")
                if(password_change_re == password_change):
                    try:
                        cmd_chngpw_1="update security_table set passwordhash = '{}' where user_id = '{}'".format(password_change,login_id)
                        cur.execute(cmd_chngpw_1)
                        mydb.commit()
                        print("Password updated successfully.\n")
                    except:
                        print("Unexpected Error occur!!! Please Try late.\nr")
                    return


                else:
                    print("Donot match with new entered password.\n")
                    continue

            else:
                print("Warning: Password should be between length of 5 and 8.\n")
                continue


    else:
        print("Incorrect Password!!!")

        
        
        
        
        


# <h1>UI code</h1>

# In[ ]:


login = ''' 

████████╗███████╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░           ██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██║░░██║██╔════╝██╔══██╗           ██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
░░░██║░░░█████╗░░███████║██║░░╚═╝███████║█████╗░░██████╔╝           ██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
░░░██║░░░██╔══╝░░██╔══██║██║░░██╗██╔══██║██╔══╝░░██╔══██╗           ██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
░░░██║░░░███████╗██║░░██║╚█████╔╝██║░░██║███████╗██║░░██║           ███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝           ╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝
'''

bye = '''

░██████╗░░█████╗░░█████╗░██████╗░           ██████╗░██╗░░░██╗███████╗██╗██╗
██╔════╝░██╔══██╗██╔══██╗██╔══██╗           ██╔══██╗╚██╗░██╔╝██╔════╝██║██║
██║░░██╗░██║░░██║██║░░██║██║░░██║           ██████╦╝░╚████╔╝░█████╗░░██║██║
██║░░╚██╗██║░░██║██║░░██║██║░░██║           ██╔══██╗░░╚██╔╝░░██╔══╝░░╚═╝╚═╝
╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝           ██████╦╝░░░██║░░░███████╗██╗██╗
░╚═════╝░░╚════╝░░╚════╝░╚═════╝░           ╚═════╝░░░░╚═╝░░░╚══════╝╚═╝╚═╝
'''
engine = sqlalchemy.create_engine('mysql+pymysql://teacher:teacher@localhost/school_management')

while True:
    print(login)
    print("Enter 1 for login")
    print("Enter 2 if you have forgotten password/reset password")
    print("Enter 3 to exit")
    print()

    login_option=input("Enter your choice: ")
    
    if (login_option== "1"):
        username=input("Enter your user id: ").upper()
        password=input("Enter password: ")
        check = login_user(username, password)
        login_id = username
        if check:
            print("---------------------------------")
            print(f"You are logged in as: {username}\n")
            runcode1 = f"SELECT fname,lname from teacher_details where teacher_id = '{username}'"
            cur.execute(runcode1)
            fullname = cur.fetchone()
            while True:
                run_catagory = "SELECT catagory from catagory_selection"
                cur.execute(run_catagory)
                get_catagory = cur.fetchall()
                # print(get_catagory)
                length_catagory = len(get_catagory)
                # print(length_catagory)
                run_grant= "show grants"
                cur.execute(run_grant)
                grant_teacher = cur.fetchall()
                grant_count = 0
                i=0
                while i<length_catagory:
                    for grant in grant_teacher:
                        # print(grant)
                        # print(get_catagory[i][0])
                        if(grant[0].count(f"`school_management`.`marksheet_catagory_{get_catagory[i][0].lower()}`") == 1):
                            if(grant[0].count("INSERT") == 1):
                                grant_count += 1

                    i += 1
            
                print("----------------------------------------------")
                try:
                    print(f"\nWELCOME {fullname[0]} {fullname[1]}\n")
                except:
                    print("Unknown Error Occured!")
                    break
                print("----------------------------------------------")
                print("Enter 1 to change password")
                print("Enter 2 to view all students marksheet based on catagory")
                print("Enter 3 to send or view message")
                if (grant_count == length_catagory):
                    print("Enter 4 to update student's terminal marksheet")
                print("Enter #9 to logout")

                option=input("Enter your choice: ")

                if (option=="1"):
                    try:
                        change_password_acc(login_id)  
                        print("-------------------------------------")
                    except:
                        print("Some Error Occured While Trying To Change Password.")
                elif(option=="4" and grant_count == length_catagory):
                    try:
                        insert_marks_by_teacher(login_id)
                    except:
                        print("Error Occured!")


                elif (option=="2"):
                    try:
                        cat = input("Enter the catagory you want to view marksheet of(e.g. A or B or ...): ")
                        quer = f"Select * from marksheet_calculation_{cat}"
                        # marksheet_view = pd.read_sql_table(f"marksheet_calculation_{cat}", engine)
                        marksheet_view = pd.read_sql_query(quer,engine)

                        print(marksheet_view)
                    except:
                        print("Cannot display marksheet right now.")
                elif (option=="3"):
                    try:
                        message_send_receive(login_id,'T')
                    except:
                        print("Error On Meessaging System")
                elif (option=="#9"):
                    print("You Have Logged Out From Your Account")
                    break
                else:
                    print("Please enter the available options 1, 2, 3, 4")
            
                
    elif (login_option=="2"):
        try:
            forget_password_acc('T')
        except:
            print("Maybe You Dont Have Stable Internet.")
        
        
    elif (login_option=="3"):
        print(bye)
        exit()
    else:
        print("INVALID OPTION!!")









