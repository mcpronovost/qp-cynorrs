<template>
    <div v-if="world" class="qp-vue">
        <div class="qp-container">

            <div :class="`qp-forum qp-singleton-${singleton}`">
                <section class="qp-forum-zones">
                    <qpForumZone v-for="(zone, n) in world.zones" :key="`zones-${n}`" :zone="zone" :singleton="singleton" />
                </section>
            </div>

        </div>
    </div>
</template>

<script setup>

import { computed, onBeforeUnmount, onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import { useStore } from "vuex";
import { API } from "@/main.js";

import qpForumZone from "@/components/forum/qpZone.vue";

// =================================================================================== //

const route = useRoute()

const store = useStore()
const rat = computed(() => store.getters.rat)

const world = ref()
const singleton = ref("index")

// =================================================================================== //
// ===--- METHODS

const setWorld = async (worldPk) => {
    // ===---
    let r = await fetch(`${API}/worlds/${worldPk}/`, {
        method: "GET",
        headers: {"Authorization": rat}
    })
    if (r.status === 200) {
        let result = await r.json()
        world.value = result.world
        initStyle(result.world.stylesheet)
    } else {
        console.log(r)
    }
    // ===---
}

const initStyle = (stylesheet) => {
    let styletag = document.createElement("style");
    styletag.setAttribute("id", "qp-custom-style");
    styletag.innerHTML = stylesheet;
    document.head.appendChild(styletag);
}

// =================================================================================== //

onMounted(() => {
    setWorld(route.params.world_pk)
})

onBeforeUnmount(() => {
    document.getElementById("qp-custom-style").remove();
})

// =================================================================================== //

</script>
