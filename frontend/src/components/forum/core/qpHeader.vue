<template>
    <header class="qp-forum-header">
        <h2 class="qp-forum-header-title">
            <span v-text="props.title"></span>
        </h2>
        <p v-if="props.description" class="qp-forum-header-description" v-text="props.description"></p>
        <hr class="qp-forum-header-divider" />
        <el-row v-if="props.crumbs?.length || showBtnChapter || showBtnReply" align="middle">
            <el-col :span="24" :sm="(showBtnChapter || showBtnReply) ? 12 : 24" style="padding-left:0;">
                <qpForumBreadcrumbs v-if="props.crumbs?.length" :crumbs="props.crumbs" />
            </el-col>
            <el-col v-if="showBtnChapter || showBtnReply" :span="24" :sm="12" style="padding-right:0;">
                <div class="qp-forum-header-buttons">
                    <el-button v-if="showBtnChapter" @click="$emit('openNewChapter')">
                        <span v-text="$t('NewChapter')"></span>
                    </el-button>
                    <el-button v-if="showBtnReply" type="primary" @click="$emit('openNewReply')">
                        <span v-text="$t('ToReply')"></span>
                    </el-button>
                </div>
            </el-col>
        </el-row>
    </header>
</template>

<script setup>

import qpForumBreadcrumbs from "@/components/forum/core/qpBreadcrumbs.vue";

const props = defineProps({
    title: {
        type: String,
        default: ""
    },
    description: {
        type: String,
        default: null
    },
    crumbs: {
        type: Object,
        default: () => {}
    },
    showBtnChapter: {
        type: Boolean,
        default: false
    },
    showBtnReply: {
        type: Boolean,
        default: false
    }
})

</script>

<style scoped>
.qp-forum-header {
    padding: 12px;
}
.qp-forum-header-title {
    font-family: "Quicksand", sans-serif;
    font-size: 52px;
    font-weight: 300;
    line-height: 120%;
    word-break: break-word;
    padding: 0 15% 12px 0;
    margin: 0;
}
.qp-forum-header-description {
    color: var(--qp-tertiary);
    font-size: 14px;
    font-weight: 400;
    line-height: 150%;
    letter-spacing: 1px;
    position: relative;
    padding: 0 30% 12px 2px;
    margin: 0;
}
.qp-forum-header-divider {
    background-color: var(--qp-primary);
    border: none;
    display: block;
    width: 64px;
    height: 2px;
    margin: 12px auto 12px 2px;
}
.qp-forum-header-buttons {
    text-align: right;
}
@media (max-width: 767px) {
    .qp-forum-header-buttons {
        text-align: left;
    }
}
@media (max-width: 1199px) {
    .qp-forum-header h2,
    .qp-forum-header p {
        padding-right: 0;
    }
}
</style>

<style>
.qp-forum-header-popper.el-popper.el-popover {
    word-break: break-word;
    min-width: 300px;
}
</style>
