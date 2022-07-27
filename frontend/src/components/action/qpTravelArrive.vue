<template>
    <div class="qp-action-travel-arrive">
        <el-row v-loading="isLoading" :gutter="20" justify="center">
            <el-col v-if="!isLoading && !hasError" class="text-center">
                <el-result icon="success" :title="$t('TravelCompleted')" style="padding-top:0">
                    <template #sub-title>
                        <div v-html="hasSuccess"></div>
                    </template>
                </el-result>
            </el-col>
            <el-col v-else-if="hasError" class="text-center">
                <el-result icon="error" :title="$t('Error')" style="padding-top:0">
                    <template #sub-title>
                        <div v-html="hasError"></div>
                    </template>
                </el-result>
            </el-col>
        </el-row>
        <div class="dialog-footer text-center">
            <el-button v-if="!isLoading && !hasError" type="primary" @click="closeTravel()">
                <span v-text="$t('Continue')"></span>
            </el-button>
            <el-button v-else-if="hasError" @click="closeTravel()">
                <span v-text="$t('Cancel')"></span>
            </el-button>
        </div>
    </div>
</template>

<script setup>

import { computed, onMounted, ref } from "vue";
import { useStore } from "vuex";
import { API } from "@/main.js";
import { Buffer } from "buffer";
import i18n from "@/plugins/i18n";

// =================================================================================== //
// ===--- PLUGINS

const { t } = i18n.global

const store = useStore()
const rat = computed(() => store.getters.rat)

// =================================================================================== //
// ===--- EMIT

const emit = defineEmits(["close"])

// =================================================================================== //
// ===--- PROPS

const props = defineProps({
    travellers: {
        type: Array,
        default: () => []
    },
    territory: {
        type: Object,
        default: () => {}
    },
    sector: {
        type: Object,
        default: () => {}
    }
})

// =================================================================================== //
// ===--- DATA

const isLoading = ref(false)
const hasError = ref(null)
const hasSuccess = ref(null)

// =================================================================================== //
// ===--- METHODS

const doSendTravelArrive = async () => {
    isLoading.value = true
    hasError.value = null
    hasSuccess.value = null
    // ===---
    let data = new FormData()
    data.append("travellers", Buffer.from(JSON.stringify(props.travellers)).toString("base64"))
    data.append("territory", props.territory.id)
    if (props.sector) {
        data.append("sector", props.sector.id)
    }
    // ===---
    const r = await fetch(`${API}/game/action/travel/`, {
        method: "POST",
        headers: {"Authorization": rat.value},
        body: data
    })
    if (r.status === 200) {
        let result = await r.json()
        console.log(result)
        hasSuccess.value = t('Youhavearrivedatyourdestination')
        store.commit("BATCH_HEROS", result.heros)
    } else {
        hasError.value = t("AnErrorOccurred")
    }
    // ===---
    isLoading.value = false
}

const closeTravel = () => {
    emit("close")
}

// =================================================================================== //
// ===--- MOUNTED

onMounted(() => {
  doSendTravelArrive()
})

</script>

<style scoped>
.qp-action-travel-choosetravellers .qp-action-travel-traveller {
    text-align: center;
    display: inline-block;
    margin: 4px;
}
.qp-action-travel-choosetravellers .qp-action-travel-traveller-avatar {
    background-color: var(--qp-default-bg);
    border: 4px solid var(--qp-default-bg);
    border-radius: 100%;
    overflow: hidden;
    width: 64px;
    height: 64px;
    opacity: 0.7;
    transition: opacity 0.3s;
    margin: 0 auto;
}
.qp-action-travel-choosetravellers .qp-action-travel-traveller-avatar.is_selected {
    border-color: var(--qp-primary);
    opacity: 1;
}
.qp-action-travel-choosetravellers .qp-action-travel-traveller-avatar:hover {
    cursor: pointer;
    opacity: 1;
}
.qp-action-travel-choosetravellers .dialog-footer {
    padding: 40px 0 0;
    margin: 0 0 -10px;
}
</style>
