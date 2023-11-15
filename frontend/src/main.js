import './assets/tailwind.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import axios from 'axios'

import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { faFontAwesome } from '@fortawesome/free-brands-svg-icons'

// Add icons to the library
library.add(faUserSecret, faFontAwesome)

axios.defaults.baseURL = 'http://127.0.0.1:8000/'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
