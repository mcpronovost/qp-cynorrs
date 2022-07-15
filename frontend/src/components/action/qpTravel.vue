<template>
    <div class="qp-action-travel">
        <el-button @click="doStartsTravel()">
            <span v-text="`voyager ici : ${props.sector}`"></span>
        </el-button>
        <!---->
        <el-dialog v-model="isShowTravel" :title="titleTravel" center destroy-on-close>
            <qpActionTravelChooseTravellers v-if="step == 'choosetravellers'" @update="updateTravellers" @step="goToStep" @close="closeTravel()" />
            <qpActionTravelArrive v-else-if="step == 'arrive'" :travellers="listTravellers" :sector="props.sector" @close="closeTravel()" />
        </el-dialog>
        <!---->
    </div>
</template>

<script setup>

import { ref } from "vue";
import i18n from "@/plugins/i18n";
import qpActionTravelChooseTravellers from "@/components/action/qpTravelChooseTravellers";
import qpActionTravelArrive from "@/components/action/qpTravelArrive";

const { t } = i18n.global

// =================================================================================== //
// ===--- PROPS

const props = defineProps({
    sector: {
        type: Number,
        default: null
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
