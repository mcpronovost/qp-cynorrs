<template>
    <div class="qp-vue qp-forum qp-singleton-zone">

        <div v-if="!isLoading && !hasError && zone">
            <div class="qp-container">
                <section class="qp-forum-zones">
                    <qpForumZone :world="props.world" :zone="zone" :singleton="'zone'" />
                </section>
            </div>
        </div>

        <qpForumLoadError v-else :isloading="isLoading" :hasError="hasError" />

    </div>
</template>

<script setup>

import { computed, onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import { useStore } from "vuex";
import { API } from "@/main.js";
import i18n from "@/plugins/i18n";

import qpForumZone from "@/components/forum/qpZone.vue";
import qpForumLoadError from "@/components/forum/qpLoadError.vue";

const { t } = i18n.global

const route = useRoute()
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
    initForumZone()
})

const zone = ref(null)

const initForumZone = async () => {
    isLoading.value = true
    hasError.value = null
    // ===---
    try {
        let response = await fetch(`${API}/worlds/zones/${route.params.zone_pk}/`, {
            method: "GET",
            headers: {"Authorization": rat.value}
        })
        let r = await response.json()
        if (response.status === 200) {
            zone.value = r
        } else {
            throw response
        }
    } catch (e) {
        if (e.status === 403) {
            hasError.value = t("YouDoesntHaveAccessToThisZone")
        } else if (e.status === 404) {
            hasError.value = t("ThisZoneDoesntExistAnymore")
        } else {
            hasError.value = t("AnErrorOccurred")
        }
    }
    // ===---
    isLoading.value = false
}

</script>
