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

app.config.globalProperties.$filters = {
    num_to_element(num, digits) {
        const lookup = [
            { value: 1, symbol: "" },
            { value: 1e3, symbol: "k" },
            { value: 1e6, symbol: "M" },
            { value: 1e9, symbol: "G" },
            { value: 1e12, symbol: "T" },
            { value: 1e15, symbol: "P" },
            { value: 1e18, symbol: "E" }
        ];
        const rx = /\.0+$|(\.[0-9]*[1-9])0+$/;
        var item = lookup.slice().reverse().find(function (item) {
            return num >= item.value;
        });
        return item ? (num / item.value).toFixed(digits).replace(rx, "$1") + item.symbol : "0";
    },
    date_to_str(date) {
        const options = { year: "numeric", month: "long", day: "numeric", hour: "numeric", minute: "numeric", hour12: false };
        return new Date(date).toLocaleString("fr", options)
    }
}

app.use(i18n)
app.use(store)
app.use(router)
app.use(ElementPlus, {
    locale: fr,
})

app.mount("#app")
