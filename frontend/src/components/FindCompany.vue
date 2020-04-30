<template>
    <div class="find">
        <form method="post" @submit.prevent="find">
            <div class="form-group text-left">
                <label for="id_data">Введите ИНН или ОГРН субьекта</label><br>
                <input v-model="data" type="text" @input="checkdata">

            </div>
            <button>Проверить</button>
            <br>
            <p>{{ message }}</p>

        </form>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        name: 'FindCompany',
        data() {
            return {
                data: '',
                message: '',
            };
        },
        methods: {
            find: function () {
                alert(this.data)

                axios({
                    url: 'http://127.0.0.1:8080/company',
                    data: {'query': this.data},
                    method: 'POST'
                })
                    .then(response => {
                        console.log(response.data)
                        if (response.data.data) {
                            alert('Компания является субъектом малого или среднего предпринимательства на сайте https://rmsp.nalog.ru/')
                        } else {
                            alert('Компания не является субъектом малого или среднего предпринимательства на сайте https://rmsp.nalog.ru/')
                        }
                    })
                    .catch(error => {
                        console.log(error)
                    })
            },
            checkdata: function (event) {
                if (event.target.value.length === 10) {
                    this.message = "Вы ввели ИНН";
                } else if (event.target.value.length === 13) {
                    this.message = "Вы ввели ОГРН";
                } else {
                    this.message = "";
                }
            }
        }
    }
</script>

<style scoped>
    form {
        margin: 200px auto;
        width: 300px;
    }
</style>
