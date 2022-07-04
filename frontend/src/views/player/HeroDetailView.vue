<template>
  <div class="qp-vue">
    <div class="qp-container">
      <el-row :gutter="20">
        <el-col :span="24">
          <qp-card>
            
          </qp-card>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
  import qpCard from "@/components/basic/qpCard.vue";
  export default {
    name: "HeroDetailView",
    components: {
      qpCard
    }
  }
</script>
