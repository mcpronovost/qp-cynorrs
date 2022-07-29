<template>
    <div v-if="props.world">

        <div v-if="!isLoading && forum">
            <el-row v-if="props.tab == 'forum'">
                <el-col :span="24">
                    <qpCard class="qp-meworld-form-forum">
                        <template #header>
                            <span v-text="$t('Forum')"></span>
                        </template>
                        <el-form ref="formForumGeneralRef" :model="formForumGeneral" :label-position="app.win.w < 1200 ? 'top' : 'right'" :rules="formForumGeneralRules" label-width="120px" status-icon :style="app.win.w < 1200 ? 'margin-top:12px;' : 'padding-right:60px;margin-top:12px;'">
                            <el-form-item :label="$t('Name')" prop="name">
                                <el-input v-model="formForumGeneral.name" :placeholder="$t('NameOfTheWorld')" :maxlength="32" show-word-limit />
                            </el-form-item>
                            <el-form-item :label="$t('Visibility')" prop="visibility">
                                <el-select v-model="formForumGeneral.visibility" :placeholder="$t('Visibility')">
                                    <el-option v-for="(visibility, n) in world.visibility_choix" :key="`visibility-${n}`" :label="visibility[1]" :value="visibility[0]" />
                                </el-select>
                            </el-form-item>
                            <el-form-item :label="$t('Open')" prop="is_active">
                                <el-checkbox v-model="formForumGeneral.is_active" />
                            </el-form-item>
                        </el-form>
                        <el-row>
                            <el-col>
                                <el-button :disabled="isLoadingSend" class="ma-6" @click="resetformForumGeneral()">
                                    <span v-text="$t('Reset')"></span>
                                </el-button>
                                <el-button :loading="isLoadingSend" class="ma-6" type="primary" @click="doformForumGeneral()">
                                    <span v-text="$t('Send')"></span>
                                </el-button>
                            </el-col>
                        </el-row>
                    </qpCard>
                </el-col>
            </el-row>
            <qpPlayerMeForumIndex v-if="props.tab == 'forum-index'" :world="props.world" :forum="forum" />
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
import { useStore } from "vuex";
import { ElMessage } from "element-plus";
import { API } from "@/main.js";
import i18n from "@/plugins/i18n";

import qpCard from "@/components/basic/qpCard.vue";
import qpPlayerMeForumIndex from "@/components/player/world/qpMeForumIndex.vue";

const { t } = i18n.global

const store = useStore();
const app = computed(() => store.getters.app)
const rat = computed(() => store.getters.rat)

const props = defineProps({
    tab: {
        type: String,
        default: "general"
    },
    world: {
        type: Object,
        default: () => {}
    }
})

onMounted(() => {
    initForum()
})

const isLoading = ref(false)
const forum = ref(null)

const initForum = async () => {
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
            initformForumGeneral(r)
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

const formForumGeneralRef = ref()
const formForumGeneral = reactive({
    name: "",
    slug: "",
    description: "",
    visibility: 0,
    is_active: false
})
const formForumGeneralRules = reactive({})

const initformForumGeneral = (r) => {
    formForumGeneral.name = r.name
    formForumGeneral.visibility = r.visibility
    formForumGeneral.is_active = r.is_active
}

const resetformForumGeneral = () => {
    initformForumGeneral(forum)
}

const doformForumGeneral = async () => {
    isLoadingSend.value = true
    await formForumGeneralRef.value.validate((valid, fields) => {
        if (valid) {
            sendformForumGeneral()
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

const sendformForumGeneral = async () => {
    isLoadingSend.value = true
    // ===---
    try {
        let data = new FormData()
        data.append("name", formForumGeneral.name)
        data.append("visibility", formForumGeneral.visibility)
        data.append("is_active", formForumGeneral.is_active)
        let response = await fetch(`${API}/me/forums/${forum.value.id}/`, {
            method: "PATCH",
            headers: {"Authorization": rat.value},
            body: data
        })
        let r = await response.json()
        if (response.status === 200) {
            ElMessage.success(t("WorldUpdatedSuccessfully"))
            initForum()
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