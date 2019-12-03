<template>
    <div id="home-app">
        <p>{{ message }}</p>
    </div>
</template>

<script>
    module.exports = {
        name: 'Home',
        data: () => {
            return { message: "Hello, welcome to your new project!" }
        }
    }
</script>

<style scoped>
    p {
        font-size: 3rem;
        text-align: center;
    }
</style>
