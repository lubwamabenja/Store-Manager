var attempt = 3; // Variable to count number of attempts.
// Below function Executes on click of login button.
function validate(){
var username = document.getElementById("username").value;
var password = document.getElementById("password").value;
if ( username == "lubwama" && password == "lubwama1"){
alert ("Login successfully");
window.location = "home.html"; // Redirecting to other pag.
return false;
}
else{
attempt --;// Decrementing by one.
alert("You have left "+attempt+" attempt;");
// Disabling fields after 3 attempts.
if( attempt == 0){
document.getElementById("username").disabled = true;
document.getElementById("password").disabled = true;
document.getElementById("submit").disabled = true;
return false;
}
}
}


//navbar Javascript
var i = 0;
var namearray= new Array();
var lastarray = new Array();
var pricearray = new Array();
function resetform () {
    var clearproduct = document.getElementById('product');
    clearproduct.value = "";
    var clearquantity = document.getElementById('quantity');
    clearquantity.value = "";
    var clearprice = document.getElementById('price');
    clearprice.value = "";
    }
function BlankCheck () {
    var errormessage = "";
    if (document.getElementById('product').value == "") {
        errormessage +="Please enter product. \n";
        document.getElementById('product').style.borderColor = "red";
        }
    if (document.getElementById('quantity').value == "") {
        errormessage +="Please enter quantity. \n";
        document.getElementById('quantity').style.borderColor = "red";
        } 
    if (document.getElementById('price').value == "") {
        errormessage +="Please enter price. \n";
        document.getElementById('price').style.borderColor = "red";
        }
    if (errormessage != "") {

        alert(errormessage);
         return false;
        }
    else {

        alert('Data entered successfully!');

        namearray[i] = (document.getElementById('product').value);
        lastarray[i] = (document.getElementById('quantity').value);
        pricearray[i] = (document.getElementById('price').value);

        i++;
        var g=0;
        document.getElementById('output').innerHTML='';  
            for(g=0; g < namearray.length; g++) {
                document.getElementById('output').innerHTML = document.getElementById('output').innerHTML + namearray[g]+" " + lastarray[g]+ " " + pricearray[g] +"<br>";
                              }
        var productsub = document.getElementById('product');
        productsub.value = "";
        var quantitysub = document.getElementById('quantity')
        quantitysub.value = "";
        var pricesub = document.getElementById('price');
        pricesub.value = "";
    }
     
}

//search bar js
function openSlideMenu(){
      document.getElementById('side-menu').style.width = '250px';
      document.getElementById('main').style.marginLeft = '250px';
    }

    function closeSlideMenu(){
      document.getElementById('side-menu').style.width = '0';
      document.getElementById('main').style.marginLeft = '0';
    }