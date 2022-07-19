<template>
    <div class="qp-vue">

        <div v-if="!isLoading && !hasError && view">
            <div id="qp-auth">
                <template v-if="view == 'register'">
                    <qpCard h="auto">
                        <el-row>
                            <el-col>
                                <el-form>
                                    forum
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
                        </el-row>
                    </qpCard>
                </template>
                <template v-if="view == 'login'">
                    <qpCard h="auto">
                        <el-row>
                            <el-col>
                                <el-form>
                                    aaa
                                </el-form>
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

import { onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import i18n from "@/plugins/i18n";

import qpCard from "@/components/basic/qpCard.vue";

// =================================================================================== //

const { t } = i18n.global

const route = useRoute()
const router = useRouter()
const store = useStore()

const isLoading = ref(true)
const hasError = ref(null)
const hasErrorSend = ref(null)
const view = ref(null)

onMounted(() => {
    if (route.name == "AuthRegister") {
        view.value = "register"
    } else if (route.name == "AuthLogin") {
        view.value = "login"
    } else if (route.name == "AuthLogout") {
        view.value = "logout"
        doLogout()
    } else {
        hasError.value = t("AnErrorOccurred")
    }
    isLoading.value = false
})

const doRegister = async () => {
    hasErrorSend.value = null
    let r = await store.dispatch("doRegister")
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
