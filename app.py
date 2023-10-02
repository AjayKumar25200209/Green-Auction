from flask import Flask,request,url_for,render_template,session,redirect
import mysql.connector
import json
import random
from datetime import datetime,timedelta,date

app = Flask(__name__)

days=3
app.secret_key="ajaykumar"
app.permanent_session_lifetime =  3*24*60*60




print(app.permanent_session_lifetime )

                        # connecting to mysql database
mydb = mysql.connector.connect(
        host="localhost",
  	    username="root",
  	    password="Ajay@2002",
        database="mylearn"
)

mycursor = mydb.cursor(dictionary=True)







@app.route('/dashboard',methods=['GET', 'POST'])
def dashboard():
    if request.method == "GET":

        if session.get('uemail') is not None :
            
            try:
                mycursor.execute("select * from auctioninfo")

                result = mycursor.fetchall()
                
                random.shuffle(result)
                
                session["array"]=[]
                array=session["array"]
                for x in result:
                    
                    data=x["ano"]
                    array.append(data)
                print(array)
                return render_template("dashboard.html",result=result) 
                
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
    
    
@app.route('/My_Auction',methods=['GET', 'POST'] )
def myauction():
    if request.method=="GET":
        if session.get('uemail')  is not None:
            
            
            return render_template("myauction.html")
        else:
            return redirect(url_for("sessioncheck"))
        
    else:
        return "uui"
    
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
        useremail = request.form.get('lemail')
        userpassword = request.form.get('lpass')
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
        print(data)
        
        data2=json.loads(data)
        print(type(data2))
        print(data2)
        if data2["ano"]=="" :
            print("none value")
        data3={"result":"success"}
        

        return data3
    else:
        return "error"
    
@app.route( '/createauction', methods=["GET",  "POST"] )
def createauction():
    if request.method=="POST":
        productname =request.form.get("productname")
        quantity =request.form.get("quantity")
        place =request.form.get("place")
        price =request.form.get("price")
        time =request.form.get("time")
        district = request.form.get("district")
        description =request.form.get("description")
        print(district,productname,quantity,place,price,time,description)
        try:
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
            return "ok ok"
            
        except Exception as e:
            return f"sorry {e}"
        
        
@app.route( '/getfulldetail', methods=["GET",  "POST"] )
def getfulldetail():
    if request.method=="POST":
        
        data=request.data.decode("UTF-8")
        ano=json.loads(data)
        
        value=ano["ano"]
        print(value)
        try:
    
           mycursor.execute("select * from auctioninfo where ano=%s ",(value,))
           result1 = mycursor.fetchone()
           result=json.dumps(result1)
        except Exception as e:
           return e
        return result

    else:
        return redirect(url_for("sessioncheck"))
        


if __name__ == '__main__':
    app.run(debug=True)
    
    