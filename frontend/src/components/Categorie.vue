<script setup>

import {api} from '@/services/api.js'

api('comptabilite', 'GET');

var column_titles = ['Date de pièce', 'Libellé pièce', 'Pièce Justificatives', 'Débit', 'Crédit'];


</script>

<template>

    <div id="categorie">
        <div id="select-categorie">
            <input type="text">
            
        </div>
        <div>

        </div>
    </div>

</template>