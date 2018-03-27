$(window).on('load', function () {

//Autocomplete
  var tags = [];
  $( "#inputNomDeVille" ).autocomplete({
    source: function (request, response) { // La liste de villes proposées se met à jour dès que 3 caractères sont rentrés
      $.get("http://infoweb-ens/~jacquin-c/codePostal/commune.php?commune="+$("#inputNomDeVille").val()+"&maxRows=3", function (reponse) {
        // Requete contenant les lettres entrées dans l'input et maxRow étant le nombre de ville à renvoyer
        let i = 0
        let sourceArray = [];
        for (ville of reponse) { // Création du dictionnaire servant de liste de proposition à jquery
          sourceArray[i] = {label:ville.Ville, value:ville.Ville} // label = texte affiché // Value = texte envoyé
          i++
        }
        response(sourceArray)
      })
    },
    minLength: 3 // Nombre de lettres necessaires à l'affichage de propositions
  });

//Recherche en fonction de la ville et des valeurs cochées/rentrées
  $("#recherche").on("click", function(event) {
    event.preventDefault()
    if ($("#type").val() != "" && $("#inputNomDeVille").val() != "") { // Si l'utilisateur a rentré une ville
      $.get("http://localhost:2056/api/"+$("#type").val()+"/"+$("#inputNomDeVille").val(), function(response) {
        //http://localhost:2056/api/activites/Vertou
        // Réquete sur l'api bottle (notre serveur python) contenant le type de requete (activites ou equipements) et la ville concernée
        $('#resultat').empty() // On vide la partie de la page reservée à l'affichage
        if (response.reussite == "true") { // Si le message renvoyé est positif
          if (response[$("#type").val()].length > 0) { // Si le tableau n'est pas vide
          $('#resultat').append(`
            <thead>
              <tr>
                <th></th>
                <th>${$("#type").val()}</th>
              </tr>
            </thead>
            <tbody>
            </tbody>`) // On ajoute l'entete du tableau
          let i = 0
          for (element of response[$("#type").val()]) { // On ajoute toute les valeurs dans tableau
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
          $('#resultat').DataTable(); // On active DataTable de jQuery ui sur le tableau
        } else { // Si le tableau recu est vide
          $("#resultat").append("<p>Pas de donnée sur cette ville</p>") // On l'affiche au client
        }
      } else { // Si reussiter == false
        alert("Erreur lors de traitement de la requete:\n" + response.message) // On affiche un pop-up avec le message d'erreur du serveur
      }
      })
      .fail(function(response) { // En cas d'erreur de communication avec le serveur on l'affiche au client
        alert("Erreur de communication avec le serveur");
})
    }
  })
})
