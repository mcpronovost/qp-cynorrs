<template>
    <div v-if="rat" class="qp-action-travel">
        <el-button class="qp-action-travel-button" @click="doStartsTravel()">
            <span v-text="$t('Travel')"></span>
        </el-button>
        <!---->
        <el-dialog v-model="isShowTravel" :title="titleTravel" center destroy-on-close>
            <qpActionTravelChooseTravellers v-if="step == 'choosetravellers'" :world="props.territory.world" @update="updateTravellers" @step="goToStep" @close="closeTravel()" />
            <qpActionTravelArrive v-else-if="step == 'arrive'" :travellers="listTravellers" :territory="props.territory" :sector="props.sector" @close="closeTravel()" />
        </el-dialog>
        <!---->
    </div>
</template>

<script setup>

import { computed, ref } from "vue";
import { useStore } from "vuex";
import i18n from "@/plugins/i18n";
import qpActionTravelChooseTravellers from "@/components/action/qpTravelChooseTravellers";
import qpActionTravelArrive from "@/components/action/qpTravelArrive";

const { t } = i18n.global

// =================================================================================== //

const store = useStore()
const rat = computed(() => store.getters.rat)

// =================================================================================== //
// ===--- PROPS

const props = defineProps({
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

const isShowTravel = ref(false)
const titleTravel = ref(t("Travel"))
const step = ref(null)
const listTravellers = ref([])

// =================================================================================== //
// ===--- METHODS

const doStartsTravel = () => {
    goToStep("choosetravellers")
    openTravel()
}

const goToStep = (s) => {
    if (s == "choosetravellers") {
        titleTravel.value = t("ChooseTravellers")
    } else if (s == "arrive") {
        titleTravel.value = ""
    } else {
        titleTravel.value = t("Travel")
    }
    step.value = s
}

const openTravel = () => {
    listTravellers.value = []
    isShowTravel.value = true
}

const closeTravel = () => {
    isShowTravel.value = false
    listTravellers.value = []
}

const updateTravellers = (travellers) => {
    listTravellers.value = travellers
}

// =================================================================================== //

</script>
