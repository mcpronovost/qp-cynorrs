<template>
    <div id="qp-app-header">
        <el-row :gutter="20" align="middle">
            <el-col :span="11" :lg="8">
                <div id="qp-header-logo">
                    <div id="qp-header-logo-img">
                        <el-image :src="logo" fit="cover">
                            <template #error>
                                <div class="image-slot"></div>
                            </template>
                        </el-image>
                    </div>
                    <div id="qp-header-logo-title">
                        <span v-text="'Cynorrs'"></span>
                    </div>
                </div>
            </el-col>
            <el-col :span="2" :lg="8" class="text-center">
                <div id="qp-header-titlse">
                    <span v-text="'Cynorrs'"></span>
                </div>
            </el-col>
            <el-col :span="11" :lg="8">
                <div id="qp-header-menu">
                    <span v-text="'Cynorrs'"></span>
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
                logo: "/static/ico/logo-square-trans.png"
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
        display: inline-block;
        transition: filter 0.4s;
    }
    #qp-header-logo:hover {
        cursor: pointer;
        filter: blur(0.5px) brightness(1.1);
    }
    #qp-header-logo-img {
        background-color: #505f65;
        border-radius: 100%;
        overflow: hidden;
        vertical-align: middle;
        display: inline-block;
        width: 42px;
        height: 42px;
        margin: 0 12px;
    }
    #qp-header-logo-img .el-image {
        width: 100%;
        height: 100%;
    }
    #qp-header-logo-title {
        color: var(--qp-bg);
        font-family: "Indie Flower", sans-serif;
        font-size: 32px;
        line-height: 120%;
        vertical-align: middle;
        display: inline-block;
    }
    @media (max-width: 768px) {
        #qp-header-logo-title {
            display: none;
        }
    }
</style>
