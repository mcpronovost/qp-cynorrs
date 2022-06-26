<template>
  <div class="qp-vue">
    <el-row :gutter="20">
        <el-col :span="24">
            <qp-card>error</qp-card>
        </el-col>
    </el-row>
  </div>
</template>

<script>
    import qpCard from "@/components/basic/qpCard.vue";
    export default {
        name: "ErrorView",
        components: {
            qpCard
        }
    }
</script>
