<template>
    <section class="qp-forum-writing-newchapter">
        <qpForumHeader :title="$t('Writing')" :description="$t('ToReply')" />
        <section class="qp-forum-writing-newchapter-form">
            <qpCard>
                <el-row>
                    <el-col :style="app.win.w < 1200 ? '' : 'padding-right:180px'">
                        <el-form ref="formNewReplyRef" :model="formNewReply" :label-position="app.win.w < 1200 ? 'top' : 'right'" :rules="formNewReplyRules" label-width="180px" status-icon>
                            <el-form-item :label="$t('Character')" prop="character">
                                <el-select v-model="formNewReply.character" :placeholder="$t('ChooseACharacter')">
                                    <el-option v-for="(character, n) in listCharacters" :key="`character-${n}`" :label="character.name" :value="character.id" />
                                </el-select>
                            </el-form-item>
                            <el-form-item :label="$t('Text')" prop="text">
                                <el-input v-model="formNewReply.text" type="textarea" :rows="12" :placeholder="$t('YourReply')" />
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
                        <el-button :loading="isLoadingSend" type="primary" @click="doNewReply()">
                            <span v-text="$t('Send')"></span>
                        </el-button>
                    </el-col>
                </el-row>
            </qpCard>
        </section>
    </section>
</template>

<script setup>

import { computed, onMounted, reactive, ref } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import { API } from "@/main.js";
import i18n from "@/plugins/i18n";

import qpCard from "@/components/basic/qpCard.vue";
import qpForumHeader from "@/components/forum/core/qpHeader.vue";

const { t } = i18n.global

const router = useRouter()
const store = useStore()
const app = computed(() => store.getters.app)
const rat = computed(() => store.getters.rat)
const heros = computed(() => store.getters.heros)

const props = defineProps({
    world: {
        type: Object,
        default: () => {}
    },
    chapter: {
        type: Object,
        default: () => {}
    }
})

onMounted(() => {
    initCharacters()
})

const listCharacters = ref([])

const initCharacters = () => {
    listCharacters.value = []
    for (const h of heros.value) {
        if (h.world.id == props.world.id) {
            // vérifier si le personnage est localisé ici
            listCharacters.value.push(h)
        }
    }
}

const hasErrorSend = ref(null)
const isLoadingSend = ref(false)
const formNewReplyRef = ref()

const formNewReply = reactive({
    character: null,
    text: ""
})

const formNewReplyRules = reactive({
    character: [
        {
            required: true,
            message: t("Thisfieldisrequired"),
            trigger: "change"
        }
    ],
    text: [
        {
            required: true,
            message: t("Thisfieldisrequired"),
            trigger: "blur"
        }
    ]
})


const doNewReply = async () => {
    hasErrorSend.value = null
    isLoadingSend.value = true
    await formNewReplyRef.value.validate((valid, fields) => {
        if (valid) {
            sendNewReply()
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

const sendNewReply = async () => {
    hasErrorSend.value = null
    isLoadingSend.value = true
    // ===---
    try {
        let data = new FormData()
        data.append("chapter", props.chapter.id)
        data.append("author", formNewReply.character)
        data.append("text", formNewReply.text)
        let response = await fetch(`${API}/worlds/chapters/${props.chapter.id}/messages/create/`, {
            method: "POST",
            headers: {"Authorization": rat.value},
            body: data
        })
        let r = await response.json()
        if (response.status === 201) {
            router.push(r.route)
        } else {
            for (let [key, val] of Object.entries(r)) {
                let k = t(`error${key}`)
                for (let v of val) {
                    hasErrorSend.value = `${k} : ${v}`
                }
            }
        }
    } catch {
        hasErrorSend.value = t("AnErrorOccurred")
    }
    isLoadingSend.value = false
}

</script>

<style scoped>
.qp-forum-writing-newchapter-form {
    padding: 12px;
}
</style>
