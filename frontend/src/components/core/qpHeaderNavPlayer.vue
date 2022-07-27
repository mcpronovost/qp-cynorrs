<template>
    <div id="qp-header-menu-player">
        <!---->
        <el-menu v-if="!rat" router mode="horizontal" menu-trigger="click">
            <el-menu-item index="AuthLogin" :route="{name:'AuthLogin'}">
                <el-icon class="mdi mdi-power" />
                <span v-text="$t('Login')"></span>
            </el-menu-item>
            <el-menu-item index="AuthRegister" :route="{name:'AuthRegister'}">
                <el-icon class="mdi mdi-login-variant" />
                <span v-text="$t('Register')"></span>
            </el-menu-item>
        </el-menu>
        <!---->
        <el-menu v-else router mode="horizontal" menu-trigger="click" :default-active="($route && $route.name) ? $route.name : null">
            <el-menu-item disabled index="notifications">
                <el-badge :hidden="true" is-dot>
                    <el-icon class="mdi mdi-bell-outline" />
                </el-badge>
            </el-menu-item>
            <el-menu-item disabled index="messages">
                <el-badge :hidden="true" :value="123" :max="99">
                    <el-icon class="mdi mdi-email-outline" />
                </el-badge>
            </el-menu-item>
            <el-sub-menu index="1">
                <template #title>
                    <span v-text="player?.playername"></span>
                </template>
                <el-menu-item index="MeProfile" :route="{name:'MeProfile'}" :disabled="($route.name && $route.name == 'MeProfile')" class="qp-multiline">
                    <span v-text="$t('SignedInAs')"></span><br />
                    <strong v-text="player?.playername"></strong>
                </el-menu-item>
                <hr />
                <el-menu-item index="MeProfile" :route="{name:'MeProfile'}" :disabled="($route.name && $route.name == 'MeProfile')">
                    <span v-text="$t('YourProfile')"></span>
                </el-menu-item>
                <el-menu-item index="MeCharacters" :route="{name:'MeCharacters'}" :disabled="($route.name && $route.name == 'MeCharacters')">
                    <span v-text="$t('YourCharacters')"></span>
                </el-menu-item>
                <el-menu-item index="MeWorlds" :route="{name:'MeWorlds'}" :disabled="($route.name && $route.name == 'MeWorlds')">
                    <span v-text="$t('YourWorlds')"></span>
                </el-menu-item>
                <hr />
                <el-menu-item disabled index="help">
                    <span v-text="$t('Help')"></span>
                </el-menu-item>
                <el-menu-item disabled index="settings">
                    <span v-text="$t('Settings')"></span>
                </el-menu-item>
                <hr />
                <el-menu-item index="AuthLogout" :route="{name:'AuthLogout'}">
                    <span v-text="$t('Logout')"></span>
                </el-menu-item>
            </el-sub-menu>
        </el-menu>
        <!---->
    </div>
</template>

<script setup>

import { computed } from "vue";
import { useStore } from "vuex";

const store = useStore()
const rat = computed(() => store.getters.rat)
const player = computed(() => store.getters.player)

</script>

<style scoped>
    /* ===--- MENU ---=== */
    #qp-header-menu-player {
        padding: 0 6px 0 0;
    }
    #qp-header-menu-player > .el-menu {
        justify-content: flex-end;
    }
</style>
