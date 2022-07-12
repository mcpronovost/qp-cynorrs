<template>
    <article v-if="props.zone" class="qp-forum-zone">
        <header class="qp-forum-header">
            <h2 class="qp-forum-header-title">
                <span v-text="props.zone.name"></span>
            </h2>
            <p class="qp-forum-header-description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam condimentum lacinia ex, commodo ultricies nisi tempor quis. Cras placerat ipsum non odio viverra auctor. Curabitur tincidunt tincidunt mi in lobortis.</p>
        </header>
        <section class="qp-forum-territories">
            <qpForumTerritory v-for="(territory, n) in props.zone.territories" :key="`territory-${n}`" :territory="territory" :singleton="props.singleton" />
        </section>
    </article>
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
    },
    singleton: {
        type: String,
        default: "zone"
    }
})

// =================================================================================== //

</script>
