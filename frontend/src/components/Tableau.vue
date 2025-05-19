<template>
  <table>
    <thead>
      <tr>
        <th v-for="(col, index) in column_names" :key="index" class="nom_colonne">
          {{ col }}
        </th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="rowIndex in 10" :key="rowIndex">
        <td v-for="(col, index) in column_names" :key="index" class="case">
            i
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup>
const column_names = ["Date", "Libellé", "Pièce justificative","Débit", "Crédit"];
</script>
