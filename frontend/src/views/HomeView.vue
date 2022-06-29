<template>
  <div class="qp-vue">
    <div class="qp-container">
        <el-row :gutter="20">
            <el-col :span="24">
                <qp-card><a href="https://www.flaticon.com/free-icons/killer-whale" target="_blank" title="killer whale icons">Killer whale icons created by edt.im - Flaticon</a></qp-card>
            </el-col>
        </el-row>
        <el-row :gutter="20">
            <el-col :md="4" class="qp-flex-column">
                <qp-card clickable bgcolor="primary" h="120px" mb="20px">
                    TRAVEL
                </qp-card>
                <qp-card>
                    blabla
                </qp-card>
            </el-col>
            <el-col :md="12" :lg="8">
                <qp-card overflow>
                    <pre>{{ $store.state }}</pre>
                </qp-card>
            </el-col>
            <el-col :md="12" :lg="8">
                <qp-card>
                    <pre>{{ $store.getters }}</pre>
                </qp-card>
            </el-col>
            <el-col :lg="4">
                <qp-card>card</qp-card>
            </el-col>
        </el-row>
    </div>
  </div>
</template>

<script>
    import qpCard from "@/components/basic/qpCard.vue";
    export default {
        name: "HomeView",
        components: {
            qpCard
        },
        mounted () {
            console.log("home")
        }
    }
</script>
