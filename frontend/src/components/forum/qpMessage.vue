<template>
    <article v-if="props.message" :id="`m${props.message.id}`" class="qp-forum-message">
        <div class="qp-forum-message-inner">
            <header class="qp-forum-header">
                <div class="qp-forum-header-profile">
                    <div class="qp-forum-header-profile-banner">
                        <el-image v-if="props.message.author.avatar" :src="props.message.author.avatar" fit="cover">
                            <template #error>
                                <div class="image-slot"></div>
                            </template>
                        </el-image>
                    </div>
                    <div class="qp-forum-header-profile-avatar">
                        <el-avatar :src="props.message.author.avatar">
                            <span v-text="props.message.author.initials"></span>
                        </el-avatar>
                    </div>
                    <div class="qp-forum-header-profile-infos">
                        <div class="qp-forum-header-profile-name">
                            <span v-text="props.message.author.name"></span>
                        </div>
                        <div class="qp-forum-header-profile-date">
                            <span v-text="datetostr(props.message.created_at)"></span>
                        </div>
                    </div>
                </div>
            </header>
            <div class="qp-forum-message-text">
                <div class="qp-forum-message-text-inner">
                    <div v-html="qpcode(props.message.text)"></div>
                </div>
            </div>
        </div>
    </article>
</template>

<script setup>

import { datetostr } from "@/plugins/filters/datetostr";
import { qpcode } from "@/plugins/filters/qpcode";

const props = defineProps({
    world: {
        type: Object,
        default: () => {}
    },
    chapter: {
        type: Object,
        default: () => {}
    },
    message: {
        type: Object,
        default: () => {}
    }
})

</script>

<style scoped>
.qp-forum-message {
    padding: 12px;
}
.qp-forum-message-inner {
    background-color: var(--qp-base);
    border-radius: 4px;
    box-shadow: 0 0 3px rgb(0, 0, 0, 4%);
    text-align: center;
    overflow: hidden;
    align-content: center;
    justify-content: center;
    height: 100%;
    padding: 0;
}
/* ===--- HEADER ---=== */
.qp-forum-header {
    padding: 0;
}
/* =- profile */
.qp-forum-header-profile {
    text-align: center;
    min-height: 250px;
    position: relative;
    margin: 0;
}
.qp-forum-header-profile-banner  {
    background-color: var(--qp-secondary);
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    overflow: hidden;
    height: 160px;
    margin: 0;
}
.qp-forum-header-profile-banner .el-image {
    width: 100%;
    height: 100%;
    opacity: 0.6;
    transform: scale(1.1);
    filter: blur(3px);
}
.qp-forum-header-profile-avatar {
    background-color: var(--qp-secondary);
    border: 6px solid var(--qp-base);
    border-radius: 100%;
    overflow: hidden;
    width: 150px;
    height: 150px;
    position: absolute;
    top: 80px;
    left: 0;
    right: 0;
    margin: 0 auto;
}
.qp-forum-header-profile-avatar .el-avatar {
    font-size: 24px;
    line-height: 100%;
    width: 100%;
    height: 100%;
}
/* =- infos */
.qp-forum-header-profile-infos {
    text-align: center;
    padding: 86px 32px 12px;
}
.qp-forum-header-profile-name {
    font-family: "Quicksand", sans-serif;
    font-size: 28px;
    line-height: 120%;
    margin: 0 0 12px;
}
.qp-forum-header-profile-date {
    font-family: "Roboto Condensed", sans-serif;
    font-size: 14px;
    line-height: 120%;
    opacity: 0.6;
    margin: 0 0 0 1px;
}
/* ===--- TEXT ---=== */
.qp-forum-message-text {
    padding: 24px 32px 64px;
}
.qp-forum-message-text-inner {
    font-family: "Poppins", sans-serif;
    font-size: 18px;
    line-height: 200%;
    text-align: justify;
    max-width: 640px;
    padding: 0;
    margin: 0 auto;
}
</style>
