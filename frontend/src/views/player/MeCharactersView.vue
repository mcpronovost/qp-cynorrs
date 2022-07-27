<template>
  <div class="qp-vue">

    <div v-if="!isLoading && !hasError && rat">
      <div class="qp-container">
        <header>
          <el-row>
            <el-col :span="24" align="left">
              <h1>
                <span v-text="$t('YourCharacters')"></span>
              </h1>
            </el-col>
          </el-row>
        </header>
        <section>
          <el-row v-if="listHeros.length">
            <el-col v-for="(character, n) in listHeros" :key="`world-${n}`" :span="24" :sm="12" :md="6">
              <qpCard clickable overflow pa="0" @click="goToCharacter(character.id, 'hero')">
                <div class="qp-profile-header">
                    <div class="qp-profile-header-banner">
                        <el-image v-if="character.avatar" :src="character.avatar" fit="cover">
                            <template #error>
                                <div class="image-slot"></div>
                            </template>
                        </el-image>
                    </div>
                    <div class="qp-profile-header-avatar">
                        <el-avatar :src="character.avatar">
                            <span v-text="character.initials"></span>
                        </el-avatar>
                    </div>
                </div>
                <div class="qp-profile-identity">
                    <h2 class="qp-profile-identity-name">
                        <span v-text="character.name"></span>
                    </h2>
                    <p class="qp-profile-identity-worldname">
                        <span v-text="character.world?.name"></span>
                    </p>
                </div>
              </qpCard>
            </el-col>
            <el-col>
                <el-pagination
                    v-if="listHeros.length"
                    background
                    hide-on-single-page
                    layout="prev, pager, next"
                    :total="totalHeros"
                    :page-size="sizeHeros"
                    :current-page="pageHeros"
                    @update:current-page="updatePageHeros"
                />
            </el-col>
          </el-row>
          <el-row v-else>
            <el-col>
              <el-empty :description="$t('NoCharacterCreated')">
                <template #image>
                  <el-icon class="mdi mdi-emoticon-sad-outline mdi-48px" />
                </template>
              </el-empty>
            </el-col>
          </el-row>
        </section>
      </div>
    </div>

    <div v-else-if="isLoading">
      <div class="qp-container">
        <div v-loading="isLoading" element-loading-background="transparent" style="height:60vh"></div>
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
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import { API } from "@/main.js";
import i18n from "@/plugins/i18n";

import qpCard from "@/components/basic/qpCard.vue";

const { t } = i18n.global

const router = useRouter()
const store = useStore()
const rat = computed(() => store.getters.rat)

const isLoading = ref(true)
const hasError = ref(null)

const listHeros = ref([])
const totalHeros = ref(0)
const sizeHeros = ref(0)
const pageHeros = ref(1)

onMounted(() => {
    if (rat.value) {
        initHeros()
    } else {
        router.push({name: "AuthLogin"})
    }
})

const initHeros = async () => {
    isLoading.value = true
    hasError.value = null
    listHeros.value = []
    // ===---
    try {
        let response = await fetch(`${API}/me/characters/heros/?page=${pageHeros.value}`, {
            method: "GET",
            headers: {"Authorization": rat.value}
        })
        let r = await response.json()
        if (response.status === 200) {
            totalHeros.value = r.count
            listHeros.value = r.results
            sizeHeros.value = r.size
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

const updatePageHeros = ($event) => {
    pageHeros.value = $event
    initHeros()
}

const goToCharacter = (id, type_of) => {
    if (type_of == "hero") {
      router.push({name: "MeCharactersHerosDetail", params: {pk: id}})
    }
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
    top: -8px;
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
    font-size: 20px;
    font-weight: 400;
    line-height: 120%;
    word-break: break-word;
    padding: 0;
    margin: 0 0 12px;
}
.qp-profile-identity-worldname {
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
        font-size: 16px;
    }
}
</style>
