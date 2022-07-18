<template>
    <div id="qp-app-smallbar">
        <el-scrollbar height="100%">
            <div v-if="rat" id="qp-smallbar-inner">
                <div v-for="(hero, n) in listHeros" :key="`hero-${n}`" class="qp-smallbar-hero">
                    <el-tooltip :content="hero.name" placement="left">
                        <el-avatar :src="hero.avatar">
                            <span v-text="hero.initials"></span>
                        </el-avatar>
                    </el-tooltip>
                </div>
            </div>
        </el-scrollbar>
    </div>
</template>

<script setup>

import { computed } from "vue";
import { useStore } from "vuex";
import { useRoute } from "vue-router";

// =================================================================================== //
// ===--- STORE

const route = useRoute()

const store = useStore()
const rat = computed(() => store.getters.rat)
const heros = computed(() => store.getters.heros)

const listHeros = computed(() => {
    if ("world_pk" in route.params) {
        return heros.value.filter((obj) => {
            return obj.world == route.params.world_pk
        })
    }
    return heros.value
})

// =================================================================================== //

</script>

<style scoped>
    #qp-smallbar-inner {
        padding: 12px 0;
    }
    @media (max-width: 1199px) {
        #qp-app-smallbar {
            width: 10vw;
            min-width: 64px;
        }
    }
    /* ===---=== */
    .qp-smallbar-hero {
        text-align: center;
        padding: 6px;
    }
</style>
