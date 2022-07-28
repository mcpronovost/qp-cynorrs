<template>
    <el-row v-if="props.world">
        <el-col :span="24">
            <qpCard class="qp-meworld-form-forum">
                <template #header>
                    <span v-text="$t('Forum')"></span>
                </template>
                <el-form ref="formWorldRef" :model="formWorld" :label-position="app.win.w < 1200 ? 'top' : 'right'" :rules="formWorldRules" label-width="120px" status-icon :style="app.win.w < 1200 ? 'margin-top:12px;' : 'padding-right:60px;margin-top:12px;'">
                    <el-form-item :label="$t('Name')" prop="name">
                        <el-input v-model="formWorld.name" :placeholder="$t('NameOfTheWorld')" :maxlength="32" show-word-limit />
                    </el-form-item>
                    <el-form-item :label="$t('Slug')" prop="slug">
                        <el-input v-model="formWorld.slug" :placeholder="$t('Slug')" disabled />
                    </el-form-item>
                    <el-form-item :label="$t('Description')" prop="description">
                        <el-input v-model="formWorld.description" :placeholder="$t('AShortDescription')" :maxlength="250" show-word-limit />
                    </el-form-item>
                    <el-form-item :label="$t('Visibility')" prop="visibility">
                        <el-select v-model="formWorld.visibility" :placeholder="$t('Visibility')">
                            <el-option v-for="(visibility, n) in world.visibility_choix" :key="`visibility-${n}`" :label="visibility[1]" :value="visibility[0]" />
                        </el-select>
                    </el-form-item>
                    <el-form-item :label="$t('Open')" prop="is_active">
                        <el-checkbox v-model="formWorld.is_active" />
                    </el-form-item>
                </el-form>
                <el-row>
                    <el-col>
                        <el-button :disabled="isLoadingSend" class="ma-6" @click="resetFormWorld()">
                            <span v-text="$t('Reset')"></span>
                        </el-button>
                        <el-button :loading="isLoadingSend" class="ma-6" type="primary" @click="doFormWorld()">
                            <span v-text="$t('Send')"></span>
                        </el-button>
                    </el-col>
                </el-row>
            </qpCard>
        </el-col>
    </el-row>
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
    world: {
        type: Object,
        default: () => {}
    }
})

onMounted(() => {
    initFormWorld(props.world)
})

const isLoadingSend = ref(false)

const formWorldRef = ref()
const formWorld = reactive({
    name: "",
    slug: "",
    description: "",
    visibility: 0,
    is_active: false
})
const formWorldRules = reactive({})

const initFormWorld = (r) => {
    formWorld.name = r.name
    formWorld.slug = r.slug
    formWorld.description = r.description
    formWorld.visibility = r.visibility
    formWorld.is_active = r.is_active
}

const resetFormWorld = () => {
    initFormWorld(props.world)
}

const doFormWorld = async () => {
    isLoadingSend.value = true
    await formWorldRef.value.validate((valid, fields) => {
        if (valid) {
            sendFormWorld()
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

const sendFormWorld = async () => {
    isLoadingSend.value = true
    // ===---
    try {
        let data = new FormData()
        data.append("name", formWorld.name)
        // data.append("slug", formWorld.slug)
        data.append("description", formWorld.description ? formWorld.description : "")
        data.append("visibility", formWorld.visibility)
        data.append("is_active", formWorld.is_active)
        let response = await fetch(`${API}/me/worlds/${route.params.pk}/`, {
            method: "PATCH",
            headers: {"Authorization": rat.value},
            body: data
        })
        let r = await response.json()
        if (response.status === 200) {
            ElMessage.success(t("WorldUpdatedSuccessfully"))
            emit("init-world", r)
            // initFormWorld(r)
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