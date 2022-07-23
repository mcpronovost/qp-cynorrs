<template>
    <section class="qp-forum-writing-newchapter">
        <qpForumHeader :title="$t('Writing')" :description="$t('ToReply')" />
        <section class="qp-forum-writing-newchapter-form">
            <qpCard>
                <el-row>
                    <el-col :style="app.win.w < 1200 ? '' : 'padding-right:180px'">
                        <el-form ref="formnewchapter" :model="formNewReply" :label-position="app.win.w < 1200 ? 'top' : 'right'" :rules="formNewReplyRules" label-width="180px" status-icon>
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
                    <el-col>
                        <el-button @click="$emit('close')">
                            <span v-text="$t('Cancel')"></span>
                        </el-button>
                        <el-button type="primary">
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
import { useStore } from "vuex";
import i18n from "@/plugins/i18n";

import qpCard from "@/components/basic/qpCard.vue";
import qpForumHeader from "@/components/forum/core/qpHeader.vue";

const { t } = i18n.global

const store = useStore()
const app = computed(() => store.getters.app)
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

</script>

<style scoped>
.qp-forum-writing-newchapter-form {
    padding: 12px;
}
</style>
