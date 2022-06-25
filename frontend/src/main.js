import { createApp } from "vue"
import App from "./App.vue"
import router from "./router"
import store from "./store"
import ElementPlus from "element-plus"
import fr from "element-plus/es/locale/lang/fr"
import "element-plus/dist/index.css"

import "@/assets/css/element.css"

const app = createApp(App)

app.use(store)
app.use(router)
app.use(ElementPlus, {
    locale: fr,
})

app.mount("#app")