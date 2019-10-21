
$('#Busqueda').keyup(function(e){
    consulta = $("#Busqueda").val();
    $.ajax({
    data: {'nombre': consulta},
    url: '/busqueda/',
    type: 'get',
    success : function(data) {
            console.log(data[0].nombre);
    },
    error : function(message) {
            console.log(message);
         }
    });
   });