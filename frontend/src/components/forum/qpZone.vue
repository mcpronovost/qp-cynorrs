<template>
    <div v-if="props.zone" class="qp-forum-zone">
        <header v-if="false" class="qp-forum-zone-header">
            <h2>
                <span v-text="props.zone.name"></span>
            </h2>
            <p>aaa</p>
        </header>
        <div v-for="(territory, n) in props.zone.territories" :key="`territory-${n}`">
            <qpForumTerritory :territory="territory" />
        </div>
    </div>
</template>

<script setup>

// import { ref } from "vue";
// import i18n from "@/plugins/i18n";
import qpForumTerritory from "@/components/forum/qpTerritory.vue";

// const { t } = i18n.global

// =================================================================================== //
// ===--- PROPS

const props = defineProps({
    zone: {
        type: Object,
        default: () => {}
    }
})

// =================================================================================== //

</script>
