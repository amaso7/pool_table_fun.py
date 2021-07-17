from datetime import datetime
datetime=datetime.now()
current_time=datetime
tables=[]
from pool_table_fun import Table 
 
for i in range (1,13):
  table=Table(i)
  tables.append(table)

def display_tables():
    
    for table in tables:
        if table.occupied==False:
            status="Un-Occupied"
            print(f"Table {table.number}: {status}")

        else:
            status="Occupied"
            print(f"\n Table--{table.number} start_time--{table.start_time.strftime('%m/%d/%Y %H:%M%:%S')}  status--{table.occupied} ")

def to_add_file():
     date=str(datetime.now())
     file_ext=".txt"
     file_name=date + file_ext
     with open(file_name,"w") as file:
         array=[]
         for table in tables:
            table_info=f"Table {table.number} Start time: {table.start_time} End time{table.end_time} Time played: {table.time_played} Cost:{table.cost}\n"
            file.write(table_info)        
  
print ("Welcome to the pool lounge")
print ("1-choose table: ")
print ("2-check out")
print ("3-view tables/admin")
print("enter q to quit")


while True:

    choice=input("")
   

    try:
        if choice== "1":

            display_tables()
            table_number=int(input("Enter table # to checkin:"))
            table=tables[table_number-1]
            table.time_start=datetime.now()
            table.checkout()

           

        elif choice=="2":
            display_tables()
            table_number=int(input("Enter Checkin Number:"))
            table=tables[table_number-1]
            table.end_time=datetime.now()
            print(f"Table {table_number} has been closed out at: {table.end_time-table.str_time('%m/%d/%Y %H:%M%:%S')}")


        elif choice=="3":
            for table in tables:
                print(f"Table # {table.number}-- Date & time:--{current_time.strftime('%m/%d/%Y %H:%M%:%S')}--occupied?--{table.occupied}")

        elif choice=="q":
            break

        else: 

             print("GOODBYE")

    except IndexError:
        print("12 TOTAL TABLES PLEASE CHOOSE A NUMBER IN RANGE")
        to_add_file()