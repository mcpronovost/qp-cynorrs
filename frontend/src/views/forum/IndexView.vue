<template>
    <div class="qp-vue qp-forum qp-singleton-index">

        <div v-if="!isLoading && !hasError && forum">
            <div class="qp-container">
                <section v-if="$route.name == 'WorldForum'" class="qp-forum-zones">
                    <qpForumZone v-for="(z, n) in forum.zones" :key="`zones-${n}`" :world="props.world" :zone="z" />
                </section>
            </div>
        </div>

        <qpForumLoadError v-else :isloading="isLoading" :hasError="hasError" />

    </div>
</template>

<script setup>

import { computed, onMounted, ref } from "vue";
import { useStore } from "vuex";
import { API } from "@/main.js";
import i18n from "@/plugins/i18n";

import qpForumZone from "@/components/forum/qpZone.vue";
import qpForumLoadError from "@/components/forum/qpLoadError.vue";

const { t } = i18n.global

const store = useStore()
const rat = computed(() => store.getters.rat)

const props = defineProps({
    world: {
        type: Object,
        default: () => {}
    }
})

const isLoading = ref(true)
const hasError = ref(null)

onMounted(() => {
    initForumIndex()
})

const forum = ref(null)

const initForumIndex = async () => {
    isLoading.value = true
    hasError.value = null
    // ===---
    try {
        let response = await fetch(`${API}/worlds/forums/${props.world.forum.id}/`, {
            method: "GET",
            headers: {"Authorization": rat.value}
        })
        let r = await response.json()
        if (response.status === 200) {
            forum.value = r
        } else {
            throw response
        }
    } catch (e) {
        if (e.status === 403) {
            hasError.value = t("YouDoesntHaveAccessToThisForum")
        } else if (e.status === 404) {
            hasError.value = t("ThisForumDoesntExistAnymore")
        } else {
            hasError.value = t("AnErrorOccurred")
        }
    }
    // ===---
    isLoading.value = false
}

</script>
