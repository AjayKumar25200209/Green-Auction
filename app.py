from flask import Flask,request,url_for,render_template,session,redirect
import mysql.connector
import json
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


@app.route('/test',methods=['GET', 'POST'])
def test():
    if request.method == "GET":
        return render_template("test.html")


@app.route('/dashboard',methods=['GET', 'POST'])
def dashboard():
    if request.method == "GET":
        if session.get('uemail') is not None :
            msg="tomato"
            return render_template("dashboard.html", msg=msg)
        else :
            
            return redirect(url_for("sessioncheck"))
        
        
    
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
            mycursor.execute("select email from userinfo where email=%s" ,(useremail,))
            result1 = mycursor.fetchone()
            
            if result1:
                mycursor.execute("select password from userinfo where email=%s" ,(useremail,))
                result2 = mycursor.fetchone()
                dpassword=result2["password"]
                if dpassword==userpassword:
                    session["uemail"] = useremail
                    session['password'] = userpassword
                    return "ok"
                else:
                    return "You Entered a incorrect Password"
            else:
                return "no user in this email" 
        else:
            return "Enter your details and then click" 
    else:
        return redirect(url_for("sessioncheck"))
        
@app.route( '/bid', methods=["GET",  "POST"] )
def bid():
    if request.method=="POST":
        data = request.data.decode("utf-8")
        
        data2=json.loads(data)
        print(type(data2))
        print(data2["ammount"])

        return "succes"
    else:
        return "error"


if __name__ == '__main__':
    app.run(debug=True)
    
    