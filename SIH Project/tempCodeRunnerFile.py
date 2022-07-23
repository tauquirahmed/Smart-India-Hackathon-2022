 # def fetch_data(self):
    #   conn=mysql.connector.connect(host="localhost", username="root", password="9831035162@Sonu", database="SIH2022")
    #   my_cursor = conn.cursor()
    #   my_cursor.execute("select * from student")
    #   data=my_cursor.fetchall()

    #   if len(data)!=0:
    #     self.student_table.delete(*self.student_table.get_children())
    #     for i in data:
    #       self.student_table.insert('',END, values=i)
    #     conn.commit()
    #   conn.close()
