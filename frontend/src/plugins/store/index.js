import { createStore } from "vuex";
import { Buffer } from "buffer";
import { getterApp, moduleApp } from "@/plugins/store/app";
import { getterRat, moduleDrat, moduleFrat } from "@/plugins/store/rat";
import { getterPlayer, modulePlayer, getterHeros } from "@/plugins/store/player";
import VuexPersistence from "vuex-persist";
import Cookies from "js-cookie";

const vuexLocal = new VuexPersistence({
    key: "qpcynorrs",
    storage: window.localStorage,
    reducer: (state) => ({
        drat: state.drat
    })
})

const vuexSession = new VuexPersistence({
    key: "qpcynorrs",
    storage: window.sessionStorage,
    reducer: (state) => ({
        player: state.player
    })
})

const vuexCookie = new VuexPersistence({
    key: "qpcynorrs",
    restoreState: (key) => {
        if (Cookies.get(key)) {
            return JSON.parse(
                Buffer.from(Cookies.get(key), "base64").toString("utf8")
            )
        }
    },
    saveState: (key, state) => {
        if (state) {
            (Cookies.set(
                key,
                Buffer.from(JSON.stringify(state)).toString("base64"),
                { expires: 30 }
            ))
        }
    },
    modules: ["frat"]
})

const winResize = (store) => {
    store.commit("SET_WINSIZES")
    window.addEventListener("resize", () => {
        store.commit("SET_WINSIZES")
    })
}

const store = createStore({
    getters: {
        app: getterApp,
        rat: getterRat,
        player: getterPlayer,
        heros: getterHeros
    },
    modules: {
        app: moduleApp,
        drat: moduleDrat,
        frat: moduleFrat,
        player: modulePlayer
    },
    plugins: [
        vuexLocal.plugin,
        vuexSession.plugin,
        vuexCookie.plugin,
        winResize
    ]
})

export default store;
