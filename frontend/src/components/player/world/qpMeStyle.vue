<template>
    <div v-if="props.world">

        <div v-if="!isLoading && style">
            <el-row v-if="props.tab == 'style'">
                <el-col :span="24">
                    <qpCard class="qp-meworld-form-style">
                        <template #header>
                            <span v-text="$t('Style')"></span>
                        </template>
                        <el-form ref="formForumStyleRef" :model="formForumStyle" :label-position="app.win.w < 1200 ? 'top' : 'right'" :rules="formForumStyleRules" label-width="120px" status-icon :style="app.win.w < 1200 ? 'margin-top:12px;' : 'padding-right:60px;margin-top:12px;'">
                            <el-form-item :label="$t('Name')" prop="name">
                                <el-input v-model="formForumStyle.name" :placeholder="$t('NameOfTheWorld')" :maxlength="32" show-word-limit />
                            </el-form-item>
                        </el-form>
                        <el-row>
                            <el-col>
                                <el-button :disabled="isLoadingSend" class="ma-6" @click="resetformForumStyle()">
                                    <span v-text="$t('Reset')"></span>
                                </el-button>
                                <el-button :loading="isLoadingSend" class="ma-6" type="primary" @click="doformForumStyle()">
                                    <span v-text="$t('Send')"></span>
                                </el-button>
                            </el-col>
                        </el-row>
                    </qpCard>
                </el-col>
            </el-row>
        </div>

        <div v-else-if="isLoading">
            <div class="qp-container">
                <div v-loading="isLoading" element-loading-background="transparent" style="height: 60vh"></div>
            </div>
        </div>

        <div v-else>
            <div class="qp-container">
                <qpCard h="auto">
                    <el-result icon="error" :title="$t('Error')" :sub-title="$t('AnErrorOccurred')" />
                </qpCard>
            </div>
        </div>

    </div>
</template>

<script setup>
import { computed, onMounted, reactive, ref } from "vue";
import { useRoute } from "vue-router";
import { useStore } from "vuex";
import { ElMessage } from "element-plus";
import { API } from "@/main.js";
import i18n from "@/plugins/i18n";

import qpCard from "@/components/basic/qpCard.vue";

const { t } = i18n.global

const route = useRoute();
const store = useStore();
const app = computed(() => store.getters.app)
const rat = computed(() => store.getters.rat)

const emit = defineEmits(["init-world"])

const props = defineProps({
    tab: {
        type: String,
        default: "style"
    },
    world: {
        type: Object,
        default: () => {}
    }
})

onMounted(() => {
    initStyle()
})

const isLoading = ref(false)
const forum = ref(null)

const initStyle = async () => {
    isLoading.value = true
    // ===---
    try {
        let response = await fetch(`${API}/me/forums/${props.world.forum.id}/`, {
            method: "GET",
            headers: {"Authorization": rat.value}
        })
        let r = await response.json()
        if (response.status === 200) {
            forum.value = r
        } else {
            throw response
        }
    } catch (e) {
        if (e.status === 403) {
            ElMessage.error(t("YouDoesntHaveAccessToThisPage"))
        } else {
            ElMessage.error(t("AnErrorOccurred"))
        }
    }
    // ===---
    isLoading.value = false
}

const isLoadingSend = ref(false)

const formForumStyleRef = ref()
const formForumStyle = reactive({
    name: "",
    slug: "",
    description: "",
    visibility: 0,
    is_active: false
})
const formForumStyleRules = reactive({})

const initformForumStyle = (r) => {
    formForumStyle.name = r.name
    formForumStyle.slug = r.slug
    formForumStyle.description = r.description
    formForumStyle.visibility = r.visibility
    formForumStyle.is_active = r.is_active
}

const resetformForumStyle = () => {
    initformForumStyle(props.world)
}

const doformForumStyle = async () => {
    isLoadingSend.value = true
    await formForumStyleRef.value.validate((valid, fields) => {
        if (valid) {
            sendformForumStyle()
        } else {
            for (let [key, val] of Object.entries(fields)) {
                let k = t(`error${key}`)
                for (let v of val) {
                    ElMessage.error(`${k} : ${v.message}`)
                }
            }
            isLoadingSend.value = false
        }
    })
}

const sendformForumStyle = async () => {
    isLoadingSend.value = true
    // ===---
    try {
        let data = new FormData()
        data.append("name", formForumStyle.name)
        // data.append("slug", formForumStyle.slug)
        data.append("description", formForumStyle.description ? formForumStyle.description : "")
        data.append("visibility", formForumStyle.visibility)
        data.append("is_active", formForumStyle.is_active)
        let response = await fetch(`${API}/me/worlds/${route.params.pk}/`, {
            method: "PATCH",
            headers: {"Authorization": rat.value},
            body: data
        })
        let r = await response.json()
        if (response.status === 200) {
            ElMessage.success(t("WorldUpdatedSuccessfully"))
            emit("init-world", r)
            // initformForumStyle(r)
        } else {
            for (let [key, val] of Object.entries(r)) {
                let k = t(`error${key}`)
                for (let v of val) {
                    ElMessage.error(`${k} : ${v}`)
                }
            }
        }
    } catch {
        ElMessage.error(t("AnErrorOccurred"))
    }
    isLoadingSend.value = false
}
</script>