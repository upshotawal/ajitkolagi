function validateform() {
  var form = document.getElementById('myform').value;
  var Bookername = document.getElementById('bname').value;
  var price = document.getElementById('price').Value;
  var contactnumber = document.getElementById('Contactnumber').value;
  var starttime = document.getElementById('Starttime').value;
  var endtime = document.getElementById('endtime').value;

  var bookerscheck = /^[A-Za-z.]{3,30}$/;
  // var passwordcheck =/^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,16}$/;
  //var pricecheck = /^[0-9]{3}$/;
  var contactcheck = /^[789][0-9]{9}$/;
  var startcheck = /^[0-9]{9}$/;

  var endcheck = /^[0-9]{9}$/;

  if(price>0){

  }
  else{
    alert("invalid");
  }

  if(contactnumber<10){

  }
  else{
    alert("invalid");
  }

  if (bookerscheck.test(Bookername)) {
    document.getElementById('bookererror').innerHTML = " ";
  } else {
    document.getElementById('bookererror').innerHTML = "** Bookername is Invalid ";
    return false;
  }
  if (pricecheck.test(price)) {
    document.getElementById('priceerror').innerHTML = " ";
  } else {
    document.getElementById('priceerror').innerHTML = "** Price is Invalid ";
    return false;
  }

  if (contactcheck.test(contactnumber)) {
    document.getElementById('contacterror').innerHTML = " ";
  } else {
    document.getElementById('contacterror').innerHTML = "** ContactNumber is Invalid ";
    return false;
  }


  if (startcheck.test(starttime)) {
    document.getElementById('starterror').innerHTML = " ";
  } else {
    document.getElementById('starterror').innerHTML = "** starttime is Invalid ";
    return false;
  }


  if (endcheck.test(endtime)) {
    document.getElementById('enderror').innerHTML = " ";
  } else {
    document.getElementById('enderror').innerHTML = "** endtime is Invalid ";
    return false;
  }



}

function employeeform() {
  var form = document.getElementById('employeeform').value;
  var name = document.getElementById('name').value;
  var post = document.getElementById('post').Value;
  var contactnumber = document.getElementById('contactnumber').value;
  var address = document.getElementById('address').value;
  var citizenshipnumber = document.getElementById('citizenshipnumber').value;

  var namecheck = /^[A-Za-z.]{3,30}$/;
  // var passwordcheck =/^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,16}$/;
  var postcheck = /^[A-Za-z.]{3,30}$/;
  var contactnumber = document.getElementById('contactnumber').value;
  var addresscheck = /^[A-Za-z.]{3,30}$/;

  var citizencheck = /^[0-9]{9}$/;

  if(contactnumber<10){

  }
  else{
    alert("invalid");
  }

  if (namecheck.test(name)) {
    document.getElementById('nameerror').innerHTML = " ";
  } else {
    document.getElementById('nameerror').innerHTML = "** name is Invalid ";
    return false;
  }
  if (postcheck.test(post)) {
    document.getElementById('posterror').innerHTML = " ";
  } else {
    document.getElementById('posterror').innerHTML = "** Post is Invalid ";
    return false;
  }

  if (contactcheck.test(contactnumber)) {
    document.getElementById('contacterror').innerHTML = " ";
  } else {
    document.getElementById('contacterror').innerHTML = "** ContactNumber is Invalid ";
    return false;
  }


  if (addresscheck.test(address)) {
    document.getElementById('addresserror').innerHTML = " ";
  } else {
    document.getElementById('addresserror').innerHTML = "** address is Invalid ";
    return false;
  }


  if (citizenshipnumber.test(citizenshipnumber)) {
    document.getElementById('citizenerror').innerHTML = " ";
  } else {
    document.getElementById('citizenerror').innerHTML = "** citizenshipnumber is Invalid ";
    return false;
  }



}
function matchform() {
  var form = document.getElementById('matchform').value;
  var price = document.getElementById('price').value;
  var duration = document.getElementById('duration').Value;
  var starttime = document.getElementById('Starttime').value;
  var endtime = document.getElementById('endtime').value;


  // var passwordcheck =/^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,16}$/;
  var pricecheck =  /^[0-9]{9}$/;
  var durationcheck = /^[789][0-9]{9}$/;
  var startcheck = /^[0-9]{9}$/;
  var endcheck = /^[0-9]{9}$/;
  if(price>0){

  }
  else{
    alert("invalid");
  }


  if (pricecheck.test(price)) {
    document.getElementById('priceerror').innerHTML = " ";
  } else {
    document.getElementById('priceerror').innerHTML = "** Price is Invalid ";
    return false;
  }

  if (durationcheck.test(duration)) {
    document.getElementById('durationerror').innerHTML = " ";
  } else {
    document.getElementById('durationerror').innerHTML = "** duration is Invalid ";
    return false;
  }


  if (startcheck.test(starttime)) {
    document.getElementById('starterror').innerHTML = " ";
  } else {
    document.getElementById('starterror').innerHTML = "** starttime is Invalid ";
    return false;
  }


  if (endcheck.test(endtime)) {
    document.getElementById('enderror').innerHTML = " ";
  } else {
    document.getElementById('enderror').innerHTML = "** endtime is Invalid ";
    return false;
  }



}
function playerform() {
  var form = document.getElementById('playerform').value;
  var Teamname = document.getElementById('Teamname').value;
  var contactnumber = document.getElementById('contactnumber').value;
  var address = document.getElementById('address').value;


  var Teamnamecheck = /^[A-Za-z.]{3,30}$/;
  // var passwordcheck =/^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,16}$/;
  var contactcheck = /^[789][0-9]{9}$/;
  var addresscheck = /^[A-Za-z.]{3,30}$/;

  if(contactnumber<10){

  }
  else{
    alert("invalid");
  }



  if (Teamnamecheck.test(Teamname)) {
    document.getElementById('Teamnameerror').innerHTML = " ";
  } else {
    document.getElementById('Teamnameerror').innerHTML = "** Teamname is Invalid ";
    return false;
  }


  if (contactcheck.test(contactnumber)) {
    document.getElementById('contacterror').innerHTML = " ";
  } else {
    document.getElementById('contacterror').innerHTML = "** ContactNumber is Invalid ";
    return false;
  }


  if (addresscheck.test(address)) {
    document.getElementById('addresserror').innerHTML = " ";
  } else {
    document.getElementById('addresserror').innerHTML = "** address is Invalid ";
    return false;
  }

}
function priceform() {
  var form = document.getElementById('priceform').value;
  var duration = document.getElementById('day').Value;
  var starttime = document.getElementById('Starttime').value;
  var endtime = document.getElementById('endtime').value;


  // var passwordcheck =/^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,16}$/;

  var daycheck = /^[A-Za-z.]{3,30}$/;
  var startcheck = /^[0-9]{9}$/;
  var endcheck = /^[0-9]{9}$/;

  if (daycheck.test(day)) {
    document.getElementById('dayerror').innerHTML = " ";
  } else {
    document.getElementById('dayerror').innerHTML = "** day is Invalid ";
    return false;
  }


  if (startcheck.test(starttime)) {
    document.getElementById('starterror').innerHTML = " ";
  } else {
    document.getElementById('starterror').innerHTML = "** starttime is Invalid ";
    return false;
  }


  if (endcheck.test(endtime)) {
    document.getElementById('enderror').innerHTML = " ";
  } else {
    document.getElementById('enderror').innerHTML = "** endtime is Invalid ";
    return false;
  }
}
function paymentform() {
  var form = document.getElementById('paymentform').value;
  var payment_method = document.getElementById('payment_method').Value;
  var amount = document.getElementById('amount').value;
  var status = document.getElementById('status').value;


  // var passwordcheck =/^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,16}$/;

  var payment_methodcheck = /^[A-Za-z.]{3,30}$/;
  // var amountcheck = /^[0-9]{9}$/;
  var statuscheck = /^[A-Za-z.]{3,30}$/;

  if (payment_methodcheck.test(payment_method)) {
    document.getElementById('paymenterror').innerHTML = " ";
  } else {
    document.getElementById('paymenterror').innerHTML = "** payment_method is Invalid ";
    return false;
  }


  if (statuscheck.test(status)) {
    document.getElementById('status').innerHTML = " ";
  } else {
    document.getElementById('statuserror').innerHTML = "** status is Invalid ";
    return false;
  }


  if (amountcheck.test(amount)) {
    document.getElementById('amounterror').innerHTML = " ";
  } else {
    document.getElementById('amounterror').innerHTML = "** amount is Invalid ";
    return false;
  }
}
function signinform() {
  var form = document.getElementById('signinform').value;
  var username = document.getElementById('uname').value;
  var password = document.getElementById('password').value;

  var usernamecheck = /^[A-Za-z.]{3,30}[0-9]$/;
  var passwordcheck =/^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,16}$/;

  if (usernamecheck.test(username)) {
    document.getElementById('usernameerror').innerHTML = " ";
  } else {
    document.getElementById('usernameerror').innerHTML = "** username is Invalid ";
    return false;
  }
  if (passwordcheck.test(password)) {
    document.getElementById('passworderror').innerHTML = " ";
  } else {
    document.getElementById('passworderror').innerHTML = "** Password is Invalid ";
    return false;
  }
}

function signupform() {
  var form = document.getElementById('signupform').value;
  var username = document.getElementById('username').value;
  var address = document.getElementById('address').Value;
  var email = document.getElementById('email').value;
  var password = document.getElementById('password').value;
  var confirmpassword = document.getElementById('confirmpassword').value;

  var usernamecheck = /^[A-Za-z.]{3,30}$/;
  var addresscheck = /^[A-Za-z.]{3,30}$/;
  var emailcheck = /^[A-Za-z_]{3,}@[A-Za-z]{3,}[.]{1}[A-Za-z.]{2,6}$/;
  var passwordcheck =/^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,16}$/;
  var confirmpasswordcheck =/^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,16}$/;

  if (usernamecheck.test(username)) {
    document.getElementById('usernameerror').innerHTML = " ";
  } else {
    document.getElementById('usernameerror').innerHTML = "** username is Invalid ";
    return false;
  }
  if (addresscheck.test(address)) {
    document.getElementById('addresserror').innerHTML = " ";
  } else {
    document.getElementById('addresserror').innerHTML = "** address is Invalid ";
    return false;
  }

  if (emailcheck.test(email)) {
    document.getElementById('emailerror').innerHTML = " ";
  } else {
    document.getElementById('emailerror').innerHTML = "** email is Invalid ";
    return false;
  }


  if (passwordcheck.test(password)) {
    document.getElementById('passworderror').innerHTML = " ";
  } else {
    document.getElementById('passworderror').innerHTML = "** password is Invalid ";
    return false;
  }


  if (confirmpasswordcheck.test(confirmpassword)) {
    document.getElementById('confirmpassword').innerHTML = " ";
  } else {
    document.getElementById('confirmpassword').innerHTML = "** confirmpassword is Invalid ";
    return false;
  }
 

}






