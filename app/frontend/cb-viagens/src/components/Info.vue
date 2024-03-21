<script setup>
import { ref } from 'vue';

const props = defineProps({
  isformSubmitted: Boolean
});

const clean = () => {
  props.isformSubmitted = false;
};
</script>

<template>
<div class="response" v-if="formSubmitted === false">
    <p>Nenhum dado selecionado</p>
</div>
<div class="response" v-if="formSubmitted">
    <div class="container">
        <div class="card-info">
            <div class="icon-card">
                <img src="../components/icons/erro.png" width="50px">
            </div>
            <div class="info">
                <!-- Informações da viagem -->
                <h2>Transportadora</h2>
                <p>Leito: 3 (completo)</p>
                <p>Tempo estimado: 6h</p>
            </div>
            <div class="price">
                <!-- Preço -->
                <h2>Preço:</h2>
                <p>R$ 1000</p>
            </div>
        </div>
        <div class="card-info">
            <div class="icon-card">
                <img src="../components/icons/erro.png" width="50px">
            </div>
            <div class="info">
                <!-- Informações da viagem -->
                <h2>Transportadora</h2>
                <p>Poltrona: 3 (completo)</p>
                <p>Tempo estimado: 6h</p>
            </div>
            <div class="price">
                <!-- Preço -->
                <h2>Preço:</h2>
                <p>R$ 1200</p>
            </div>
        </div>
    </div>
</div>
</template>

<style>

.container {
display: flex;
justify-content: center;
flex-direction: column;
}

.card-info {
display: flex;
flex-direction: row;
width: 100%;
margin: 10px;
padding: 20px;
border: 1px solid #ccc;
border-radius: 5px;
background-color: rgba(206, 206, 206, 0.418);
}

.icon-card {
width: 100%;
padding: 0;
display: flex;
justify-content: center;
background-color: rgb(0, 125, 163);
}

.info {
flex: 1;
}

.price {
display: flex;
flex-direction: column;
align-items: flex-end;
}

h2 {
margin-bottom: 10px;
}

p {
margin: 5px 0;
}

</style>