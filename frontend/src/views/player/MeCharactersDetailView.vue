<template>
    <div class="qp-vue">
        <div v-if="!isLoading && !hasError && rat && character">
            <div class="qp-container">
                <header>
                    <el-row>
                        <el-col align="left">
                            <h1>
                                <span v-text="character.name"></span>
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
                            <qpCard class="qp-mecharacter-form-general" :style="app.win.w < 1200 ? '' : 'padding-right:60px'">
                                <el-form ref="formCharacterRef" :model="formCharacter" :label-position="app.win.w < 1200 ? 'top' : 'right'" :rules="formCharacterRules" label-width="120px" status-icon>
                                    <el-form-item :label="$t('Firstname')" prop="firstname">
                                        <el-input v-model="formCharacter.firstname" :placeholder="$t('Firstname')" :maxlength="32" show-word-limit />
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

const formCharacterRef = ref()
const formCharacter = reactive({
    firstname: "",
})
const formCharacterRules = reactive({})

const initFormCharacter = (r) => {
    formCharacter.firstname = r.firstname
}

</script>

<style scoped>

</style>
