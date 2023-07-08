<script setup>
    import axios from 'axios'
    import { ref, reactive } from 'vue'
    import store from './../store'

    let title = ref('')
    const initFormData = reactive({
        title: '',
        author: '',
        review: ''
    })
    const formData = reactive({initFormData})
    const error = ref({})

    const handleSubmitForm = async (event) => {
        if (event) {
            event.preventDefault()
        }
        const formDataJson = JSON.stringify(formData)
        const csrfToken = store.token
        const axiosConfig = { headers: {
            "X-CSRFToken": csrfToken,
            }
        }

        let response;
        try {
            response = await axios.post('/api/review/create/', formDataJson, axiosConfig)
        } catch(error) {
            error.value = error.response
            if (error.response === 500) {
                alert("Server failure. Please try again later")
            }
            console.log(error.value)
        }
        console.log(response)
        if (response.status === 201) {
            for (let key of Object.keys(formData)) {
                formData[key] = initFormData[key]
            }
        }
    }

</script>
<template>
    <form @submit.prevent="handleSubmitForm">
        <div>
            <div>
                <input type="text" v-model="formData.title" required name="title" placeholder="Your book title"/>
                <p> {{  formData.title  }}</p>
                <br/>
            </div>
            <div>
                <input type="text" v-model="formData.author" required name="author" placeholder="Author of the book"/>
                <p> {{  formData.author  }}</p>
                <br/>
            </div>
            <div>
                <textarea v-model="formData.review" required name="review" placeholder="Write your review here"></textarea>
                <p> {{  formData.review  }}</p>
            </div>
            <br/>
            <button>Submit Review</button>
        </div>
    </form>
</template>