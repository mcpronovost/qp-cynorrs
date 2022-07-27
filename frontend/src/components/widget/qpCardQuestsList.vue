<template>
    <qpCard h="auto">
        <template #header>
            <span v-text="$t('Quests')"></span>
        </template>
        <ul class="qp-quests-list">
            <li class="qp-quests-item">
                <div class="qp-quests-item-icon">
                    <el-icon class="mdi mdi-leaf" />
                </div>
                <div class="qp-quests-item-text">
                    <p class="qp-quests-item-title" v-text="'Récolter des plantes'"></p>
                    <p class="qp-quests-item-description" v-text="'Parcourir les alentours pour trouver des plantes utiles.'"></p>
                </div>
                <div class="qp-quests-item-progress">
                    <el-progress :percentage="50" :stroke-width="4" :show-text="false" />
                </div>
            </li>
            <li class="qp-quests-item">
                <div class="qp-quests-item-icon">
                    <el-icon class="mdi mdi-sword" />
                </div>
                <div class="qp-quests-item-text">
                    <p class="qp-quests-item-title" v-text="'Problème de vermine'"></p>
                    <p class="qp-quests-item-description" v-text="'Éliminer les créatures qui ont envahi la région et détruisent les récoltes.'"></p>
                </div>
                <div class="qp-quests-item-progress">
                    <el-progress :percentage="50" :stroke-width="4" :show-text="false" />
                </div>
            </li>
        </ul>
        <el-button size="small">
            <span v-text="$t('SeeAllQuests')"></span>
        </el-button>
    </qpCard>
</template>

<script setup>

import qpCard from "@/components/basic/qpCard.vue";

</script>

<style scoped>
.qp-quests-list {
    text-align: left;
    list-style: none;
    padding: 0 0 12px;
    margin: 0;
}
.qp-quests-item {
    list-style: none;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    transition: opacity 0.3s;
    padding: 12px 0 0;
    margin: 0;
}
.qp-quests-item:hover {
    cursor: pointer;
    opacity: 0.6;
}
.qp-quests-item-icon {
    color: var(--qp-default-txt);
    font-size: 32px;
    line-height: 120%;
    flex: 1 1 48px;
}
.qp-quests-item-text {
    flex: 1 1 calc(100% - 48px);
}
.qp-quests-item-title {
    color: var(--qp-default-txt);
    font-weight: 600;
    padding: 0;
    margin: 0 0 6px;
}
.qp-quests-item-description {
    color: var(--qp-default-txt);
    font-size: 12px;
    line-height: 150%;
    opacity: 0.6;
    padding: 0;
    margin: 0;
}
.qp-quests-item-progress {
    flex: 1 1 100%;
    padding: 22px 0 12px;
}
</style>
