<template>
    <div class="qp-vue">
        <div v-if="!isLoading && !hasError && rat && world">
            <div class="qp-container">
                <header>
                    <el-row>
                        <el-col align="left">
                            <h1>
                                <span v-text="world.name"></span>
                            </h1>
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
                            <qpPlayerMeWorldGeneral v-if="tab.startsWith('general')" :world="world" @init-world="initWorld" />
                            <qpPlayerMeWorldForum v-else-if="tab.startsWith('forum')" :tab="tab" :world="world" @init-world="initWorld" />
                            <el-row v-else-if="tab == 'style'">
                                <el-col :span="24">
                                    <qpCard class="qp-meworld-form-style">
                                        <template #header>
                                            <span v-text="$t('Style')"></span>
                                        </template>
                                        <el-result icon="info" :title="$t('UnderDevelopment')" />
                                    </qpCard>
                                </el-col>
                            </el-row>
                            <el-row v-else-if="tab == 'style-stylesheets'">
                                <el-col :span="24">
                                    <qpCard class="qp-meworld-form-style">
                                        <template #header>
                                            <span v-text="$t('Stylesheets')"></span>
                                        </template>
                                        <el-result icon="info" :title="$t('UnderDevelopment')" />
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
import { computed, onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import { API } from "@/main.js";
import i18n from "@/plugins/i18n";

import qpCard from "@/components/basic/qpCard.vue";
import qpPlayerMeNav from "@/components/player/core/qpMeNav.vue";
import qpPlayerMeWorldGeneral from "@/components/player/world/qpMeGeneral.vue";
import qpPlayerMeWorldForum from "@/components/player/world/qpMeForum.vue";

const { t } = i18n.global

const route = useRoute();
const router = useRouter();
const store = useStore();
const rat = computed(() => store.getters.rat);

const isLoading = ref(true);
const hasError = ref(null);

const navs = ref([
    {
        tab: "general",
        title: t("GeneralInformations"),
        caption: t("NameDescriptionVisibilityAndMore"),
        icon: "mdi mdi-account-outline"
    },
    {
        tab: "forum",
        title: t("Forum"),
        caption: t("ZonesTerritoriesSectorsAndSettings"),
        icon: "mdi mdi-forum-outline",
        subs: [
            {
                tab: "forum-index",
                title: t("Index")
            }
        ]
    },
    {
        tab: "style",
        title: t("Style"),
        caption: t("ColoursAndCustomStylesheet"),
        icon: "mdi mdi-brush-variant",
        subs: [
            {
                tab: "style-stylesheets",
                title: t("Stylesheets")
            }
        ]
    }
])
const tab = ref("general")
const goToTab = (t) => {tab.value = t}

onMounted(() => {
    if (rat.value) {
        initWorld()
    } else {
        router.push({ name: "AuthLogin" })
    }
})

const world = ref()

const initWorld = async () => {
    isLoading.value = true
    hasError.value = null
    // ===---
    try {
        let response = await fetch(`${API}/me/worlds/${route.params.pk}/`, {
            method: "GET",
            headers: {"Authorization": rat.value}
        })
        let r = await response.json()
        if (response.status === 200) {
            world.value = r
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

</style>
