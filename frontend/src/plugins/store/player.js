import { API } from "@/main.js";
import { Buffer } from "buffer";

export const getterPlayer = (state) => {
    if (state.player.j) {
        return JSON.parse(
            Buffer.from(state.player.j, "base64").toString("utf8")
        )
    }
    return null
}

export const getterHeros = (state) => {
    if (state.player.h) {
        return JSON.parse(
            Buffer.from(state.player.h, "base64").toString("utf8")
        )
    }
    return []
}

export const getterWorlds = (state) => {
    if (state.player.w) {
        return JSON.parse(
            Buffer.from(state.player.w, "base64").toString("utf8")
        )
    }
    return []
}

export const modulePlayer = {
    state: () => ({
        j: null,
        h: null,
        c: null,
        w: null
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
        },
        BATCH_HEROS (state, payload) {
            if (payload) {
                state.h = Buffer.from(JSON.stringify(payload)).toString("base64")
            } else {
                state.h = null
            }
        },
        BATCH_WORLDS (state, payload) {
            if (payload) {
                state.w = Buffer.from(JSON.stringify(payload)).toString("base64")
            } else {
                state.w = null
            }
        }
    },
    actions: {
        async getPlayer ({ commit, dispatch, getters }) {
            if (getters.rat) {
                let r = await fetch(`${API}/me/`, {
                    method: "GET",
                    headers: {"Authorization": getters.rat}
                })
                if (r.status === 200) {
                    let result = await r.json()
                    commit("BATCH_PLAYER", result.player)
                    commit("BATCH_HEROS", result.heros)
                    commit("BATCH_WORLDS", result.worlds)
                } else if (r.status === 401) {
                    dispatch("doLogout")
                }
            }
        },
        async getHeros ({ commit, dispatch, getters }) {
            if (getters.rat) {
                let r = await fetch(`${API}/me/heros/`, {
                    method: "GET",
                    headers: {"Authorization": getters.rat}
                })
                if (r.status === 200) {
                    let result = await r.json()
                    commit("BATCH_HEROS", result.heros)
                } else if (r.status === 401) {
                    dispatch("doLogout")
                }
            }
        },
        async doRegister ({ dispatch }, { username, email, password}) {
            let data = new FormData()
            if (username) {
                data.append("username", username)
            }
            if (email) {
                data.append("email", email)
            }
            if (password) {
                data.append("password", password)
            }
            let response = await fetch(`${API}/register/`, {
                method: "POST",
                body: data
            })
            let result = await response.json()
            if (response.status === 200) {
                dispatch("doLogin", {username, password})
            } else {
                return {
                    "valid": false,
                    "data": result
                }
            }
        },
        async doLogin ({ commit }, { username, password}) {
            let data = new FormData()
            data.append("username", username)
            data.append("password", password)
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
                return true
            } else {
                return false
            }
        },
        async doLogout ({ commit, getters }) {
            let response = await fetch(`${API}/logout/`, {
                method: "POST",
                headers: {"Authorization": getters.rat}
            })
            commit("BATCH_PLAYER", null)
            commit("BATCH_HEROS", null)
            commit("BATCH_WORLDS", null)
            commit("SET_DRAT", null)
            commit("SET_FRAT", null)
            return response
        }
    }
}