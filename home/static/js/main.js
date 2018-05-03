"use strict";

(function () {

    _initContact();
    _postContact();
})();

function _initContact() {

    var contactEl = document.getElementsByClassName("contact");

    for (var index = 0; index < contactEl.length; index++) {
        contactEl[index].addEventListener("click", function (e) {
            var formEl = document.getElementById("overlay");
            formEl.classList.add("show-form");
        });
    }
    document.getElementById("close").addEventListener("click", function (e) {
        var formEl = document.getElementById("overlay");
        formEl.classList.remove("show-form");
    });
}

function _postContact(){
     
    document.getElementById("send")
            .addEventListener("click", (e) => {
            const post_data = {
                'name': document.getElementById("name").value,
                'email': document.getElementById("email").value,
                'message': document.getElementById("message").value
            };
            
            _validate(post_data);
    });


}

function _validate(data){
    let proced = true;
    let errors = [];

    Object.keys(data)
    .map((value)=>{
       if(!data[value]){
            proced = false;
            errors.push(value);
        }else{
            document.getElementById(value).classList.remove('error');
        } 
    });
    if(!validateEmail(data.email)){
        console.log('email invalido');
        document.getElementById('email').classList.add('error');
        proced = false;
    }
    for(let index=0; index<errors.length; index++){
        let error = errors[index];
        document.getElementById(error).classList.add('error');
    }

    if(proced){
        // Object.keys(data)
        // .map((value)=>{
        //     document.getElementById(value).classList.remove('error');
        // });
         _postData(data);
    } 
}
function validateEmail(email) {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}
function _postData(data){

    fetch('contact/', {method:'POST', body: JSON.stringify(data)})
    .then(function(res){ return res.json(); })
    .then(res => _showSucess())
    .catch(err => console.log(err));
}

function _showSucess(){
    document.getElementById('form').classList.remove('active');
    document.getElementById('success').classList.add('active');
}
