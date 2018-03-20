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
    if ($("#type").val() != "" && $("#inputNomDeVille").val() != "") {
      $.get("./api/"+$("#type").val()+"/"+$("#inputNomDeVille").val(), function(response) {
        $("#resultat").append(
          `
          <tr>
            <th></th>
            <th>${$("#type").val()}</th>
          </tr>
          `
        )
        let i = 0
        for (element of response) {
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
    }
  })
}
