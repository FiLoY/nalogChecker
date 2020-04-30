<template>
    <div id="app">
        <FindCompany/><hr>
        <GetRecentlyFindResults/>

    </div>
</template>

<script>
    import FindCompany from './components/FindCompany'
    import GetRecentlyFindResults from './components/GetRecentlyFindResults'

    export default {
        name: 'App',
        components: {
            FindCompany,
            GetRecentlyFindResults,
        }
    }
</script>

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }
</style>
