from flask import Flask,request,url_for,render_template,session,redirect
import mysql.connector
import json
import random
from datetime import datetime,timedelta,date
from apscheduler.schedulers.background import BackgroundScheduler
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

days=3
app.secret_key="ajaykumar"
app.permanent_session_lifetime =  3*24*60*60











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
                    recever_email2= data["bidding"][bidno]["bidderemail"]
                    html_content=  f"""
                                    
                                    
                                    <h1>Hi {x["aowner"]} </h1>
                                    <h3>Auction Number : {x["ano"]}</h3>
                                    <p>Your Auction was Successfully Completed and thanks for using our Website </p>
                                    <h3>Auction Winner Contact Details are below</h3>
                                    <p>Name : {x["chbidder"]} <br>Email Id : {data["bidding"][bidno]["bidderemail"]} <br>Mobile Number : {data["bidding"][bidno]["biddernumber"]}</p>
                                    <p ></p>"""
                    mycursor.execute("select number from userinfo where email=%s " ,(x["aoemail"],))
                    result2=mycursor.fetchone()
                    html_content2=  f"""
                                    
                                    
                                    <h1>Hi  {data["bidding"][bidno]["biddername"]} </h1>
                                    <h3>Auction Number : {x["ano"]}</h3>
                                    <p>Your Auction was Successfully Completed and thanks for using our Website </p>
                                    <h3>Auction Owner Contact Details are below</h3>
                                    <p>Name : {x["aowner"]} <br>Email Id : {x["aoemail"]} <br>Mobile Number : {result2["number"]}</p>
                                    <p ></p>"""
                    message2=MIMEMultipart()                    
                    message2["from"]=sender_email
                    message2["to"]=recever_email2
                    message2["subject"]=subject
                    message2.attach(MIMEText(html_content2,"html"))

                    smtp_server="smtp.gmail.com"
                    port = 587

                    server=smtplib.SMTP(smtp_server,port)
                    server.starttls()
                    server.login(sender_email,s_password)
                    server.sendmail(sender_email,recever_email2,message2.as_string())

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



print(app.permanent_session_lifetime )











@app.route('/dashboard',methods=['GET', 'POST'])
def dashboard():
    if request.method == "GET":

        if session.get('uemail') is not None :
            
            try:
                mycursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")
                mydb.commit()

                mycursor.execute("select * from auctioninfo where status='active'; " )

                result = mycursor.fetchall()
                
                random.shuffle(result)
                
                session["array"]=[]
                array=session["array"]
                for x in result:
                    
                    data=x["ano"]
                    array.append(data)
                
                msg="No auction is Currently Active"
                if result:
                    return render_template("dashboard.html",result=result)
                else:
                    return render_template("dashboard.html",result=result ,msg=msg) 
                     
                    

                
                
            except Exception as e:
                print("error : ",e)
                msg="Sorry Something went wrong please try again later"
                return render_template("dashboard.html",msg=msg)
        else :
            
            return redirect(url_for("sessioncheck"))
        
@app.route('/test',methods=['GET', 'POST'])
def test():
    if request.method == "GET":
        print(session["array"])

        return "success"
        
        
    
@app.route('/',methods=['GET', 'POST'] )
def sessioncheck():
    #session['uemail'] = None
    #session.pop('uemail',None)

    if request.method=="GET":
        if session.get('uemail') is not None:
            return redirect("/dashboard")
        else :
            return render_template("index.html")
    elif request.method=="POST":
        return "eppadi da panna itha ethuku da unnaku intha polapuu "
    
            # my auction active status route
@app.route('/My_Auction',methods=['GET', 'POST'] )
def myauction():
    if request.method=="GET":
        if session.get('uemail')  is not None:
            try:
                mycursor.execute("select * from auctioninfo where status='active'and aoemail=%s ", (session["uemail"],))

                result = mycursor.fetchall()
                result.reverse()
                if result:
                    return render_template("myauction.html",result=result) 
                else:
                    msg="No auction is Currently Active"
                    return render_template("myauction.html",msg=msg)

                    
                
            except Exception as e:
                print("error : ",e)
                msg=f"Sorry Something went wrong please try again later : {e}"
                return render_template("myauction.html",msg=msg)
            
            
        else:
            return redirect(url_for("sessioncheck"))
        
    else:
        return redirect(url_for("sessioncheck"))
    
@app.route('/activemyauction',methods=['GET', 'POST'] )
def activemyauction():
    if request.method=="POST":
        if session.get('uemail')  is not None:
            try:
                mycursor.execute("select * from auctioninfo where  aoemail=%s and status='active' ", (session["uemail"],))

                result = mycursor.fetchall()
                result.reverse()
                if result:
                    return render_template("activemyauction.html",result=result) 
                else:
                    msg="No auction is Currently active"
                    return render_template("activemyauction.html",msg=msg)
                
                
            except Exception as e:
                print("error : ",e)
                msg=f"Sorry Something went wrong please try again later : {e}"
                return render_template("activemyauction.html",msg=msg)
            
            
        else:
            return redirect(url_for("sessioncheck"))
        
    else:
        return redirect(url_for("sessioncheck"))
    
    
@app.route('/completedmyauction',methods=['GET', 'POST'] )
def completedmyauction():
    if request.method=="POST":
        if session.get('uemail')  is not None:
            try:
                mycursor.execute("select * from auctioninfo where  aoemail=%s and status='completed' ", (session["uemail"],))

                result = mycursor.fetchall()
                result.reverse()
                if result:
                    return render_template("completedmyauction.html",result=result) 
                else:
                    msg="No auction is Currently Completed"
                    return render_template("completedmyauction.html",msg=msg)
                
                
            except Exception as e:
                print("error : ",e)
                msg=f"Sorry Something went wrong please try again later : {e}"
                return render_template("completedmyauction.html",msg=msg)
            
            
        else:
            return redirect(url_for("sessioncheck"))
        
    else:
        return redirect(url_for("sessioncheck"))
    
@app.route('/logout',methods=['GET', 'POST'] )
def logout():
    if request.method=="GET":
        if session.get('uemail')  is not None:
            session['uemail']=None
            session["username"] = None
            session["unumber"] = None
            session['password'] = None
            return redirect(url_for("sessioncheck"))
        else:
            return redirect(url_for("sessioncheck"))
    else:
        return redirect(url_for("sessioncheck"))
        

            
    
    
    
                #getting the input and stored in session and mysql database  
@app.route('/register',methods=['GET', 'POST'])
def get():
    if request.method == "POST":

                # getting the user inputs
        username = request.form.get('uname')
        useremail = request.form.get('uemail')
        usernumber = request.form.get('unumber')
        userpassword = request.form.get('upass')
        
        if useremail and username and usernumber and userpassword:
            
                # storing in session
                session["username"] = username
                session["uemail"] = useremail
                session["unumber"] = usernumber
                session['password'] = userpassword
                
                try:
                    mycursor=mydb.cursor(dictionary=True)
                    mycursor.execute("select name from userinfo where name=%s", (username,))
                    myresult2=mycursor.fetchall()    
                    mycursor.execute("select email from userinfo where email=%s", (useremail,))
                    myresult1=mycursor.fetchall()
                    mycursor.execute("select number from userinfo where number=%s", (usernumber,))
                    myresult3=mycursor.fetchall()
                    
                except Exception as e:
                    return f"Error: {e} Error Occurred please try Again later "
                    
               
                if not myresult1  and   not myresult2 and not myresult3 :
                    mycursor.execute(" insert into userinfo (name,email,number,password ) values(%s,%s,%s,%s)" ,(username,useremail,usernumber,userpassword))
                    mydb.commit()
                    return "ok"
                elif myresult1  and   not myresult2 and not myresult3 : 
                    return "This email id already have an account"
                elif not myresult1  and   myresult2 and not myresult3 : 
                    return "This username already taken"
                elif not myresult1  and   not myresult2 and  myresult3 : 
                    return "This phone number already have an account"
                elif myresult1 and myresult2 and not myresult2:
                    return " This email id and username already Exists"
                elif not myresult1 and myresult2 and myresult3:
                    return "This username and phone number Already Exits"
                elif myresult1 and not myresult2 and myresult3:
                    return "This Email id and phone number Already have an Account"
                elif myresult1 and myresult2 and myresult3:
                    return "Already an account exists with this email id ,username and phone number "
                    
                    
                else:
                    return " from server Something Went Wong please try Again Later"
        else:
            return "Enter all the details and then click"
    else:
        return  redirect(url_for("sessioncheck"))
    
                # login functions
@app.route( '/login', methods=["GET",  "POST"] )
def login():
    if request.method == "POST":
        useremail = request.form.get('lemail').strip()
        userpassword = request.form.get('lpass').strip()
        if useremail and userpassword:
            mycursor.execute("select * from userinfo where email=%s" ,(useremail,))
            result1 = mycursor.fetchone()
            
            if result1:
                mycursor.execute("select password from userinfo where email=%s" ,(useremail,))
                result2 = mycursor.fetchone()
                dpassword=result2["password"]
                if dpassword==userpassword:
                    session["uemail"] = useremail
                    session['password'] = userpassword
                    session['username'] = result1['name']
                    session['unumber'] = result1['number']
                    
                    return "ok"
                else:
                    return "You Entered a incorrect Password"
            else:
                return "no user in this email" 
        else:
            return "Enter your details and then click" 
    else:
        return redirect(url_for("sessioncheck"))
        
        # getting the bidding ammount for auctions
@app.route( '/bid', methods=["GET",  "POST"] )
def bid():
    if request.method=="POST":
        
        data = request.data.decode("utf-8")
        
        
        data2=json.loads(data)
        print(data2)
        if data2["ammount"]=="" :
            print("none value")
            return "Enter the ammount and then click"
        elif data2["ano"]=="" :
            print("no value")
            return "Can't get the auction Number "
        else:
            
            
            ano=data2["ano"]
            cprice=data2["ammount"]
            mycursor.execute("select * from auctioninfo where ano=%s",(ano,))
            result = mycursor.fetchone()
            if result["aoemail"]==session["uemail"]:
                return "you cannot bid for your own auction"
            elif result["chbidder"]==session["username"]:
                return "Already You are the highest bidder for this auction"
            
                
            else:
            
           

                nnbid=result["nbid"]
                try:
                    if nnbid is None:
                            if int(result["sprice"])  >= int(data2["ammount"]):
                                return "your Bidding ammount is less than the starting price of this auction "
                            else:
                                mycursor.execute("update auctioninfo set nbid=1  where ano=%s", (ano,))
                                mydb.commit()
                                bid_data={"bidno1":{"bidderemail":session["uemail"],"biddername":session["username"],"biddernumber":session["unumber"],"bidammount":data2["ammount"],"nobid":1}}
                                bid={"bidding":bid_data}
                                jbid=json.dumps(bid)
                                
                                chbidder=session["username"]
                                mycursor.execute(" update auctioninfo set biddings=%s , chbidder=%s ,cprice=%s where ano=%s",(jbid,chbidder,cprice,ano))
                                mydb.commit()
                                bdetail={"bidding":{"bidno1":{"bidnum":1,"ano":ano,"bammount":data2["ammount"]}}}
                                jbdetail=json.dumps(bdetail)
                                datee=date.today()
                                value=(ano,session["username"],session["uemail"],jbdetail,datee,1)
                                
                                mycursor.execute("insert into mybiddinginfo (ano,biddername,bidderemail,biddetail,date,nbid) values(%s,%s,%s,%s,%s,%s)",(value))
                                mydb.commit()
                                return "data stored"                        
                    else:
                            if int(result["cprice"])  >= int(data2["ammount"]):
                                return "your Bidding ammount is less than the current price of this auction "
                            else:
                                nbid=nnbid+1
                                mycursor.execute("update auctioninfo set nbid=%s  where ano=%s", (nbid,ano,))
                                olddata=json.loads(result["biddings"])
                                bidd=f"bidno{nbid}"

                                
                                newdata = {bidd:{"bidderemail":session["uemail"],"biddername":session["username"],"biddernumber":session["unumber"],"bidammount":data2["ammount"],"nobid":nbid}}
                                
                                olddata["bidding"].update(newdata)
                                jdata=json.dumps(olddata)
                                mycursor.execute(" update auctioninfo set biddings=%s , chbidder=%s ,cprice=%s where ano=%s",(jdata,session["username"],cprice,ano))
                                print("ithu varaikum okl")
                                mycursor.execute("select * from mybiddinginfo where bidderemail=%s and ano=%s ", (session["uemail"],ano))
                                mybid=mycursor.fetchone()
                                if mybid is not None:
                                    nobid=mybid["nbid"]+1
                                    jstr=mybid["biddetail"]
                                    odata=json.loads(jstr)
                                    print(jstr)
                                    bidname=f"bidno{nobid}"
                                    
                                    
                                    # jodata=json.loads(odata)
                                    bdetail2={bidname:{"bidnum":nbid,"ano":ano,"bammount":data2["ammount"]}}
                                    odata["bidding"].update(bdetail2)
                                    jbdetail1=json.dumps(odata)
                                
                                    print(jbdetail1)
                                    
                                    mycursor.execute("update mybiddinginfo set biddetail=%s , nbid=%s where bidderemail=%s and ano=%s ",(jbdetail1,nobid,mybid["bidderemail"],ano))
                                    mydb.commit()
                                    print("already bidded")
                                    return "data stored" 
                                else:
                                    datee=date.today()
                                    
                                    bdetail={"bidding":{"bidno1":{"bidnum":nbid,"ano":ano,"bammount":data2["ammount"]}}}
                                    jbdetail=json.dumps(bdetail)
                                    value=(ano,session["username"],session["uemail"],jbdetail,datee,1)
                                    mycursor.execute("insert into mybiddinginfo (ano,biddername,bidderemail,biddetail,date,nbid) values(%s,%s,%s,%s,%s,%s)",(value))
                                    mydb.commit()
                                    print("not already bidded")
                                    return "data stored" 
                            
                            
                        
                except Exception as e:
                        mydb.rollback()
                        
                        return f"Error in storing the data and reset action no : {e}"
    else:
        return "error"
    
@app.route( '/createauction', methods=["GET",  "POST"] )
def createauction():
    if request.method=="POST":
        productname =request.form.get("productname").lower().strip()
        print("product nname: ",productname)
        quantity =request.form.get("quantity").strip()
        place =request.form.get("place").strip()
        price =request.form.get("price").strip()
        time =request.form.get("time")
        district = request.form.get("district")
        description =request.form.get("description")
        print(district,productname,quantity,place,price,time,description)
        if not productname:
            return "Please Enter the Product Name"
        elif not quantity:
            return "Please Enter the quantity "
        elif not place:
            return "Please Enter the place of Farm "
        elif not time:
            return "Please Enter the Time Duration "
        elif not district:
            return "Please Enter the district "
        elif not price:
            return "Please Enter the Starting price "
        try:
            if time=="5min":
                time4=time.strip("min")
                print("time4" ,time4)
                time3=int(time4)
                namee=session.get("username")
                email=session.get("uemail")
                datee=date.today()
                ctime=datetime.now().replace(microsecond=0,second=0)
                stime=ctime.time()
                hour=timedelta(minutes=time3)
                etime=(ctime+hour).time()
                print(etime)
                status="active"
                values=(namee,productname,price,quantity,place,time4,district,description,stime,etime,datee,status,email)
                mycursor.execute("insert into auctioninfo (aowner,pname,sprice,quantity,flocation,time,district,description,stime,etime,date,status,aoemail) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,(values))
                mydb.commit()
                return "Auction Successfully Created"
            else:
                time2=int(time)
                namee=session.get("username")
                email=session.get("uemail")
                datee=date.today()
                ctime=datetime.now().replace(microsecond=0,second=0)
                stime=ctime.time()
                hour=timedelta(hours=time2)
                etime=(ctime+hour).time()
                print(etime)
                status="active"
                values=(namee,productname,price,quantity,place,time,district,description,stime,etime,datee,status,email)
                mycursor.execute("insert into auctioninfo (aowner,pname,sprice,quantity,flocation,time,district,description,stime,etime,date,status,aoemail) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,(values))
                mydb.commit()
                return "Auction Successfully Created"
            
        except Exception as e:
            return f"Something Went Wrong"
        
        
@app.route( '/getfulldetail', methods=["GET",  "POST"] )
def getfulldetail():
    if request.method=="POST":
        
        data=request.data.decode("UTF-8")
        ano=json.loads(data)
        
        value=ano["ano"]
        try:
    
           mycursor.execute("select * from auctioninfo where ano=%s ",(value,))
           result1 = mycursor.fetchone()
           result=json.dumps(result1)
           return result
        except Exception as e:
           return "error"
        

    else:
        return redirect(url_for("sessioncheck"))
    
    
    # getting the bidded auction info 
@app.route( '/My_Bidding', methods=["GET",  "POST"] )
def mybidding():
    if request.method=="GET":
        if session.get('uemail') is not None:
            #datee=date.today()
            session["array2"]=[]
            array2=session["array2"]
            session["array4"]=[]
            array4=session["array4"]
            try:
                mycursor.execute("select * from mybiddinginfo where bidderemail=%s",( session["uemail"] ,) )
                result1=mycursor.fetchall()
                for x in result1:
                    mycursor.execute("select * from auctioninfo where ano=%s and status='active' ",(x["ano"],))
                    result2=mycursor.fetchone()
                    if result2:
                        array2.append(result2)
                    else:
                        array4.append(result2)
                array2.reverse()
                
                if array2:
                    return render_template("mybidding.html",array2=array2)
                else:
                    msg="No action is Currently Active that you have Bidded"
                    return render_template("mybidding.html" ,msg=msg)
                    
                
            except Exception as e:
                msg=f"Error {e}"
                
                return render_template("mybidding.html",msg=msg)
        else:
            msg="Sorry Something went Wrong Please try again later"
            return redirect(url_for("sessioncheck"))
        
@app.route( '/completedmybidding', methods=["GET",  "POST"] )
def completedmybidding():
    if request.method=="POST":
        if session.get('uemail') is not None:
            #datee=date.today()
            session["array2"]=[]
            array2=session["array2"]
            session["array4"]=[]
            array4=session["array4"]
            try:
                mycursor.execute("select * from mybiddinginfo where bidderemail=%s",( session["uemail"] ,) )
                result1=mycursor.fetchall()
                for x in result1:
                    mycursor.execute("select * from auctioninfo where ano=%s and status='completed' ",(x["ano"],))
                    result2=mycursor.fetchone()
                    if result2:
                        array2.append(result2)
                    else:
                        array4.append(result2)
                array2.reverse()
                
                if array2:
                    return render_template("completedmybidding.html",array2=array2)
                else:
                    msg="No action is Currently Completed that you have Bidded"
                    return render_template("completedmybidding.html" ,msg=msg)
                    
                
            except Exception as e:
                msg=f"Error {e}"
                
                return render_template("completedmybidding.html",msg=msg)
        else:
            msg="Sorry Something went Wrong Please try again later"
            return redirect(url_for("sessioncheck"))
        
@app.route( '/activemybidding', methods=["GET",  "POST"] )
def activemybidding():
    if request.method=="POST":
        if session.get('uemail') is not None:
            #datee=date.today()
            session["array2"]=[]
            array2=session["array2"]
            session["array4"]=[]
            array4=session["array4"]
            try:
                mycursor.execute("select * from mybiddinginfo where bidderemail=%s",( session["uemail"] ,) )
                result1=mycursor.fetchall()
                for x in result1:
                    mycursor.execute("select * from auctioninfo where ano=%s and status='active' ",(x["ano"],))
                    result2=mycursor.fetchone()
                    if result2:
                        array2.append(result2)
                    else:
                        array4.append(result2)
                array2.reverse()
                
                if array2:
                    return render_template("activemybidding.html",array2=array2)
                else:
                    msg="No action is Currently Active that you have Bidded"
                    return render_template("activemybidding.html" ,msg=msg)
                    
                
            except Exception as e:
                msg=f"Error {e}"
                
                return render_template("activemybidding.html",msg=msg)
        else:
            msg="Sorry Something went Wrong Please try again later"
            return redirect(url_for("sessioncheck"))
        
@app.route( '/Profile', methods=["GET",  "POST"] )
def profile():
    if session.get('uemail') is not None:
        try:
            result={"name":session["username"],"email":session["uemail"],"number":session["unumber"]}
            return render_template("profile.html" , result=result)
        except Exception as e:
            return redirect(url_for("sessioncheck"))
    else:
        return redirect(url_for("sessioncheck"))

        

@app.route( '/About', methods=["GET",  "POST"] )
def about():
    if session.get('uemail') is not None:
        return render_template("about.html")
    else:
        return redirect(url_for("sessioncheck"))

        


    # seaching specific auction details
@app.route( '/auctiondetail', methods=["GET",  "POST"] )
def auctiondetail():
    if request.method=="POST":
        
        data=request.form.get("formsearch")
        try:
            mycursor.execute("select * from auctioninfo where ano=%s",(data,))
            result=mycursor.fetchone()
            if result:
                print(type(result))
                return result
            else:
                print("no data")
                return "No Data in This Auction Number"
            
        except Exception as e:
            return "Please try again later"
    else:
        return redirect(url_for("sessioncheck"))
    
@app.route( '/track', methods=["GET",  "POST"] )
def track():
    if request.method=="POST":
        ano=request.data.decode("UTF-8")
        ano=json.loads(ano)
        print(ano["ano"])
        try:
            mycursor.execute("select * from mybiddinginfo where ano=%s and bidderemail=%s" ,(ano["ano"],session["uemail"]))
            result=mycursor.fetchone()
            if result:
                result2=json.loads(result["biddetail"])
                result3=result2["bidding"]
                print(result2)
                i=1
                
                
                return render_template("track.html" , result=result ,result3=result3,i=i)
            else:
                return " can't able to fetch the data"
            
        except Exception as e:
            print(e)
            return f"Error happend so please try again later"
        
        # myauction track biddings
        
@app.route( '/track1', methods=["GET",  "POST"] )
def track1():
    if request.method=="POST":
        ano=request.data.decode("UTF-8")
        ano=json.loads(ano)
        print(ano["ano"])
        try:
            mycursor.execute("select * from auctioninfo where ano=%s and aoemail=%s" ,(ano["ano"],session["uemail"]))
            result=mycursor.fetchone()
            if result:
                biddings=result["biddings"]
                if biddings:
                    result2=json.loads(result["biddings"])
                    
                    result3=result2["bidding"]
                    print(result2)
                    i=1
                    
                    
                    return render_template("track2.html" , result=result ,result3=result3,i=i)
                else:
                    return "no"
            else:
                return "can't able to fetch the data"
            
        except Exception as e:
            print(e)
            return f"Error happend so please try again later"
        
        # filter the data 
@app.route( '/filter', methods=["GET",  "POST"] )
def filter():
    if request.method=="POST":
        try:
            product=request.form.get("productname")
            quantity=request.form.get("quantity")
            disrict=request.form.get("district")
            qfilter=request.form.get("qfilter")
            if not qfilter and not quantity and not product and not disrict:
                print(disrict)
                return "Please Enter Any Detail"
            elif qfilter and quantity :
                
                if  product  and disrict:
                    if qfilter=="less":
                        mycursor.execute("select * from auctioninfo where pname=%s and district=%s and quantity<%s and status='active' " , (product,disrict,quantity))
                        result=mycursor.fetchall()
                        if result:
                            return render_template("filter.html",result=result)
                        else:
                            msg="No Auction is Currently Active With The Given Filter"
                            return render_template("filter.html",result=result ,msg=msg)
                    elif qfilter=="greater":
                        mycursor.execute("select * from auctioninfo where pname=%s and district=%s and quantity>%s and status='active' " , (product,disrict,quantity))
                        result=mycursor.fetchall()
                        if result:
                            return render_template("filter.html",result=result)
                        else:
                            msg="No Auction is Currently Active With The Given Filter"
                            return render_template("filter.html",result=result ,msg=msg)
                    elif qfilter=="equal":
                        mycursor.execute("select * from auctioninfo where pname=%s and district=%s and quantity=%s and status='active' " , (product,disrict,quantity))
                        result=mycursor.fetchall()
                        if result:
                            return render_template("filter.html",result=result)
                        else:
                            msg="No Auction is Currently Active With The Given Filter"
                            return render_template("filter.html",result=result ,msg=msg)
                elif not product and not disrict:
                    if qfilter=="less":
                        mycursor.execute("select * from auctioninfo where  quantity<%s and status='active' " , (quantity,))
                        result=mycursor.fetchall()
                        if result:
                            return render_template("filter.html",result=result)
                        else:
                            msg="No Auction is Currently Active With The Given Filter"
                            return render_template("filter.html",result=result ,msg=msg)
                    elif qfilter=="greater":
                        mycursor.execute("select * from auctioninfo where  quantity>%s  and status='active' " , (quantity,))
                        result=mycursor.fetchall()
                        if result:
                            return render_template("filter.html",result=result)
                        else:
                            msg="No Auction is Currently Active With The Given Filter"
                            return render_template("filter.html",result=result ,msg=msg)
                    elif qfilter=="equal":
                        mycursor.execute("select * from auctioninfo where  quantity=%s  and status='active'" , (quantity,))
                        result=mycursor.fetchall()
                        if result:
                            return render_template("filter.html",result=result)
                        else:
                            msg="No Auction is Currently Active With The Given Filter"
                            return render_template("filter.html",result=result ,msg=msg)
                elif  product and not disrict:
                    if qfilter=="less":
                        mycursor.execute("select * from auctioninfo where pname=%s and quantity<%s and status='active' " , (product,quantity))
                        result=mycursor.fetchall()
                        if result:
                            return render_template("filter.html",result=result)
                        else:
                            msg="No Auction is Currently Active With The Given Filter"
                            return render_template("filter.html",result=result ,msg=msg)
                    elif qfilter=="greater":
                        mycursor.execute("select * from auctioninfo where pname=%s and quantity>%s and status='active' " , (product,quantity))
                        result=mycursor.fetchall()
                        if result:
                            return render_template("filter.html",result=result)
                        else:
                            msg="No Auction is Currently Active With The Given Filter"
                            return render_template("filter.html",result=result ,msg=msg)
                    elif qfilter=="equal":
                        mycursor.execute("select * from auctioninfo where pname=%s and  quantity=%s and status='active' " , (product,quantity))
                        result=mycursor.fetchall()
                        if result:
                            return render_template("filter.html",result=result)
                        else:
                            msg="No Auction is Currently Active With The Given Filter"
                            return render_template("filter.html",result=result ,msg=msg)
                elif  not product  and disrict:
                    
                    if qfilter=="less":
                        mycursor.execute("select * from auctioninfo where  district=%s and quantity<%s and status='active' " , (disrict,quantity))
                        result=mycursor.fetchall()
                        if result:
                            return render_template("filter.html",result=result)
                        else:
                            msg="No Auction is Currently Active With The Given Filter"
                            return render_template("filter.html",result=result ,msg=msg)
                    elif qfilter=="greater":
                        mycursor.execute("select * from auctioninfo where  district=%s and quantity>%s  and status='active'" , (disrict,quantity))
                        result=mycursor.fetchall()
                        if result:
                            return render_template("filter.html",result=result)
                        else:
                            msg="No Auction is Currently Active With The Given Filter"
                            return render_template("filter.html",result=result ,msg=msg)
                    elif qfilter=="equal":
                        mycursor.execute("select * from auctioninfo where  district=%s and quantity=%s and status='active' " , (disrict,quantity))
                        result=mycursor.fetchall()
                        if result:
                            return render_template("filter.html",result=result)
                        else:
                            msg="No Auction is Currently Active With The Given Filter"
                            return render_template("filter.html",result=result ,msg=msg)
                     
            
            elif not qfilter and not quantity:
                if product and disrict:
                    mycursor.execute("select * from auctioninfo where  district=%s and pname=%s and status='active' " , (disrict,product))
                    result=mycursor.fetchall()
                    if result:
                        return render_template("filter.html",result=result)
                    else:
                        msg="No Auction is Currently Active With The Given Filter"
                        return render_template("filter.html",result=result ,msg=msg)
                    
               
                elif  product and not disrict:
                    mycursor.execute("select * from auctioninfo where pname=%s and status='active' " , (product,))
                    result=mycursor.fetchall()
                    if result:
                        return render_template("filter.html",result=result)
                    else:
                        msg="No Auction is Currently Active With The Given Filter"
                        return render_template("filter.html",result=result ,msg=msg)
                        
                elif not product and  disrict:
                    mycursor.execute("select * from auctioninfo where  district=%s and status='active' " , (disrict,))
                    result=mycursor.fetchall()
                    if result:
                        return render_template("filter.html",result=result)
                    else:
                        msg="No Auction is Currently Active With The Given Filter"
                        return render_template("filter.html",result=result ,msg=msg)
            elif not qfilter and quantity:
                return "select quantity Filter"    
            elif qfilter and not quantity:
                return " Enter the quantity Details"       
                
            
                
        except Exception as e:
            print(e)
            return "error"
    else:
        return redirect(url_for("sessioncheck"))
    
@app.route( '/feed', methods=["GET",  "POST"] )
def feed():
    if request.method=="POST":
        try:
            feed=request.form.get("ffeed")
            mycursor.execute("insert into feedback (username , emailid ,feed) values(%s,%s,%s) " ,(session["username"] ,session["uemail"],feed))
            mydb.commit()
            return "Your Feed back Has been Submitted"
        except Exception as e:
            return "Something Went Wrong Please Try Again later"
    else:
        return redirect(url_for("sessioncheck"))

if __name__ == '__main__':
    app.run(debug=True )
    
    