<template>
    <div v-if="app.win.w > 767" id="qp-app-smallbar">
        <el-scrollbar height="100%">
            <div v-if="rat" id="qp-smallbar-inner">
                <div v-for="(hero, n) in listHeros" :key="`hero-${n}`" class="qp-smallbar-hero" @click="goToCharacter(hero.id)">
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
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";

const route = useRoute()
const router = useRouter()
const store = useStore()
const app = computed(() => store.getters.app)
const rat = computed(() => store.getters.rat)
const heros = computed(() => store.getters.heros)

const listHeros = computed(() => {
    if ("slug" in route.params) {
        return heros.value.filter((obj) => {
            return obj.world?.slug == route.params.slug
        })
    }
    return heros.value
})

const goToCharacter = (id) => {
    router.push({name: "MeCharactersHerosDetail", params: {pk: id}})
}

</script>

<style scoped>
    #qp-smallbar-inner {
        padding: 12px 0;
    }
    @media (max-width: 1199px) {
        #qp-app-smallbar {
            width: 64px;
            min-width: 64px;
        }
    }
    /* ===---=== */
    .qp-smallbar-hero {
        text-align: center;
        padding: 6px;
    }
    .qp-smallbar-hero:hover {
        cursor: pointer;
    }
</style>
