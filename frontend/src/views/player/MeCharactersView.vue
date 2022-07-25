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
          <el-row v-if="listCharacters.length">
            <el-col v-for="(world, n) in listCharacters" :key="`character-${n}`">
              <qpCard clickable pa="12px">
                <el-row align="middle">
                  <el-col :span="24" :md="12" align="left">
                    <div class="qp-mecharacters-overview">
                      <h2 class="qp-mecharacters-overview-title">
                        <span v-text="'Qalatlán'"></span>
                      </h2>
                      <div v-if="false" class="qp-mecharacters-overview-tags">
                        <el-tag type="danger" effect="plain" size="small"><span v-text="$t('Closed')"></span></el-tag>
                      </div>
                      <p>Lorem ipsum dolor sit amet.</p>
                    </div>
                  </el-col>
                </el-row>
              </qpCard>
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
import { useStore } from "vuex";

import qpCard from "@/components/basic/qpCard.vue";

const store = useStore()
const rat = computed(() => store.getters.rat)

const isLoading = ref(true)
const hasError = ref(null)
const listCharacters = ref([])

onMounted(() => {
  console.log("onMounted")
  isLoading.value = false
})

</script>

<style scoped>
/* ===--- overview ---=== */
.qp-mecharacters-overview-title {
  font-family: "Quicksand", sans-serif;
  font-size: 32px;
  font-weight: 400;
  line-height: 120%;
  padding: 0;
  margin: 0 0 12px;
}
.qp-mecharacters-overview-tags {
  margin: 12px 0;
}
/* ===--- infolist ---=== */
.qp-mecharacters-infolist {
  list-style: none;
  padding: 0;
  margin: 0;
}
.qp-mecharacters-infolist li {
  text-align: center;
  list-style: none;
  display: inline-flex;
  flex: 1 1 25%;
  flex-direction: column;
  flex-wrap: wrap;
  padding: 0;
  margin: 4px 12px;
}
.qp-mecharacters-infolist span {
  display: block;
  padding: 0;
  margin: 0;
}
.qp-mecharacters-infolist .qp-value {
  color: var(--qp-primary);
  font-size: 24px;
  font-weight: 600;
  line-height: 120%;
  order: 1;
}
.qp-mecharacters-infolist .qp-label {
  font-size: 12px;
  font-weight: 400;
  line-height: 120%;
  display: block;
  order: 2;
  margin: 6px 0 0;
}
@media (max-width: 991px) {
  .qp-mecharacters-overview,
  .qp-mecharacters-infolist {
    text-align: center;
  }
}
</style>
