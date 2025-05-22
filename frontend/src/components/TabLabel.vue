<script setup>

const {isActive, tabName, tabColor} = defineProps({
  isActive: {
    type: Boolean,
    default: false
  },
  tabName: {
    type: String,
    default: 'Tab'
  },
  tabColor: {
    type: String,
    default: 'blue'
  }
})
</script>

<template>
  <div :class="['tab-label', isActive ? 'active' : '']" :style="'background-color: ' + tabColor">
    <span>{{ tabName }}</span>
    <button @click="$emit('close')">X</button>
  </div>
</template>

<style scoped>
.tab-label {
  margin: 4px;
  display: flex;
  position: relative;
  align-items: center;
  gap: 1.5rem;
  padding: 8px 16px;
  border-radius: 24px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  background-color: v-bind(tabColor);
}
.tab-label.active {
  margin: 0;
  border-radius: 16px 16px 0px 0px;
  border-bottom: 5px solid v-bind(tabColor);
}

.tab-label.active:before {
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
  box-shadow: -10px 5px 0 0 v-bind(tabColor);
}
.tab-label.active:after {
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
  box-shadow: 10px 5px 0 0 v-bind(tabColor);
}

.tab-label.active div:after{
  content: "";
  position: absolute;
  bottom: 10px;
  left: 10px;
  height: 30px;
  width: 40px;
  background: #CCC;
}
</style>
