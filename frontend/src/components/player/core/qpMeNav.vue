<template>
    <nav class="qp-menav">
        <el-collapse accordion>
            <el-collapse-item name="general">
                <template #title>
                    <div @click="$emit('goto', 'general')">
                        <div class="qp-menav-icon">
                            <el-icon class="mdi mdi-account-outline" />
                        </div>
                        <div class="qp-menav-text">
                            <span class="qp-menav-title" v-text="$t('GeneralInformations')"></span>
                            <span class="qp-menav-caption" v-text="$t('NameDescriptionVisibilityAndMore')"></span>
                        </div>
                    </div>
                </template>
                <div>
                    (à venir)
                </div>
            </el-collapse-item>
            <el-collapse-item name="forum">
                <template #title>
                    <div @click="$emit('goto', 'forum')">
                        <div class="qp-menav-icon">
                            <el-icon class="mdi mdi-forum-outline" />
                        </div>
                        <div class="qp-menav-text">
                            <span class="qp-menav-title" v-text="$t('Forum')"></span>
                            <span class="qp-menav-caption" v-text="$t('ZonesTerritoriesSectorsAndSettings')"></span>
                        </div>
                    </div>
                </template>
                <ul>
                    <li>
                        <span v-text="$t('Settings')"></span>
                    </li>
                    <li>
                        <span v-text="$t('Settings')"></span>
                    </li>
                </ul>
            </el-collapse-item>
            <el-collapse-item name="style">
                <template #title>
                    <div @click="$emit('goto', 'style')">
                        <div class="qp-menav-icon">
                            <el-icon class="mdi mdi-brush-variant" />
                        </div>
                        <div class="qp-menav-text">
                            <span class="qp-menav-title" v-text="$t('Style')"></span>
                            <span class="qp-menav-caption" v-text="$t('ColoursAndCustomStylesheet')"></span>
                        </div>
                    </div>
                </template>
                <div>
                    (à venir)
                </div>
            </el-collapse-item>
        </el-collapse>
    </nav>
</template>

<script setup>

</script>

<style scoped>

</style>
