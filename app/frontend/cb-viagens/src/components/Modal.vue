<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
  isOpen: Boolean
});

const { emit } = defineEmits();

const closeModal = () => {
  emit('close');
};
</script>

<template>
  <div v-if="isOpen" class="modal">
    <div class="modal-content">
      <img class="icon" src="./icons/erro.png" width="50px">
      <p class="text">Insira os valores para realizar a cotação</p>
      <button @click="closeModal">Fechar</button>
    </div>
  </div>
</template>

<style scoped>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  align-items: center;
  display: flex;
  justify-content: center;
  flex-direction: column;
  background-color: white;
  padding: 20px;
  border-radius: 5px;
  width: 50%;
  height: 30%;
}

.icon {
  padding-bottom: 10px;
}

button{
  margin-top: 30px;
  background-color: rgb(0, 110, 153);
  border: none;
  border-radius: 5px;
  height: 30px;
  width: 80px;
}
</style>