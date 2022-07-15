<template>
    <article v-if="props.sector" class="qp-forum-sector">
        <div class="qp-forum-sector-inner">
            <header class="qp-forum-header">
                <h2 class="qp-forum-header-title">
                    <span v-text="props.sector.name"></span>
                </h2>
                <p class="qp-forum-header-description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam condimentum lacinia ex, commodo ultricies nisi tempor quis. Cras placerat ipsum non odio viverra auctor. Curabitur tincidunt tincidunt mi in lobortis.</p>
            </header>
        </div>
    </article>
</template>

<script setup>

// import { ref } from "vue";
// import i18n from "@/plugins/i18n";
// import qpActionTravel from "@/components/action/qpTravel.vue";

// const { t } = i18n.global

// =================================================================================== //
// ===--- PROPS

const props = defineProps({
    sector: {
        type: Object,
        default: () => {}
    },
    singleton: {
        type: String,
        default: "sector"
    }
})

// =================================================================================== //

</script>
