<template>
    <div class="qp-vue">
        <div class="qp-container">
            <el-row :gutter="20">
                <el-col :span="24">
                    <qpCard>
                        <el-result icon="error" :title="$t('Error')" :sub-title="'...'" />
                    </qpCard>
                </el-col>
                <el-col :span="24">
                    <qpCard>
                        <a href="https://www.flaticon.com/free-icons/killer-whale" target="_blank" title="killer whale icons">Killer whale icons created by edt.im - Flaticon</a>
                    </qpCard>
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<script setup>

import qpCard from "@/components/basic/qpCard.vue";

</script>
