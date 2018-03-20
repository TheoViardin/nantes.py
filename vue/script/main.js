$(window).on('load', function () {

//Autocomplete
  var tags = [];
  $( "#inputNomDeVille" ).autocomplete({
    source: function (request, response) {
      $.get("http://infoweb-ens/~jacquin-c/codePostal/commune.php?commune="+$("#inputNomDeVille").val()+"&maxRows=3", function (reponse) {
        let i = 0
        let sourceArray = [];
        for (ville of reponse) {
          sourceArray[i] = {label:ville.Ville, value:ville.Ville}
          i++
        }
        response(sourceArray)
      })
    },
    minLength: 3
  });

  $("#recherche").on("click", function() {
    console.log($("#type").val())
      console.log($("#inputNomDeVille").val())
    if ($("#type").val() != "" && $("#inputNomDeVille").val() != "") {
      console.log("localhost:2056/api/"+$("#type").val()+"/"+$("#inputNomDeVille").val())
      $.get("http://localhost:2056/api/"+$("#type").val()+"/"+$("#inputNomDeVille").val(), function(response) {
        //http://localhost:2056/api/activites/Vertou
        console.log("test")
        $("#resultat").append(
          `
          <tr>
            <th></th>
            <th>${$("#type").val()}</th>
          </tr>
          `
        )
        let i = 0
        for (element of response[$("#type").val()]) {
          $("#resultat").append(
            `
            <tr>
              <td>${i}</td>
              <td>${element[0]}</td>
            </tr>
            `
          )
          i++
        }
      })
      .fail(function(response) {
  console.log( response );
})
    }
  })
})
