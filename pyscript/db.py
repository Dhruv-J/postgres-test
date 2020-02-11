import psycopg2

#connect to the db
con = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres")

cur = con.cursor()
insertQuery = 'insert into public.choice_table (id, class_name, start_time, professor, building, choice) values (%s, %s, %s, %s, %s, %s)'
toInsert = (4, 'sampleClass', '12:00 PM', 'sampleProfessor', 'Bascom Hall', 'g')
cur.execute(insertQuery, toInsert)
cur.execute('select id, choice from public.choice_table')
rows = cur.fetchall()
for r in rows:
    print(r)
    #print("r[0]: "+r[0]+" r[1]: "+r[1])

#close the connections
con.close()
