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

  $("#recherche").on("click", function(event) {
    event.preventDefault()
    console.log($("#type").val())
      console.log($("#inputNomDeVille").val())
    if ($("#type").val() != "" && $("#inputNomDeVille").val() != "") {
      console.log("localhost:2056/api/"+$("#type").val()+"/"+$("#inputNomDeVille").val())
      $.get("http://localhost:2056/api/"+$("#type").val()+"/"+$("#inputNomDeVille").val(), function(response) {
        //http://localhost:2056/api/activites/Vertou
        $('#resultat').empty()
        if (response.reussite == "true") {
          $('#resultat').append(`
            <thead>
              <tr>
                <th></th>
                <th>${$("#type").val()}</th>
              </tr>
            </thead>
            <tbody>
            </tbody>`)
          let i = 0
          for (element of response[$("#type").val()]) {
            console.log(element)
            $("#resultat tbody").append(
              `
              <tr>
                <td>${i}</td>
                <td>${element[0]}</td>
              </tr>
              `
            )
            i++
          }
          $('#resultat').DataTable();
        } else {
          $("#resultat").append("<p>Pas de donnée sur cette ville</p>")
        }
      })
      .fail(function(response) {
  console.log( response );
})
    }
  })
})
