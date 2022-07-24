<template>
    <footer class="qp-forum-footer">
        <el-row align="middle">
            <el-col :span="24" :sm="12">
                <qpForumBreadcrumbs v-if="props.crumbs?.length" :crumbs="props.crumbs" />
            </el-col>
            <el-col :span="24" :sm="12">
                <div class="qp-forum-footer-buttons">
                    <el-button v-if="showBtnChapter" @click="$emit('openNewChapter')">
                        <span v-text="$t('NewChapter')"></span>
                    </el-button>
                    <el-button v-if="showBtnReply" type="primary" @click="$emit('openNewReply')">
                        <span v-text="$t('ToReply')"></span>
                    </el-button>
                </div>
            </el-col>
        </el-row>
    </footer>
</template>

<script setup>

import qpForumBreadcrumbs from "@/components/forum/core/qpBreadcrumbs.vue";

const props = defineProps({
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
.qp-forum-footer {
    padding: 0;
}
.qp-forum-footer-buttons {
    text-align: right;
}
@media (max-width: 767px) {
    .qp-forum-footer-buttons {
        text-align: left;
    }
}
</style>
