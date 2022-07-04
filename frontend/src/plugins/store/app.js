export const getterApp = (state) => {
    return {
        win: state.app.win
    }
}

export const moduleApp = {
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
}
