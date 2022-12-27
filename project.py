import mysql.connector as sqltor
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
con=sqltor.connect(host="localhost",user="root",password="parthiv9221",database='t1')
cur=con.cursor()

cur.execute('use t1')

def menutour():
    print("""
    
##==========================================================================##  
||                                                                          ||
||                   CHOOSE ONE OF THE GIVEN OPTION :-                      ||
||__________________________________________________________________________||                                    
||                                                                          ||
||                     1  Lusail---->5000                                   ||
||                     2. Cornice---->1000                                  ||                    
||                     3. Dukhan---->10000                                  ||                    
||                     4. Aqua Park---->20000                               ||                    
||                     5. Doha Downtown--->1000                             ||                   
||                     6. City Skylines--->5000                             ||                  
||                                                                          ||                   
##==========================================================================##
""")

def menuextras():
    print("""
    
##==========================================================================##  
||                                                                          ||
||                   CHOOSE ONE OF THE GIVEN OPTION :-                      ||
||__________________________________________________________________________||                                    
||                                                                          ||
||                     1  indoors---->5000                                  ||
||                     2. outdoors---->1000                                 ||                    
||                     3. pool and spa---->10000                            ||                    
||                     4. laundary---->20000                                ||                    
||                     5. wheel chair assiatance--->1000                    ||                   
||                     6. Guide--->5000                                     ||                  
||                                                                          ||                   
##==========================================================================##
""")


def menubookroom():
    print("""
    
##==========================================================================##  
||                                                                          ||
||                   CHOOSE ONE OF THE GIVEN OPTION :-                      ||
||__________________________________________________________________________||                                    
||                                                                          ||
||                     1  Delux size---->15000                              ||
||                     2. King size---->100000                              ||                    
||                     3. Queen size---->5000                               ||                    
||                     4. Master bed---->3000                               ||                    
||                     5. Double bed --->2000                               ||                   
||                     6. single--->1000                                    ||                  
||                                                                          ||                   
##==========================================================================##
""")


def menurestraunt():
    print("""
    
##==========================================================================##  
||                                                                          ||
||                   CHOOSE ONE OF THE GIVEN OPTION :-                      ||
||__________________________________________________________________________||                                    
||                                                                          ||
||                     1  Indian Cuisine---->15000                          ||
||                     2. Italian---->100000                                ||                    
||                     3. Continental---->5000                              ||                    
||                     4. Thai Cuisine---->3000                             ||                    
||                     5. Buffet--->5000                                    ||                   
||                     6. Chinese--->1000                                   ||                  
||                                                                          ||                   
##==========================================================================##
""")



def upd():
    print("""
    
##==========================================================================##  
||                                                                          ||
||                   PLEASE SELECT THE UPDATION :-                          ||
||__________________________________________________________________________||                                    
||                                                                          ||
||                     1.To update Name                                     ||
||                     2.To update Age                                      ||                    
||                     3.To update Gender                                   ||                    
||                     4.To update phone                                    ||                    
||                     5.To update email                                    ||                   
||                     6.To exit                                            ||                                                                                            
##==========================================================================##
""")

def menupay():
    print("""
    
##==========================================================================##  
||                                                                          ||
||                             WE ACCEPT                                    ||
||__________________________________________________________________________||                                    
||                                                                          ||
||                     1  CREDIT CARD                                       ||
||                     2. DEBIT CARD                                        ||                    
||                     3. INTERNET BANKING                                  ||                    
||                     4. CASH                                              ||                    
||                     5. PAYTM                                             ||                   
##==========================================================================##
""")

def mainmenu():
     print("""
    
##==========================================================================##  
||                                                                          ||
||                     CHOOSE ONE OF THE GIVEN OPTION :-                    ||
||__________________________________________________________________________||
||                                                                          ||
||                         1. REGISTER YOURSELF                             ||
||                         2. BOOK A ROOM                                   ||
||                         3. RESTRAUNT                                     ||
||                         4. EXTRAS                                        ||
||                         5. TOUR AND TRAVELS                              ||
||                         6. DELETION                                      ||
||                         7. TO SEE REGISTRED CUTOMERS                     ||
||                         8. BILL PAYMENT                                  ||
||                         9. TERMS AND CONDITIONS                          ||
||                         10.EXIT                                          ||     
||                                                                          ||
##==========================================================================##
""")

def submenu():
    print("""
    
##==========================================================================##  
||                                                                          ||
||                             SELECT YOUR CHOICE                           ||
||__________________________________________________________________________||                                    
||                                                                          ||
||                     1  TO REGISTER                                       ||
||                     2. TO UPDATE THE REGISTERED DETAILS                  ||                    
||                     3. TO VIEW THE DETAILS OF THE EXISTING CUSTOMERS     ||
||                     4. EXIT                                              ||                   
##==========================================================================##
""") 

def thankyou():
    print("\n"
              "      \n"
              "   ##======================================================##\n"
              "   || _____        ___                          ___        ||\n"
              "   ||   |   |   | |   | |\   | |  /      |   | |   | |   | ||\n"
              "   ||   |   |___| |___| | \  | |_/       |___| |   | |   | ||\n"
              "   ||   |   |   | |   | |  \ | | \           | |   | |   | ||\n"
              "   ||   |   |   | |   | |   \| |  \       ___| |___| |___| ||\n"
              "   ##======================================================##\n"
              "\n")
    
def welcome():
    print("""  
  
               ___       ___   ___            ___     
     |      | |    |    |   | |   | |\    /| |    
     |  /\  | |__  |    |     |   | | \  / | |__   
     | /  \ | |    |    |     |   | |  \/  | |       
     |/    \| |___ |___ |___| |___| |      | |___      
     _________________________________________________  
  
    
    """)
    

def notreg():
    print("""
    
##==========================================================================##  
||                                                                          ||
||                       THE USER IS NOT REGISTERED                         ||                                                   
||           PLEASE REGISTER WITH US TO CONTINUE ENJOYING THE SERVICES      ||                   
##==========================================================================##
""")
    
def existreg():
    print("""
    
##==========================================================================##  
||                                                                          ||
||                      THE USER IS ALREADY REGISTERED WITH US              ||                                                   
||                          PLEASE CHOOSE ANY OTHER OPTION                  ||                   
##==========================================================================##
""")

def menudelete():
    print("""
    
##==========================================================================##  
||                                                                          ||
||                     PLEASE SELECT THE DELETION :-                        ||
||__________________________________________________________________________||                                    
||                                                                          ||
||                     1.To delete details from client table                ||
||                     2.To delete details from bookroom table              ||                    
||                     3.To delete details from restraunt table             ||                    
||                     4.To delete details from tourism table               ||                    
||                     5.To delete details from extras table                ||                   
||                     6.To exit                                            ||                                                                                            
##==========================================================================##
""")

def viewdetails():
    print("""
    
##==========================================================================##  
||                                                                          ||
||                                  DETAILS                                 ||                                                   
||                                                                          ||                   
##==========================================================================##
""") 

def menubill():
    print("""
    
##==========================================================================##  
||                                                                          ||
||                             BILL CALCULATOR                              ||                                                   
||                                                                          ||                   
##==========================================================================##
""") 

def menuprofit():
    print("""
    
##==========================================================================##  
||                                                                          ||
||                             SELECT YOUR CHOICE                           ||
||__________________________________________________________________________||                                    
||                                                                          ||
||                     1  TO GET INVOICE                                    ||
||                     2. TO VIEW MARKET ANALYSIS                           ||                    
||                     3. EXIT                                              ||                   
##==========================================================================##
""") 

def login():
    print("""
    
##==========================================================================##  
||                                                                          ||
||                             SELECT YOUR CHOICE                           ||
||__________________________________________________________________________||                                    
||                                                                          ||
||                    1   IF YOU ARE A ADMIN                                ||
||                    2.  IF YOU ARE A EMPLOYEE                             ||                    
||                    3.  EXIT                                              ||                   
##==========================================================================##
""") 

def adminmenu():
    print("""
    
##==========================================================================##  
||                                                                          ||
||                             SELECT YOUR CHOICE                           ||
||__________________________________________________________________________||                                    
||                                                                          ||
||                    1   TO VIEW MARKET ANALYSIS                           ||
||                    2.  TO VIEW DETAILS OF EMPLOYEES                      ||                    
||                    3.  EXIT                                              ||                   
##==========================================================================##
""") 

def menuitemcode():
    print("""
    
##==========================================================================##  
||                                    |                                     ||
||       LABEL                        |          ITEM CODE                  ||
||____________________________________|_____________________________________||                                    
||                                    |                                     ||
||       BOOKROOM                     |               B/b                   ||
||       RESTRAUNT                    |               R/r                   ||                    
||       EXTRAS                       |               E/e                   ||                    
||       TOURISM                      |               T/t                   ||                                                                                                              
##==========================================================================##
""")

def termsandconditons():
    print("""
    
##==========================================================================##  
||                                                                          ||
||                             TERMS AND CONDITIONS                         ||                                                   
||                                                                          ||                   
##==========================================================================##
""") 
   
    print('''
          
1. Hotel rooms are rented for hotel days.

2. A hotel day starts at 2:00 p.m. on the day of arrival and ends at 12:00 a.m. of the following day.
   Failure to check out by 12:00 p.m. will result in an additional fee for extending a hotel day. 
   A charge for the extension until 4:00 p.m. amounts to PLN 80.00,
   after 4:00 p.m. the hotel will charge for an additional hotel day.

3. The hotel reserves the right to pre-authorize your credit card upon check-in 
   or collect a fee for the entire stay in the form of a cash deposit.

4. In case the guest fails to appear in the hotel by 6 p.m. of the accommodation day despite making a reservation, 
   the fee for the room shall be charged by the hotel.

5. The hotel guest cannot hand over a room to third persons, 
   even if the period for which the guest paid has not yet expired.

6. Persons who are not checked in the hotel may stay in a hotel room from 07:00 a.m. till 10:00 p.m. 
   Persons staying in a room after 10:00 p.m. must check in the hotel.

7. The hotel may refuse to accept the guests who grossly violated the Hotel Rules and Regulations during the last stay 
   by damaging the hotel's or guests' property or by inflicting damage on other guests, 
   hotel employees or other persons staying in the hotel 
   or in other way violated the stay of other guests or the functioning of the hotel.

8. The hotel accepts guests traveling with pets. 
   Only one pet is allowed per room for an extra charge and the guest bears full responsibility 
   for any damage caused by their pet. Pets must be leashed in common areas. 
   Due to hygienic reasons, pets are not allowed in the hotel restaurant.
   
The hotel renders services in accordance with its category and standard. 
Guests are requested to submit any complaints regarding the quality of services
at the reception desk as soon as possible, 
thus allowing for the hotel's immediate reaction.

The hotel is obliged to ensure:

A) conditions for full and undisturbed rest of the guest

B) safety of stay and privacy. Every guest provides its consent to processing 
   their personal information for the purposes of checking in
  and placing its data in the hotel database
  as per the Personal Data Protection Act of 29.10.1997. 
  (Journal of Laws of 1997, no. 133, item 883 as later amended). 
  The guest has the right to review and correct its personal data.

C) professional and polite service in respect of all services rendered by the hotel

D) cleaning of the room and performing necessary repairs of equipment 
   during the guest's absence or in their presence is so requested by the guest

E) in case of any defects which could not be repaired, 
  the hotel shall make every effort to, where possible,
  change the room or in any other way redress the inconvenience.''')
    

def viewreg():
    viewdetails()
    df=pd.read_sql_query("select * from client",con)
    print('''        ---THE CONTENTS OF CLIENT TABLE ARE AS FOLLOWS---''')
    print()
    print(tabulate(df,tablefmt='psql',headers=['idno','name','age','gender','phone','email']))
    con.commit()       #to print details of client table as a dataframe
    print()
    
def viewbookroom():
    viewdetails()
    df=pd.read_sql_query("select * from bookroom",con)
    print('''        ---The contents of bookroom table are as follows---''')
    print(tabulate(df,tablefmt='psql',headers=['idno','room_no','cost','bedtype','mode_of_pay']))
    con.commit()     #to print details of bookroom table as a dataframe
    print()
    
def viewrestraunt():
    viewdetails()
    df=pd.read_sql_query("select * from restraunt",con)
    print('''        ---THE CONTENT OF THE RESTRAUNT TABLE ARE AS FOLLOWS---''')
    print(tabulate(df,tablefmt='psql',headers=['idno','cuisine','cost','mode_of_pay']))
    con.commit()       #to print details of restraunt table as a dataframe
    print()
    
def viewextras():
    viewdetails()
    df=pd.read_sql_query("select * from extras",con)
    print('''        ---THE CONTENT OF THE EXTRAS  TABLE ARE AS FOLLOWS---''')
    print(tabulate(df,tablefmt='psql',headers=['idno','facilities','cost','mode_of_pay']))
    con.commit()       #to print details of extras table as a dataframe
    print()

def viewtourism():
    viewdetails()
    df=pd.read_sql_query("select * from tourism",con)
    print('''        ---THE CONTENT OF THE TOURISM TABLE ARE AS FOLLOWS---''')
    print(tabulate(df,tablefmt='psql',headers=['idno','location','cost','mode_of_pay']))
    con.commit()      #to print details of tourism table as a dataframe
    print()

    
def olddetailsbookroom(idn):  
    print("""
        _______________________________ 
        |                             |
        |Your details are as follows:-|
        |_____________________________| 
        
        """)                               #shows the old details of a client
    cur.execute("select * from bookroom where idno=(%s);",(idn,))
    d=cur.fetchall()
    for i in d:
            print("""     QatarID:-""",i[0])
            print('''     room_no:-''',i[1])
            print('''     cost:-''',i[2])
            print('''     bed_type:-''',i[3])
            print('''     mode of payment:-''',i[4])
            
        
def newdetailsbookroom(qid):
    cur.execute('select * from bookroom where idno=(%s)',(qid,))
    dat=cur.fetchall() 
    for row in dat:                 #shows the new details of a client
        print('')
        print('''
           ------------------------      
           | YOUR NEW DETAILS ARE |
           ------------------------      
                ''')
        print('')                
        print("""     QatarId:-""",row[0])
        print('''     room_no-''',row[1])
        print('''     bed_type:-''',row[2])
        print('''     cost:-''',row[3])
        print('''     mode of payment:-''',row[4])
        
        
def olddetailsextras(idn):
    print("""
        _______________________________ 
        |                             |
        |Your details are as follows:-|
        |_____________________________| 
        
        """)                                 #shows the old details of a client
    cur.execute("select * from extras where idno=(%s);",(idn,))
    d=cur.fetchall()
    for i in d:
        print("""     QatarID:-""",i[0])
        print('''     facilities:-''',i[1])
        print('''     cost:-''',i[2])
        print('''     mode_of_pay:-''',i[3])
        
        

def newdetailsextras(qid):
    cur.execute('select * from extras where idno=(%s)',(qid,))
    dat=cur.fetchall()
    for row in dat:              #shows the old details of a client
        print('')
        print('''
           ------------------------      
           | YOUR NEW DETAILS ARE |
           ------------------------      
                ''')
        print('')                
        print("""     QatarId:-""",row[0])
        print('''     facilities-''',row[1])
        print('''     cost:-''',row[2])
        print('''     mode_of_payment:-''',row[3])
        
        
def olddetailstourism(idn):
    print("""
        _______________________________ 
        |                             |
        |Your details are as follows:-|
        |_____________________________| 
        
        """)                                #shows the old details of a client
    cur.execute("select * from tourism where idno=(%s);",(idn,))
    d=cur.fetchall()
    for i in d:
        print("""     QatarID:-""",i[0])
        print('''     location:-''',i[1])
        print('''     cost:-''',i[2])
        print('''     mode_of_payment:-''',i[3])
        
  
        
def newdetailtourism(qid):
    cur.execute('select * from tourism where idno=(%s)',(qid,))
    dat=cur.fetchall()
    for row in dat:              #shows the old details of a client
        print('')
        print('''
           ------------------------      
           | YOU NEW DETAILS ARE  |
           ------------------------      
                ''')
        print('')                
        print("""     QatarId:-""",row[0])
        print('''     location-''',row[1])
        print('''     cost:-''',row[2])
        print('''     mode_of_payment:-''',row[3])
        


def olddetailsrestraunt(idn):
    print("""
        _______________________________ 
        |                             |
        |Your details are as follows:-|
        |_____________________________| 
        
        """)                                #shows the old details of a client
    cur.execute("select * from restraunt where idno=(%s);",(idn,))
    d=cur.fetchall()
    for i in d:
        print("""     QatarID:-""",i[0])
        print('''     Cuisine:-''',i[1])
        print('''     Cost:-''',i[2])
        print('''     Mode of payment:-''',i[3])
        
   
        
def newdetailsrestraunt(qid):
    cur.execute('select * from restraunt where idno=(%s)',(qid,))
    dat=cur.fetchall()
    for row in dat:             #shows the old details of a client
        print('')
        print('''
           ------------------------      
           | YOU NEW DETAILS ARE  |
           ------------------------      
                ''')
        print('')                
        print("""     QatarId:-""",row[0])
        print('''     cuisine''',row[1])
        print('''     cost:-''',row[2])
        print('''     Mode of payment:-''',row[3])
        

    
def detailsreg(idn):
    print("""
        _______________________________ 
        |                             |
        |Your details are as follows:-|
        |_____________________________| 
        
        """)
    cur.execute("select * from client where idno=(%s);",(idn,))
    d=cur.fetchall()
    for i in d:
        print("""     QatarID:-""",i[0])
        print('''     Name:-''',i[1])
        print('''     Age:-''',i[2])      #to view details of a registered client
        print('''     Gender:-''',i[3])
        print('''     Phone:-''',i[4])
        print('''     email:-''',i[5])
    




cur.execute("create table if not exists client"
            "("
            "idno char(12) primary key,"
            "name char(20),"
            "age int(10),"
            "gender char(1),"
            "phone char(10),"
           "email varchar(20))")


def reg():
    while True:
            idn=input("Qatar ID:")
            if len(idn)==12 :
                break
            else:
                print("********12 digits required*********")
    cur.execute('select * from client where idno=(%s)',(idn,))
    dat=cur.fetchall()
    a=[]
    for i in dat:
        a.append(i)     #checks whether a user is already registered 
    if len(a)==1:
        existreg()
        detailsreg(idn)
            
    else:          
        name=input("Customer name:")         #takes the required output 
        while True:
            age=int(input("Age:"))
            if type(age)!=int:
                print("********Wrong input(only digits)*********")
            else:
                break

        
        while True:
            gen=input("Gender M/F:")
            if gen==("M") or gen==("F"):
                break
            else:
                print("********M\F only********")
        
        while True:
            ph=input("Mobile Number('8 DIGITS ONLY'):")
            if len(ph)==8:
                break
            else:
                print("********8 digits required*********")
        while True:
            email=input("Enter your mail:")
            if type(email)==str:
                break
            if len(email)==50:
                print("*********invalid input**********")
            
        cur.execute('''insert into client(idno,name,age,gender,phone,email) values(%s,%s,%s,%s,%s,%s)
                    ''',(idn,name,age,gen,ph,email,))
        con.commit()
        print(" ")      #register the given user 
        print("""   
          __________________________        
          |                        |
          |YOU HAVE BEEN REGISTERED| 
          |________________________|     
             """)
          
        detailsreg(idn)        
        con.commit()
                                          #shows the details of the newly registered client
        viewreg()
        con.commit()
        
def updreg():
    upd()
    ch=int(input("Enter your preference:-"))
    if ch==1:
        name()
    elif ch==2:
        age()                    #to update the registered details of client
    elif ch==3:
        gen()
    elif ch==4:
        ph()
    elif ch==5:
        mail()







def age():
        qid=int(input('ENTER YOUR QatarId NO:'))
        cur.execute('select * from client where idno=(%s)',(qid,))
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)      # It fetches the details of client,
                            # and checks whether he is registered with client table or not
        if len(a)!=1:
            notreg()
            
        else:
            print('')
            print('''
            ------------------------    
            | YOUR OLD DETAILS ARE |
            ------------------------
            ''')
            
            print("")
            print("""     QatarID:-""",i[0])
            print('''     Name:-''',i[1])             #print client's old details
            print('''     Age:-''',i[2])
            print('''     Gender:-''',i[3])
            print('''     Phone:-''',i[4])
            print('''     email:-''',i[5])
            n=input('ENTER NEW AGE:-')
            cur.execute('update client set age=(%s) where idno=(%s);',(n,qid,))
            con.commit()
            cur.execute('select * from client where idno=(%s)',(qid,))
            dat=cur.fetchall()
            for row in dat:
                print('')
                print('''
           ------------------------      
           | YOU NEW DETAILS ARE  |
           ------------------------      
                ''')
                print('')                
                print("""     QatarId:-""",row[0])
                print('''     Name:-''',row[1])
                print('''     Age:-''',row[2])
                print('''     Gender:-''',row[3])    #shows his new details 
                print('''     Phone:-''',row[4])
                print('''     email:-''',row[5])
                con.commit()
        return("")
    
def gen():
        qid=int(input('ENTER YOUR QatarId NO:'))
        cur.execute('select * from client where idno=(%s)',(qid,))
        dat=cur.fetchall()
        a=[]
        for i in dat:            # It fetches the details of client,
            a.append(i)       # and checks whether he is registered with client table or not
                              # if not registered it shows a message-"not registered"
        if len(a)!=1:
            notreg()
            
        else:
            print('')
            print('''
            ------------------------    
            | YOUR OLD DETAILS ARE |
            ------------------------
            ''')
            
            print("")
            print("""     QatarId:-""",i[0])           #print client's old details
            print('''     Name:-''',i[1])
            print('''     Age:-''',i[2])
            print('''     Gender:-''',i[3])
            print('''     Phone:-''',i[4])
            print('''     email:-''',i[5])
            n=input('ENTER NEW GENDER:-')
            cur.execute('update client set gender=(%s) where idno=(%s);',(n,qid,))
            con.commit()
            cur.execute('select * from client where idno=(%s)',(qid,))
            dat=cur.fetchall()
            for row in dat:
                print('')
                print('''
           ------------------------      
           | YOU NEW DETAILS ARE  |
           ------------------------      
                ''')
                print('')                
                print("""     QatarId:-""",row[0])
                print('''     Name:-''',row[1])
                print('''     Age:-''',row[2])
                print('''     Gender:-''',row[3])    #shows his new details 
                print('''     Phone:-''',row[4])
                print('''     email:-''',row[5])
                con.commit()
        return("")
    
def mail():
    qid=int(input('ENTER YOUR QatarId:'))
    cur.execute('select * from client where idno=(%s)',(qid,))
    dat=cur.fetchall()
    a=[]
    for i in dat:          # It fetches the details of client,
        a.append(i)       # and checks whether he is registered with client table or not
                          # if not registered it shows a message-"not registered"
    if len(a)!=1:
        notreg()
            
    else:
        print('')
        print('''
            ------------------------    
            | YOUR OLD DETAILS ARE |
            ------------------------
            ''')
            
        print("")
        print("""     QatarId:-""",i[0])
        print('''     Name:-''',i[1])
        print('''     Age:-''',i[2])
        print('''     Gender:-''',i[3])         #print client's old details
        print('''     Phone:-''',i[4])
        print('''     email:-''',i[5])
        n=input('ENTER NEW EMAIL:-')
        cur.execute('update client set email=(%s) where idno=(%s);',(n,qid,))
        con.commit()
        cur.execute('select * from client where idno=(%s)',(qid,))
        dat=cur.fetchall()
        for row in dat:
            print('')
            print('''
           ------------------------      
           | YOU NEW DETAILS ARE  |
           ------------------------      
                ''')
            print('')                
            print("""     QatarId:-""",row[0])
            print('''     Name:-''',row[1])
            print('''     Age:-''',row[2])          #shows his new details 
            print('''     Gender:-''',row[3])
            print('''     Phone:-''',row[4])
            print('''     email-''',row[5])
            con.commit()
    return("")


def name():
        qid=int(input('ENTER YOUR Qatar ID NO:'))
        cur.execute('select * from client where idno=(%s)',(qid,))
        dat=cur.fetchall()
        a=[]
        for i in dat:             # It fetches the details of client,
            a.append(i)       # and checks whether he is registered with client table or not
                              # if not registered it shows a message-"not registered"
        if len(a)!=1:
            notreg()
            
        else:
            print('')
            print('''
            ------------------------    
            | YOUR OLD DETAILS ARE |
            ------------------------
            ''')
            
            print("")
            print("""     QatarID:-""",i[0])
            print('''     Name:-''',i[1])
            print('''     Age:-''',i[2])          #print client's old details
            print('''     Gender:-''',i[3])
            print('''     Phone:-''',i[4])
            print('''     email:-''',i[5])
            n=input('ENTER NEW NAME:-')
            cur.execute('update client set name=(%s) where idno=(%s);',(n,qid,))
            con.commit()
            cur.execute('select * from client where idno=(%s)',(qid,))
            dat=cur.fetchall()
            for row in dat:
                print('')
                print('''
           ------------------------      
           | YOU NEW DETAILS ARE  |
           ------------------------      
                ''')
                print('')                
                print("""     QatarID.:-""",row[0])
                print('''     Name:-''',row[1])
                print('''     Age:-''',row[2])          #shows his new details 
                print('''     Gender:-''',row[3])
                print('''     Phone:-''',row[4])
                print('''     email:-''',row[5])
                con.commit()
        return("")    
        
def ph():
        qid=int(input('ENTER YOUR QatarId NO:'))
        cur.execute('select * from client where idno=(%s)',(qid,))
        dat=cur.fetchall()
        a=[]                          
        for i in dat:           # It fetches the details of client,
            a.append(i)       # and checks whether he is registered with client table or not
                              
        if len(a)!=1:
            notreg()
            
        else:
            print('')
            print('''
            ------------------------    
            | YOUR OLD DETAILS ARE |
            ------------------------
            ''')
            
            print("")
            print("""     QatarId:-""",i[0])
            print('''     Name:-''',i[1])
            print('''     Age:-''',i[2])            #print client's old details
            print('''     Gender:-''',i[3])
            print('''     Phone:-''',i[4])
            print('''     email:-''',i[5])
            n=input('ENTER NEW PHONE NO:-')
            cur.execute('update client set phone=(%s) where idno=(%s);',(n,qid,))
            con.commit()
            cur.execute('select * from client where idno=(%s)',(qid,))
            dat=cur.fetchall()
            for row in dat:
                print('')
                print('''
           ------------------------      
           | YOU NEW DETAILS ARE  |
           ------------------------      
                ''')
                print('')                
                print("""     QatarId:-""",row[0])
                print('''     Name:-''',row[1])
                print('''     Age:-''',row[2])          #shows his new details
                print('''     Gender:-''',row[3])
                print('''     Phone:-''',row[4])
                print('''     email-''',row[5])
                con.commit()
        return("")      
    
cur.execute("create table if not exists bookroom"
            "("
            "idno char(12) primary key,"
            "room_no int(20),"
            "cost int(10),"
           "bed_type varchar(20),"
           "mode_of_pay varchar(20))")



def bookroom():
        while True:
            idn=input("Qatar ID(12 DIGITS):")
            if len(idn)==12:
                break
            else:
                print("********PLEASE ENTER ONLY 12 DIGITS*********")
        
        cur.execute('select * from client where idno=(%s)',(idn,))
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)            # It fetches the details of client,
                             # and checks whether he is registered with client table or not
        if len(a)!=1:        # if not registered it shows a message-"not registered"
            notreg()
            
        else:
            cur.execute('select * from bookroom where idno=(%s)',(idn,))
            dat=cur.fetchall()
            a=[]
            for i in dat:
                a.append(i)            # It fetches the details of bookroom,
                             # and checks whether he is registered with client table or not
            if len(a)==1:      #if registered message is shown-"already registered"
                existreg()
                olddetailsbookroom(idn)
            
            else:
                viewbookroom()
                menubookroom()             #shows a menu and takes the details as shown
               
                while True:
                    bt=input("Enter the bed_type:")
                    if type(bt)==str:
                        break                              
                    if len(bt)==20:
                        print("*********invalid input**********")
        
                while True:
                    rn=int(input("Enter the room no:"))
                    if type(rn)!=int:
                        print("********Wrong input(only digits)*********")
                    else:
                        break
        
                while True:
                    cost=int(input("Enter the cost:"))
                    num=int(input("Enter the number of persons:-"))
                    if type(cost)==int:
                        total=cost*num
                        break
                    else:
                        print("********Invalid Input *********")
            
                while True:
                    menupay()
                    mop=input("Please enter the mode of payment:")
                    if type(mop)!=str:
                        print("********Wrong input(only characters)*********")
                    else:
                        break
       
            
                cur.execute('''insert into bookroom(idno,room_no,cost,bed_type,mode_of_pay) values(%s,%s,%s,%s,%s)
                            ''',(idn,rn,total,bt,mop,))
                con.commit()
                print(" ")
                print("""   
          __________________________        
          |                        |
          |YOU HAVE BEEN REGISTERED| 
          |________________________|        
             """)                     #it inserts the given data and shows the details
          
                print("""
        _______________________________ 
        |                             |
        |Your details are as follows:-|
        |_____________________________| 
        
        """)
                cur.execute("select * from bookroom where idno=(%s);",(idn,))
                d=cur.fetchall()
                for i in d:
                    print("""     QatarID:-""",i[0])
                    print('''     room_no:-''',i[1])
                    print('''     cost:-''',i[2])  
                    print('''     bed_type:-''',i[3])
                    print('''     mode of payment:-''',i[4])
                    
                viewbookroom()
                con.commit()
                
            
        
        
    
def updbookroom():
        qid=int(input('ENTER YOUR QatarId NO(12 DIGITS):'))
        cur.execute('select * from bookroom where idno=(%s)',(qid,))
        dat=cur.fetchall()
        a=[]
        for i in dat:             
            a.append(i)             # It fetches the details of client,
                             # and checks whether he is registered with client table or not
            
        if len(a)!=1:
            notreg()     # if not registered it shows a message-"not registered"
        
        else:
            print("""
        _______________________________ 
        |                             |
        |Your details are as follows:-|
        |_____________________________| 
        
        """)
            
            cur.execute("select * from bookroom where idno=(%s);",(qid,))
            d=cur.fetchall()
            for i in d:
                print("""     QatarID:-""",i[0])
                print('''     room_no:-''',i[1])        # shows his previous details 
                print('''     cost:-''',i[2])
                print('''     bed_type:-''',i[3])
                print('''     mode of payment:-''',i[4])
               
            

            viewbookroom()           #shows details of the bookroom table
            
            n=int(input('ENTER the new room_no:-'))
            cur.execute('update bookroom set room_no=(%s) where idno=(%s);',(n,qid,))
            
            menubookroom()
            b=input('ENTER the new bed type:-')
            cur.execute('update bookroom set bed_type=(%s) where idno=(%s);',(b,qid,))
            
            c=int(input('ENTER the updated cost:-'))
            num=int(input("Enter the number of person:-"))
            tot=c*num
            cur.execute('update bookroom set cost=(%s) where idno=(%s);',(tot,qid,))
            
            menupay()
            d=input("Enter the new mode of payment:-")
            cur.execute('update bookroom set mode_of_pay=(%s) where idno=(%s);',(d,qid,))
            con.commit()
            
            newdetailsbookroom(qid)      #shows updated details
                                                     
            viewbookroom()               #shows details of the bookroom table 
            con.commit()                             #after updating the details 


cur.execute("create table if not exists extras"
            "("
            "idno char(12) primary key,"
            "facilities varchar(20),"
            "cost int(10),"
           "mode_of_pay varchar(20))")



def extras():
        while True:
            idn=input("Qatar ID(12 DIGITS):")
            if len(idn)==12 :
                break
            else:
                print("********PLEASE ENTER ONLY 12 DIGITS*********")
        
        
        cur.execute('select * from client where idno=(%s)',(idn,))
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)         # It fetches the details of client,
                             # and checks whether he is registered with client table or not
                             # if not registered it shows a message-"not registered"
        if len(a)!=1:
            notreg()
            
        
        else:
             cur.execute('select * from extras where idno=(%s)',(idn,))
             dat=cur.fetchall()
             a=[]
             for i in dat:
                 a.append(i)
                                       # It fetches the details of extras table,
                               # and checks whether he is registered with client table or not
                               #if registered message is shown-"already registered"
             if len(a)==1:
                existreg()
                olddetailsextras(idn)
                    
                
                
             else:
                 viewextras()   #shows a menu and takes the details as shown
                 menuextras()
               
                 while True:
                    fc=input("Enter the facilities:")
                    if type(fc)!=str:
                        print("********Wrong input(only digits)*********")
                    else:
                        break
        
                 while True:
                     cost=int(input("Enter the cost:"))
                     num=int(input("Enter the number of persons:-"))
                     if type(cost)==int:
                         total=cost*num
                         break
                     else:
                         print("********Invalid Input *********")
                 while True:
                     menupay()
                
                     mop=input("Enter the mode_of_payment:")
                     if type(mop)==str:
                        break
                     if len(mop)==20:
                         print("*********invalid input**********")
            
                 cur.execute('''insert into extras(idno,facilities,cost,mode_of_pay) values(%s,%s,%s,%s)
                             ''',(idn,fc,total,mop,))
                 con.commit()
                 print(" ")
                 print("""   
          __________________________        
          |                        |
          |YOU HAVE BEEN REGISTERED| 
          |________________________|     
             """)                        #it inserts the given data and shows the details
          
                 print("""
        _______________________________ 
        |                             |
        |Your details are as follows:-|
        |_____________________________| 
        
        """)
                 cur.execute("select * from extras where idno=(%s);",(idn,))
                 d=cur.fetchall()
                 for i in d:
                     print("""     QatarID:-""",i[0])
                     print('''     facilities:-''',i[1])
                     print('''     cost:-''',i[2])
                     print('''     mode_of_pay:-''',i[3])
                 viewextras()
                 con.commit()   
                 
                 
        
        
    
    

def updextras():
        qid=int(input('ENTER YOUR QatarId NO(12 DIGITS):'))
        cur.execute('select * from extras where idno=(%s)',(qid,))
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)          # It fetches the details of client,
                             # and checks whether he is registered with client table or not
            
        if len(a)!=1:
            notreg()    # if not registered it shows a message-"not registered"
        else:
            print("""
        _______________________________ 
        |                             |
        |Your details are as follows:-|
        |_____________________________| 
        
        """)
            cur.execute("select * from extras where idno=(%s);",(qid,))
            d=cur.fetchall()
            for i in d:
                print("""     QatarID:-""",i[0])
                print('''     facilities:-''',i[1])      # shows his previous details
                print('''     cost:-''',i[2])
                print('''     mode_of_pay:-''',i[3])
                
            
            menuextras()       #shows details of the extras table
            
            n=input('ENTER facilities:-')
            cur.execute('update extras set facilities=(%s) where idno=(%s);',(n,qid,))
            
            c=int(input('ENTER the cost:-'))
            num=int(input("Enter the number of person:-"))
            tot=c*num
            cur.execute('update extras set cost=(%s) where idno=(%s);',(tot,qid,))
            con.commit()
            
            menupay()
            b=input('ENTER mode_of_payment:-')
            cur.execute('update extras set mode_of_pay=(%s) where idno=(%s);',(b,qid,))
            con.commit()
            
            newdetailsextras(qid)       #shows updated details
            viewextras()            #shows details of the extras table 
            con.commit()                        #after updating the details
  
            
cur.execute("create table if not exists restraunt"
            "("
            "idno char(12) primary key,"
            "cuisine varchar(20),"
            "cost int,"
            "mode_of_pay varchar(20))")
            


def restraunt():
        while True:
            idn=input("Qatar ID(12 DIGITS):")
            if len(idn)==12 :
                break
            else:
                print("********PLEASE ENTER ONLY 12 DIGITS*********")
                
        cur.execute('select * from client where idno=(%s)',(idn,))
        dat=cur.fetchall()
        a=[]
        for i in dat:          # It fetches the details of client,
            a.append(i)       # and checks whether he is registered with client table or not
        if len(a)!=1:         # if not registered it shows a message-"not registered"
            notreg()
        
        else:
             cur.execute('select * from restraunt where idno=(%s)',(idn,))
             dat=cur.fetchall()
             a=[]
             for i in dat:                  # It fetches the details of restraunt,
                 a.append(i)      # and checks whether he is registered with client table or not
             if len(a)==1:        #if registered message is shown-"already registered"
                existreg()
                olddetailsrestraunt(idn)
                
                
            
             else:
                 viewrestraunt()
                 menurestraunt()             #shows a menu and takes the details as shown
        
                 while True:
                    cu=input("Please enter the type of Cuisine you prefer:")
                    if type(cu)==str:
                        break
                    if len(cu)==25:
                        print("*********invalid input**********")
                
                 while True:
                    cost=int(input("cost of the item per head:"))
                    num=int(input("Enter the number of persons:-"))
                    if type(cost)!=int:
                        print("********Wrong input(only digits)*********")
                    else:
                        total=cost*num
                        break
                 while True:
                     menupay()
                     mop=input("Please enter the mode of payment:")
                     if type(mop)!=str:
                         print("********Wrong input(only characters)*********")
                     else:
                        break

            

                 cur.execute('''insert into restraunt(idno,cuisine,cost,mode_of_pay) values(%s,%s,%s,%s)
                             ''',(idn,cu,total,mop,))
                 con.commit()
                 print(" ")                #it inserts the given data and shows the details
                 print("""   
          __________________________        
          |                        |
          |YOU HAVE BEEN REGISTERED| 
          |________________________|     
             """)
                 print("""
         _______________________________ 
        |                             |
        |Your details are as follows:-|
        |_____________________________| 
        
                  """)
          
            
                 cur.execute("select * from restraunt where idno=(%s);",(idn,))
                 d=cur.fetchall()
                 for i in d:
                     print("""     QatarID:-""",i[0])
                     print('''     Cuisine:-''',i[1])
                     print('''     Cost:-''',i[2])
                     print('''     Mode of payment:-''',i[3])
                 
                 viewrestraunt()
                 con.commit()
                 
        

def updrest():
    qid=int(input('ENTER YOUR QatarId NO(12 DIGITS):'))
    cur.execute('select * from restraunt where idno=(%s)',(qid,))
    dat=cur.fetchall()
    a=[]
    for i in dat:        # It fetches the details of client,
        a.append(i)      # and checks whether he is registered with client table or not 
    if len(a)!=1:
        notreg()    # if not registered it shows a message-"not registered" 
    else:
        print("""
        _______________________________ 
        |                             |
        |Your details are as follows:-|
        |_____________________________| 
        
        """)
        cur.execute("select * from restraunt where idno=(%s);",(qid,))
        d=cur.fetchall()
        for i in d:
            print("""     QatarID:-""",i[0])
            print('''     Cuisine:-''',i[1])    # shows his previous details
            print('''     Cost:-''',i[2])           
            print('''     Mode of payment:-''',i[3])
            
        print()
        menurestraunt()           #shows details of the restraunt table
        n=input('ENTER the new cuisine:-')
        cur.execute('update restraunt set cuisine=(%s) where idno=(%s);',(n,qid,))
        
        c=int(input('ENTER the updated cost:-'))
        num=int(input("Enter the number of person:-"))
        tot=c*num
        cur.execute('update restraunt set cost=(%s) where idno=(%s);',(tot,qid,))
        
        menupay()
        mop=input("Please enter the new mode of payment:")
        cur.execute('update restraunt set mode_of_pay=(%s) where idno=(%s);',(mop,qid,))
        con.commit()
        
        newdetailsrestraunt(qid)    #shows updated details
        viewrestraunt()             #shows details of the restraunt table 
                                                #after updating the details 
        con.commit()
     
        
cur.execute("create table if not exists tourism"
            "("
            "idno char(12) primary key,"
            "location varchar(20),"
            "cost int(20),"
           "mode_of_payment varchar(20))")
    
def tourism():
        while True:
            idn=input("Qatar ID(12 DIGITS):")
            if len(idn)==12 :
                break
            else:
                print("********PLEASE ENTER ONLY 12 DIGITS*********")
                
        cur.execute('select * from client where idno=(%s)',(idn,))
        dat=cur.fetchall()
        a=[]
        for i in dat:         # It fetches the details of client,
            a.append(i)       # and checks whether he is registered with client table or not
                              # if not registered it shows a message-"not registered"
        if len(a)!=1:
            notreg()
            
            
            
        else:
            cur.execute('select * from tourism where idno=(%s)',(idn,))
            dat=cur.fetchall()
            a=[]
            for i in dat:          # It fetches the details of tourism table,
                a.append(i)       # and checks whether he is registered with client table or not
                                  #if registered message is shown-"already registered"
            if len(a)==1:
                existreg()
                olddetailstourism(idn)
                
                
            
            else:
                viewtourism()      #shows a menu and takes the details as shown
                menutour()
               
                while True:
                    l=input("Enter the location:")
                    if len(l)==20:
                        print("********Wrong input(only digits)*********")
                    else:
                        break
                
        
                while True:
                    cost=int(input("Enter the cost:"))
                    if type(cost)==int:
                        break
                    else:
                        print("********Invalid Input *********")
        
                while True:
                    menupay()
                    mop=input("Enter the mode of payment:")
                    num=int(input("Enter the number of persons:-"))
                    if type(mop)==str:
                        total=cost*num
                        break
                    else:
                        print("*********invalid input**********")
            
                cur.execute('''insert into tourism(idno,location,cost,mode_of_payment) values(%s,%s,%s,%s)
                            ''',(idn,l,total,mop,))
                con.commit()         
                print(" ")               #it inserts the given data and shows the details
                print("""   
          __________________________        
          |                        |
          |YOU HAVE BEEN REGISTERED| 
          |________________________|     
             """)
          
                print("""
        _______________________________ 
        |                             |
        |Your details are as follows:-|
        |_____________________________| 
        
        """)
                cur.execute("select * from tourism where idno=(%s);",(idn,))
                d=cur.fetchall()
                for i in d:
                    print("""     QatarID:-""",i[0])
                    print('''     location:-''',i[1])
                    print('''     cost:-''',i[2])
                    print('''     mode_of_payment:-''',i[3])
                viewtourism()
                con.commit()
            
            
        


def updtourism():
        qid=input('ENTER YOUR QatarId NO(12 DIGITS):')
        cur.execute('select * from tourism where idno=(%s)',(qid,))
        dat=cur.fetchall()
        a=[]
        for i in dat:           # It fetches the details of client,
            a.append(i)        # and checks whether he is registered with client table or not 
            
        if len(a)!=1:
            notreg()     # if not registered it shows a message-"not registered" 
        else:
            print("""
        _______________________________ 
        |                             |
        |Your details are as follows:-|
        |_____________________________| 
        
        """)
            cur.execute("select * from tourism where idno=(%s);",(qid,))
            d=cur.fetchall()
            for i in d:
                print("""     QatarID:-""",i[0])
                print('''     location:-''',i[1])        # shows his previous details
                print('''     cost:-''',i[2])
                print('''     mode_of_payment:-''',i[3])
                
            
            menutour()            #shows details of the tourism table
            n=input('ENTER location:-')
            cur.execute('update tourism set location=(%s) where idno=(%s);',(n,qid,))
            
            
            c=int(input('ENTER the cost:-'))
            num=int(input("Enter the number of person:-"))
            tot=c*num
            cur.execute('update tourism set cost=(%s) where idno=(%s);',(tot,qid,))
            con.commit()
            menupay()
            b=input('ENTER mode_of_payment:-')
            cur.execute('update tourism set mode_of_payment=(%s) where idno=(%s);',(b,qid,))
            con.commit()
            newdetailtourism(qid)     #shows updated details
            #                                    shows details of the tourism table 
                                                 #after updating the details 
            viewtourism()
            con.commit()
            

            
def bill():
    menubill()
    while True:
            idn=input("Qatar ID(12 DIGITS):")
            if len(idn)==12:
                break
            else:
                print("********PLEASE ENTER ONLY 12 DIGITS*********")  
                
    cur.execute('select * from client where idno=(%s)',(idn,))
    dat=cur.fetchall()
    a=[]
    for i in dat:
        a.append(i)            # It fetches the details of client,
                             # and checks whether he is registered with client table or not
    if len(a)!=1:        # if not registered it shows a message-"not registered"
        notreg()
            
    else:
    
    
        cur.execute('select client.idno from client where idno=(%s);',(idn,))
        dat=cur.fetchall()
        z=[]
        a=[]
        n=[]
        for i in dat:
            z.append(i)
        con.commit()
    
    
        if len(z)==1:
            cur.execute('select bookroom.cost from bookroom where idno=(%s);',(idn,))
            dat=cur.fetchall()
        for i in dat:
            a.append(i)
            n.append("bookroom")
            
        con.commit()
    
    
        cur.execute('select restraunt.cost from restraunt where idno=(%s);',(idn,))
        dat=cur.fetchall()
        for i in dat:
            a.append(i)
            n.append("restraunt")
            
        con.commit()
    
        cur.execute('select extras.cost from extras where idno=(%s);',(idn,))
        dat=cur.fetchall()
        for i in dat:
            a.append(i)
            n.append("extras")
            
        con.commit()
    
        cur.execute('select tourism.cost from tourism where idno=(%s);',(idn,))
        dat=cur.fetchall()
        for i in dat:
            a.append(i)
            n.append("tourism")
    
    
        df=pd.DataFrame([n,a])
        print(tabulate(df, tablefmt = 'psql')) 
        
        ilist=[]
        sum=[]
        num=int(input("Enter the number of facilities:"))
        menuitemcode()
        for i in range(0,num):
            itc=input("Enter the item code(b/r/e/t):")
            if itc=='b' or itc=='B':
                sp1=float(input("Enter the selling price:"))
                sum.append(sp1)
                item1="bookroom"
                ilist.append(item1)
            if itc=='r' or itc=="R":
                sp2=float(input("Enter the selling price:"))
                sum.append(sp2)
                item2="restraunt"
                ilist.append(item2)
            if itc=="e" or itc=="E":
                sp3=float(input("Enter the selling price:"))
                sum.append(sp3)
                item3="extras"
                ilist.append(item3)
            if itc=='t' or itc=="T":
                sp4=float(input("Enter the selling price:"))
                sum.append(sp4)
                item4="tourism"
                ilist.append(item4)
            
        
        
        
        print()
        print("-"*65)
        print("\t\t\t\t\t\t\t INVOICE")
        print("-"*65)
        print()
        amount=0   
        for j in sum:
            amount=amount+j
        
        for i in ilist:
            if i=='bookroom':
                print("ITEM:{0:>40s}".format(item1))
                print("Price:\t\t\t{0:30.2f}".format(sp1))
            elif i=='restraunt':
                print("ITEM:{0:>40s}".format(item2))
                print("Price:\t\t\t{0:30.2f}".format(sp2))
            elif i=='extras':
                print("ITEM:{0:>40s}".format(item3))
                print("Price:\t\t\t{0:30.2f}".format(sp3))
            elif i=='tourism':
                print("ITEM:{0:>40s}".format(item4))
                print("Price:\t\t\t{0:30.2f}".format(sp4))
        
        print("-"*65)
        print("Amount payable:\t\t\t{0:23.2f}".format(amount))
        print("-"*65)
        
        
        z=[]
        cur.execute("select client.email from client where idno=(%s)",(idn,))
        dat=cur.fetchall()
        for i in dat:
            z.append(i)
        print()   
        print("THE INVOICE HAS BEEN SEND TO YOUR MAIL ID:-",z)
            
        con.commit()
    
def profit():
        a=[]
        n=[]
        cur.execute('select sum(bookroom.cost) from bookroom;')
        dat=cur.fetchall()
        for i in dat:
            a.append(i)
            n.append("bookroom")
            
        con.commit()
        
        
        cur.execute('select sum(restraunt.cost) from restraunt;')
        dat=cur.fetchall()
        for i in dat:
            a.append(i)
            n.append("restraunt")
            
        con.commit()
        
        cur.execute('select sum(extras.cost) from extras;')
        dat=cur.fetchall()
        for i in dat:
            a.append(i)
            n.append("extras")
            
        con.commit()
        
        cur.execute('select sum(tourism.cost) from tourism;')
        dat=cur.fetchall()
        for i in dat:
            a.append(i)
            n.append("tourism")
            
        con.commit()
        
        plt.plot(n,a)
        plt.title("MARKET ANALYSIS")
        plt.xlabel("Departments")
        plt.ylabel("Net profit")
        plt.show()
        
        con.commit()
        
def check():
        idn=input("Qatar ID(12 DIGITS):")
        cur.execute('select client.idno from client')
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)                 #to check whether the given QID has been registered 
        df=pd.DataFrame(a)              # with the hotel
        head=0
        for i,j in df.iteritems():                
            for x in j:
                if idn==x:
                    head=head+1
        
        if head==1:
            print("THE USER WITH QID",idn,"HAS BEEN REGISTRED WITH US")
        else:
            print("THE USER WITH QID",idn,"HAS NOT BEEN REGISTRED WITH US")
        
            
        cur.execute('select bookroom.idno from bookroom;')
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)          #to check whether the given QID has been registered
        df=pd.DataFrame(a)       # with the bookroom
        head=0
        for i,j in df.iteritems():
            for x in j:
                if idn==x:
                    head=head+1
        
        if head==1:
            print("THE USER WITH QID",idn,"HAS BEEN REGISTRED WITH BOOKROOM TABLE")
        else:
            print("THE USER WITH QID",idn,"HAS NOT BEEN REGISTRED WITH BOOKROOM TABLE")
                    
        
                    
        cur.execute('select restraunt.idno from restraunt;')
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)
        df=pd.DataFrame(a)
        head=0                         #to check whether the given QID has been registered
        for i,j in df.iteritems():     # with the restraunt
            for x in j:
                if idn==x:
                    head=head+1
                    
        if head==1:
            print("THE USER WITH QID",idn,"HAS BEEN REGISTRED WITH OUR RESTRAUNT TABLE")
        else:
            print("THE USER WITH QID",idn,"HAS NOT BEEN REGISTRED WITH OUR RESTRAUNT TABLE")
        
        
        cur.execute('select extras.idno from extras;')
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)
        df=pd.DataFrame(a)
        head=0                        #to check whether the given QID has been registered
        for i,j in df.iteritems():    # with extras table
            for x in j:
                if idn==x:
                    head=head+1
                    
        if head==1:
            print("THE USER WITH QID",idn,"HAS BEEN REGISTRED WITH OUR EXTRAS TABLE")
        else:
            print("THE USER WITH QID",idn,"HAS NOT BEEN REGISTRED WITH OUR EXTRAS TABLE")
        
        
        cur.execute('select tourism.idno from tourism;')
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)
        df=pd.DataFrame(a)
        head=0                       #to check whether the given QID has been registered
        for i,j in df.iteritems():   #tourism
            for x in j:
                if idn==x:
                    head=head+1
        if head==1:
            print("THE USER WITH QID",idn,"HAS BEEN REGISTRED WITH OUR TOURISM TABLE")
        else:
            print("THE USER WITH QID",idn,"HAS NOT BEEN REGISTRED WITH OUR TOURISM TABLE")
        con.commit()         
                    
def deletion():
    menudelete()
    s=int(input("enter your choice:-"))
    if s==1:
        viewreg()   #deletes info from client as well as all other tables
        
        while True:
            idn=int(input("enter QatarID(12 DIGITS):"))
            if type(idn)==int:
                break
            else:
                print("----PLEASE ENTER ONLY 12 DIGITS----")           
        print()
        print("User with QID",idn," has been deleted","\n")
        cur.execute('delete from client where idno=(%s);',(idn,))
        con.commit()
        cur.execute('delete from bookroom where idno=(%s);',(idn,))
        con.commit()
        cur.execute('delete from restraunt where idno=(%s);',(idn,))
        con.commit()
        cur.execute('delete from tourism where idno=(%s);',(idn,))
        con.commit()
        cur.execute('delete from extras where idno=(%s);',(idn,))
        con.commit()
        
        df=pd.read_sql_query("select * from client",con)
        print('''      ---THE CONTENTS OF THE NEW CLIENT TABLE ARE:-''','\n')
        print(tabulate(df,tablefmt='psql',headers=['idno','name','age','gender','phone','email']))
        
        con.commit()
    elif s==2:
        viewbookroom()
        
        while True:
            idn=int(input("enter QatarID(12 DIGITS):"))
            if type(idn)==int:
                break                #deletes info from bookroom table
            else:
                print("----PLEASE ENTER ONLY 12 DIGITS----")
        print()
        print("User with QID",idn," has been deleted","\n")
        cur.execute('delete from bookroom where idno=(%s);',(idn,))
        con.commit()
        
        df=pd.read_sql_query("select * from bookroom",con)
        print('''      ---THE CONTENTS OF THE NEW BOOKROOM TABLE ARE:-''','\n')
        print(tabulate(df,tablefmt='psql',headers=['idno','room_no','cost','bedtype','mode_of_pay']))
        con.commit()
    elif s==3:
        viewrestraunt()
        
        while True:
            idn=int(input("enter QatarID(12 DIGITS):"))
            if type(idn)==int:
                break             #deletes info from restraunt table
            else:
                print("----PLEASE ENTER ONLY 12 DIGITS----")
        print()
        cur.execute('delete from restraunt where idno=(%s);',(idn,))
        con.commit()
        print("User with QID",idn," has been deleted","\n")
        df=pd.read_sql_query("select * from restraunt",con)
        print('''      ---THE CONTENTS OF THE NEW RESTRAUNT ARE:-''','\n')
        print(tabulate(df,tablefmt='psql',headers=['idno','cuisine','cost','mode_of_pay']))
        con.commit()
    elif s==4:
        viewtourism()
        
        while True:
            idn=int(input("enter QatarID(12 DIGITS):"))
            if type(idn)==int:                 
                break          #deletes info from tourism table
            else:
                print("----PLEASE ENTER ONLY 12 DIGITS----")
        print()
        print("User with QID",idn," has been deleted","\n")
        cur.execute('delete from tourism where idno=(%s);',(idn,))
        con.commit()
        df=pd.read_sql_query("select * from tourism",con)
        print('''      ---THE CONTENTS OF THE NEW TOURISM TABLE ARE:-''','\n')
        print(tabulate(df,tablefmt='psql',headers=['idno','location','cost','mode_of_pay']))
        con.commit()
    elif s==5:
        viewextras()
        
        while True:
            idn=int(input("enter QatarID(12 DIGITS):"))
            if type(idn)==int:
                break           #deletes info from extras table
            else:
                print("----PLEASE ENTER ONLY 12 DIGITS----")
        print()
        print("User with QID",idn," has been deleted","\n")
        cur.execute('delete from extras where idno=(%s);',(idn,))
        con.commit()
        df=pd.read_sql_query("select * from extras",con)
        print('''      ---THE CONTENTS OF THE NEW EXTRAS TABLE ARE:-''','\n')
        print(tabulate(df,tablefmt='psql',headers=['idno','facilities','cost','mode_of_pay']))
        con.commit()
    else:
        print("wrong choice")        
    
        
def main():
    welcome()


    while True:
        mainmenu()
        x=int(input("""SELECT YOUR OPTION:-"""))    #ask the user to enter his choice 
        
        if x==1:
            print()
            submenu()
            nch=int(input("enter your choice:"))
            if nch==1:
                reg()
                thankyou()
            elif nch==2:
                updreg() 
                thankyou()  #to register a client
            elif nch==3:
                viewreg()
                thankyou()
      
        elif x==2:
            submenu()
            nch=int(input("enter your choice:"))
            if nch==1:
                bookroom()
                thankyou()
            elif nch==2:
                updbookroom()   
                thankyou()         # to book a room for client
            elif nch==3:
                viewbookroom()
                thankyou()
    
        
        elif x==3:
            submenu()
            nch=int(input("enter your choice:"))
            if nch==1:
                restraunt()
                thankyou()
            elif nch==2:                  # to book food services
                updrest()
                thankyou()
            elif nch==3:
                viewrestraunt()
                thankyou()
      
        
        elif x==4:
          submenu()
          nch=int(input("enter your choice:"))
          if nch==1:
           extras()
           thankyou()
          elif nch==2:
           updextras()  
           thankyou()        #to book other extra facilities 
          elif nch==3:
            viewextras()
            thankyou()
           
        elif x==5:
            submenu()
            nch=int(input("enter your choice:"))
            if nch==1:
                tourism()
                thankyou()
            elif nch==2:
                updtourism() 
                thankyou()#To book tours and travels 
            elif nch==3:
                viewtourism()
                thankyou()
   
        elif x==6:
            deletion() 
            thankyou()    # to delete a user 
        
        elif x==7:
            check()
            thankyou()
       
        elif x==8:
            menuprofit()
            nch=int(input("enter your choice:"))
            if nch==1:
                bill()  
                thankyou()     #for invoice and market analysis
            elif nch==2:
                profit()
                thankyou()
    
        elif x==9:
            termsandconditons()
            thankyou()            #terms and conditions
        
        
        elif x==10:
            thankyou()             # show a thank you message 
            break
            
    print(" ")
    

        
while True:
            login()
            inp=int(input("Select your choice:"))
            if inp==1:
                idn=int(input("Enter the admin idno:"))
                adminmenu()
                x=int(input("Select your choice:"))
            
                if x==1:
                        profit()
                
            
                elif x==2:
                    df=pd.read_sql_query('select * from login;',con)
                    print(tabulate(df, tablefmt = 'psql',headers=['empid','name','email','salary']))
                
                
                
            
            elif inp==2:
                idn=int(input("Enter the employee idno:"))
                cur.execute('select * from login where clientid=(%s)',(idn,))
                dat=cur.fetchall()
                a=[]
                for i in dat:
                    a.append(i)      
                if len(a)!=1:
                    print("INVALID ID")
                    break
            
                else:
                    main()
                    
            
            
            elif inp==3:
                break

            
       


    



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
       
            

  