function myfun(){

    back = document.getElementById("back")
    back.style.display = "flex"
    
    register = document.getElementById("reg");
    register.style.display = "flex";
    
}


function login2(){
    


    back = document.getElementById("back")
    back.style.display = "flex"
    
    register = document.getElementById("reg2");
    register.style.display = "flex";
    
}

function myfun2(){

    back = document.getElementById("back")
    back.style.display = "none"
    
    register = document.getElementById("reg");
    register.style.display = "none";
    
}

function myfun3(){

    back = document.getElementById("back")
    back.style.display = "none"
    
    register = document.getElementById("reg2");
    register.style.display = "none";
    
}


document.addEventListener("DOMContentLoaded", function() {
    // Your code here, including the event listener registration
document.getElementById("signform").addEventListener("submit", function(event) {
    // Prevent the form from submitting
    event.preventDefault();
    


    //collecting input values
     
     username = document.getElementById("name").value;
     useremail = document.getElementById("email").value;
     usernumber = document.getElementById("number").value;
     userpassword = document.getElementById("password").value;
     form = document.getElementById("signform");
     msg = document.getElementById("signmsg")



    // validating if input field is empty or not

    unumber = usernumber.trim()
    num = unumber.length

    
    if (username.trim()==""){
        alert("Enter Your Name and then click Submit")
        return false;

    }

    if (useremail.trim()==""){
        alert("Enter Your Email id and then click Submit")
        return false;

    }
    if (usernumber.trim()==""){
        alert("Enter Your Phone Number and then click Submit")
        return false;

    }
    
    if (userpassword.trim()==""){
        alert("Enter Your Password and then click Submit")
        return false;

    }

    if (num !== 10){
        alert("Enter a valid  Phone Number and then click Submit")
        return false;
        

    }
    showloading();

    fetch("/register",{
        method:"POST",
        body: new FormData(form)
        
    })
    .then(res=>{
        console.log(res)
        if (!res.ok){
            throw new error("Something Went wrong please try again later ")
        }
        else{
            return res.text();
        }
    })
    .then(data=>{
        console.log(data)
        setTimeout(() => {
            hideloading2();
            if (data=="ok"){
                window.location.href="/dashboard"
            }
            else{
                msg.style.color="red"
                msg.innerHTML=data
            }
        }, 5000);
    })

    .catch(error=>{
        setTimeout(() => {
            hideloading2()
            msg.style.color="red"
            msg.innerHTML=error
            console.log(error)
            }, 5000);
    })

})})

function showloading(){
    load = document.getElementById("loading");
    load.style.display="block"
    register = document.getElementById("reg2");
    register.style.display = "none";
    register = document.getElementById("reg");
    register.style.display = "none";
}

function hideloading1(){
    load = document.getElementById("loading");
    load.style.display="none"
    register = document.getElementById("reg2");
    register.style.display = "block";
}

function hideloading2(){
    load = document.getElementById("loading");
    load.style.display="none"
    register = document.getElementById("reg");
    register.style.display = "block";
}





                            // login form validate 
document.addEventListener("DOMContentLoaded", function() {
document.getElementById("login").addEventListener("submit", function(event){ 
    event.preventDefault();

            // getting the required elements
    form=document.getElementById("login")
    msg=document.getElementById("msg")
    useremail = document.getElementById("lemail").value;
    userpassword = document.getElementById("lpassword").value;

            // check whether the input box is empty or not
    if (useremail.trim()==""){
        alert("Enter Your Email id and then click Submit")
        return false;

    }

    if (userpassword.trim()==""){
        alert("Enter Your Password and then click Submit")
        return false;

    }
        // preventing the default form submission and shows loading screen
    
    showloading();

        // sending login form data to server and handiling the response 
    fetch("/login", {
          method: "POST",
          body: new FormData(form)
    })

    .then(res=>{
        
        if (!res.ok){
            
            throw new Error("Error in fetching your data please try again later");
        }
        else{
            return res.text()
        }
    })

    .then(data=>{
        setTimeout(() => {
            hideloading1();



            if (data=="ok"){

                window.location.href="/dashboard";
    
            }
            else{
                msg.style.color="red"
                msg.innerHTML=data;
                
            }
            
        }, 5000);
    })

    .catch(error=>{
        setTimeout(() => {
            hideloading1();
            msg.style.color="red"
            msg.innerHTML=error;
            console.log(error)
            
        }, 5000);
        
    });

})});



// function myfetch() {
//     fetch("/register")
//         .then(res =>{
//             console.log(res)
//             return res.text();
//         })

//         .then(data => {
//             console.log(data);
//         })
//         .catch(error => {
//             console.error('Fetch error:', error)
//         });

//     window.location.href= "/"
// };

        // event listener for bid now button in dashboard
document.addEventListener("DOMContentLoaded", function() {

    classs=document.querySelectorAll(".bidbutton")
    classs.forEach(element => {
        element.addEventListener("click",function(event){
            var element =event.target
            let dataid = element.getAttribute("data-id")
            let cprice= element.getAttribute("data-cprice")
            let sprice=element.getAttribute("data-sprice")
            blur = document.getElementById("blur")
            blur.style.display="flex";
            bidding = document.getElementById("bidding")
            bidding.style.display="flex";
            ano = document.getElementById("demo2")
            ccprice = document.getElementById("cprice")
            ssprice = document.getElementById("sprice")
            ano.innerHTML="Auction No : "+dataid+"";
            ccprice.innerHTML="Current Price : " +cprice+"";
            ssprice.innerHTML="Starting Price : "+sprice+""
            ano=document.getElementById("getbid")
            ano.setAttribute("data-ano" ,dataid)

        
        })
            



    })

})


function back5(){
            blur = document.getElementById("blur")
            blur.style.display="none";
            bidding = document.getElementById("bidding")
            bidding.style.display="none";
            document.getElementById("getbidammount").value="";


}

function back8(){
            blur = document.getElementById("blur")
            blur.style.display="none";
            bidd = document.getElementById("cauc")
            bidd.style.display="none";

}

function create(){
            blur = document.getElementById("blur")
            blur.style.display="flex";
            bidd = document.getElementById("cauc")
            bidd.style.display="flex";


    
}

        // getting the bidding amount
document.addEventListener("DOMContentLoaded", function() {

    document.getElementById("getbid").addEventListener("click" , function() {
        ammount=document.getElementById("getbidammount")
        amount=ammount.value
        auction=document.getElementById("getbid")
        ano = auction.getAttribute("data-ano")

        if (amount==""){
            alert("Enter the ammount and then click")
        }
        else{

            fetch("/bid",{
                method:"POST",
                body:JSON.stringify({"ammount":amount,"ano": ano})
            })
            .then(res=>{
                if (!res.ok){
                    throw "Error Acuquired"
                }
                else{
                    return res.text()
                }
            
            })
        
            .then(data=>{
                if (data=="data stored"){
                    blur = document.getElementById("blur")
                    blur.style.zIndex="7"
            
                    document.getElementById("message").innerHTML=data;
                    document.getElementById("mssg").style.display="block"
                    console.log(data)
                }
                else{
                    blur = document.getElementById("blur")
                    blur.style.zIndex="7"
            
                    document.getElementById("message").innerHTML=data;
                    document.getElementById("mssg").style.display="block"
                    console.log(data)
                }

            })
            .catch(error=>{
                blur = document.getElementById("blur")
                blur.style.zIndex="7"
        
                document.getElementById("message").innerHTML=error;
                document.getElementById("mssg").style.display="block"
                console.log(error)
            })

        }
        

        
    
    })
})

  // getting the bidding amount from full details
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("getbid2").addEventListener("click" , function() {
        ammount=document.getElementById("getbidammount2")
        amount=ammount.value
        auction=document.getElementById("getbid2")
        ano = auction.getAttribute("data-ano")

        if (amount==""){
            console.log(ammount)
            alert("Enter the ammount and then click")
        }
        
        else{

            fetch("/bid",{
                method:"POST",
                body:JSON.stringify({"ammount":amount,"ano": ano})
            })
            .then(res=>{
                if (!res.ok){
                    throw "Error Acuquired"
                }
                else{
                    return res.text()
                }
            
            })
        
            .then(data=>{
                if (data=="data stored"){
                    blur = document.getElementById("blur")
                    blur.style.zIndex="7"
            
                    document.getElementById("message").innerHTML=data;
                    document.getElementById("mssg").style.display="block"
                    console.log(data)
                }
                else{
                    blur = document.getElementById("blur")
                    blur.style.zIndex="7"
                    document.getElementById("message").innerHTML=data;
                    document.getElementById("mssg").style.display="block"
                }

            })
            .catch(error=>{
                    blur = document.getElementById("blur")
                    blur.style.zIndex="7"
                    document.getElementById("message").innerHTML=error;
                    document.getElementById("mssg").style.display="block"
                
            })

        }
        

        
    
    })
})
        // creating new auction

document.addEventListener("DOMContentLoaded" ,function(){
    
    document.getElementById("createform").addEventListener("submit" , function(event){

        createform=document.getElementById("createform")
        event.preventDefault()
        data= new FormData(createform)

        fetch("/createauction",{
            method:"post",
            body:data
        })
        .then((res)=>{
            console.log(res)
            if(res.ok){
                return res.text()
            }
            else{
                return  "failure"
            }
            

        })
        .then((data)=>{
            console.log(data)
            
        })
    })
        

})


        // normal loading animation for every page
window.addEventListener("load", function(){

    setInterval(() => {
        document.querySelector(".blur2").classList.add("remove")
        document.querySelector(".blur2").addEventListener("transioned",function(){
            
        })
        

        
    }, 1000);
})

        // getting full detail of an auction dashboard

document.addEventListener("DOMContentLoaded", function(){
    document.getElementById("contentt").addEventListener("click", function(event){
        

    
    
           if(event.target.classList.contains('more')){

            main=document.getElementById("details")
            
            blur = document.getElementById("blur")
            blur.style.display="flex";
            
            


            element=event.target
            anum=element.getAttribute("data-ano")

            fetch("/getfulldetail",{
                method:"POST",
                body:JSON.stringify({"ano":anum})

            })
            .then(res=>{
                if(!res.ok){
                    throw "Something Went Wrong can't able to fetch the data"

                }
                else{
                    return res.text()
                }
            })
            .then(data=>{
                
                if(data!=="error"){

                    btt=document.getElementById("getbid2")
                    jdata=JSON.parse(data)
                    
                    if(jdata["status"]=="completed"){
                        try{
                            document.querySelector(".ttrack").style.display="block"
                            document.querySelector(".ttrack").setAttribute("data-ano" , jdata["ano"])

                        }
                        catch{

                        }
                        document.querySelector(".special").style.display="none"
                        
                    }
                    else if (jdata["status"]=="active"){
                        try{

                            document.querySelector(".ttrack").style.display="none"
                        }
                        catch{
                            
                        }
                        document.querySelector(".special").style.display="block"
                    }
                    
                    btt.setAttribute("data-ano" , jdata["ano"])
                    document.getElementById("demo3").innerHTML="Auction No : "+jdata["ano"]+"";
                    document.getElementById("ano").innerHTML=jdata["ano"]
                    document.getElementById("aowner").innerHTML=jdata["aowner"]
                    document.getElementById("product").innerHTML=jdata["pname"]
                    document.getElementById("sprice").innerHTML=jdata["sprice"]
                    document.getElementById("cprice").innerHTML=jdata["cprice"]
                    document.getElementById("stime").innerHTML=jdata["stime"]
                    document.getElementById("etime").innerHTML=jdata["etime"]
                    document.getElementById("district").innerHTML=jdata["district"]
                    document.getElementById("flocation").innerHTML=jdata["flocation"]
                    document.getElementById("time").innerHTML=""+jdata["time"]+"Hours"
                    document.getElementById("date").innerHTML=jdata["date"]
                    document.getElementById("status").innerHTML=jdata["status"]
                    document.getElementById("quantity").innerHTML=jdata["quantity"]
                    document.getElementById("chbidder").innerHTML=jdata["chbidder"]
                    main.style.display="flex"

                    try{
                        track2=document.getElementById("track")
                        track2.setAttribute("data-ano" , jdata["ano"])
                        
                        

                    }
                    catch(error){
                        
                        

                    }
                    
                }
                else{
                    throw "cannot able to fetch the full details please try again later"

                }

            })
            .catch(error=>{
                document.getElementById("message").innerHTML=error;
                document.getElementById("mssg").style.display="block"
                
            })


            
        }
    })
           
            

        

})


        // getting the bidding details for myauctions
document.addEventListener("DOMContentLoaded", function(){
    document.querySelector(".ttrack").addEventListener("click" , function(){
        ano=document.querySelector(".ttrack").getAttribute("data-ano")

        fetch("/track1",{
            method:"POST",
            body:JSON.stringify({"ano":ano })
        })
        .then(res=>{
            if(res.ok){
                return res.text()
            }
            else{
                throw "cannot Able to fetch the data"
            }
        })
        .then(data=>{
            if (data=="no"){
                mesg=document.querySelector(".msg")
                mesg.style.display="block"
                document.getElementById("message").innerHTML="No One Bidded For this auction"
            }
            else if (data=="can't able to fetch the data"){
                mesg=document.querySelector(".msg")
                mesg.style.display="block"
                document.getElementById("message").innerHTML="can't able to fetch the data"

            }
            else if(data=="Error happend so please try again later"){
                mesg=document.querySelector(".msg")
                mesg.style.display="block"
                document.getElementById("message").innerHTML="Error happend so please try again later"
            }
            else{
                document.getElementById("trackk").innerHTML=data
                document.getElementById("trackk").style.display="flex"
                document.getElementById("blur").style.zIndex=8

            }
        })
        .catch(error=>{
            console.log(error)
        })

    })
})



        // removing the full detail popup and  also blur div
function back7(){
    blur = document.getElementById("blur")
    blur.style.display="none";
    main=document.getElementById("details")
    main.style.display="none"
    document.getElementById("searchform").value=""

}





function myfun10(){
        main=document.getElementById("details")
        main.style.zIndex=1
        bidding = document.getElementById("biddingg")
        bidding.style.display="flex";

}

function back9(){
        bidding = document.getElementById("biddingg")
        bidding.style.display="none";
        main=document.getElementById("details")
        main.style.zIndex=6
        document.getElementById("getbidammount2").value="";

}

    //  filter addEventListener button
document.addEventListener("DOMContentLoaded", function(){
    document.querySelector(".filter").addEventListener("click" , function(){
        document.querySelector(".filter3").style.display="flex"

    })
})

    //  filter addEventListener button for mobile
    document.addEventListener("DOMContentLoaded", function(){
        document.querySelector(".mfilter").addEventListener("click" , function(){
            document.querySelector(".filter3").style.display="flex"
    
            console.log("okokopkl")
        })
    })

            // getting the specific auction details
document.addEventListener("DOMContentLoaded" ,function(){
    document.getElementById("search").addEventListener("submit" , function(event){
        event.preventDefault();
        formdetail=document.getElementById("search")
        sform=document.getElementById("searchform").value
        fetch("/auctiondetail",{
            method:"POST",
            body : new FormData(formdetail)
        })
        .then(res=>{
            if (res.ok){
                console.log(" status ok")
                return res.text()
            }
            else{
                throw "Error can't fetch the data response status is not ok"
            }
        })
        .then(data=>{
            if (data=="No Data in This Auction Number"){

                blur = document.getElementById("blur9")
                blur.style.display="flex";
                document.getElementById("messsage").innerHTML=data;
                document.getElementById("msssg").style.display="block"

            }
            else if (data=="Please try again later"){
                blur = document.getElementById("blur9")
                blur.style.display="flex";
                document.getElementById("messsage").innerHTML=data;
                document.getElementById("msssg").style.display="block"

            }
            else{
                jdata=JSON.parse(data)
                blur = document.getElementById("blur")
                blur.style.display="flex";
                if(jdata["status"]=="completed"){
                    document.querySelector(".special").style.display="none"
                }
                else if (jdata["status"]=="active"){
                    document.querySelector(".special").style.display="block"
                }
                document.getElementById("demo3").innerHTML="Auction No : "+jdata["ano"]+"";
                document.getElementById("ano").innerHTML=jdata["ano"]
                document.getElementById("aowner").innerHTML=jdata["aowner"]
                document.getElementById("product").innerHTML=jdata["pname"]
                document.getElementById("sprice").innerHTML=jdata["sprice"]
                document.getElementById("cprice").innerHTML=jdata["cprice"]
                document.getElementById("stime").innerHTML=jdata["stime"]
                document.getElementById("etime").innerHTML=jdata["etime"]
                document.getElementById("district").innerHTML=jdata["district"]
                document.getElementById("flocation").innerHTML=jdata["flocation"]
                document.getElementById("time").innerHTML=""+jdata["time"]+"Hours"
                document.getElementById("date").innerHTML=jdata["date"]
                document.getElementById("status").innerHTML=jdata["status"]
                document.getElementById("quantity").innerHTML=jdata["quantity"]
                document.getElementById("chbidder").innerHTML=jdata["chbidder"]
                document.getElementById("getbid2").setAttribute("data-ano" , jdata["ano"])
                main=document.getElementById("details")
                main.style.display="flex";


            }
            
        })
        .catch(error=>{
            blur = document.getElementById("blur9")
            blur.style.zIndex="7"
            document.getElementById("messsage").innerHTML=error;
            document.getElementById("msssg").style.display="block"
        })
        
    })
})

            // for ok button of message div
document.addEventListener("DOMContentLoaded", function(){


    document.getElementById("okok").addEventListener("click", function(){
        blur = document.getElementById("blur")
        blur.style.zIndex="5"
        document.getElementById("mssg").style.display="none"
        document.getElementById("searchform").value=""




    })
})
    //    message from search an auction
document.addEventListener("DOMContentLoaded", function(){


    document.getElementById("ookok").addEventListener("click", function(){
        blur9 = document.getElementById("blur9")
        blur9.style.display="none"
        document.getElementById("msssg").style.display="none"
        document.getElementById("searchform").value=""




    })
})

            // tracking the bidder details
document.addEventListener("DOMContentLoaded", function(){
    document.getElementById("track").addEventListener("click", function(){
        track3=document.getElementById("track")
        actionnum=track3.getAttribute("data-ano")

        
        fetch("/track",{
            method:"POST",
            body:JSON.stringify({"ano":actionnum})
        })
        .then(res=>{
            if(res.ok){
                console.log("status ok")
                return res.text()
            }
            else{
                throw "Status not ok and can't get the data of this auction"
            }
        })
        .then(data=>{
            document.getElementById("trackk").innerHTML=data

        })
        .catch(errorr=>{
            console.log(errorr)
        })
        document.getElementById("trackk").style.display="flex"
        document.getElementById("blur").style.zIndex=8
       

            
            
        })
        
    })


function back0(){
    document.getElementById("trackk").style.display="none"
    document.getElementById("blur").style.zIndex=5
    parent=document.getElementById("parent")
    parent.removeChild(pelement)

}

function back11(){
    document.querySelector(".filter3").style.display="none"
}

        // completed button addEventListener in mybidding.html
document.addEventListener("DOMContentLoaded", function(){
    document.querySelector(".completed").addEventListener("click", function(){
        document.querySelector(".completed").style.backgroundColor="rgb(94,93,240)";
        document.querySelector(".active").style.backgroundColor="rgb(156, 156, 156)";
        fetch("/completedmybidding" ,{
            method:"POST",
        })
        .then(res=>{
            if(res.ok){
                return res.text()
            }
            else{
                throw "Cannot Able to Fetch the data"
            }
        })
        .then(data=>{
            document.querySelector(".act").remove();
            document.querySelector(".content").innerHTML=data
            
        })
        .catch(error=>{
            blur = document.getElementById("blur")
            blur.style.zIndex="7"
            document.getElementById("message").innerHTML=error;
            document.getElementById("mssg").style.display="block" 
        })


    })
})

        //  active button addEventListener in mybidding.html
document.addEventListener("DOMContentLoaded", function(){
    document.querySelector(".active").addEventListener("click", function(){
        document.querySelector(".active").style.backgroundColor="rgb(94,93,240)";
        document.querySelector(".completed").style.backgroundColor="rgb(156, 156, 156)";
        fetch("/activemybidding" ,{
            method:"POST",
        })
        .then(res=>{
            if(res.ok){
                return res.text()
            }
            else{
                throw "Cannot Able to Fetch the data"
            }
        })
        .then(data=>{
            document.querySelector(".act").remove();
            document.querySelector(".content").innerHTML=data
            
        })
        .catch(error=>{
            blur = document.getElementById("blur")
            blur.style.zIndex="7"
            document.getElementById("message").innerHTML=error;
            document.getElementById("mssg").style.display="block" 
        })



    })
})
            // filter and load the content in dashboard
document.addEventListener("DOMContentLoaded", function(){
    document.querySelector(".filterform").addEventListener("submit", function(event){
        event.preventDefault();
        filterform = document.querySelector(".filterform")
        fetch("/filter" , {
            method:"POST",
            body: new FormData(filterform)
        })
        .then(res=>{
            if(res.ok){
                return res.text()
            }
            else{
                throw "cannot able to filter "
            }
        })
        .then(data=>{
            if(data=="Please Enter Any Detail"){
                document.getElementById("fill").innerHTML=data
            }
            else if(data=="Enter the quantity Details"){
                document.getElementById("fill").innerHTML=data
            }
            else if(data=="select quantity Filter"){
                document.getElementById("fill").innerHTML=data
            }
            else if(data=="error"){
                document.getElementById("fill").innerHTML="something Went Wrong Please Try Again"
            }
            
            else{
                document.querySelector(".filter3").style.display="none"
                document.querySelector(".type7").value=""
                document.querySelector(".act").remove()
                document.getElementById("contentt").innerHTML=data

            }
        })
        .catch(error=>{
            document.getElementById("fill").innerHTML=error

        })

    })
})


            //    completed button addEventListener in myauction.html
document.addEventListener("DOMContentLoaded", function(){
    document.querySelector(".macompleted").addEventListener("click", function(){
        document.querySelector(".macompleted").style.backgroundColor="rgb(94,93,240)";
        document.querySelector(".maactive").style.backgroundColor="rgb(156, 156, 156)";
        fetch("/completedmyauction",{
            method:"POST"       
        })
        .then(res=>{
            if(res.ok){
                return res.text()
            }
            else{
                throw "Can't able to Fetch the data"
            }
        })
        .then(data=>{
            document.querySelector(".act").remove();
            document.querySelector(".content").innerHTML=data
        })
        .catch(error=>{
            blur = document.getElementById("blur")
            blur.style.zIndex="7"
            document.getElementById("message").innerHTML=error;
            document.getElementById("mssg").style.display="block"         
        
        })
    })
})

        //  active button addEventListener in myauction.html
document.addEventListener("DOMContentLoaded", function(){
    document.querySelector(".maactive").addEventListener("click", function(){
        document.querySelector(".maactive").style.backgroundColor="rgb(94,93,240)";
        document.querySelector(".macompleted").style.backgroundColor="rgb(156, 156, 156)";
        fetch("/activemyauction",{
            method:"POST"       
        })
        .then(res=>{
            if(res.ok){
                return res.text()
            }
            else{
                throw "Can't able to Fetch the data"
            }
        })
        .then(data=>{
            document.querySelector(".act").remove();
            document.querySelector(".content").innerHTML=data
        })
        .catch(error=>{
            blur = document.getElementById("blur")
            blur.style.zIndex="7"
            document.getElementById("message").innerHTML=error;
            document.getElementById("mssg").style.display="block"         
        
        })


    })
})





