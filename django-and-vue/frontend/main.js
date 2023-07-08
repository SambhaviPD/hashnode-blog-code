import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

const el = document.getElementById('app')

if (el) {
    const data = {...el.dataset}
    console.log('data: ', data)
    const app = createApp(App, data)
    app.use(createPinia())
    app.mount('#app')
}



