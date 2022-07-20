<template>
    <nav class="qp-forum-breadcrumbs">
        <ul>
            <li v-for="(crumb, n) in props.crumbs" :key="`crumb-${n}`" @click="goToView(crumb.view, crumb.data)">
                <span v-text="crumb.name"></span>
            </li>
        </ul>
    </nav>
</template>

<script setup>

// import { ref } from "vue";
// import i18n from "@/plugins/i18n";
import { useRouter } from "vue-router";
import { slugify } from "@/plugins/filters/slugify";

// =================================================================================== //

// const { t } = i18n.global
const router = useRouter()

// =================================================================================== //
// ===--- PROPS

const props = defineProps({
    crumbs: {
        type: Array,
        default: () => []
    }
})

// =================================================================================== //
// ===--- METHODS

const goToView = (view, data) => {
    if (view == "world") {
        router.push({name: "WorldForum", params: {
            world_pk: data.world.id,
            slug: data.world.slug
        }})
    } else if (view == "zone") {
        router.push({name: "WorldForumZone", params: {
            world_pk: data.world.id,
            slug: data.world.slug,
            zone_pk: data.zone.id,
            zone_slug: slugify(data.zone.name)
        }})
    } else if (view == "territory") {
        router.push({name: "WorldForumTerritory", params: {
            world_pk: data.world.id,
            slug: data.world.slug,
            zone_pk: data.zone.id,
            zone_slug: slugify(data.zone.name),
            territory_pk: data.territory.id,
            territory_slug: slugify(data.territory.name)
        }})
    } else if (view == "sector") {
        router.push({name: "WorldForumSector", params: {
            world_pk: data.world.id,
            slug: data.world.slug,
            zone_pk: data.zone.id,
            zone_slug: slugify(data.zone.name),
            territory_pk: data.territory.id,
            territory_slug: slugify(data.territory.name),
            sector_pk: data.sector.id,
            sector_slug: slugify(data.sector.name)
        }})
    }
}

// =================================================================================== //

</script>
