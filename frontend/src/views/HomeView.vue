<template>
  <div class="qp-vue">
    <el-row :gutter="20">
        <el-col :span="24">
            <qp-card>card</qp-card>
        </el-col>
    </el-row>
    <el-row :gutter="20">
        <el-col :lg="8">
            <qp-card>card</qp-card>
        </el-col>
        <el-col :span="8">
            <qp-card color="primary">card</qp-card>
        </el-col>
        <el-col :span="4">
            <qp-card>card</qp-card>
        </el-col>
        <el-col :span="4">
            <qp-card>card</qp-card>
        </el-col>
    </el-row>
  </div>
</template>

<script>
    import qpCard from "@/components/core/qpCard.vue";
    export default {
        name: 'HomeView',
        components: {
            qpCard
        }
    }
</script>
