<template>
    <div id="qp-app-header">
        <el-row :gutter="20">
            <el-col :span="24">
                <div id="qp-header-logo">
                    <img :src="logo" alt ="" />
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    export default {
        name: "qpHeader",
        data () {
            return {
                logo: "/static/ico/favicon-180.png"
            }
        }
    }
</script>

<style scoped>
    #qp-app-header {
        background-color: var(--qp-primary);
        box-shadow: 0 0 3px rgba(67, 82, 89, 0.04);
        box-sizing: border-box;
        height: 64px;
        position: relative;
        z-index: 1;
    }
    #qp-header-logo {
        width: 48px;
        height: 48px;
    }
    #qp-header-logo .el-image {
        width: 100%;
        height: 100%;
    }
</style>
