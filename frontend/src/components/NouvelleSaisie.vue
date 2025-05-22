<script setup>
import {api} from '@/services/api.js'

api('comptabilite', 'GET')
    .then(response => {
      // Traitez la réponse ici
    })
    .catch(error => {
      console.error('Erreur lors de la récupération des données :', error);
    });

</script>

<template>


  <div>


    <div id="saisie">
      <div>
        <h1>Ceci est le form pour réaliser une saisie</h1>

        <form>
          <label for="numero-de-compte">Numéro de compte</label>
          <input type="text" id="numero-de-compte"/>

          <label for="categorie">Nom de la catégorie</label>
          <input type="text" id="categorie"/>

          <label for="date">Date</label>
          <input type="text" id="date">
        </form>


      </div>
    </div>

    <div id="contrepartie">


    </div>
  </div>


</template>
