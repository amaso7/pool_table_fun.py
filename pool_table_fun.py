from datetime import datetime
datetime=datetime.now()
current_time=datetime

tables=[]

class Table:
    def __init__(self, number):
       self.number = number
       self.occupied = False
       self.start_time = None
       self.end_time = None
       self.time_played = None
       self.current_time = None
       self.cost=None

    def checkout(self):
      self.occupied=True
      self.start_time=datetime.now()
      print(f"You checkout Table {self.number} {self.occupied} {self.start_time.strftime('%m/%d/%Y %H:%M%:%S')}")


    def checkin(self):
        self.occupied=False
        self.start_time=None
        self.end_time= delta.time.now()
        self.time_played=self.end_time-self.start_time
        print(f"Table Closed  {self.number} {self.occupied} {self.end_time.strftime('%m/%d/%Y %H:%M%:%S')}")
           
       
def to_add_file():
     date=str(datetime.now())
     file_ext=".txt"
     admin_file=date + file_ext
     with open(admin_file,"a") as file:
         for table in tables:
            table_info=f"Table {table.number} Start time: {table.start_time} End time{table.end_time} Time played: {table.time_played} Cost:{table.cost}\n"
            file.write(table_info)
