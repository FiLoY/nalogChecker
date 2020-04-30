<template>
    <div class="recentlyqueries">
        <p>Предыдущие проверки(в пределах 5мин):</p>
        <p v-for="item in this.recently_requests.data" :key="item">
            Компания {{ item[0] }}<span v-if="item[1]"> является </span><span v-else> не является</span>
            <span> субъектом малого или среднего предпринимательства на сайте https://rmsp.nalog.ru/</span>
        </p>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'FindCompany',
        data() {
            return {
                recently_requests: '',
            };
        },
        created() {
            axios
                .get('http://127.0.0.1:8080/company')
                .then(response => {
                    this.recently_requests = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
</script>

<style scoped>
    form {
        margin: 200px auto;
        width: 300px;
    }
</style>
