<template>
  <div class="qp-vue">

    <div v-if="!isLoading && !hasError && rat">
      <div v-if="!showCreateWorld" class="qp-container">
        <header>
          <el-row>
            <el-col :span="24" :sm="12" align="left">
              <h1>
                <span v-text="$t('YourWorlds')"></span>
              </h1>
            </el-col>
            <el-col :span="24" :sm="12" :align="app.win.w >= 768 ? 'right' : 'left'">
              <el-button :disabled="!player.limits.can_create_worlds" @click="openCreateWorld()">
                <span v-text="$t('CreateWorld')"></span>
              </el-button>
            </el-col>
          </el-row>
        </header>
        <section>
          <el-row v-if="listWorlds.length">
            <el-col v-for="(world, n) in listWorlds" :key="`world-${n}`">
              <qpCard clickable pa="12px">
                <el-row align="middle">
                  <el-col :span="24" :md="12" align="left">
                    <div class="qp-meworlds-overview">
                      <div class="qp-meworlds-overview-tags">
                        <el-tag v-if="!world.is_active" type="danger" effect="plain" size="small"><span v-text="$t('Closed')"></span></el-tag>
                        <el-tag v-if="player.id == world.creator" effect="plain" size="small"><span v-text="$t('Creator')"></span></el-tag>
                        <el-tag v-if="world.administrators.includes(player.id)" effect="plain" size="small"><span v-text="$t('Administration')"></span></el-tag>
                        <el-tag v-if="world.moderators.includes(player.id)" effect="plain" size="small"><span v-text="$t('Moderation')"></span></el-tag>
                      </div>
                      <h2 class="qp-meworlds-overview-title">
                        <span v-text="world.name"></span>
                      </h2>
                      <p v-if="world.description" v-text="world.description"></p>
                    </div>
                  </el-col>
                  <el-col :span="24" :md="12" align="right">
                    <ul class="qp-meworlds-infolist">
                      <li>
                        <span class="qp-label" v-text="$t('Player', world.count_players)"></span>
                        <span class="qp-value" v-text="$filters.num_to_element(world.count_players, 1)"></span>
                      </li>
                      <li>
                        <span class="qp-label" v-text="$t('Character', world.count_heros)"></span>
                        <span class="qp-value" v-text="$filters.num_to_element(world.count_heros, 1)"></span>
                      </li>
                      <li>
                        <span class="qp-label" v-text="$t('Chapter', world.count_chapters)"></span>
                        <span class="qp-value" v-text="$filters.num_to_element(world.count_chapters, 1)"></span>
                      </li>
                      <li>
                        <span class="qp-label" v-text="$t('Message', world.count_messages)"></span>
                        <span class="qp-value" v-text="$filters.num_to_element(world.count_messages, 1)"></span>
                      </li>
                    </ul>
                  </el-col>
                </el-row>
              </qpCard>
            </el-col>
            <el-col>
                <el-pagination
                    background
                    hide-on-single-page
                    layout="prev, pager, next"
                    :total="totalWorlds"
                    :page-size="sizeWorlds"
                    :current-page="pageWorlds"
                    @update:current-page="updatePageWorlds"
                />
            </el-col>
          </el-row>
          <el-row v-else>
            <el-col>
              <el-empty :description="$t('NoWorldCreated')">
                <template #image>
                  <el-icon class="mdi mdi-emoticon-sad-outline mdi-48px" />
                </template>
              </el-empty>
            </el-col>
          </el-row>
        </section>
      </div>
      <div v-else-if="showCreateWorld" class="qp-container">
        <header>
          <el-row>
            <el-col :span="24">
              <h1>
                <span v-text="$t('CreateWorld')"></span>
              </h1>
            </el-col>
          </el-row>
        </header>
        <section>
            <el-row>
                <el-col>
                    <qpCard>
                        <el-row>
                            <el-col>
                                <el-form ref="formCreateWorldRef" :model="formCreateWorld" :label-position="app.win.w < 1200 ? 'top' : 'right'" label-width="120px" status-icon>
                                    <el-form-item :label="$t('Name')" prop="name" :rules="[{required: true, message: $t('Thisfieldisrequired'), trigger: 'blur'}]">
                                        <el-input v-model="formCreateWorld.name" type="text" maxlength="32" show-word-limit :placeholder="$t('YourPersonalUsername')" />
                                    </el-form-item>
                                    <el-form-item :label="$t('Description')" prop="description" :rules="[{required: true, message: $t('Thisfieldisrequired'), trigger: 'blur'}]">
                                        <el-input v-model="formCreateWorld.description" type="text" maxlength="250" @keyup.enter="closeCreateWorld()" />
                                    </el-form-item>
                                </el-form>
                            </el-col>
                            <el-col v-if="hasErrorSend">
                                <el-alert type="error" show-icon>
                                    <template #default>
                                        <div v-html="hasErrorSend"></div>
                                    </template>
                                </el-alert>
                            </el-col>
                            <el-col>
                                <el-button :disabled="isLoadingSend" @click="closeCreateWorld()">
                                    <span v-text="$t('Cancel')"></span>
                                </el-button>
                                <el-button type="primary" :loading="isLoadingSend">
                                    <span v-text="$t('Send')"></span>
                                </el-button>
                            </el-col>
                        </el-row>
                    </qpCard>
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

import { computed, onMounted, reactive, ref } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import { API } from "@/main.js";
import i18n from "@/plugins/i18n";

import qpCard from "@/components/basic/qpCard.vue";

const { t } = i18n.global

const router = useRouter()
const store = useStore()
const rat = computed(() => store.getters.rat)
const app = computed(() => store.getters.app)
const player = computed(() => store.getters.player)

const isLoading = ref(true)
const isLoadingSend = ref(false)
const hasError = ref(null)
const hasErrorSend = ref(null)
const listWorlds = ref([])
const totalWorlds = ref(0)
const pageWorlds = ref(1)
const sizeWorlds = ref(0)

onMounted(() => {
    if (rat.value) {
        initWorlds()
    } else {
        router.push({name: "AuthLogin"})
    }
})

const initWorlds = async () => {
    isLoading.value = true
    hasError.value = null
    listWorlds.value = []
    // ===---
    let response = await fetch(`${API}/worlds/?page=${pageWorlds.value}`, {
        method: "GET",
        headers: {"Authorization": rat.value}
    })
    let r = await response.json()
    if (response.status === 200) {
        totalWorlds.value = r.count
        listWorlds.value = r.results
        sizeWorlds.value = r.size
    } else {
        hasError.value = t("ThisWorldDoesntExistAnymore")
    }
    // ===---
    isLoading.value = false
}

const updatePageWorlds = ($event) => {
    pageWorlds.value = $event
    initWorlds()
}

const showCreateWorld = ref(false)
const formCreateWorldRef = ref()
const formCreateWorld = reactive({
    "name": "",
    "description": ""
})

const openCreateWorld = () => {
    showCreateWorld.value = true
}

const closeCreateWorld = () => {
    showCreateWorld.value = false
}

</script>

<style scoped>
/* ===--- overview ---=== */
.qp-meworlds-overview-title {
  font-family: "Quicksand", sans-serif;
  font-size: 32px;
  font-weight: 400;
  line-height: 120%;
  padding: 0;
  margin: 0 0 12px;
}
.qp-meworlds-overview-tags .el-tag {
  margin: 0 6px 6px 0;
}
/* ===--- infolist ---=== */
.qp-meworlds-infolist {
  list-style: none;
  padding: 0;
  margin: 0;
}
.qp-meworlds-infolist li {
  text-align: center;
  list-style: none;
  display: inline-flex;
  flex: 1 1 25%;
  flex-direction: column;
  flex-wrap: wrap;
  padding: 0;
  margin: 4px 12px;
}
.qp-meworlds-infolist span {
  display: block;
  padding: 0;
  margin: 0;
}
.qp-meworlds-infolist .qp-value {
  color: var(--qp-primary);
  font-size: 24px;
  font-weight: 600;
  line-height: 120%;
  order: 1;
}
.qp-meworlds-infolist .qp-label {
  font-size: 12px;
  font-weight: 400;
  line-height: 120%;
  display: block;
  order: 2;
  margin: 6px 0 0;
}
@media (max-width: 991px) {
  .qp-meworlds-overview,
  .qp-meworlds-infolist {
    text-align: center;
  }
}
</style>
