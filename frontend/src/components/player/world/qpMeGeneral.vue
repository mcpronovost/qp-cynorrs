<template>
    <el-row v-if="props.world">
        <el-col :span="24" :sm="17">
            <qpCard pa="0">
                <div class="qp-meworld-banner">
                    <div class="qp-meworld-banner-inner">
                        <el-image v-if="formWorld.banner" :src="formWorld.banner" fit="cover">
                            <template #error>
                                <div class="image-slot"></div>
                            </template>
                        </el-image>
                    </div>
                </div>
                <div class="qp-meworld-identity">
                    <h1 class="qp-meworld-identity-name">
                        <span v-text="formWorld.name"></span>
                    </h1>
                    <p class="qp-meworld-identity-description">
                        <span v-text="formWorld.description"></span>
                    </p>
                </div>
            </qpCard>
        </el-col>
        <el-col :span="24" :sm="7">
            <qpCard class="qp-meworld-general-upload">
                <el-upload ref="formWorldBannerRef" action="#" accept="image/*" :auto-upload="false" :show-file-list="false" :limit="1" :on-change="doChangeBanner" :on-exceed="doExceedBanner">
                    <div class="qp-meworld-general-upload-icon">
                        <el-icon>
                            <Picture />
                        </el-icon>
                    </div>
                    <div class="qp-meworld-general-upload-text">
                        <span v-text="$t('ChangeBanner')"></span>
                    </div>
                    <div class="qp-meworld-general-upload-info">
                        <span v-text="$t('1200x250pxSizeRecommended')"></span>
                    </div>
                </el-upload>
            </qpCard>
        </el-col>
        <el-col :span="24">
            <qpCard class="qp-meworld-form-general">
                <template #header>
                    <span v-text="$t('GeneralInformations')"></span>
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
import { Picture } from "@element-plus/icons-vue";
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
    banner: null,
    banner_file: null,
    visibility: 0,
    is_active: false
})
const formWorldRules = reactive({})

const initFormWorld = (r) => {
    formWorld.name = r.name
    formWorld.slug = r.slug
    formWorld.description = r.description
    formWorld.banner = r.banner
    formWorld.banner_file = null
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
        if (formWorld.banner_file) {
            data.append("banner", formWorld.banner_file)
        }
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

const formWorldBannerRef = ref()

const doExceedBanner = (event) => {
    formWorldBannerRef.value.clearFiles()
    formWorldBannerRef.value.handleStart(event[0])
}

const doChangeBanner = (event) => {
    if (event.raw.type !== "image/jpeg") {
        ElMessage.error(t("FileFormatMustBeJPG"))
        return false
    } else if (event.raw.size / 1024 / 1024 > 1) {
        ElMessage.error(t("FileSizeCanNotExceed1MB"))
        return false
    }
    formWorld.banner = URL.createObjectURL(event.raw)
    formWorld.banner_file = event.raw
}

</script>

<style>
/* ===--- banner ---=== */
.qp-meworld-banner {
    text-align: center;
    min-height: 150px;
    position: relative;
    margin: 0;
}
.qp-meworld-banner-inner  {
    background-color: var(--qp-default-disabled-bg);
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    overflow: hidden;
    height: 150px;
    margin: 0;
}
.qp-meworld-banner-inner .el-image {
    width: 100%;
    height: 100%;
    opacity: 0.9;
}
@media (max-width: 767px) {
    .qp-meworld-banner {
        min-height: 100px;
    }
    .qp-meworld-banner-inner  {
        height: 100px;
    }
}
/* ===--- identity ---=== */
.qp-meworld-identity {
    padding: 20px 12px 20px;
}
.qp-meworld-identity-name {
    font-family: "Quicksand", sans-serif;
    font-size: 32px;
    font-weight: 400;
    line-height: 120%;
    word-break: break-word;
    padding: 0;
    margin: 0 0 12px;
}
.qp-meworld-identity-description {
    font-family: "Roboto Condensed", sans-serif;
    font-size: 14px;
    font-weight: 400;
    font-style: italic;
    line-height: 120%;
    letter-spacing: 1px;
    opacity: 0.6;
    padding: 0;
    margin: 0 0 12px;
}
@media (max-width: 767px) {
    .qp-meworld-identity-name {
        font-size: 20px;
    }
}
/* ===--- upload ---=== */
.qp-meworld-general-upload {
    display: flex;
    align-items: center;
}
.qp-meworld-general-upload .el-upload {
    flex-direction: column;
    transition: opacity 0.4s;
}
.qp-meworld-general-upload .el-upload:hover {
    opacity: 0.6;
}
.qp-meworld-general-upload-icon {
    font-size: 24px;
    line-height: 120%;
    margin: 0 0 8px;
}
.qp-meworld-general-upload-text {
    font-size: 16px;
    line-height: 120%;
    margin: 0 0 4px;
}
.qp-meworld-general-upload-info {
    font-size: 12px;
    line-height: 120%;
    opacity: 0.6;
}
</style>