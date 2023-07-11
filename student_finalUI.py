#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector 
import smtplib
import random
from datetime import date
import pandas as pd
import sqlalchemy


mydb = mysql.connector.connect(host="localhost", user="student", password="student", database="school_management")
cur = mydb.cursor()


def fill_entrance_form_table():       
    today = str(date.today())
    #print(today)
    today_date_only = int(today[0:4])
    today_date_only_str = str(today_date_only)
    

    #student fname -------------------------------
    while True:
        student_fname = input("Enter student first name: ").upper()
        f_name_split_list = student_fname.split()
        student_fname = ""
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
            student_fname = f_name_split_list[0]
            break
        elif(len(f_name_split_list) == 2):
            student_fname = f_name_split_list[0]+" "+f_name_split_list[1]
            break     
        else:
            print("Invalid String!!!!!!")
            
    #--------------------------------student lname-        
    while True:
        student_lname = input("Enter student lastname: ").upper()
        l_name_split_list = student_lname.split()
        student_lname = ""
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
            student_lname = l_name_split_list[0]
            break     
        else:
            print("Invalid String!!!!!!")
    
    
    # date of birth -------------------------------
    while True:
        dob_year = input("Enter year of birth(AD): ")
        if(dob_year.isnumeric() == False):
            print("invaid input")
            continue
        elif( int(dob_year)<1970 or int(dob_year)>(int(today_date_only_str)-10)):
            print("invaid input")
            continue
            
            
        dob_month  = input("Enter month of birth: ")
        if (dob_month.isnumeric() == False):
            print("invaid input")
            continue
        elif( int(dob_month)<1 or int(dob_month)>12):
            print("invaid input")
            continue
            
            
        dob_day  = input("Enter day of birth: ")
        if (dob_day.isnumeric() == False):
            print("invaid input")
            continue
        elif( int(dob_day)<1 or int(dob_day)>32):
            print("invaid input")
            continue
       
        dob = dob_year+'-'+dob_month+'-'+dob_day
        break

    #Gender-----------------------------
    while True:
        gender = input("Enter Your Gender(M for Male, F for Female and O for Others): ").upper()
        if(gender != 'M' and gender != 'F' and gender != 'O'):
            print("!!! Invalid input")
            continue
        else:
            break
    
    
    #address ---------------------------
    while True:
        address = input("Enter Your Current Address: ")
        if(len(address)>50):
            print("!!! Invalid input")
            continue
        else:
            break
    
    
    #---------------------------- email-------------------
    while True:
        student_email = input("Enter student mail: ").lower()
        if((student_email.count('@')==1) and (student_email.count('.com')==1) and (len(student_email)>6)):
            break
        print("INVALID EMAIL")
    #-------------------------------- faculty and catagory ----------------------
    while True:
        faculty = input("Enter The Faculty You Want To Study(Science or Management): ")
        # desc1= '''\nCatagory A: Physics    | Chemistry | Computer  | Maths    | English\nCatagory B: Physics    | Chemistry | Biology   | Maths    | English\nCatagory C: Accounting | Business  | Economics | English  | Nepali\nCatagory You Wanna Enroll Into(Type A,B or C): '''
        ex9= "Select catagory,subject1,subject2,subject3,subject4,subject5,subject6 from catagory_selection where faculty = 'Science' and class =11"
        ex10 = "Select catagory,subject1,subject2,subject3,subject4,subject5,subject6 from catagory_selection where faculty = 'Management' and class = 11"
        print(f"\nCatagory description for {faculty} faculty:")

        if faculty.lower() == "science":
            cur.execute(ex9)
            science_cat_desc = cur.fetchall()
            for desc in science_cat_desc:
                print(desc)

            arr = []
            for i in science_cat_desc:
                arr.append(i[0])
                
            if(arr==[]):
                print("No catagory available now")
                return
            
                

            catagory = input(f"Catagory You Wanna Enroll Into{arr}: ").upper()
            if(arr.count(catagory) == 1):
                break
            else:
                print("Invalid input")
                continue
            


        elif faculty.lower() == "management":
            cur.execute(ex10)
            management_cat_desc = cur.fetchall()
            for desc in management_cat_desc:
                print(desc)
            arr = []
            for i in management_cat_desc:
                arr.append(i[0])

            if(arr==[]):
                print("No catagory available now")
                return
            catagory = input(f"Catagory You Wanna Enroll Into{arr}: ").upper()
            if(arr.count(catagory) == 1):
                break
            else:
                print("Invalid input")
                continue
        else:
            print("No Such Faculty In School. Try Again!")
            return
            
        
    
    while True:
        gpa_ = input("Enter Your Grade 10 Gpa: ")
        gpa_test_float = gpa_.replace('.','0',1) #to check float or not

        if(gpa_test_float.isnumeric() == True):


            if((float(gpa_)>=2.0) and (float(gpa_)<=4.0)):
                
                break

            else:
                print("Invalid input\n Gpa should be between 2.0 and 4.0")
                return

        else:
            print("Invalid input!!")
            continue


    #-------------------gaurdain name ----------------------
    while True:
        gname= input("Enter Gaurdain Name:").upper()
        gname_list = gname.split()
        gname = ""
        check_isalp = 0
        for gname_split in gname_list:
            if(gname_split.isalpha()==False):
                check_isalp = 1
        #check string is alphabet or not        
        if(check_isalp == 1):
            print("Invalid String!!!")
            continue
        #put string in proper format    
        if(len(gname_list) == 2):
            gname = gname_list[0]+" "+gname_list[1]
            break

        elif(len(gname_list) == 3):
            gname = gname_list[0]+" "+gname_list[1]+" "+gname_list[2]
            break

        else:
            print("Invalid String!!!!!!")
            continue


        


#gaurdain phone number--------------------------------
    while True:
        gphone= input("Enter Phone Number: ")
        if((len(gphone) == 10) and (gphone.isnumeric() == True) ):
            break
            
        else:
            print("Invalid input!!!")
            continue


    status = "Waiting"

    try:
        op_to_insert = input("Are you sure you want to register(Y/N)").upper()
        if(op_to_insert == 'Y'):
            cmd_eroll_gen = "Select count(entrance_roll) from entrance_form"
            cur.execute(cmd_eroll_gen)
            total_e_form = cur.fetchall()
            e_roll = "E"+today_date_only_str+"-"+str(total_e_form[0][0]+1).zfill(5)       


            command_1 = "Insert into entrance_form values('{}','{}','{}','{}','{}','{}','{}','{}','{}',{},'{}',{},'{}')".format(e_roll,student_fname,student_lname,dob,gender,address,student_email,faculty,catagory,gpa_,gname,gphone,status)
            cur.execute(command_1)
            mydb.commit()
            print("\n\n----------------------------------------------------")
            print("Your exam roll number is: ",e_roll)
            print("----------------------------------------------------")
            print("Form submitted successfully")
        else:
            print("Process Terminated!!!")
    except:
        mydb.rollback()
        print("Error while inserting")



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


# In[2]:


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
        
#
        
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


# In[3]:


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
        

        


# In[4]:


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
        
            


# In[5]:


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
            
        
        
            
        
        
        


# In[6]:


#change password

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

        
    


# In[7]:
#Marksheet View

def see_marksheet(login_id):
    run10 = f"SELECT catagory from registration where s_roll = '{login_id}'"
    cur.execute(run10)
    cat = cur.fetchone()
    run11 = f"SELECT * from catagory_selection where catagory = '{cat[0]}'"
    cur.execute(run11)
    subjects = cur.fetchone()
    if(subjects == None):
        print("Invalid Catagory.")
        return

    manipulate = int("2" + (login_id[1:4]))
    print(f"Your exam year could be: {manipulate} and {manipulate+1}")
    year = int(input("Enter the year you wanna view the result of: "))


    if(year != manipulate and year != manipulate+1):
        print(f"Exam not given for Year {year}.")
        print("Try Again!")
        return

    term = input("Enter the terminal which you want to view result of(1,2,3 or F): ").upper()
    print("---------------------------------------------------------------------------------------")
    if (term != "1" and term != "2" and term != "3" and term != "F"):
        print("Invalid Terminal.")
        return

    run166 = f"Select terminal from marksheet_calculation_{cat[0]} where year_of_exam = {year} and student_roll_number = '{login_id}' and terminal = '{term}'"
    cur.execute(run166)
    ter = cur.fetchone()
    if(ter == None):
        print(f"Result Not Published Yet For Year {year} ,Terminal {term}.")
        return


    run13 = f"SELECT * from marksheet_catagory_{cat[0]}"
    cur.execute(run13)
    marks = cur.fetchone()
    marks = marks[3:-1]
    print(f"\n\nStudent Catagory: {subjects[0]}")
    print(f"Class: {subjects[1]}")
    print(f"Faculty: {subjects[2]}")
    print(f"Terminal: {term}")
    print("\nSUBJECT                                Marks")
    if(subjects[8] == None):
        trunc_subject = subjects[3:-1]
        for i in range(len(trunc_subject)):
            word = trunc_subject[i].ljust(20)
            print(f"{word}                      {marks[i]}")


    else:
        trunc_subject = subjects[3:]
        for i in range(len(trunc_subject)):
            word = trunc_subject[i].ljust(20)
            print(f"{word}                      {marks[i]}")



    print("\n\n")
    query1 = f"Select total_marks_obtained, percentage, remarks from marksheet_calculation_{cat[0]} where student_roll_number = '{login_id}' and terminal = '{term}' and year_of_exam = {year}"
    tab = pd.read_sql_query(query1,engine)
    print(tab)





# In[ ]:


#username="S076-579"
#password="SDDDF"

login = '''

░██████╗████████╗██╗░░░██╗██████╗░███████╗███╗░░██╗████████╗                ██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
██╔════╝╚══██╔══╝██║░░░██║██╔══██╗██╔════╝████╗░██║╚══██╔══╝                ██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
╚█████╗░░░░██║░░░██║░░░██║██║░░██║█████╗░░██╔██╗██║░░░██║░░░                ██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
░╚═══██╗░░░██║░░░██║░░░██║██║░░██║██╔══╝░░██║╚████║░░░██║░░░                ██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
██████╔╝░░░██║░░░╚██████╔╝██████╔╝███████╗██║░╚███║░░░██║░░░                ███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
╚═════╝░░░░╚═╝░░░░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░                ╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝

'''

bye = '''

░██████╗░░█████╗░░█████╗░██████╗░           ██████╗░██╗░░░██╗███████╗██╗██╗
██╔════╝░██╔══██╗██╔══██╗██╔══██╗           ██╔══██╗╚██╗░██╔╝██╔════╝██║██║
██║░░██╗░██║░░██║██║░░██║██║░░██║           ██████╦╝░╚████╔╝░█████╗░░██║██║
██║░░╚██╗██║░░██║██║░░██║██║░░██║           ██╔══██╗░░╚██╔╝░░██╔══╝░░╚═╝╚═╝
╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝           ██████╦╝░░░██║░░░███████╗██╗██╗
░╚═════╝░░╚════╝░░╚════╝░╚═════╝░           ╚═════╝░░░░╚═╝░░░╚══════╝╚═╝╚═╝
'''

while True:
    run_grant = "Show grants"
    cur.execute(run_grant)
    all_grants = cur.fetchall()
    grant_count = 0
    for grant in all_grants:
        if(grant[0].count("`school_management`.`entrance_form`") == 1):
            if(grant[0].count("INSERT") == 1):
                grant_count = 1

    print(login)
    print("Enter 1 to login")
    print("Enter 2 if you have forgotten password")
    if(grant_count == 1):
        print("Enter 3 to sign up to participate in entrance exam")
    print("Enter #9 to exit")
    print()

    login_option=input("Enter your choice: ")
    
    if(login_option == "3" and grant_count == 1):
        try:
            fill_entrance_form_table()
        except:
            print("Unexpected Error Occured.")

    elif (login_option== "1"):
        username=input("Enter your user id: ").upper()
        password=input("Enter password: ")
        check = login_user(username, password)
        login_id = username
        if check:
            print("---------------------------------")
            print(f"You are logged in as: {username}\n")
            runcode1 = f"SELECT fname,lname from registration where s_roll = '{username}'"
            cur.execute(runcode1)
            fullname = cur.fetchone()
            while True:
                print("----------------------------------------------")
                try:
                    print(f"\nWELCOME {fullname[0]} {fullname[1]}\n")
                except:
                    print("Unknown Error. Try Again!")
                    break
                print("----------------------------------------------")
                print("Enter 1 to change password")
                print("Enter 2 to see your terminal marksheets")
                print("Enter 3 to send or view message")
                print("Enter 4 to logout")
                option=input("Enter your choice: ")

                if (option=="1"):
                    try:
                        change_password_acc(login_id)  
                        print("-------------------------------------")
                    except:
                        print("Unexpected Error Occured.")          
                elif (option=="2"):
                    try:
                        engine = sqlalchemy.create_engine('mysql+pymysql://student:student@localhost/school_management')
                        see_marksheet(login_id)
                    except:
                        print("Unexpected Error Occured.")
                elif (option=="3"):
                    try:
                        message_send_receive(login_id,'S')
                    except:
                        print("Unexpected Error Occured.")
                elif (option=="4"):
                    print("You Have Logged Out From Your Account")
                    break
                else:
                    print("Please enter the available options 1, 2, 3, 4")
            
                
    elif (login_option=="2"):
        try:
            forget_password_acc('S')
        except:
            print("Unexpected Error Occured.")
        
        
    elif (login_option=="#9"):
        print(bye)
        exit()
    else:
        print("INVALID OPTION!!")





