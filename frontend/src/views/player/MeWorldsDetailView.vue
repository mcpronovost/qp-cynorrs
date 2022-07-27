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
                            <qpCard h="auto">
                                (navigation)
                            </qpCard>
                        </el-col>
                        <el-col :span="24" :md="18">
                            <qpCard class="qp-meworld-form-general" :style="app.win.w < 1200 ? '' : 'padding-right:60px'">
                                <el-form ref="formWorldRef" :model="formWorld" :label-position="app.win.w < 1200 ? 'top' : 'right'" :rules="formWorldRules" label-width="120px" status-icon>
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
                                </el-form>
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
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import { API } from "@/main.js";
import i18n from "@/plugins/i18n";

import qpCard from "@/components/basic/qpCard.vue";

const { t } = i18n.global

const route = useRoute();
const router = useRouter();
const store = useStore();
const app = computed(() => store.getters.app);
const rat = computed(() => store.getters.rat);

const isLoading = ref(true);
const hasError = ref(null);

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
            initFormWorld(r)
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

const formWorldRef = ref()
const formWorld = reactive({
    name: "",
    slug: "",
    description: "",
    visibility: 0
})
const formWorldRules = reactive({})

const initFormWorld = (r) => {
    formWorld.name = r.name
    formWorld.slug = r.slug
    formWorld.description = r.description
    formWorld.visibility = r.visibility
}

</script>

<style scoped>

</style>
