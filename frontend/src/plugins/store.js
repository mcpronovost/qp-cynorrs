import { createStore } from "vuex";
import { Buffer } from "buffer";
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
                key, Buffer.from(JSON.stringify(state)).toString("base64"), {
                    expires: 30
                }
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
        app: (state) => {
            return {
                win: state.app.win
            }
        },
        player: (state) => {
            return state.player
        },
        rat: (state) => {
            if (state.drat.s && state.frat.e) {
                let s = Buffer.from(state.drat.s, "base64").toString("utf8")
                let e = Buffer.from(state.frat.e, "base64").toString("utf8")
                return `Token ${s}${e}`
            } else {
                return null
            }
        }
    },
    modules: {
        app: {
            state: () => ({
                win: {w: 1880, h: 980}
            }),
            mutations: {
                SET_WINSIZES (state) {
                    state.win = {
                        w: window.innerWidth,
                        h: window.innerHeight
                    }
                }
            }
        },
        player: {
            state: () => ({

            }),
            actions: {
                async getPlayer () {
                    console.log("getPlayer start")
                    let response = await fetch(
                        `/api/login/`, {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json;charset=utf-8",
                                //"Authorization": getters.rat
                            },
                            body: JSON.stringify({
                                "username": "",
                                "password": ""
                            })
                        }
                    )
                    let result = await response.json()
                    return result
                }
            }
        },
        drat: {
            state: () => ({
                s: null,
            }),
            mutations: {
                SET_DRAT (state, payload) {
                    if (payload) {
                        let data = state.s ? Buffer.from(state.s, "base64").toString("utf8") : null
                        data = payload
                        state.s = Buffer.from(data).toString("base64")
                    } else {
                        state.s = null
                    }
                }
            }
        },
        frat: {
            state: () => ({
                e: null
            }),
            mutations: {
                SET_FRAT (state, payload) {
                    if (payload) {
                        let data = state.e ? Buffer.from(state.e, "base64").toString("utf8") : null
                        data = payload
                        state.e = Buffer.from(data).toString("base64")
                    } else {
                        state.e = null
                    }
                }
            }
        }
    },
    plugins: [
        vuexLocal.plugin,
        vuexSession.plugin,
        vuexCookie.plugin,
        winResize
    ]
})

export default store;
