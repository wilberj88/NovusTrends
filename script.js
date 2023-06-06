document.getElementById('requestForm').addEventListener('submit', function(event) {
  event.preventDefault();
  
  var name = document.getElementById('name').value;
  var email = document.getElementById('email').value;
  
  alert('Gracias por tu solicitud, ' + name + '! Te contactaremos pronto en ' + email + '.');
});
