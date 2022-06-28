import { API } from "@/main.js";
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
        app: (state) => {
            return {
                win: state.app.win
            }
        },
        player: (state) => {
            if (state.player.j) {
                return JSON.parse(
                    Buffer.from(state.player.j, "base64").toString("utf8")
                )
            }
            return null
        },
        rat: (state) => {
            if (state.drat.s && state.frat.e) {
                let s = Buffer.from(state.drat.s, "base64").toString("utf8")
                let e = Buffer.from(state.frat.e, "base64").toString("utf8")
                return `Token ${s}${e}`
            }
            return null
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
                j: null
            }),
            mutations: {
                SET_PLAYER (state, payload) {
                    if (payload) {
                        let data = Buffer.from(state.j, "base64").toString("utf8")
                        if (data) {
                            data = JSON.parse(data)
                        } else {
                            data = {}
                        }
                        // ===---
                        data[payload[0]] = payload[1]
                        // ===---
                        state.j = Buffer.from(JSON.stringify(data)).toString("base64")
                    }
                },
                BATCH_PLAYER (state, payload) {
                    if (payload) {
                        let data = state.j
                        if (data) {
                            data = JSON.parse(Buffer.from(data, "base64").toString("utf8"))
                        } else {
                            data = {}
                        }
                        // ===---
                        let items = Object.entries(payload)
                        for (let i = 0; i < items.length; i++) {
                            data[items[i][0]] = items[i][1]
                        }
                        // ===---
                        state.j = Buffer.from(JSON.stringify(data)).toString("base64")
                    } else {
                        state.j = null
                    }
                }
            },
            actions: {
                async getPlayer ({ commit, dispatch, getters }) {
                    if (getters.rat) {
                        let r = await fetch(`${API}/`, {
                            method: "GET",
                            headers: {"Authorization": getters.rat}
                        })
                        if (r.status === 200) {
                            let result = await r.json()
                            commit("BATCH_PLAYER", result.player)
                        } else if (r.status === 401) {
                            dispatch("doLogout")
                        }
                    }
                },
                async doLogin ({ commit }) {
                    let data = new FormData()
                    data.append("username", "")
                    data.append("password", "")
                    let response = await fetch(`${API}/login/`, {
                        method: "POST",
                        body: data
                    })
                    if (response.status === 200) {
                        let result = await response.json()
                        let token = result.token
                        let half = Math.ceil(token.length / 2)
                        commit("SET_DRAT", token.slice(0, half))
                        commit("SET_FRAT", token.slice(half))
                    }
                },
                async doLogout ({ commit, getters }) {
                    await fetch(`${API}/logout/`, {
                        method: "POST",
                        headers: {"Authorization": getters.rat}
                    })
                    commit("BATCH_PLAYER", null)
                    commit("SET_DRAT", null)
                    commit("SET_FRAT", null)
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
                        state.s = Buffer.from(payload).toString("base64")
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
                        state.e = Buffer.from(payload).toString("base64")
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
