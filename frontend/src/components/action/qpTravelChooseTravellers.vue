<template>
    <div class="qp-action-travel-choosetravellers">
        <el-row v-loading="isLoading" :gutter="20" justify="center">
            <el-col v-if="!isLoading && listHeros.length" class="text-center">
                <div v-for="(traveller, n) in listHeros" :key="`traveller-${n}`" class="qp-action-travel-traveller" @click="toggleTraveller('hero', n)">
                    <el-tooltip :content="traveller.name">
                        <div :class="`qp-action-travel-traveller-avatar${traveller.is_selected ? ' is_selected':''}`">
                            <el-image v-if="traveller.avatar" :src="traveller.avatar" fit="cover">
                                <template #error>
                                    <div class="image-slot"></div>
                                </template>
                            </el-image>
                        </div>
                    </el-tooltip>
                </div>
            </el-col>
            <el-col v-else-if="!listHeros.length" class="text-center">
                <el-result style="padding-top:0;padding-bottom:0;">
                    <template #icon><i></i></template>
                    <template #sub-title>
                        <div v-text="$t('NoAvailableTravellers')"></div>
                    </template>
                </el-result>
            </el-col>
        </el-row>
        <div class="dialog-footer text-center">
            <el-button @click="closeTravel()">
                <span v-text="$t('Cancel')"></span>
            </el-button>
            <el-button :disabled="!isValidChooseTravellers" type="primary" @click="goToStep('arrive')">
                <span v-text="$t('Continue')"></span>
            </el-button>
        </div>
    </div>
</template>

<script setup>

import { computed, onMounted, ref } from "vue";
import { useStore } from "vuex";

// =================================================================================== //
// ===--- STORE

const store = useStore()
const heros = computed(() => store.getters.heros)

// =================================================================================== //
// ===--- EMIT

const emit = defineEmits(["update", "step", "close"])

// =================================================================================== //
// ===--- PROPS

const props = defineProps({
    world: {
        type: Number,
        default: null
    }
})

// =================================================================================== //
// ===--- DATA

const isLoading = ref(false)
const listHeros = ref([])

const listTravellers = computed(() => {
    let result = []
    for (let item of listHeros.value) {
        if (item.is_selected) {
            item["type"] = "hero"
            result.push(item)
        }
    }
    return result
})

const isValidChooseTravellers = computed(() => {
    if (listTravellers.value.length) {return true}
    return false
})

// =================================================================================== //
// ===--- METHODS

const initTravellers = async () => {
    isLoading.value = true
    listHeros.value = []
    // ===---
    for (const hero of heros.value) {
        if (hero.world == props.world && hero.is_can_travel) {
            listHeros.value.push(hero)
        }
    }
    // ===---
    isLoading.value = false
}
const toggleTraveller = (type_of, index) => {
    if (type_of == "hero") {
        listHeros.value[index]["is_selected"] = !listHeros.value[index]["is_selected"]
    }
    emit("update", listTravellers.value)
}
const goToStep = (step) => {
    emit("step", step)
}
const closeTravel = () => {
    emit("close")
}

// =================================================================================== //
// ===--- MOUNTED

onMounted(() => {
  initTravellers()
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
