<template>
    <div id="qp-sidebar-nav">
        <el-menu router :default-active="($route && $route.params && 'slug' in $route.params) ? $route.params.slug : $route.name" :collapse="app.win.w < 1200 || app.sidebar?.collapse">
            <el-menu-item index="Home" :route="{name:'Home'}">
                <i class="mdi mdi-home"></i>
                <span v-text="$t('Home')"></span>
            </el-menu-item>
            <!---->
            <template v-for="(world, n) in player?.worldnavs">
                <el-sub-menu v-if="$route.params.slug && $route.params.slug == world.slug" :key="`world-nav-group-${n}`" :index="world.slug">
                    <template #title>
                        <i class="mdi mdi-hops"></i>
                        <span v-text="world.name"></span>
                    </template>
                    <el-menu-item disabled :index="`${world.slug}-rules`" :route="{name:'World', params: {world_pk: world.id, slug: world.slug}}">
                        <i class="mdi mdi-scale-balance"></i>
                        <span v-text="$t('Rules')"></span>
                    </el-menu-item>
                    <el-menu-item disabled :index="`${world.slug}-context`" :route="{name:'World', params: {world_pk: world.id, slug: world.slug}}">
                        <i class="mdi mdi-script-text"></i>
                        <span v-text="$t('Context')"></span>
                    </el-menu-item>
                    <el-menu-item :index="world.slug" :route="{name:'WorldForum', params: {world_pk: world.id, slug: world.slug}}">
                        <i class="mdi mdi-forum-outline"></i>
                        <span v-text="$t('Forum')"></span>
                    </el-menu-item>
                    <el-menu-item disabled :index="`${world.slug}-community`" :route="{name:'World', params: {world_pk: world.id, slug: world.slug}}">
                        <i class="mdi mdi-account-group"></i>
                        <span v-text="$t('Community')"></span>
                    </el-menu-item>
                </el-sub-menu>
                <el-menu-item v-else :key="`world-nav-${n}`" :index="world.slug" :route="{name:'WorldForum', params: {world_pk: world.id, slug: world.slug}}">
                    <i class="mdi mdi-hops"></i>
                    <span v-text="world.name"></span>
                </el-menu-item>
            </template>
            <!---->
        </el-menu>
    </div>
</template>

<script setup>

import { computed } from "vue";
import { useStore } from "vuex";

// =================================================================================== //
// ===--- STORE

const store = useStore()
const app = computed(() => store.getters.app)
const player = computed(() => store.getters.player)

// =================================================================================== //

</script>

<style scoped>
    #qp-sidebar-nav i.mdi {
        border-radius: 6px;
        color: var(--qp-app-sidebar-txt);
        font-size: 24px;
        line-height: 32px;
        text-align: center;
        display: inline-block;
        width: 32px;
        height: 32px;
        padding: 0;
        margin: 0 12px 3px 0;
    }
    #qp-sidebar-nav span {
        color: var(--qp-app-sidebar-txt);
        font-size: 14px;
        font-weight: 500;
        line-height: 120%;
        display: block;
        padding: 0;
        margin: 0;
    }
    #qp-sidebar-nav .el-menu-item.is-active i.mdi {
        color: var(--qp-app-sidebar-accent);
    }
    #qp-sidebar-nav .el-menu-item.is-active span {
        color: var(--qp-app-sidebar-accent);
    }
    #qp-sidebar-nav .el-menu-item:not(.is-disabled):hover i.mdi,
    #qp-sidebar-nav .el-menu-item:not(.is-disabled):hover span,
    #qp-sidebar-nav .el-sub-menu__title:not(.is-disabled):hover i.mdi,
    #qp-sidebar-nav .el-sub-menu__title:not(.is-disabled):hover span {
        opacity: 0.7;
    }
    #qp-sidebar-nav .el-menu-item-group .el-menu-item span {
        display: inline-block;
        padding: 0;
    }
    @media (max-width: 1199px) {
        #qp-sidebar-nav span {
            display: none;
        }
    }
</style>

<style>
    #qp-sidebar-nav .el-icon.el-sub-menu__icon-arrow {
        color: var(--qp-app-sidebar-txt);
    }
    @media (max-width: 1199px) {
        #qp-sidebar-nav > .el-menu {
            margin: 0 auto;
        }
        #qp-sidebar-nav > ul > li {
            justify-content:center;
            padding: 0;
        }
        #qp-sidebar-nav > ul > li > i.mdi {
            font-size: 32px!important;
            margin: 0 auto!important;
        }
        #qp-sidebar-nav .el-icon.el-sub-menu__icon-arrow {
            display: none;
        }
    }
</style>