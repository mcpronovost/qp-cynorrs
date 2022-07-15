<template>
    <div id="qp-sidebar-profile">
        <div id="qp-sidebar-banner">
            <el-image v-if="player?.banner" :src="player.banner" fit="cover">
                <template #error>
                    <div class="image-slot"></div>
                </template>
            </el-image>
        </div>
        <div id="qp-sidebar-avatar">
            <el-image v-if="player?.avatar" :src="player.avatar" fit="cover">
                <template #error>
                    <div class="image-slot"></div>
                </template>
            </el-image>
        </div>
        <div id="qp-sidebar-name">
            <h2>
                <span v-text="player?.name"></span>
            </h2>
        </div>
        <div v-if="rat" id="qp-sidebar-title">
            <p>
                <span v-text="title"></span>
            </p>
        </div>
        <div v-else>
            <el-button>
                <span v-text="$t('Login')"></span>
            </el-button>
        </div>
    </div>
</template>

<script setup>

import { computed, ref } from "vue";
import { useStore } from "vuex";

// =================================================================================== //
// ===--- STORE

const store = useStore()
const rat = computed(() => store.getters.rat)
const player = computed(() => store.getters.player)

// =================================================================================== //
// ===--- DATA

const title = ref("Qui ne fait que passer")

</script>

<style scoped>
    #qp-sidebar-profile {
        text-align: center;
        min-height: 240px;
        position: relative;
        margin: 0 0 32px;
    }
    #qp-sidebar-banner .el-image,
    #qp-sidebar-avatar .el-image {
        width: 100%;
        height: 100%;
    }
    #qp-sidebar-banner {
        background-color: var(--qp-secondary);
        height: 120px;
        margin: 0 0 96px;
    }
    #qp-sidebar-avatar {
        background-color: var(--qp-secondary);
        border: 8px solid var(--qp-base);
        border-radius: 100%;
        overflow: hidden;
        width: 120px;
        height: 120px;
        position: absolute;
        top: 60px;
        left: 0;
        right: 0;
        margin: 0 auto;
    }
    #qp-sidebar-name h2 {
        color: var(--qp-primary);
        font-family: "Oswald", sans-serif;
        font-size: 20px;
        font-weight: 500;
        line-height: 120%;
        padding: 0;
        margin: 0 0 6px;
    }
    #qp-sidebar-title p {
        color: var(--qp-secondary);
        font-size: 14px;
        font-weight: 400;
        font-style: italic;
        line-height: 120%;
        letter-spacing: 1px;
        padding: 0;
        margin: 0;
    }
    @media (max-width: 1199px) {
        #qp-sidebar-profile {
            min-height: 76px;
        }
        #qp-sidebar-banner {
            height: 48px;
            margin-bottom: 48px;
        }
        #qp-sidebar-avatar {
            border-width: 4px;
            width: 48px;
            height: 48px;
            top: 18px;
        }
        #qp-sidebar-name,
        #qp-sidebar-title {
            display: none;
        }
    }
</style>
