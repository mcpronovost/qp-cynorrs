<template>
    <article v-if="props.zone" class="qp-forum-zone">
        <div class="qp-forum-zone-inner">
            <header class="qp-forum-header">
                <h2 class="qp-forum-header-title">
                    <span v-text="props.zone.name"></span>
                </h2>
                <p class="qp-forum-header-description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam condimentum lacinia ex, commodo ultricies nisi tempor quis. Cras placerat ipsum non odio viverra auctor. Curabitur tincidunt tincidunt mi in lobortis.</p>
                <nav class="qp-forum-breadcrumbs" v-if="singleton == 'zone'">
                    <ul>
                        <li @click="goToWorld(props.world)">
                            <span v-text="props.world.name"></span>
                        </li>
                    </ul>
                </nav>
            </header>
            <section class="qp-forum-territories">
                <qpForumTerritory v-for="(territory, n) in props.zone.territories" :key="`territory-${n}`" :world="props.world" :zone="props.zone" :territory="territory" :singleton="props.singleton" />
            </section>
        </div>
    </article>
</template>

<script setup>

// import { ref } from "vue";
// import i18n from "@/plugins/i18n";
import { useRouter } from "vue-router";
import qpForumTerritory from "@/components/forum/qpTerritory.vue";

// =================================================================================== //

// const { t } = i18n.global
const router = useRouter()

// =================================================================================== //
// ===--- PROPS

const props = defineProps({
    world: {
        type: Object,
        default: () => {}
    },
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
// ===--- METHODS

const goToWorld = (world) => {
    router.push({name: "World", params: {
        world_pk: world.id,
        slug: world.slug
    }})
}

// =================================================================================== //

</script>
