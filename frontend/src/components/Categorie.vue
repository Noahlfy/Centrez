<script setup>

import {api} from '@/services/api.js'

api('comptabilite', 'GET');

var comptes;

api('comptes', 'GET') 
    .then(response => {
        // Traitez la réponse ici
        comptes = [response.data];
    })
    .catch(error => {  
        console.error('Erreur lors de la récupération des données :', error);
    });

console.log(comptes)



var column_titles = ['Date de pièce', 'Libellé pièce', 'Pièce Justificatives', 'Débit', 'Crédit'];


function next_categorie() {

}

</script>

<template>

    <div id="categorie">
        <div id="select-categorie">
            <input type="text">
            <span @click="next_categorie();"></span>
        </div>
        <div>

        </div>
    </div>

</template>