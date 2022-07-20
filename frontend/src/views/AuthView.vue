<template>
    <div class="qp-vue">

        <div v-if="!isLoading && !hasError && view">
            <div id="qp-auth">
                <template v-if="!rat && view == 'register'">
                    <qpCard h="auto" pa="0">
                        <el-scrollbar max-height="90vh">
                            <div id="qp-auth-banner"></div>
                            <div id="qp-auth-title">
                                <h2>
                                    <span v-text="$t('Register')"></span>
                                </h2>
                            </div>
                            <el-row>
                                <el-col>
                                    <el-form ref="formRegisterRef" :model="formRegister" :label-position="app.win.w < 1200 ? 'top' : 'right'" label-width="120px" status-icon>
                                        <el-form-item :label="$t('Username')" prop="username" :rules="[{required: true, message: $t('Thisfieldisrequired'), trigger: 'blur'}]">
                                            <el-input v-model="formRegister.username" type="text" maxlength="32" show-word-limit :placeholder="$t('YourPersonalUsername')" :prefix-icon="User" />
                                        </el-form-item>
                                        <el-form-item :label="$t('Playername')" prop="playername" :rules="[{required: true, message: $t('Thisfieldisrequired'), trigger: 'blur'}]">
                                            <el-input v-model="formRegister.playername" type="text" maxlength="32" show-word-limit :placeholder="$t('YourPublicPlayername')" :prefix-icon="User" />
                                        </el-form-item>
                                        <el-form-item :label="$t('Email')" prop="email" :rules="[{required: true, message: $t('Thisfieldisrequired'), trigger: 'blur'}]">
                                            <el-input v-model="formRegister.email" type="email" maxlength="250" :placeholder="$t('YourEmailAddress')" :prefix-icon="Message" />
                                        </el-form-item>
                                        <el-form-item :label="$t('Password')" prop="password" :rules="[{required: true, message: $t('Thisfieldisrequired'), trigger: 'blur'}]">
                                            <el-input v-model="formRegister.password" type="password" maxlength="250" :prefix-icon="Lock" @keyup.enter="doRegister()" />
                                        </el-form-item>
                                    </el-form>
                                </el-col>
                                <el-col v-if="hasErrorSend">
                                    <el-alert type="error" show-icon>
                                        <template #default>
                                            <div v-html="hasErrorSend"></div>
                                        </template>
                                    </el-alert>
                                </el-col>
                                <el-col>
                                    <el-button :loading="isLoadingSend">
                                        <span v-text="$t('Cancel')"></span>
                                    </el-button>
                                    <el-button type="primary" :loading="isLoadingSend" @click="doRegister()">
                                        <span v-text="$t('Send')"></span>
                                    </el-button>
                                </el-col>
                                <el-col>
                                    <el-link :disabled="isLoadingSend" @click="goToLogin()">
                                        <span v-text="$t('AlreadyHaveAnAccount')"></span>
                                    </el-link>
                                </el-col>
                            </el-row>
                        </el-scrollbar>
                    </qpCard>
                </template>
                <template v-if="!rat && view == 'login'">
                    <qpCard h="auto" pa="0">
                        <el-scrollbar max-height="90vh">
                            <div id="qp-auth-banner"></div>
                            <div id="qp-auth-title">
                                <h2>
                                    <span v-text="$t('Login')"></span>
                                </h2>
                            </div>
                            <el-row>
                                <el-col>
                                    <el-form ref="formLoginRef" :model="formLogin" :label-position="app.win.w < 1200 ? 'top' : 'right'" label-width="120px" status-icon>
                                        <el-form-item :label="$t('Username')" prop="username" :rules="[{required: true, message: $t('Thisfieldisrequired'), trigger: 'blur'}]">
                                            <el-input v-model="formLogin.username" type="text" maxlength="32" show-word-limit :placeholder="$t('YourPersonalUsername')" :prefix-icon="User" />
                                        </el-form-item>
                                        <el-form-item :label="$t('Password')" prop="password" :rules="[{required: true, message: $t('Thisfieldisrequired'), trigger: 'blur'}]">
                                            <el-input v-model="formLogin.password" type="password" maxlength="250" :prefix-icon="Lock" @keyup.enter="doLogin()" />
                                        </el-form-item>
                                    </el-form>
                                </el-col>
                                <el-col v-if="hasErrorSend">
                                    <el-alert type="error" show-icon>
                                        <template #default>
                                            <div v-html="hasErrorSend"></div>
                                        </template>
                                    </el-alert>
                                </el-col>
                                <el-col>
                                    <el-button>
                                        <span v-text="$t('Cancel')"></span>
                                    </el-button>
                                    <el-button type="primary" @click="doLogin()">
                                        <span v-text="$t('Send')"></span>
                                    </el-button>
                                </el-col>
                                <el-col>
                                    <el-link @click="goToRegister()">
                                        <span v-text="$t('DontHaveAnAccount')"></span>
                                    </el-link>
                                </el-col>
                            </el-row>
                        </el-scrollbar>
                    </qpCard>
                </template>
                <template v-if="view == 'logout'">
                    <qpCard h="auto">
                        <div v-loading="true" element-loading-background="transparent" style="width:200px;height:200px;"></div>
                        <div>
                            <span v-text="$t('Logout')"></span>
                        </div>
                    </qpCard>
                </template>
            </div>
        </div>

        <div v-else-if="isLoading">
            <div class="qp-container">
                <div v-loading="isLoading" element-loading-background="transparent" style="height:60vh"></div>
            </div>
        </div>

        <div v-else>
            <div id="qp-auth">
                <qpCard h="auto">
                    <el-result icon="error" :title="$t('Error')" :sub-title="hasError" style="padding-bottom:24px" />
                    <el-button @click="goToHome()" style="margin-bottom:40px">
                        <span v-text="$t('BackToHome')"></span>
                    </el-button>
                </qpCard>
            </div>
        </div>

    </div>
</template>

<script setup>

import { computed, onMounted, reactive, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import { Lock, Message, User } from "@element-plus/icons-vue";
import i18n from "@/plugins/i18n";

import qpCard from "@/components/basic/qpCard.vue";

// =================================================================================== //

const { t } = i18n.global

const route = useRoute()
const router = useRouter()
const store = useStore()

const app = computed(() => store.getters.app)
const rat = computed(() => store.getters.rat)

const isLoading = ref(true)
const isLoadingSend = ref(false)
const hasError = ref(null)
const hasErrorSend = ref(null)
const view = ref(null)

onMounted(() => {
    if (!rat.value && route.name == "AuthRegister") {
        goToRegister()
    } else if (!rat.value && route.name == "AuthLogin") {
        goToLogin()
    } else if (route.name == "AuthLogout") {
        view.value = "logout"
        doLogout()
    } else {
        hasError.value = t("AnErrorOccurred")
    }
    isLoading.value = false
})

const goToRegister = () => {
    view.value = "register"
    history.pushState(history.state, null, "/register")
}

const goToLogin = () => {
    view.value = "login"
    history.pushState(history.state, null, "/login");
}

const goToHome = () => {
    router.push({name: "Home"})
}

const formRegisterRef = ref()
const formRegister = reactive({
    username: "",
    playername: "",
    email: "",
    password: ""
})

const doRegister = async () => {
    hasErrorSend.value = null
    isLoadingSend.value = true
    await formRegisterRef.value.validate((valid, fields) => {
        if (valid) {
            sendRegister()
        } else {
            for (let [key, val] of Object.entries(fields)) {
                let k = t(`${key}`)
                for (let v of val) {
                    hasErrorSend.value = `${k} : ${v.message}`
                }
            }
            isLoadingSend.value = false
        }
    })
}

const sendRegister = async () => {
    hasErrorSend.value = null
    isLoadingSend.value = true
    const r = await store.dispatch("doRegister", formRegister)
    if (r.valid) {
        router.push({name: "Home"})
    } else {
        for (let [key, val] of Object.entries(r.data)) {
            let k = t(`${key}`)
            let v = t(`${val}`)
            hasErrorSend.value = `${k} : ${v}`
        }
        isLoadingSend.value = false
    }
}

const formLoginRef = ref()
const formLogin = reactive({
    username: "",
    password: ""
})

const doLogin = async () => {
    hasErrorSend.value = null
    isLoadingSend.value = true
    await formLoginRef.value.validate((valid, fields) => {
        if (valid) {
            sendLogin()
        } else {
            for (let [key, val] of Object.entries(fields)) {
                let k = t(`${key}`)
                for (let v of val) {
                    hasErrorSend.value = `${k} : ${v.message}`
                }
            }
            isLoadingSend.value = false
        }
    })
}

const sendLogin = async () => {
    hasErrorSend.value = null
    isLoadingSend.value = true
    const r = await store.dispatch("doLogin", formLogin)
    if (r.valid) {
        router.push({name: "Home"})
    } else {
        for (let [key, val] of Object.entries(r.data)) {
            let k = t(`${key}`)
            let v = t(`${val}`)
            hasErrorSend.value = `${k} : ${v}`
        }
        isLoadingSend.value = false
    }
}

const doLogout = async () => {
    await store.dispatch("doLogout")
    router.push({name: "Home"})
}

// =================================================================================== //

</script>

<style scoped>
#qp-auth {
    background-color: var(--qp-primary);
    box-sizing: border-box;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100vw;
    height: 100vh;
    padding: 20px;
    margin: 0 auto;
}
#qp-auth .qp-card {
    max-width: 500px;
}
#qp-auth-banner {
    background-color: #8f999e;
    height: 200px;
    margin: 0 0 20px;
}
#qp-auth-title h2 {
    font-family: "Quicksand", sans-serif;
    font-size: 32px;
    font-weight: 400;
    line-height: 120%;
    padding: 12px;
    margin: 0 0 12px;
}
</style>
