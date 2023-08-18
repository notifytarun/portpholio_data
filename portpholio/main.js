var act = document.getElementById('active');
var bar = document.getElementsByClassName('bar');

bar.addEventListener('click',function() {

    


  
    document.getElementById("bar").innerHTML = "Hello World";
  


})

window.onscroll = function() {myFunction()};

function myFunction() {

    if (window.scrollY > 159) {
        document.getElementsByTagName('li').style('color')='red';
        
      }


}
