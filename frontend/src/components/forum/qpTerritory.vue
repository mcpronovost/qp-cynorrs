<template>
    <article v-if="props.territory" class="qp-forum-territory" :style="`flex-basis:${territory.flexbasis};`">
        <div class="qp-forum-territory-inner">
            <header class="qp-forum-header">
                <h2 class="qp-forum-header-title" @click="goToTerritory(props.territory)">
                    <span v-text="props.territory.name"></span>
                </h2>
                <p class="qp-forum-header-description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam condimentum lacinia ex, commodo ultricies nisi tempor quis. Cras placerat ipsum non odio viverra auctor. Curabitur tincidunt tincidunt mi in lobortis.</p>
                <nav class="qp-forum-breadcrumbs" v-if="singleton == 'territory'">
                    <ul>
                        <li @click="goToWorld(props.world)">
                            <span v-text="props.world.name"></span>
                        </li>
                        <li @click="goToZone(props.zone)">
                            <span v-text="props.zone.name"></span>
                        </li>
                    </ul>
                </nav>
            </header>
            <section v-if="props.singleton == 'territory_hide'" class="qp-forum-sectors">
                <qpForumSector v-for="(sector, n) in props.territory.sectors" :key="`sector-${n}`" :sector="sector" :singleton="props.singleton" />
            </section>
            <section v-if="props.singleton == 'territory'" class="qp-forum-chapters">
                aaa
            </section>
        </div>
    </article>
</template>

<script setup>

// import { ref } from "vue";
// import i18n from "@/plugins/i18n";
import { useRouter } from "vue-router";
import { slugify } from "@/plugins/filters/slugify";
import qpForumSector from "@/components/forum/qpSector.vue";

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
// ===--- METHODS

const goToWorld = (world) => {
    router.push({name: "World", params: {
        world_pk: world.id,
        slug: world.slug
    }})
}

const goToZone = (zone) => {
    router.push({name: "WorldZone", params: {
        world_pk: props.world.id,
        slug: props.world.slug,
        zone_pk: zone.id,
        zone_slug: slugify(zone.name)
    }})
}

const goToTerritory = (territory) => {
    router.push({name: "WorldTerritory", params: {
        world_pk: props.world.id,
        slug: props.world.slug,
        zone_pk: props.zone.id,
        zone_slug: slugify(props.zone.name),
        territory_pk: territory.id,
        territory_slug: slugify(territory.name)
    }})
}

// =================================================================================== //

</script>
