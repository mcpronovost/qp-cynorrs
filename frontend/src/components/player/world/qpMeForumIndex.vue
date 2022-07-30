<template>
  <el-row>
    <el-col :span="24">
      <qpCard class="qp-meworld-form-forum">
        <template #header>
          <span v-text="$t('Index')"></span>
        </template>
        <el-tabs v-if="listZones.length" v-model="tabIndex" addable @tab-add="openAddZone()">
          <el-tab-pane v-for="(zone, n) in listZones" :key="`zone-${n}`" :label="zone.name" :name="zone.id">
            <template #label>
              <span class="custom-tabs-label">
                <span v-text="zone.name"></span>
              </span>
              <el-icon class="mdi mdi-pencil is-icon-close" @click="openEditZone(zone)" />
            </template>
            <div>
                <el-table :data="zone.territories" :show-header="false" :empty-text="$t('NoTerritories')" style="width:100%">
                    <el-table-column type="expand">
                        <template #default="props">
                            <div>
                                <el-table :data="props.row.sectors" :show-header="false" :empty-text="$t('NoSectors')" style="width:100%;">
                                    <el-table-column prop="ordering" align="center" width="48" />
                                    <el-table-column prop="name" />
                                    <el-table-column prop="action" fixed="right" width="60">
                                        <template #default="props">
                                            <el-button size="small" @click="openEditSector(props.row)">
                                                <el-icon class="mdi mdi-pencil" />
                                            </el-button>
                                        </template>
                                    </el-table-column>
                                    <template #append>
                                        <div class="text-center pa-6">
                                            <el-button size="small" @click="openAddSector(props.row)">
                                                <span v-text="$t('AddANewSector')"></span>
                                            </el-button>
                                        </div>
                                    </template>
                                </el-table>
                            </div>
                        </template>
                    </el-table-column>
                    <el-table-column prop="name" />
                    <el-table-column prop="action" fixed="right" width="60">
                        <template #default="props">
                            <el-button size="small" @click="openEditTerritory(props.row)">
                                <el-icon class="mdi mdi-pencil" />
                            </el-button>
                        </template>
                    </el-table-column>
                    <template #append>
                        <div class="text-center pa-6">
                            <el-button size="small" @click="openAddTerritory(zone)">
                                <span v-text="$t('AddANewTerritory')"></span>
                            </el-button>
                        </div>
                    </template>
                </el-table>
            </div>
          </el-tab-pane>
        </el-tabs>
        <div v-else>
            <el-button @click="openAddZone()">
                <span v-text="$t('AddANewZone')"></span>
            </el-button>
        </div>
      </qpCard>
      <!---->
      <el-dialog v-model="showAddZone" :title="$t('AddANewZone')" width="800px" destroy-on-close>
        <qpDialogZoneAdd :forum="props.forum" @init-forum="$emit('init-forum')" @close="closeAddZone()" />
      </el-dialog>
      <el-dialog v-model="showEditZone" :title="$t('EditAZone')" width="800px" destroy-on-close>
        <qpDialogZoneEdit :zone="currentZone" @init-forum="$emit('init-forum')" @close="closeEditZone()" />
      </el-dialog>
      <!---->
      <el-dialog v-model="showAddTerritory" :title="$t('AddANewTerritory')" width="800px" destroy-on-close>
        <qpDialogTerritoryAdd :zone="currentZone" @init-forum="$emit('init-forum')" @close="closeAddTerritory()" />
      </el-dialog>
      <el-dialog v-model="showEditTerritory" :title="$t('EditATerritory')" width="800px" destroy-on-close>
        <qpDialogTerritoryEdit :territory="currentTerritory" @init-forum="$emit('init-forum')" @close="closeEditTerritory()" />
      </el-dialog>
      <!---->
      <el-dialog v-model="showAddSector" :title="$t('AddANewSector')" width="800px" destroy-on-close>
        <qpDialogSectorAdd :territory="currentTerritory" @init-forum="$emit('init-forum')" @close="closeAddSector()" />
      </el-dialog>
      <el-dialog v-model="showEditSector" :title="$t('EditASector')" width="800px" destroy-on-close>
        <qpDialogSectorEdit :sector="currentSector" @init-forum="$emit('init-forum')" @close="closeEditSector()" />
      </el-dialog>
      <!---->
    </el-col>
  </el-row>
</template>

<script setup>
import { onMounted, ref } from "vue";

import qpCard from "@/components/basic/qpCard.vue";
import qpDialogZoneAdd from "@/components/player/world/qpMeForumIndexZoneAdd.vue";
import qpDialogZoneEdit from "@/components/player/world/qpMeForumIndexZoneEdit.vue";
import qpDialogTerritoryAdd from "@/components/player/world/qpMeForumIndexTerritoryAdd.vue";
import qpDialogTerritoryEdit from "@/components/player/world/qpMeForumIndexTerritoryEdit.vue";
import qpDialogSectorAdd from "@/components/player/world/qpMeForumIndexSectorAdd.vue";
import qpDialogSectorEdit from "@/components/player/world/qpMeForumIndexSectorEdit.vue";

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
const currentZone = ref()
const currentTerritory = ref()
const currentSector = ref()

const initIndex = () => {
  listZones.value = props.forum.zones
  if (listZones.value.length) {
    tabIndex.value = listZones.value[0].id
  }
}

onMounted(() => {
  initIndex()
})

const showAddZone = ref(false)
const showEditZone = ref(false)
const showAddTerritory = ref(false)
const showEditTerritory = ref(false)
const showAddSector = ref(false)
const showEditSector = ref(false)

const openAddZone = () => {
    showAddZone.value = true
}
const closeAddZone = () => {
    showAddZone.value = false
}

const openEditZone = (z) => {
    currentZone.value = z
    showEditZone.value = true
}
const closeEditZone = () => {
    showEditZone.value = false
}

const openAddTerritory = (z) => {
    currentZone.value = z
    showAddTerritory.value = true
}
const closeAddTerritory = () => {
    showAddTerritory.value = false
}

const openEditTerritory = (t) => {
    currentTerritory.value = t
    showEditTerritory.value = true
}
const closeEditTerritory = () => {
    showEditTerritory.value = false
}

const openAddSector = (t) => {
    currentTerritory.value = t
    showAddSector.value = true
}
const closeAddSector = () => {
    showAddSector.value = false
}

const openEditSector = (s) => {
    currentSector.value = s
    showEditSector.value = true
}
const closeEditSector = () => {
    showEditSector.value = false
}

</script>
