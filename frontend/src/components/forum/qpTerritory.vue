<template>
    <article v-if="props.territory" class="qp-forum-territory" :style="`flex-basis:${territory.flexbasis};`">
        <div class="qp-forum-territory-inner">
            <header class="qp-forum-header">
                <h2 class="qp-forum-header-title">
                    <span v-text="props.territory.name"></span>
                </h2>
                <p class="qp-forum-header-description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam condimentum lacinia ex, commodo ultricies nisi tempor quis. Cras placerat ipsum non odio viverra auctor. Curabitur tincidunt tincidunt mi in lobortis.</p>
            </header>
            <section v-if="props.singleton == 'territory'" class="qp-forum-sectors">
                <qpForumSector v-for="(sector, n) in props.territory.sectors" :key="`sector-${n}`" :sector="sector" :singleton="props.singleton" />
            </section>
        </div>
    </article>
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
    },
    singleton: {
        type: String,
        default: "territory"
    }
})

// =================================================================================== //

</script>
