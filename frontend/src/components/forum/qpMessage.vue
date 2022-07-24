<template>
    <article v-if="props.message" :id="`m${props.message.id}`" class="qp-forum-message">
        <div v-loading="isLoadingSend" class="qp-forum-message-inner">
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
            <qpForumWritingEdit v-if="showEditMessage" :message="props.message" @close="closeEditMessage()" />
            <div v-else class="qp-forum-message-text">
                <div class="qp-forum-message-text-inner">
                    <div v-html="qpcode(props.message.text)"></div>
                </div>
            </div>
            <footer class="qp-forum-message-footer">
                <div v-if="rat && player?.id == props.message.author?.player?.id && !showEditMessage">
                    <el-tooltip :content="$t('EditMessage')" placement="bottom-end">
                        <el-button size="small" @click="openEditMessage()">
                            <el-icon class="mdi mdi-pencil" />
                        </el-button>
                    </el-tooltip>
                    <el-tooltip :content="$t('DeleteMessage')" placement="bottom-end">
                        <el-button size="small" @click="doDeleteMessage()">
                            <el-icon class="mdi mdi-close" />
                        </el-button>
                    </el-tooltip>
                </div>
            </footer>
        </div>
    </article>
</template>

<script setup>

import { computed, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import { ElNotification, ElMessageBox } from "element-plus";
import { API } from "@/main.js";
import { datetostr } from "@/plugins/filters/datetostr";
import { qpcode } from "@/plugins/filters/qpcode";
import i18n from "@/plugins/i18n";

import qpForumWritingEdit from "@/components/forum/qpWritingEdit.vue";

const { t } = i18n.global

const route = useRoute()
const router = useRouter()
const store = useStore()
const rat = computed(() => store.getters.rat)
const player = computed(() => store.getters.player)

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

const isLoadingSend = ref(false)

const doDeleteMessage = () => {
    isLoadingSend.value = true
    ElMessageBox.confirm(
        t("Areyousureyouwanttodeletethismessage"),
        t("DeleteMessage"),
        {
            confirmButtonText: t("Delete"),
            cancelButtonText: t("Cancel"),
            type: "warning"
        }
    ).then(() => {
        sendDeleteMessage()
    }).catch(() => {
        isLoadingSend.value = false
    })
}

const sendDeleteMessage = async () => {
    isLoadingSend.value = true
    // ===---
    try {
        let data = new FormData()
        data.append("id", props.message.id)
        let response = await fetch(`${API}/worlds/messages/${props.message.id}/delete/`, {
            method: "DELETE",
            headers: {"Authorization": rat.value},
            body: data
        })
        if (response.status === 204) {
            router.go(route.fullPath)
            ElNotification({
                title: t("Success"),
                message: t("MessageDeletedSuccessfully"),
                type: "success"
            })
        } else {
            ElNotification({
                title: t("Error"),
                message: t("AnErrorOccurred"),
                type: "error"
            })
            isLoadingSend.value = false
        }
    } catch (e) {
        ElNotification({
            title: t("Error"),
            message: `${t("AnErrorOccurred")} : ${e}`,
            type: "error"
        })
        isLoadingSend.value = false
    }
}

const showEditMessage = ref(false)

const openEditMessage = () => {
    showEditMessage.value = true
}

const closeEditMessage = () => {
    showEditMessage.value = false
}

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
    padding: 24px 32px;
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
/* ================================--- FOOTER ---=== */
.qp-forum-message-footer {
    text-align: right;
    padding: 0 24px 24px;
}
</style>
