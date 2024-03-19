<template>
    <div class="sidebar">
        <img src="../assets/logo.png" class="logo">
        <router-link to="/"><img src="./icons/calculator.png" class="icon">Calculadora de Viagem</router-link>
    </div>

</template>

<style scoped>
    .sidebar {
        width: 35%;
        background-color: #171f35;
        padding-top: 20px;
        height: 100vh;
    }

    .sidebar .logo {
        display: block;
        margin: 0 auto; /* Para centralizar a imagem horizontalmente */
        width: 150px;
        align-items: center;
        margin-top: 10px;
    }

    .sidebar .icon {
        width: 15px;
        margin-right: 15px;
    }

    .sidebar a {
        display: block;
        color: white;
        text-decoration: none;
        padding: 10px;
        margin-top: 30px;
        margin-left: 10px;
    }

    .sidebar a:hover {
        background-color: #555;
    }

</style>