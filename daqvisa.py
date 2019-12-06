#!/usr/bin/python
import visa
import MySQLdb
import time
import schedule # To schedule time for the program to execute

qw=visa.ResourceManager()
er=qw.open_resource('USB0::10893::20737::MY58001167::0::INSTR')
print(er.query('*IDN?'))
time.sleep(1)
er.write("*RST")
time.sleep(0.5)
er.write("*CLS")
time.sleep(0.5)
er.write("ROUT:SCAN (@203)")
time.sleep(0.5)
er.write("CONF:TEMP (@203)")

try:
    db=MySQLdb.connect("127.0.0.1", "nectec", "1q2w3e4r", "Temperaturedb")
    curs=db.cursor()
    print("Successfully connected to Database")
    update=True
    while update:
        def job():
           from datetime import datetime
           now=datetime.now()
           datetime=now.strftime('%Y-%m-%d %H:%M:%S')
           #time.sleep(0.5)
           temp = {}
           er.write("MEAS:TEMP? (@203)")
           temp['value']=float(er.read())
           qq=temp['value']
           print("%.2f" % qq)
           #time.sleep(0.5)
           curs.execute("INSERT INTO DAQ970A_DATA VALUES (%s, %s)", (datetime, qq, ))
           #time.sleep(0.5)
           print("Data uploaded to Database")
           db.commit()

           #time.sleep(5)
        schedule.every(10).minutes.do(job)
        while True:
            schedule.run_pending()

except Exception as e:
      print (e)
      update=False
      curs.close
      db.close

