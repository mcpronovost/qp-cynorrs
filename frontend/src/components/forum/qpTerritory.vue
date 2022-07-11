<template>
    <div v-if="props.territory" class="qp-forum-territory">
        <header class="qp-forum-header">
            <h2>
                <span v-text="props.territory.name"></span>
            </h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam condimentum lacinia ex, commodo ultricies nisi tempor quis. Cras placerat ipsum non odio viverra auctor. Curabitur tincidunt tincidunt mi in lobortis.</p>
        </header>
        <div v-for="(sector, n) in props.territory.sectors" :key="`sector-${n}`">
            <qpForumSector :sector="sector" />
        </div>
    </div>
</template>

<script setup>

// import { ref } from "vue";
// import i18n from "@/plugins/i18n";
import qpForumSector from "@/components/forum/qpSector.vue";

// const { t } = i18n.global

// =================================================================================== //
// ===--- PROPS

const props = defineProps({
    territory: {
        type: Object,
        default: () => {}
    }
})

// =================================================================================== //

</script>
