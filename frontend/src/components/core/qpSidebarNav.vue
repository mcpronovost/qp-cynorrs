<template>
    <div id="qp-sidebar-nav">
        <el-menu router :default-active="($route && $route.params && 'slug' in $route.params) ? $route.params.slug : $route.name" :collapse="app.win.w < 1200">
            <el-menu-item index="Home" :route="{name:'Home'}">
                <i class="mdi mdi-home"></i>
                <span v-text="$t('Home')"></span>
            </el-menu-item>
            <el-menu-item index="qalatlan" :route="{name:'World', params: {world_pk: 1, slug: 'qalatlan'}}">
                <i class="mdi mdi-hops"></i>
                <span v-text="'Qalatlán'"></span>
            </el-menu-item>
            <el-menu-item index="rhansidor" :route="{name:'World', params: {world_pk: 2, slug: 'rhansidor'}}">
                <i class="mdi mdi-hops"></i>
                <span v-text="'Rhansidor'"></span>
            </el-menu-item>
            <el-sub-menu index="3">
                <template #title>
                    <i class="mdi mdi-bookshelf"></i>
                    <span>Navigation</span>
                </template>
                <el-menu-item index="1-1">
                    <span v-text="'item one'"></span>
                </el-menu-item>
                <el-menu-item index="Profile" :route="{name:'Profile'}">
                    <span v-text="'profile'"></span>
                </el-menu-item>
                <el-sub-menu index="Profile" :route="{name:'Profile'}">
                    <template #title>
                        <span>Navigator two</span>
                    </template>
                    <el-menu-item index="1-1">
                        <span v-text="'item one'"></span>
                    </el-menu-item>
                    <el-menu-item index="1-2">
                        <span v-text="'item two'"></span>
                    </el-menu-item>
                </el-sub-menu>
            </el-sub-menu>
            <el-sub-menu index="4">
                <template #title>
                    <i class="mdi mdi-cog"></i>
                    <span>Test</span>
                </template>
                <el-menu-item-group title="Group One">
                    <el-menu-item index="1-1">item one</el-menu-item>
                    <el-menu-item index="1-2">item one</el-menu-item>
                </el-menu-item-group>
                <el-menu-item-group title="Group Two">
                    <el-menu-item index="1-3">item three</el-menu-item>
                </el-menu-item-group>
                <el-sub-menu index="1-4">
                    <template #title>item four</template>
                    <el-menu-item index="1-4-1">item one</el-menu-item>
                </el-sub-menu>
            </el-sub-menu>
            <el-sub-menu index="5">
                <template #title>
                    <i class="mdi mdi-hexagon-multiple"></i>
                    <span>En construction</span>
                </template>
                <el-menu-item-group title="Group One">
                    <el-menu-item index="1-1">item one</el-menu-item>
                    <el-menu-item index="1-2">item one</el-menu-item>
                </el-menu-item-group>
                <el-menu-item-group title="Group Two">
                    <el-menu-item index="1-3">item three</el-menu-item>
                </el-menu-item-group>
                <el-sub-menu index="1-4">
                    <template #title>item four</template>
                    <el-menu-item index="1-4-1">item one</el-menu-item>
                </el-sub-menu>
            </el-sub-menu>
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

// =================================================================================== //

</script>

<style scoped>
    #qp-sidebar-nav i.mdi {
        border-radius: 6px;
        color: var(--qp-secondary);
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
        color: var(--qp-secondary);
        font-size: 14px;
        font-weight: 500;
        line-height: 120%;
        display: block;
        padding: 0;
        margin: 0;
    }
    #qp-sidebar-nav .el-menu-item.is-active i.mdi {
        color: var(--qp-primary);
    }
    #qp-sidebar-nav .el-menu-item.is-active span {
        color: var(--qp-primary);
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
        color: var(--qp-secondary);
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