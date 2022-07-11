<template>
    <div id="qp-app-smallbar">
        <el-scrollbar height="100%">
            <div id="qp-smallbar-inner">
                <div v-for="(hero, n) in heros" :key="`hero-${n}`" class="qp-smallbar-hero">
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

// =================================================================================== //
// ===--- STORE

const store = useStore()
const heros = computed(() => store.getters.heros)

// =================================================================================== //

</script>

<style scoped>
    #qp-app-smallbar {
        background-color: var(--qp-base);
        box-shadow: 0 0 3px rgba(67, 82, 89, 0.04);
        box-sizing: border-box;
        vertical-align: top;
        display: inline-block;
        height: calc(100vh - 64px);
        width: 64px;
    }
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
