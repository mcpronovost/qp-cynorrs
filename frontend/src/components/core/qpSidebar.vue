<template>
    <div id="qp-app-sidebar">
        <el-scrollbar height="100%">
            <div id="qp-sibebar-inner">
                <div id="qp-sibebar-main">
                    <qp-sidebar-profile />
                    <qp-sidebar-nav />
                </div>
                <div id="qp-sidebar-footer">
                    <span v-html="$i18n.t('TextCopyrights')"></span>
                </div>
            </div>
        </el-scrollbar>
    </div>
</template>

<script>
    import { mapGetters } from "vuex";
    import qpSidebarProfile from "@/components/core/qpSidebarProfile.vue";
    import qpSidebarNav from "@/components/core/qpSidebarNav.vue";
    export default {
        name: "qpSidebar",
        components: {
            qpSidebarProfile,
            qpSidebarNav
        },
        data () {
            return {
            }
        },
        computed: {
            ...mapGetters([
                "app"
            ])
        },
        methods: {
            clickMenu (e) {
                console.log(e)
            }
        }
    }
</script>

<style scoped>
    #qp-app-sidebar {
        background-color: var(--qp-base);
        box-shadow: 0 0 3px rgba(67, 82, 89, 0.04);
        box-sizing: border-box;
        display: inline-block;
        vertical-align: top;
        height: calc(100vh - 64px);
        width: 300px;
    }
    #qp-sibebar-inner {
        display: flex;
        flex-direction: column;
        height: calc(100vh - 64px);
    }
    #qp-sibebar-main {
        flex: 1 1 auto;
    }
    #qp-sidebar-footer {
        color: var(--qp-secondary);
        font-size: 12px;
        line-height: 120%;
        text-align: center;
        flex: 0 0 auto;
        padding: 12px;
    }
    @media (max-width: 1199px) {
        #qp-app-sidebar {
            width: 64px;
        }
    }
</style>
