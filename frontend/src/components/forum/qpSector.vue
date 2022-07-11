<template>
    <div v-if="props.sector" class="qp-forum-sector">
        <h3>
            <span v-text="props.sector.name"></span>
        </h3>
        <qpActionTravel :sector="props.sector.id" />
    </div>
</template>

<script setup>

// import { ref } from "vue";
// import i18n from "@/plugins/i18n";
import qpActionTravel from "@/components/action/qpTravel.vue";

// const { t } = i18n.global

// =================================================================================== //
// ===--- PROPS

const props = defineProps({
    sector: {
        type: Object,
        default: () => {}
    }
})

// =================================================================================== //

</script>
