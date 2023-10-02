function myfun(){

    back = document.getElementById("back")
    back.style.display = "flex"
    
    register = document.getElementById("reg");
    register.style.display = "flex";
    
}


function login2() {
    


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
            data3=JSON.parse(data)
            console.log(data3)
            console.log(data3["result"])
        })
        .catch(error=>{
            console.log(error)
        })
    
    })
})

      // getting the bidding amount from full details
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("getbid2").addEventListener("click" , function() {
        ammount=document.getElementById("getbidammount")
        amount=ammount.value
        auction=document.getElementById("getbid")
        ano = auction.getAttribute("data-ano")
        

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
            data3=JSON.parse(data)
            console.log(data3)
            console.log(data3["result"])
        })
        .catch(error=>{
            console.log(error)
        })
    
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

        // getting full detail of an auction

document.addEventListener("DOMContentLoaded", function(){
    detail=document.querySelectorAll(".more")

    detail.forEach(item=>{
        item.addEventListener("click", function(event){
            blur = document.getElementById("blur")
            blur.style.display="flex";
            main=document.getElementById("details")
            main.style.display="flex";


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
                console.log(data)
                jdata=JSON.parse(data)
                btt=document.getElementById("getbid2")
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




            })
            .catch(error=>{
                console.log(error)
            })
            
        })

    })

})
        // removing the full detail popup and  also blur div
function back7(){
    blur = document.getElementById("blur")
    blur.style.display="none";
    main=document.getElementById("details")
    main.style.display="none"

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

}




