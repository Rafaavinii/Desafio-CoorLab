<script setup>
import Modal from '@/components/Modal.vue';
import { ref, reactive } from 'vue';

const travel = reactive({
  destination: '',
  date: ''
})

const formSubmitted = ref(false)

const isModalOpen = ref(false);

const search = () => {
  if (travel.destination === '' || travel.date === ''){
    isModalOpen.value = true
  } else {
    console.log(travel.destination, travel.date)
    formSubmitted.value = true
  }
}

const closeModal = () => {
  isModalOpen.value = false;
};

</script>


<template>
  <div class="main-content">
      <div class="card">
          <div class="card-header"><img src="../components/icons/caminhao.png" width="20px" class="icon-caminhao">Calculadora de Viagem</div>
          <div class="card-body">
              <div class="form-section">
                  <h2 class="title">Calcule o Valor da Viagem</h2>
                  <form @submit.prevent="search">
                      <div class="form-group">
                          <label for="destino">Destino:</label>
                          <input type="text" id="destino" v-model="travel.destination">
                      </div>
                      <div class="form-group">
                          <label for="data">Data:</label>
                          <input type="date" id="data" v-model="travel.date">
                      </div>
                      <button type="submit">Buscar</button>
                  </form>
              </div>
              <div class="info-section" v-if="formSubmitted === false" >
                  Nenhum dado selecionado
              </div>
              <div class="info-section" v-if="formSubmitted">
                  
              </div>
          </div>
      </div>
  </div>

  <Modal :isOpen="isModalOpen" @click="closeModal" />
</template>



<style scoped>
.main-content {
flex: 1;
display: flex;
justify-content: center;
align-items: center;
}
.card {
background-color: #ffffff;
box-shadow: 0 4px 8px rgba(46, 46, 46, 0.356);
border-radius: 8px;
width: 80%; /* Ajuste conforme necessário */
}
.card-header {
background-color: #171f35;
padding: 20px;
border-top-left-radius: 8px;
border-top-right-radius: 8px;
color: white;
}

.card-body {
padding: 20px;
display: flex;
}
.form-section, .info-section {
width: 50%;
padding: 20px;
}

.title {
  padding-top: 40px;
}

.form-section {
  background-color: rgba(206, 206, 206, 0.418);
  border-radius: 8px;
}

.form-group {
margin-bottom: 1rem;
display: flex;
flex-flow: column;
}

button {
padding: 0.5rem 1rem;
background-color: #56caf8;
color: #fff;
border: none;
border-radius: 4px;
cursor: pointer;
margin-bottom: 60px;
}

button:hover {
background-color: #0056b3;
}

label {
  font-size: 15px;
}

input{
  height: 35px;
  border-color: rgba(128, 128, 128, 0.13);
  border-radius: 4px;
}

form {
  padding-top: 15px;
}


.icon-caminhao{
  margin-right: 5px;
  margin-top: 5px;
  width: 22px;
}
</style>
