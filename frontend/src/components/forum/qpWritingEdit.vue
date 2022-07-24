<template>
    <section class="qp-forum-writing-editmessage">
        <section class="qp-forum-writing-editmessage-form">
            <el-row>
                <el-col :style="app.win.w < 1200 ? '' : 'padding-right:180px'">
                    <el-form ref="formEditMessageRef" :model="formEditMessage" :label-position="app.win.w < 1200 ? 'top' : 'right'" :rules="formEditMessageRules" label-width="180px" status-icon>
                        <el-form-item :label="$t('Text')" prop="text">
                            <el-input v-model="formEditMessage.text" type="textarea" :rows="12" :placeholder="$t('YourMessage')" />
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
                    <el-button :disabled="isLoadingSend" @click="$emit('close')">
                        <span v-text="$t('Cancel')"></span>
                    </el-button>
                    <el-button :loading="isLoadingSend" type="primary" @click="doEditMessage()">
                        <span v-text="$t('Send')"></span>
                    </el-button>
                </el-col>
            </el-row>
        </section>
    </section>
</template>

<script setup>

import { computed, onMounted, reactive, ref } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import { API } from "@/main.js";
import i18n from "@/plugins/i18n";

const { t } = i18n.global

const router = useRouter()
const store = useStore()
const app = computed(() => store.getters.app)
const rat = computed(() => store.getters.rat)

const props = defineProps({
    message: {
        type: Object,
        default: () => {}
    }
})

onMounted(() => {
    initText()
})

const initText = () => {
    formEditMessage.text = props.message.text
}

const hasErrorSend = ref(null)
const isLoadingSend = ref(false)
const formEditMessageRef = ref()

const formEditMessage = reactive({
    text: ""
})

const formEditMessageRules = reactive({
    text: [
        {
            required: true,
            message: t("Thisfieldisrequired"),
            trigger: "blur"
        }
    ]
})


const doEditMessage = async () => {
    hasErrorSend.value = null
    isLoadingSend.value = true
    await formEditMessageRef.value.validate((valid, fields) => {
        if (valid) {
            sendEditMessage()
        } else {
            for (let [key, val] of Object.entries(fields)) {
                let k = t(`error${key}`)
                for (let v of val) {
                    hasErrorSend.value = `${k} : ${v.message}`
                }
            }
            isLoadingSend.value = false
        }
    })
}

const sendEditMessage = async () => {
    hasErrorSend.value = null
    isLoadingSend.value = true
    // ===---
    try {
        let data = new FormData()
        data.append("text", formEditMessage.text)
        let response = await fetch(`${API}/worlds/messages/${props.message.id}/edit/`, {
            method: "PATCH",
            headers: {"Authorization": rat.value},
            body: data
        })
        let r = await response.json()
        if (response.status === 200) {
            router.go(r.route)
        } else {
            for (let [key, val] of Object.entries(r)) {
                let k = t(`error${key}`)
                for (let v of val) {
                    hasErrorSend.value = `${k} : ${v}`
                }
            }
            isLoadingSend.value = false
        }
    } catch {
        hasErrorSend.value = t("AnErrorOccurred")
        isLoadingSend.value = false
    }
}

</script>

<style scoped>
.qp-forum-writing-editmessage-form {
    padding: 12px;
}
</style>
