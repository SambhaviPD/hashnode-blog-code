<script setup>
import axios from 'axios'
import { reactive, onMounted } from 'vue'

let data = reactive({
    title: 'Hello World',
    contentList: []
})
onMounted(async ()=>{
    let response;
    try {
        response = await axios.get('/api/posts/')
    } catch(error) {
        response = error.response
    }

    if (response.status === 200) {
        let responseData = response.data
        data.title = "Post"
        data.contentList = responseData.data
    } else {
        data.title = "Not found"
    }
})
</script>

<template>
    <div>
        <h1> {{  data.title  }}</h1>
        <div v-for="content in data.contentList" :key="content.id">
            <h3>{{ content.id }} {{ content.title }}</h3>
        </div>
    </div>
</template>