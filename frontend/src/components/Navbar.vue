<script setup>

import GrandLivre from '@/Views/GrandLivre.vue'
import Saisie from '@/Views/Saisie.vue'
import Accueil from '@/Views/Accueil.vue'
import Comptabilite from '@/Views/Comptabilite.vue'
import Budget from '@/Views/Budget.vue'
import PiecesJustificatives from '@/Views/PiecesJustificatives.vue'
import EditionDeDocuments from '@/Views/EditionDeDocuments.vue'
import Juridique from '@/Views/Juridique.vue'
import Documentation from '@/Views/Documentation.vue'
import {ref, watch} from 'vue'
import TabLabel from "@/components/TabLabel.vue";

const IsNavbarOpen = ref(false)
const currentTab = ref('')
const tabs = ref([])
const currentColor = ref('')
const tabList = ref([
  {name: 'Accueil', component: Accueil, fixed: true},
  {name: 'Comptabilité', component: Comptabilite, fixed: true},
  {name: 'Budget', component: Budget, fixed: true},
  {name: 'PiecesJustificatives', component: PiecesJustificatives, fixed: true},
  {name: 'EditionDeDocuments', component: EditionDeDocuments, fixed: true},
  {name: 'Juridique', component: Juridique, fixed: true},
  {name: 'Documentation', component: Documentation, fixed: true},
  {name: 'GrandLivre', component: GrandLivre, fixed: false},
  {name: 'Saisie', component: Saisie, fixed: false},
])
const arborescence = [
  {
    name: 'Comptabilité',
    icon: 'mdi-bank',
    color: '#AEDFF7', // Bleu pastel
    components: ['GrandLivre', 'Saisie', 'Chèques'],
  },
  {
    name: 'Budget',
    icon: 'mdi-chart-bar',
    color: '#C8E6C9', // Vert menthe clair
    components: ['Global', 'Evenement', 'Reference'],
  },
  {
    name: 'PiecesJustificatives',
    icon: 'mdi-receipt',
    color: '#FFE0B2', // Orange pâle
    components: [],
  },
  {
    name: 'EditionDeDocuments',
    icon: 'mdi-file-document-outline',
    color: '#D1C4E9', // Violet doux
    components: [],
  },
  {
    name: 'Juridique',
    icon: 'mdi-gavel',
    color: '#FFCDD2', // Rouge rosé léger
    components: [],
  },
  {
    name: 'Documentation',
    icon: 'mdi-book-open-variant',
    color: '#FFF9C4', // Jaune très clair
    components: [],
  },
];

watch(currentTab, (newVal) => {
  const tab = tabs.value.find(t => t.name === newVal);
  if (tab && tab.color) {
    currentColor.value = tab.color;
  } else {
    currentColor.value = '#CCC';
  }
});

function ouvrirOnglet(name) {

  const tab = tabList.value.find(t => t.name === name)
  if (!tab) {
    console.warn(`Composant introuvable pour : ${name}`)
    return
  }

  const ongletDejaOuvert = tabs.value.some(t => t.name === name)
  const estTitrePrincipal = arborescence.some(t => t.name === name)

  // Si c'est le nom d'un titre du menu, on l'ajoute en fixe à gauche du menu des onglets ouverts
  if (estTitrePrincipal && !ongletDejaOuvert) {
    // Si il y en a déjà un d'ouvert on le remplace
    // Aussi, on met toujours le menu en premier dans l'affichage, d'où l'utilisation de shift et unshift (et plus globalement l'utilisation de listes)
    const menu_names = arborescence.map(t => t.name)
    for (let i = 0; i < menu_names.length; i++) {
      const index = tabs.value.findIndex(t => t.name === menu_names[i]);
      if (index !== -1) {
        tabs.value.splice(index, 1);
      }
    }
    const arbo_associe = arborescence.find(t => t.name === name)
    tabs.value.unshift({name: name, component: tab.component, color: arbo_associe.color})
  } else if (!ongletDejaOuvert) {

    // si name n'est pas dans tabs
    const arbo_associe = arborescence.find(t => t.components.includes(name))
    const titre_associe = arbo_associe.name
    if (!(tabs.value.some(t => t.name === titre_associe))) {
      ouvrirOnglet(titre_associe)
    }
    tabs.value.push({name: name, component: tab.component, color: arbo_associe.color})
  }
  // On met à jour l'onglet actif
  currentTab.value = name

}

function fermerOnglet(tabName) {
  const index = tabs.value.findIndex(t => t.name === tabName);
  if (index !== -1) {
    tabs.value.splice(index, 1);
  }
  if (tabName === currentTab.value) {
    currentTab.value = tabs.value.length > 0 ? tabs.value[0].name : '';
  }
}

</script>

<template>
  <v-navigation-drawer
      expand-on-hover
      absolute
      permanent
      rail
      ref="navbar"
      @mouseover="IsNavbarOpen = true"
      @mouseleave="IsNavbarOpen = false"
  >
    <v-list>
      <v-list-item
          prepend-avatar="https://randomuser.me/api/portraits/women/85.jpg"
          subtitle="sandra_a88@gmailcom"
          title="Sandra Adams"
      ></v-list-item>
    </v-list>

    <v-divider></v-divider>
    <div v-for="arbo in arborescence">
      <v-list density="compact" nav>
        <v-list-item :prepend-icon="arbo.icon" :title="arbo.name" :bg="arbo.color" @click="ouvrirOnglet(arbo.name)"/>
        <v-list-item v-for="componants in arbo.components"
                     :key="componants"
                     :title="componants"
                     v-if="IsNavbarOpen"
                     @click="ouvrirOnglet(componants)"></v-list-item>
      </v-list>
      <v-divider></v-divider>
    </div>
  </v-navigation-drawer>
  <div style="height: 100%; background-color: #F5EDED;" class="flex-column ml-14 px-4 py-2">
    <div class="tab-container">
      <v-btn
          icon
          @click="ouvrirOnglet('Accueil')"
          class="rounded-full -mb-1 mx-1"
          :style="{ backgroundColor: currentTab === 'Accueil' ? '#E0E0E0' : 'transparent', height: '36px', width: '36px' }">
        <v-icon>mdi-home</v-icon>
      </v-btn>
      <tab-label
          v-for="tab in tabs.values()"
          :key="tab.name"
          :isActive="currentTab === tab.name"
          :tabName="tab.name"
          :tab-color="tab.color"
          @click="currentTab = tab.name"
          @close="fermerOnglet(tab.name)">
      </tab-label>
    </div>
    <div class="canva">
      <component v-if="tabs.find(t => t.name === currentTab)" :is="tabs.find(t => t.name === currentTab)?.component"
                 class="tab"></component>
    </div>
  </div>
</template>

<style scoped>

.tab-container {
  display: flex;
  min-height: 48.21px;
  flex-direction: row;
  justify-content: start;
  gap: 0.25rem;
  align-items: baseline;
  border-radius: 5px;
  overflow: clip;
}

.canva {
  position: relative;
  z-index: 100;
  width: 100%;
  height: 93%; /* TODO: A fix de toute urgence */
  background-color: whitesmoke;
  border-radius: 8px;
  border: 0.3rem solid v-bind(currentColor);
}

.tab {
  height: 100%;
  width: 100%;
  padding: 10px;
}
</style>


