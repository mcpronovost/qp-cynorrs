import { Buffer } from "buffer";

export const getterRat = (state) => {
    if (state.drat.s && state.frat.e) {
        let s = Buffer.from(state.drat.s, "base64").toString("utf8")
        let e = Buffer.from(state.frat.e, "base64").toString("utf8")
        return `Token ${s}${e}`
    }
    return null
}

export const moduleDrat = {
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
}

export const moduleFrat = {
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

