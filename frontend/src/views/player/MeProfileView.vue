<template>
    <div class="qp-vue">
        <div v-if="!isLoading && !hasError && rat">
            <div class="qp-container">
                <header>
                    <el-row>
                        <el-col align="left">
                            <h1>
                                <span v-text="$t('YourProfile')"></span>
                            </h1>
                        </el-col>
                    </el-row>
                </header>
                <section>
                    <el-row>
                        <el-col>
                            <qpCard pa="0">
                                <div class="qp-profile-header">
                                    <div class="qp-profile-header-banner">
                                        <el-image v-if="formProfile.banner" :src="formProfile.banner" fit="cover">
                                            <template #error>
                                                <div class="image-slot"></div>
                                            </template>
                                        </el-image>
                                    </div>
                                    <div class="qp-profile-header-avatar">
                                        <el-avatar :src="formProfile.avatar">
                                            <span v-text="formProfile.initials"></span>
                                        </el-avatar>
                                    </div>
                                </div>
                                <div class="qp-profile-identity">
                                    <h2 class="qp-profile-identity-name">
                                        <span v-text="formProfile.playername"></span>
                                    </h2>
                                    <p class="qp-profile-identity-title">
                                        <span v-text="formProfile.title"></span>
                                    </p>
                                </div>
                            </qpCard>
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
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import { API } from "@/main.js";
import i18n from "@/plugins/i18n";

import qpCard from "@/components/basic/qpCard.vue";

const { t } = i18n.global

const router = useRouter();
const store = useStore();
const rat = computed(() => store.getters.rat);

const isLoading = ref(true);
const hasError = ref(null);

onMounted(() => {
    if (rat.value) {
        initProfile()
    } else {
        router.push({ name: "AuthLogin" })
    }
})

// const hasErrorSend = ref(null)
// const isLoadingSend = ref(false)
// const formProfileRef = ref()
const formProfile = reactive({
    avatar: null,
    banner: null,
    initials: ""
})
// const formProfileRules = reactive({})

const initProfile = async () => {
    isLoading.value = true
    hasError.value = null
    // ===---
    try {
        let response = await fetch(`${API}/me/`, {
            method: "GET",
            headers: {"Authorization": rat.value}
        })
        let r = await response.json()
        if (response.status === 200) {
            formProfile.avatar = r.avatar
            formProfile.banner = r.banner
            formProfile.playername = r.playername
            formProfile.title = "Qui ne fait que passer"
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

</script>

<style scoped>
/* =- header */
.qp-profile-header {
    text-align: center;
    min-height: 250px;
    position: relative;
    margin: 0;
}
.qp-profile-header-banner  {
    background-color: var(--qp-default-disabled-bg);
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    overflow: hidden;
    height: 160px;
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
    width: 150px;
    height: 150px;
    position: absolute;
    top: 80px;
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
/* ===--- identity ---=== */
.qp-profile-identity {
    padding: 6px 12px 20px;
}
.qp-profile-identity-name {
    font-family: "Quicksand", sans-serif;
    font-size: 32px;
    font-weight: 400;
    line-height: 120%;
    word-break: break-word;
    padding: 0;
    margin: 0 0 12px;
}
.qp-profile-identity-title {
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
    .qp-profile-identity-name {
        font-size: 24px;
    }
}
</style>
