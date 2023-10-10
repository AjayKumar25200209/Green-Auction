import mysql.connector
import json
from datetime import datetime,timedelta,date
from apscheduler.schedulers.background import BackgroundScheduler
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText







                        # connecting to mysql database
mydb = mysql.connector.connect(
        host="localhost",
  	    username="root",
  	    password="Ajay@2002",
        database="greenauction",
        pool_name=None,
        pool_reset_session=None
)

mycursor = mydb.cursor(dictionary=True)





def test():
    try:
        time=datetime.now().replace(microsecond=0,second=0)
        timee= str(time.time())
        mycursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")
        mycursor.execute("select * from auctioninfo where etime<=%s and status='active' " ,(timee,))
        result=mycursor.fetchall()
        print(result)
        if result:
            for x in result:
                
                sender_email="ajayjeyapal@gmail.com"
                recever_email=x["aoemail"]
                subject="Green Auction"
                s_password="vxclabpkwfwwjhma"
                
                nb=x["nbid"]
                print(nb)
                if nb :
                    data=json.loads(x["biddings"]) 
                    bidno=f'bidno{x["nbid"]}'
                    html_content=  f"""
                                    
                                    
                                    <h1>Hi {x["aowner"]} </h1>
                                    <h3>Auction Number : {x["ano"]}</h3>
                                    <p>Your Auction was Successfully Completed </p>
                                    <h3>Auction Winner Contact Details are below</h3>
                                    <p>Name : {x["chbidder"]} <br>Email Id : {data["bidding"][bidno]["bidderemail"]} <br>Mobile Number : {data["bidding"][bidno]["biddernumber"]}</p>
                                    <p ></p>"""
                else:
                    html_content=  f"""
                                    
                                    
                                    <h1>Hi {x["aowner"]} </h1>
                                    <h3>Auction Number : {x["ano"]}</h3>
                                    <p>No One Bidded For Your Auction <br>Dont't Worry Create An another auction and I Hope For The best And thanks for using Our Website   </p>"""
                                    
                            
                

                message=MIMEMultipart()
                message["from"]=sender_email
                message["to"]=recever_email
                message["subject"]=subject
                message.attach(MIMEText(html_content,"html"))

                smtp_server="smtp.gmail.com"
                port = 587

                server=smtplib.SMTP(smtp_server,port)
                server.starttls()
                server.login(sender_email,s_password)
                server.sendmail(sender_email,recever_email,message.as_string())
                server.quit()
                
                mycursor.execute("update auctioninfo set status='completed' where ano=%s" ,(x["ano"],) )
                mydb.commit()
                print("its working")
            
        else:
                print("There is no auction to send email in this minute" ,timee)
    except Exception as e:
        print(e)
    
sched=BackgroundScheduler()
job=sched.add_job(test,"interval",minutes=1)
sched.start()

while True:
    pass