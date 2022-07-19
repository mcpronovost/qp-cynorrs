<template>
    <div class="qp-vue">

        <div v-if="!isLoading && !hasError && view">
            <div id="qp-auth">
                <template v-if="view == 'register'">
                    <qpCard h="auto">
                        <div id="qp-auth-banner"></div>
                        <el-row>
                            <el-col>
                                <el-form ref="formRegisterRef" :model="formRegister" :label-position="app.win.w < 1200 ? 'top' : 'right'" label-width="180px" status-icon>
                                    <el-form-item :label="$t('Username')" prop="username" :rules="[{required: true, message: $t('Thisfieldisrequired'), trigger: 'blur'}]">
                                        <el-input v-model="formRegister.username" type="text" maxlength="32" show-word-limit :placeholder="$t('YourPersonalUsername')" :prefix-icon="User" />
                                    </el-form-item>
                                    <el-form-item :label="$t('Email')" prop="email" :rules="[{required: true, message: $t('Thisfieldisrequired'), trigger: 'blur'}]">
                                        <el-input v-model="formRegister.email" type="email" maxlength="250" :placeholder="$t('YourEmailAddress')" :prefix-icon="Message" />
                                    </el-form-item>
                                    <el-form-item :label="$t('Password')" prop="password" :rules="[{required: true, message: $t('Thisfieldisrequired'), trigger: 'blur'}]">
                                        <el-input v-model="formRegister.password" type="password" maxlength="250" :prefix-icon="Lock" />
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
                                <el-button type="primary" @click="doRegister()">
                                    <span v-text="$t('Send')"></span>
                                </el-button>
                            </el-col>
                            <el-col>
                                <el-link @click="goToLogin()">
                                    <span v-text="$t('AlreadyHaveAnAccount')"></span>
                                </el-link>
                            </el-col>
                        </el-row>
                    </qpCard>
                </template>
                <template v-if="view == 'login'">
                    <qpCard h="auto">
                        <div id="qp-auth-banner"></div>
                        <el-row>
                            <el-col>
                                <el-form ref="formRegisterRef" :model="formRegister" :label-position="app.win.w < 1200 ? 'top' : 'right'" label-width="180px" status-icon>
                                    <el-form-item :label="$t('Username')" prop="username" :rules="[{required: true, message: $t('Thisfieldisrequired'), trigger: 'blur'}]">
                                        <el-input v-model="formRegister.username" type="text" maxlength="32" show-word-limit :placeholder="$t('YourPersonalUsername')" :prefix-icon="User" />
                                    </el-form-item>
                                    <el-form-item :label="$t('Password')" prop="password" :rules="[{required: true, message: $t('Thisfieldisrequired'), trigger: 'blur'}]">
                                        <el-input v-model="formRegister.password" type="password" maxlength="250" :prefix-icon="Lock" />
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
                                <el-button type="primary" @click="doRegister()">
                                    <span v-text="$t('Send')"></span>
                                </el-button>
                            </el-col>
                            <el-col>
                                <el-link @click="goToRegister()">
                                    <span v-text="$t('DontHaveAnAccount')"></span>
                                </el-link>
                            </el-col>
                        </el-row>
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
                    <el-result icon="error" :title="$t('Error')" :sub-title="hasError" />
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

const isLoading = ref(true)
const hasError = ref(null)
const hasErrorSend = ref(null)
const view = ref(null)

onMounted(() => {
    if (route.name == "AuthRegister") {
        goToRegister()
    } else if (route.name == "AuthLogin") {
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
}

const goToLogin = () => {
    view.value = "login"
}

const formRegisterRef = ref()
const formRegister = reactive({
    username: "",
    email: "",
    password: ""
})

const doRegister = async () => {
    hasErrorSend.value = null
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
        }
    })
}

const sendRegister = async () => {
    hasErrorSend.value = null
    const r = await store.dispatch("doRegister", formRegister)
    if (r.valid) {
        console.log(r)
    } else {
        for (let [key, val] of Object.entries(r.data)) {
            let k = t(`${key}`)
            let v = t(`${val}`)
            hasErrorSend.value = `${k} : ${v}`
        }
    }
}

const doLogout = async () => {
    await store.dispatch("doLogout")
    router.push({name: "Home"})
}

// =================================================================================== //

</script>

<style scoped>
#qp-auth-banner {
    background-color: #8f999e;
    height: 200px;
    margin: -20px -20px 20px;
}
</style>
