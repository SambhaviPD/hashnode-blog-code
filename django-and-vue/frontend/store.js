import {reactive} from 'vue'


export default store = reactive({
    token: null,
    setToken(newToken) {
        this.token = newToken
    },
})