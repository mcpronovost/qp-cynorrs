export const getterApp = (state) => {
    return {
        win: state.app.win,
        sidebar: state.app.sidebar
    }
}

export const moduleApp = {
    state: () => ({
        win: {w: 1880, h: 980},
        sidebar: {
            collapse: false
        }
    }),
    mutations: {
        SET_WINSIZES (state) {
            state.win = {
                w: window.innerWidth,
                h: window.innerHeight
            }
        },
        TOGGLE_SIDEBAR (state) {
            state.sidebar.collapse = !state.sidebar.collapse
        }
    }
}
