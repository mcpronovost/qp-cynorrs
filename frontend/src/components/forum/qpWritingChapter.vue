<template>
    <section class="qp-forum-writing-newchapter">
        <qpForumHeader :title="$t('Writing')" :description="$t('NewChapter')" />
        <section class="qp-forum-writing-newchapter-form">
            <qpCard>
                <el-row>
                    <el-col :style="app.win.w < 1200 ? '' : 'padding-right:180px'">
                        <el-form ref="formNewChapterRef" :model="formNewChapter" :label-position="app.win.w < 1200 ? 'top' : 'right'" :rules="formNewChapterRules" label-width="180px" status-icon>
                            <el-form-item :label="$t('Title')" prop="title">
                                <el-input v-model="formNewChapter.title" type="text" :placeholder="$t('NewChapterTitle')" />
                            </el-form-item>
                            <el-form-item :label="$t('Character')" prop="character">
                                <el-select v-model="formNewChapter.character" :placeholder="$t('ChooseACharacter')">
                                    <el-option v-for="(character, n) in listCharacters" :key="`character-${n}`" :label="character.name" :value="character.id" />
                                </el-select>
                            </el-form-item>
                            <el-form-item :label="$t('Text')" prop="text">
                                <el-input v-model="formNewChapter.text" type="textarea" :rows="12" :placeholder="$t('YourMessage')" />
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
                        <el-button :loading="isLoadingSend" type="primary" @click="doNewChapter()">
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
    territory: {
        type: Object,
        default: () => {}
    },
    sector: {
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
        if (h.world == props.world.id) {
            // vérifier si le personnage est localisé ici
            listCharacters.value.push(h)
        }
    }
}

const hasErrorSend = ref(null)
const isLoadingSend = ref(false)
const formNewChapterRef = ref()

const formNewChapter = reactive({
    title: "",
    character: null,
    text: ""
})

const formNewChapterRules = reactive({
    title: [
        {
            required: true,
            message: t("Thisfieldisrequired"),
            trigger: "blur"
        }
    ],
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


const doNewChapter = async () => {
    hasErrorSend.value = null
    isLoadingSend.value = true
    await formNewChapterRef.value.validate((valid, fields) => {
        if (valid) {
            sendNewChapter()
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

const sendNewChapter = async () => {
    hasErrorSend.value = null
    isLoadingSend.value = true
    // ===---
    try {
        let data = new FormData()
        data.append("title", formNewChapter.title)
        data.append("author", formNewChapter.character)
        data.append("territory", props.territory.id)
        if (props.sector) {
            data.append("sector", props.sector.id)
        }
        let response = await fetch(`${API}/worlds/territories/${props.territory.id}/chapters/create/`, {
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
    } catch (e) {
        console.log(e)
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
