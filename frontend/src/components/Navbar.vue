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


import {ref} from 'vue'

const currentTab = ref('')
const tabs = ref([])
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
    components: ['GrandLivre', 'Saisie', 'Chèques'],
  },
  {
    name: 'Budget',
    components: ['Global', 'Evenement', 'Reference'],
  },
  {
    name: 'PiecesJustificatives',
    components: [],
  },
  {
    name: 'EditionDeDocuments',
    components: [],
  },
  {
    name: 'Juridique',
    components: [],
  },
  {
    name: 'Documentation',
    components: [],
  },
];


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
    tabs.value.unshift({name: name, component: tab.component})
  } else if (!ongletDejaOuvert) {

    // si name n'est pas dans tabs
    const titre_associe = arborescence.find(t => t.components.includes(name)).name

    console.log(titre_associe)
    if (!(tabs.value.some(t => t.name == titre_associe))) {
      // Cas où un sous-titre est ajouté, mais le titre ne l'est pas encore
      ouvrirOnglet(titre_associe)
      tabs.value.push({name: name, component: tab.component})
    } else {
      // Cas classique où c'est un sous-titre comme 'GrandLivre' qui est ajouté
      tabs.value.push({name: name, component: tab.component})
    }

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
  <div>
    <div id="nav_container">
      <nav>
        <ul>
          <li><a href="#">Accueil</a>
          </li>
          <li class="deroulant" v-for="arbo in arborescence" :key="arbo.name">
            <a href="#" @click.prevent="ouvrirOnglet(arbo.name)">{{ arbo.name }}</a>
            <ul class="sous">
              <li v-for="component in arbo.components" :key="component">
                <a @click="ouvrirOnglet(component)">{{ component }}</a>
              </li>
            </ul>
          </li>
        </ul>
      </nav>
    </div>

    <div id="fenetres">
      <div id="onglets">
        <div v-for="tab in tabs" :key="tab.name" :class="['tab-button', { active: currentTab === tab.name }]"
             @click="currentTab = tab.name">
          <span> {{ tab.name }} </span>
          <button v-if=" !(tabList.find(t => t.name === tab.name )?.fixed)" id="fermer-onglet"
                  @click.stop="fermerOnglet(tab.name)">x
          </button>
        </div>
      </div>
      <component v-if="tabs.find(t => t.name === currentTab)" :is="tabs.find(t => t.name === currentTab)?.component"
                 class="tab"></component>
    </div>
  </div>
</template>

<style scoped>
.tab-button {
  display: flex;
  align-items: center;
  gap: 1rem;
  background-color: #CCC;
  cursor: pointer;
  padding: 2px 16px;
  border-radius: 32px 32px 32px 32px;
  height: 33px;
  font-size: 14px;
}

.active {
  position: relative;
  background-color: #CCC;
  border-radius: 16px 16px 0 0;
  border-bottom: 12px solid #CCC;
}

.active:before {
  content: "";
  position: absolute;
  bottom: -5px;
  right: -40px;
  height: 30px;
  width: 40px;
  background: transparent;
  /* border-radius of pseudo element */
  border-bottom-left-radius: 50%;
  /* box shadow to give the shadow of the pseudo-element the same color as the background */
  box-shadow: -10px 5px 0 0 #CCC;
}
.active:after {
  content: "";
  position: absolute;
  bottom: -5px;
  left: -40px;
  height: 30px;
  width: 40px;
  background: transparent;
  /* border-radius of pseudo element */
  border-bottom-right-radius: 50%;
  /* box shadow to give the shadow of the pseudo-element the same color as the background */
  box-shadow: 10px 5px 0 0 #CCC;
}
</style>


