<template>
    <div id="home-app">
        <p>{% templatetag openvariable %} message {% templatetag closevariable %} </p>
    </div>
</template>

<script>
    module.exports = {
        name: 'Home',
        data: () => {
            return { message: "{{ project_name|title }}, project!" }
        }
    }
</script>

<style scoped>
    p {
        font-size: 3rem;
        text-align: center;
    }
</style>