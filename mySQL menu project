## THEMA 1 ##
import MySQLdb as mysql
mydb = mysql.connect(host="localhost",user="root", passwd = "1234", db="bnp55")
cursor = mydb.cursor()
drop = "DROP TABLE Sequence"
cursor.execute(drop)
statement = """CREATE TABLE Sequence (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, sequence_type CHAR(3), sequence TEXT, creator VARCHAR(50))"""
cursor.execute(statement)
cursor.close()
mydb.close()

## THEMA 2 ##
class Sequence():
    ''' Sequence class with id, sequence type (DNA,RNA), sequence and creator'''
    def __init__(self, id , sequence_type, sequence , creator) :
        self.id= id
        if sequence_type.upper() == 'DNA' or sequence_type.upper() == 'RNA':
            self.sequence_type= sequence_type.upper()
        else:
            print("Warning, You have to provide DNA or RNA for the sequence type")
            self.sequence_type=sequence_type.upper()
        self.sequence= sequence.upper()
        self.creator = creator


    def print_info(self):
        ''' Print all the info '''
        print("id:%s, sequence type:%s, sequence:%s, creator:%s"%(self.id,self.sequence_type,self.sequence,self.creator))
        return [self.id,self.sequence_type,self.sequence,self.creator]
        

    def validate(self): 
        ''' Validate the given sequence'''
        if self.sequence_type.upper() == 'DNA':
            valid = self.sequence.count('A')+self.sequence.count('C')+self.sequence.count('T')+self.sequence.count('G')
            if valid == len(self.sequence):
                return True
            else:
                print("Not valid DNA sequence")
                return False
        elif self.sequence_type.upper() == 'RNA':
            valid = self.sequence.count('A')+self.sequence.count('C')+self.sequence.count('U')+self.sequence.count('G')
            if valid == len(self.sequence):
                return True
            else:
                print("Not valid RNA sequence")
                return False
        else:
            print("You have not provided correctly the biological type of the sequence (DNA or RNA)")
            return False

sqs=Sequence(2,'dna','taga','eva')
sqs.validate()
sqs.print_info()
## THEMA 2 -END ##



## THEMA 3 ##
# create the connection with the database
import MySQLdb as mysql
mydb = mysql.connect(host="localhost",user="root", passwd = "1234", db="bnp55")
cursor = mydb.cursor()

# print the menu
print ("Select a number from the menu below")
print ("1: Insert new record")
print ("2: Delete existing record")
print ("3: Print record")
print ("4: Exit")
option = int(input("What do you want to do? Type a valid number: "))

while option!=4:
    if option == 1:
        id= input("Enter the id. If you don't know the id press enter: ")
        seq_type = str(input("Enter the biological type of the sequence (RNA or DNA): "))
        seq = str(input("Provide the sequence:  "))
        name = str(input("Type your name: "))
        seq1 = Sequence(1,seq_type, seq, name)
        x=seq1.validate()
        if x==False:
            mydb.close()
            option = int(input("Remember, 1:insert, 2:delete, 3:print, 4:exit. Enter a valid number: ")) 
        else:
            if id == "" :
              statement = """SELECT *FROM sequence WHERE id=(SELECT max(id) FROM sequence)"""
              cursor.execute(statement)
              max= cursor.fetchall()
              id = max[0][0] +1
              seq2 = Sequence(id,seq_type, seq, name)
              statement2= """ INSERT INTO Sequence (id, sequence_type,sequence,creator) VALUES (%s, %s, %s, %s)"""
              entry = seq2.print_info()
              cursor.execute(statement2,entry)
              mydb.commit()
              print("Your record has been succesfully inserted.")
              option = int(input("Remember, 1:insert, 2:delete, 3:print, 4:exit. Choose what do you want to do next: "))
            else: 
              seq3 = Sequence(id,seq_type, seq, name)
              statement2= """ INSERT INTO Sequence (id, sequence_type,sequence,creator) VALUES (%s, %s, %s, %s)"""
              entry = seq3.print_info()        
              cursor.execute(statement2,entry)
              mydb.commit()
              print("Your record has been succesfully inserted.")
              option = int(input("Remember, 1:insert, 2:delete, 3:print, 4:exit. Choose what do you want to do next: "))
            
    elif option == 2:
        delete = input("Which record do you want to delete? Please type the id: ")
        cursor.execute(""" SELECT COUNT(id) FROM Sequence WHERE id = %s""",[delete])
        results= cursor.fetchall()
        count= results[0][0]
        if count==0:
            print("Sorry, there is not record with that id")
            option = int(input("Remember, 1:insert, 2:delete, 3:print, 4:exit. Choose what do you want to do next: "))
        else:
            cursor.execute(""" SELECT * FROM Sequence WHERE id = %s""",[delete])
            result= cursor.fetchall()
            print(result)
            confirm = str(input("Are you sure you want to delete this record? y/n: "))
            while confirm != "y" and confirm != "n":
                 confirm = str(input("i dont understand type y for yes or n for no: "))
            if confirm == "y":
                cursor.execute(""" DELETE fROM Sequence WHERE id= %s""",[delete])
                mydb.commit()
                print("Your record has been deleted.")
                option = int(input("Remember, 1:insert, 2:delete, 3:print, 4:exit. Choose what do you want to do next: "))
            elif confirm == "n" :
                print("OK then...")
                option = int(input("Remember, 1:insert, 2:delete, 3:print, 4:exit. Choose what do you want to do next: "))
           
    elif option == 3:
        select = input("Which record do you want to print. Enter the id: ")
        cursor.execute(""" SELECT COUNT(id) FROM Sequence WHERE id = %s""",[select])
        results= cursor.fetchall()
        count= results[0][0]
        if count==0:
            print("Sorry, there is not record with that id")
            option = int(input("Remember, 1:insert, 2:delete, 3:print, 4:exit. Choose what do you want to do next: "))
        else:
            cursor.execute(""" select * from Sequence WHERE id= %s""",[select])
            results= cursor.fetchall()
            Sequence(results[0][0],results[0][1],results[0][2],results[0][3]).print_info() 
            option = int(input("Remember, 1:insert, 2:delete, 3:print, 4:exit. Choose what do you want to do next: "))
    elif option<1 or option>4:
            print("Try again, you have to type 1,2,3 or 4")
            option = int(input("Remember, 1:insert, 2:delete, 3:print, 4:exit. Enter a valid number: "))    
if option==4:
    cursor.execute(""" select * from Sequence""")
    results= cursor.fetchall()
    print(results)
    print("These are all the records frrom Sequence Table, now you will exit the program.")
    mydb.close()
## THEMA 3- END ##




















## THEMA 1 ##
import MySQLdb as mysql

## THEMA 2 ##
class Sequence():
    ''' Sequence class with id, sequence type (DNA,RNA), sequence and creator'''
    def __init__(self, id , sequence_type, sequence , creator) :
        self.id= id
        if sequence_type.upper() == 'DNA' or sequence_type.upper() == 'RNA':
            self.sequence_type= sequence_type.upper()
        else:
            print("Warning, You have to provide DNA or RNA for the sequence type")
            self.sequence_type=sequence_type.upper()
        self.sequence= sequence.upper()
        self.creator = creator


    def print_info(self):
        ''' Print all the info '''
        print("id:%s, sequence type:%s, sequence:%s, creator:%s"%(self.id,self.sequence_type,self.sequence,self.creator))
        return [self.id,self.sequence_type,self.sequence,self.creator]
        

    def validate(self): 
        ''' Validate the given sequence'''
        if self.sequence_type.upper() == 'DNA':
            valid = self.sequence.count('A')+self.sequence.count('C')+self.sequence.count('T')+self.sequence.count('G')
            if valid == len(self.sequence):
                return True
            else:
                print("Not valid DNA sequence")
                return False
        elif self.sequence_type.upper() == 'RNA':
            valid = self.sequence.count('A')+self.sequence.count('C')+self.sequence.count('U')+self.sequence.count('G')
            if valid == len(self.sequence):
                return True
            else:
                print("Not valid RNA sequence")
                return False
        else:
            print("You have not provided correctly the biological type of the sequence (DNA or RNA)")
            return False

sqs=Sequence(2,'dna','taga','eva')
sqs.validate()
sqs.print_info()
## THEMA 2 -END ##



## THEMA 3 ##
# create the connection with the database
import MySQLdb as mysql
mydb = mysql.connect(host="localhost",user="root", passwd = "1234", db="bnp55")
cursor = mydb.cursor()

# print the menu
print ("Select a number from the menu below")
print ("1: Insert new record")
print ("2: Delete existing record")
print ("3: Print record")
print ("4: Exit")
option = int(input("What do you want to do? Type a valid number: "))

while option!=4:
    if option == 1:
        id= (input("Enter the id. If you don't know the id press enter: "))
        seq_type = str(input("Enter the biological type of the sequence (RNA or DNA): "))
        seq = str(input("Provide the sequence:  "))
        name = str(input("Type your name: "))
        seq1 = Sequence(1,seq_type, seq, name)
        x=seq1.validate()
        if x==False:
            mydb.close()
            break
        else:
            statement = """SELECT id FROM sequence WHERE id=(SELECT max(id) FROM sequence)""" # select max(id) from sequence
            cursor.execute(statement)
            max= cursor.fetchall()
            try:
                id2 = max[0][0] +1
            except:
                id2 = 1
            print(id2)
            if id == "" :                   
              seq2 = Sequence(id2,seq_type, seq, name)
              statement2= """ INSERT INTO Sequence (id, sequence_type,sequence,creator) VALUES (%s, %s, %s, %s)"""
              entry = seq2.print_info()
              cursor.execute(statement2,entry)
              mydb.commit()
              print("Your record has been succesfully inserted.")
              option = int(input("Remember, 1:insert, 2:delete, 3:print, 4:exit. Choose what do you want to do next: "))
            else: 
              while True:
                  try :
                      seq3 = Sequence(id,seq_type, seq, name)
                      statement2= """ INSERT INTO Sequence (id, sequence_type,sequence,creator) VALUES (%s, %s, %s, %s)"""
                      entry = seq3.print_info()        
                      cursor.execute(statement2,entry)
                      mydb.commit()
                      print("Your record has been succesfully inserted.")
                      option = int(input("Remember, 1:insert, 2:delete, 3:print, 4:exit. Choose what do you want to do next: "))
                      break
                  except IntergrityError:
                      print("tha parei ayth thn timh",id2 )
                      id = id2            
    elif option == 2:
        delete = input("Which record do you want to delete? Please type the id: ")
        cursor.execute(""" SELECT COUNT(id) FROM Sequence WHERE id = %s""",[delete])
        results= cursor.fetchall()
        count= results[0][0]
        if count==0:
            print("Sorry, there is not record with that id")
            option = int(input("Remember, 1:insert, 2:delete, 3:print, 4:exit. Choose what do you want to do next: "))
        else:
            cursor.execute(""" SELECT * FROM Sequence WHERE id = %s""",[delete])
            result= cursor.fetchall()
            print(result)
            confirm = str(input("Are you sure you want to delete this record? y/n: "))
            while confirm != "y" and confirm != "n":
                 confirm = str(input("i dont understand type y for yes or n for no: "))
            if confirm == "y":
                cursor.execute(""" DELETE fROM Sequence WHERE id= %s""",[delete])
                mydb.commit()
                print("Your record has been deleted.")
                option = int(input("Remember, 1:insert, 2:delete, 3:print, 4:exit. Choose what do you want to do next: "))
            elif confirm == "n" :
                print("OK then...")
                option = int(input("Remember, 1:insert, 2:delete, 3:print, 4:exit. Choose what do you want to do next: "))           
    elif option == 3:
        select = input("Which record do you want to print. Enter the id: ")
        cursor.execute(""" SELECT COUNT(id) FROM Sequence WHERE id = %s""",[select])
        results= cursor.fetchall()
        count= results[0][0]
        if count==0:
            print("Sorry, there is not record with that id")
            option = int(input("Remember, 1:insert, 2:delete, 3:print, 4:exit. Choose what do you want to do next: "))
        else:
            cursor.execute(""" select * from Sequence WHERE id= %s""",[select])
            results= cursor.fetchall()
            Sequence(results[0][0],results[0][1],results[0][2],results[0][3]).print_info() 
            option = int(input("Remember, 1:insert, 2:delete, 3:print, 4:exit. Choose what do you want to do next: "))
    elif option<1 or option>4:
            print("Try again, you have to type 1,2,3 or 4")
            option = int(input("Remember, 1:insert, 2:delete, 3:print, 4:exit. Enter a valid number: "))    
if option==4:
    cursor.execute(""" select * from Sequence""")
    results= cursor.fetchall()
    print(results)
    print("These are all the records frrom Sequence Table, now you will exit the program.")
    mydb.close()
## THEMA 3- END ##
