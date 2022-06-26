import { createApp } from "vue"
import App from "./App.vue"
import i18n from "@/plugins/i18n"
import router from "@/plugins/router"
import store from "@/plugins/store"
import ElementPlus from "element-plus"
import fr from "element-plus/es/locale/lang/fr"
import "element-plus/dist/index.css"

import "@/assets/element.css"

const app = createApp(App)

app.use(i18n)
app.use(store)
app.use(router)
app.use(ElementPlus, {
    locale: fr,
})

app.mount("#app")
