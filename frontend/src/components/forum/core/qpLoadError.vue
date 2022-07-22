<template>
    <div>

        <div v-if="props.isLoading">
            <div class="qp-container">
                <div v-loading="props.isLoading" element-loading-background="transparent" style="height:60vh"></div>
            </div>
        </div>

        <div v-else-if="props.hasError">
            <div class="qp-container">
                <qpCard h="auto">
                    <el-result icon="error" :title="$t('Error')" :sub-title="props.hasError" />
                </qpCard>
            </div>
        </div>

    </div>
</template>

<script setup>

import qpCard from "@/components/basic/qpCard.vue";

const props = defineProps({
    isLoading: {
        type: Boolean,
        default: true
    },
    hasError: {
        type: String,
        default: null
    }
})

</script>
