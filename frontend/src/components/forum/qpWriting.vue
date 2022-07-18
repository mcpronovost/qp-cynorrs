<template>
    <section class="qp-forum-writing-newchapter">
        <header class="qp-forum-header">
            <h3 class="qp-forum-header-title">
                <span v-text="$t('Writing')"></span>
            </h3>
            <p v-if="props.type == 'chapter'" class="qp-forum-header-description" v-text="$t('NewChapter')"></p>
            <hr class="qp-forum-header-divider" />
        </header>
        <section class="qp-forum-writing-newchapter-form">
            <qpCard>
                <el-row>
                    <el-col :style="app.win.w < 1200 ? '' : 'padding-right:180px'">
                        <el-form ref="formnewchapter" :model="formNewChapter" :label-position="app.win.w < 1200 ? 'top' : 'right'" label-width="180px" status-icon>
                            <el-form-item :label="$t('Title')" prop="title" :rules="[{required: true, message: $t('Thisfieldisrequired'), trigger: 'blur'}]">
                                <el-input v-model="formNewChapter.title" maxlength="90" show-word-limit :placeholder="$t('Titleofthenewchapter')" />
                            </el-form-item>
                            <el-form-item :label="$t('Description')" prop="description">
                                <el-input v-model="formNewChapter.description" maxlength="200" show-word-limit :placeholder="$t('Descriptionofthenewchapter')" />
                            </el-form-item>
                            <el-form-item :label="$t('Text')" prop="text" :rules="[{required: true, message: $t('Thisfieldisrequired'), trigger: 'blur'}]">
                                <el-input v-model="formNewChapter.text" type="textarea" :rows="10" :placeholder="$t('YourMessage')" />
                            </el-form-item>
                        </el-form>
                    </el-col>
                    <el-col>
                        <el-button @click="closeWriting()">
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

import { computed, reactive } from "vue";
import { useStore } from "vuex";

import qpCard from "@/components/basic/qpCard.vue";

// =================================================================================== //

const store = useStore()
const app = computed(() => store.getters.app)

// =================================================================================== //
// ===--- EMIT

const emit = defineEmits(["close"])

// =================================================================================== //
// ===--- PROPS

const props = defineProps({
    type: {
        type: String,
        default: "chapter"
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

// =================================================================================== //
// ===--- DATA

const formNewChapter = reactive({
    title: "",
    description: "",
    text: ""
})

// =================================================================================== //
// ===--- METHODS

const closeWriting = () => {
    emit("close")
}

// =================================================================================== //

</script>

<style scoped>
.qp-forum-writing-newchapter-form {
    padding: 12px;
}
</style>
