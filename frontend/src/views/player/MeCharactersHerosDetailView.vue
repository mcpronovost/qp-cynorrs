<template>
    <div class="qp-vue">
        <div v-if="!isLoading && !hasError && rat && character">
            <div class="qp-container">
                <header>
                    <el-row align="middle">
                        <el-col :span="24" :sm="12" align="left">
                            <h1>
                                <span v-text="character.name"></span>
                            </h1>
                        </el-col>
                        <el-col :span="24" :sm="12" :align="app.win.w >= 768 ? 'right' : 'left'">
                            <el-button disabled type="primary">
                                <span v-text="$t('ShowProfile')"></span>
                            </el-button>
                        </el-col>
                    </el-row>
                </header>
                <section>
                    <el-row>
                        <el-col :span="24" :md="6">
                            <qpCard h="auto" pa="0">
                                <qpPlayerMeNav :navs="navs" :tab="tab" @goto="goToTab" />
                            </qpCard>
                        </el-col>
                        <el-col :span="24" :md="18" style="padding:0">
                            <el-row>
                                <el-col :span="24" :sm="17">
                                    <qpCard pa="0">
                                        <div class="qp-profile-header">
                                            <div class="qp-profile-header-banner">
                                                <el-image v-if="formCharacter.avatar" :src="formCharacter.avatar" fit="cover">
                                                    <template #error>
                                                        <div class="image-slot"></div>
                                                    </template>
                                                </el-image>
                                            </div>
                                            <div class="qp-profile-header-avatar">
                                                <el-avatar :src="formCharacter.avatar">
                                                    <span v-text="character.initials"></span>
                                                </el-avatar>
                                            </div>
                                        </div>
                                    </qpCard>
                                </el-col>
                                <el-col :span="24" :sm="7">
                                    <qpCard class="qp-meprofile-general-upload">
                                        <el-upload ref="formCharacterAvatarRef" action="#" accept="image/*" :auto-upload="false" :show-file-list="false" :limit="1" :on-change="doChangeAvatar" :on-exceed="doExceedAvatar">
                                            <div class="qp-meprofile-general-upload-icon">
                                                <el-icon>
                                                    <User />
                                                </el-icon>
                                            </div>
                                            <div class="qp-meprofile-general-upload-text">
                                                <span v-text="$t('ChangeAvatar')"></span>
                                            </div>
                                            <div class="qp-meprofile-general-upload-info">
                                                <span v-text="$t('150x150pxSizeMinimum')"></span>
                                            </div>
                                        </el-upload>
                                    </qpCard>
                                </el-col>
                            </el-row>
                            <el-row>
                                <el-col :span="24">
                                    <qpCard class="qp-mecharacter-form-general">
                                        <template #header>
                                            <span v-text="$t('GeneralInformations')"></span>
                                        </template>
                                        <el-form ref="formCharacterRef" :model="formCharacter" :label-position="app.win.w < 1200 ? 'top' : 'right'" :rules="formCharacterRules" label-width="120px" status-icon :style="app.win.w < 1200 ? 'margin-top:12px;' : 'padding-right:60px;margin-top:12px;'">
                                            <el-form-item :label="$t('First Name')" prop="first_name">
                                                <el-input v-model="formCharacter.first_name" :placeholder="$t('First Name')" :maxlength="32" show-word-limit />
                                            </el-form-item>
                                            <el-form-item :label="$t('Middle Name')" prop="middle_name">
                                                <el-input v-model="formCharacter.middle_name" :placeholder="$t('Middle Name')" :maxlength="32" show-word-limit />
                                            </el-form-item>
                                            <el-form-item :label="$t('Last Name')" prop="last_name">
                                                <el-input v-model="formCharacter.last_name" :placeholder="$t('Last Name')" :maxlength="32" show-word-limit />
                                            </el-form-item>
                                            <el-form-item :label="$t('Gender')" prop="gender">
                                                <el-select v-model="formCharacter.gender" :placeholder="$t('Gender')">
                                                    <el-option v-for="(item, n) in character.gender_choix" :key="`gender-${n}`" :label="item[1]" :value="item[0]" />
                                                </el-select>
                                            </el-form-item>
                                        </el-form>
                                        <el-row>
                                            <el-col>
                                                <el-button :disabled="isLoadingSend" class="ma-6" @click="resetFormCharacter()">
                                                    <span v-text="$t('Reset')"></span>
                                                </el-button>
                                                <el-button :loading="isLoadingSend" class="ma-6" type="primary" @click="doFormCharacter()">
                                                    <span v-text="$t('Send')"></span>
                                                </el-button>
                                            </el-col>
                                        </el-row>
                                    </qpCard>
                                </el-col>
                            </el-row>
                        </el-col>
                    </el-row>
                </section>
            </div>
        </div>

        <div v-else-if="isLoading">
            <div class="qp-container">
                <div v-loading="isLoading" element-loading-background="transparent" style="height: 60vh"></div>
            </div>
        </div>

        <div v-else>
            <div class="qp-container">
                <qpCard h="auto">
                    <el-result icon="error" :title="$t('Error')" :sub-title="hasError" />
                </qpCard>
            </div>
        </div>
    </div>
</template>

<script setup>
import { computed, onMounted, reactive, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import { ElMessage } from "element-plus";
import { User } from "@element-plus/icons-vue";
import { API } from "@/main.js";
import i18n from "@/plugins/i18n";

import qpCard from "@/components/basic/qpCard.vue";
import qpPlayerMeNav from "@/components/player/core/qpMeNav.vue";

const { t } = i18n.global

const route = useRoute();
const router = useRouter();
const store = useStore();
const app = computed(() => store.getters.app);
const rat = computed(() => store.getters.rat);

const isLoading = ref(true);
const hasError = ref(null);

const navs = ref([
    {
        tab: "general",
        title: t("GeneralInformations"),
        caption: t("NameAvatarGenderAndMore"),
        icon: "mdi mdi-account-outline"
    }
])
const tab = ref("general")
const goToTab = (t) => {tab.value = t}

onMounted(() => {
    if (rat.value) {
        initCharacter()
    } else {
        router.push({ name: "AuthLogin" })
    }
})

const character = ref()

const initCharacter = async () => {
    isLoading.value = true
    hasError.value = null
    // ===---
    try {
        let response = await fetch(`${API}/me/characters/${route.params.pk}/`, {
            method: "GET",
            headers: {"Authorization": rat.value}
        })
        let r = await response.json()
        if (response.status === 200) {
            character.value = r
            initFormCharacter(r)
        } else {
            throw response
        }
    } catch (e) {
        if (e.status === 403) {
            hasError.value = t("YouDoesntHaveAccessToThisPage")
        } else {
            hasError.value = t("AnErrorOccurred")
        }
    }
    // ===---
    isLoading.value = false
}

const hasErrorSend = ref(null)
const isLoadingSend = ref(false)

const formCharacterRef = ref()
const formCharacter = reactive({
    first_name: "",
    middle_name: "",
    last_name: "",
    gender: "",
    avatar: null
})
const formCharacterRules = reactive({})

const initFormCharacter = (r) => {
    formCharacter.first_name = r.first_name
    formCharacter.middle_name = r.middle_name
    formCharacter.last_name = r.last_name
    formCharacter.gender = r.gender
    formCharacter.avatar = r.avatar
    formCharacter.avatar_file = null
}

const resetFormCharacter = () => {
    initFormCharacter(character.value)
}

const doFormCharacter = async () => {
    hasErrorSend.value = null
    isLoadingSend.value = true
    await formCharacterRef.value.validate((valid, fields) => {
        if (valid) {
            sendFormCharacter()
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

const sendFormCharacter = async () => {
    hasErrorSend.value = null
    isLoadingSend.value = true
    // ===---
    try {
        let data = new FormData()
        data.append("first_name", formCharacter.first_name)
        data.append("middle_name", formCharacter.middle_name)
        data.append("last_name", formCharacter.last_name)
        data.append("gender", formCharacter.gender)
        if (formCharacter.avatar_file) {
            data.append("avatar", formCharacter.avatar_file)
        }
        let response = await fetch(`${API}/me/characters/${route.params.pk}/`, {
            method: "PATCH",
            headers: {"Authorization": rat.value},
            body: data
        })
        let r = await response.json()
        if (response.status === 200) {
            ElMessage.success(t("CharacterUpdatedSuccessfully"))
            character.value = r
            initFormCharacter(r)
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

const formCharacterAvatarRef = ref()

const doExceedAvatar = (event) => {
    formCharacterAvatarRef.value.clearFiles()
    formCharacterAvatarRef.value.handleStart(event[0])
}

const doChangeAvatar = (event) => {
    if (event.raw.type !== "image/jpeg") {
        ElMessage.error(t("FileFormatMustBeJPG"))
        return false
    } else if (event.raw.size / 1024 / 1024 > 1) {
        ElMessage.error(t("FileSizeCanNotExceed1MB"))
        return false
    }
    formCharacter.avatar = URL.createObjectURL(event.raw)
    formCharacter.avatar_file = event.raw
}

</script>

<style scoped>
/* ===--- profile ---=== */
.qp-profile-header {
    text-align: center;
    min-height: 150px;
    position: relative;
    margin: 0;
}
.qp-profile-header-banner  {
    background-color: var(--qp-default-disabled-bg);
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    overflow: hidden;
    height: 100px;
    margin: 0;
}
.qp-profile-header-banner .el-image {
    width: 100%;
    height: 100%;
    opacity: 0.6;
}
.qp-profile-header-avatar {
    background-color: var(--qp-default-bg);
    border: 6px solid var(--qp-default-bg);
    border-radius: 100%;
    overflow: hidden;
    width: 120px;
    height: 120px;
    position: absolute;
    top: 8px;
    left: 0;
    right: 0;
    margin: 0 auto;
}
.qp-profile-header-avatar .el-avatar {
    font-size: 24px;
    line-height: 100%;
    width: 100%;
    height: 100%;
}
@media (max-width: 767px) {
    .qp-profile-header {
        min-height: 160px;
    }
    .qp-profile-header-banner  {
        height: 100px;
    }
    .qp-profile-header-avatar {
        width: 100px;
        height: 100px;
        top: 40px;
    }
}
</style>

<style>
.qp-meprofile-general-upload {
    display: flex;
    align-items: center;
}
.qp-meprofile-general-upload .el-upload {
    flex-direction: column;
    transition: opacity 0.4s;
}
.qp-meprofile-general-upload .el-upload:hover {
    opacity: 0.6;
}
.qp-meprofile-general-upload-icon {
    font-size: 24px;
    line-height: 120%;
    margin: 0 0 8px;
}
.qp-meprofile-general-upload-text {
    font-size: 16px;
    line-height: 120%;
    margin: 0 0 4px;
}
.qp-meprofile-general-upload-info {
    font-size: 12px;
    line-height: 120%;
    opacity: 0.6;
}
</style>
