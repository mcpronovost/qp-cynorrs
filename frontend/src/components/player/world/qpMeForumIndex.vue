<template>
  <el-row>
    <el-col :span="24">
      <qpCard class="qp-meworld-form-forum">
        <template #header>
          <span v-text="$t('Index')"></span>
        </template>
        <el-tabs v-model="tabIndex" addable @tab-add="doAddZone()">
          <el-tab-pane v-for="(zone, n) in listZones" :key="`zone-${n}`" :label="zone.name" :name="zone.id">
            <template #label>
              <span class="custom-tabs-label">
                <span v-text="zone.name"></span>
              </span>
              <el-icon class="mdi mdi-pencil is-icon-close" @click="doRemoveZone(zone)" />
            </template>
          </el-tab-pane>
        </el-tabs>
      </qpCard>
    </el-col>
  </el-row>
</template>

<script setup>
import { onMounted, ref } from "vue";

import qpCard from "@/components/basic/qpCard.vue";

const props = defineProps({
    world: {
        type: Object,
        default: () => {}
    },
    forum: {
        type: Object,
        default: () => {}
    }
})

const tabIndex = ref()
const listZones = ref([])

const initIndex = () => {
  listZones.value = props.forum.zones
  if (listZones.value.length) {
    tabIndex.value = listZones.value[0].id
  }
}

onMounted(() => {
  initIndex()
})

const doAddZone = () => {
  console.log("doAddZone")
}

const doRemoveZone = ($event) => {
  console.log("doRemoveZone : ", $event)
}

</script>
