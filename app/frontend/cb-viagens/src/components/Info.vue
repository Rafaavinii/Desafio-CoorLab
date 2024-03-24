<script setup>
import { ref, onMounted, watchEffect, watch } from 'vue';

const props = defineProps({
  isformSubmitted: Boolean,
  selectedCity: String,
});

watchEffect(() => {
  console.log(props.selectedCity);
});


const responseData = ref(null);

const fetchDataFromAPI = (city) => {
  fetch('http://127.0.0.1:8000/api/' + city)
    .then(response => {
      if (!response.ok) {
        throw new Error('Erro ao carregar dados da API');
      }
      return response.json();
    })
    .then(data => {
      responseData.value = data;
    })
    .catch(error => {
      console.error(error);
    });
};

watch(() => props.selectedCity, (newCity) => {
  const responseData = fetchDataFromAPI(newCity)

  console.log(responseData)
  
});



</script>

<template>
    <!-- <div v-if="responseData">
      <h2>Dados da API:</h2>
      <ul>
        <li v-for="item in responseData" :key="item.id">
          {{ item.name }} - {{ item.description }}
        </li>
      </ul>
    </div> -->
<div class="response" v-if="isformSubmitted === false">
    <p>Nenhum dado selecionado</p>
</div>
<div class="response" v-if="isformSubmitted">
    <div class="container">
      <p class="first-item">Estas são as melhores alternativas de viagem para a data selecionada</p>

        <div class="card-info">
        <div class="details">
            <div class="icon-card">
                <img src="../components/icons/coin.png" width="30px" height="30px">
            </div>
            <div class="info">
                <h2>{{ responseData.duration.name }}</h2>
                <p>Leito: {{ responseData.duration.seat }} (completo)</p>
                <p>Tempo estimado: {{responseData.duration.duration}}h</p>
            </div>
        </div>
        <div class="price">
            <h2>Preço:</h2>
            <p>R$ {{responseData.duration.price_confort}}</p>
        </div>
        </div>
        <div class="card-info">
        <div class="details">
            <div class="icon-card">
                <img src="../components/icons/time.png" width="30px" height="30px">
            </div>
            <div class="info">
                <h2>{{ responseData.price_econ.name }}</h2>
                <p>Leito: {{ responseData.price_econ.seat }} (completo)</p>
                <p>Tempo estimado: {{responseData.price_econ.duration}}h</p>
            </div>
        </div>
        <div class="price">
            <h2>Preço:</h2>
            <p>R$ {{responseData.price_econ.price_econ}}</p>
        </div>
        </div>
        
    </div>
</div>
</template>

<style>
.info-section {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.response {
  width: 100%;
  height: 100%;
  margin-left: 20px;
}

.container {
  display: flex;
  flex-flow: column;
  justify-content: center;
  align-items: center;
}

.card-info{
  display: flex;
  flex-flow: row nowrap;
  justify-content: center;
  margin: 5px;
  width: 100%;
}

.details{
  display: flex;
  background-color: #b9c0d481;
  border-radius: 8px;
  width: 90%;
}

.info{
  padding: 10px;
  width: 70%;
  margin-left: 10px;
}

.price {
  background-color: #b9c0d481;
  border-radius: 8px;
  margin-left: 10px;
  width: 30%;
  padding: 10px;
}

.icon-card{
  background-color: #3f98bb;
  padding: 20px;
  border-radius: 8px 0 0 8px;
  display: flex;
  justify-content: center;
  align-items: center;
}

</style>