$(document).ready(function(){
    
    //Aqui ya comenzamos usando el JQUERY
    // Para obtenr valores lo hacemos mediante un query $('Aqui dentro va la clase, el id) $('#username') $('.username')
    $('#ingresar').click(function(e){ 
        e.preventDefault();
        var user = $("#username").val();
        var password = $("#password").val();
        console.log(user, password)


        //Comenzamos peticiones con AJAX

        $.ajax({
            method: "POST",
            url: "http://localhost:8000/login",
            data: ({ user: user, pass: password }),
    
          }).done(function(data) {
            alert(data); // imprimimos la respuesta
          }).fail(function() {
            alert("Algo salió mal");
          }).always(function() {
            alert("Siempre se ejecuta")
          });

          
    });





  });