import { createApp } from "vue"
import App from "@/App.vue"
import i18n from "@/plugins/i18n"
import router from "@/plugins/router"
import store from "@/plugins/store"
import ElementPlus from "element-plus"
import fr from "element-plus/es/locale/lang/fr"
import "element-plus/dist/index.css"

import "@/assets/css/element.css"

const app = createApp(App)

export const SITE = {
    "name": "Cynorrhodonnismes",
    "shortname": "Cynorrs"
}

export const API = (
    process.env.NODE_ENV === "production" ?
    "https://mcpronovost.pythonanywhere.com/api" :
    "http://localhost:8000/api"
)

app.use(i18n)
app.use(store)
app.use(router)
app.use(ElementPlus, {
    locale: fr,
})

app.mount("#app")
