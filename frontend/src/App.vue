<template>
    <div id="qp-app">
        <qp-header />
        <qp-sidebar />
        <div id="qp-app-main">
            <el-scrollbar height="100%">
                <router-view :key="$route.path" />
            </el-scrollbar>
        </div>
        <qp-smallbar />
    </div>
</template>

<script>
import qpHeader from "@/components/core/qpHeader.vue";
import qpSidebar from "@/components/core/qpSidebar.vue";
import qpSmallbar from "@/components/core/qpSmallbar.vue";
export default {
    name: "App",
    components: {
        qpHeader,
        qpSidebar,
        qpSmallbar
    },
    data () {
        return {
            test: this.$route
        }
    },
    mounted () {
        let token = "fa3ab65b4e41d78422eb4964c6a8bfe3d9cf180755111617c8b6b4e01c2bbe1b"
        let half = Math.ceil(token.length / 2)
        this.$store.commit("SET_DRAT", token.slice(0, half))
        this.$store.commit("SET_FRAT", token.slice(half))
    }
};
</script>

