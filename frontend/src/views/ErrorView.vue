<template>
  <div class="qp-vue">
    <el-row :gutter="20">
        <el-col :span="24">
            <qp-card>error</qp-card>
        </el-col>
        <el-col :span="24">
            <qp-card><a href="https://www.flaticon.com/free-icons/killer-whale" target="_blank" title="killer whale icons">Killer whale icons created by edt.im - Flaticon</a></qp-card>
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
