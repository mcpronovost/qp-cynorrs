<template>
    <div id="qp-sidebar-nav">
        <el-menu router :collapse="app.win.w < 1200">
            <el-menu-item index="1" :route="{name:'Home'}">
                <i class="mdi mdi-home"></i>
                <span v-text="'Home'"></span>
            </el-menu-item>
            <el-menu-item index="2" :route="{name:'About'}">
                <i class="mdi mdi-hops"></i>
                <span v-text="'About'"></span>
            </el-menu-item>
            <el-sub-menu index="3">
                <template #title>
                    <i class="mdi mdi-bookshelf"></i>
                    <span>Navigator One</span>
                </template>
                <el-menu-item index="1-1">
                    <span v-text="'item one'"></span>
                </el-menu-item>
                <el-menu-item index="1-2">
                    <span v-text="'item two'"></span>
                </el-menu-item>
                <el-sub-menu index="8">
                    <template #title>
                        <span>Navigator two</span>
                    </template>
                    <el-menu-item index="1-1">
                        <span v-text="'item one'"></span>
                    </el-menu-item>
                    <el-menu-item index="1-2">
                        <span v-text="'item two'"></span>
                    </el-menu-item>
                </el-sub-menu>
            </el-sub-menu>
            <el-sub-menu index="4">
                <template #title>
                    <i class="mdi mdi-home"></i>
                    <span>Navigator One</span>
                </template>
                <el-menu-item-group title="Group One">
                    <el-menu-item index="1-1">item one</el-menu-item>
                    <el-menu-item index="1-2">item one</el-menu-item>
                </el-menu-item-group>
                <el-menu-item-group title="Group Two">
                    <el-menu-item index="1-3">item three</el-menu-item>
                </el-menu-item-group>
                <el-sub-menu index="1-4">
                    <template #title>item four</template>
                    <el-menu-item index="1-4-1">item one</el-menu-item>
                </el-sub-menu>
            </el-sub-menu>
            <el-sub-menu index="5">
                <template #title>
                    <i class="mdi mdi-home"></i>
                    <span>Navigator One</span>
                </template>
                <el-menu-item-group title="Group One">
                    <el-menu-item index="1-1">item one</el-menu-item>
                    <el-menu-item index="1-2">item one</el-menu-item>
                </el-menu-item-group>
                <el-menu-item-group title="Group Two">
                    <el-menu-item index="1-3">item three</el-menu-item>
                </el-menu-item-group>
                <el-sub-menu index="1-4">
                    <template #title>item four</template>
                    <el-menu-item index="1-4-1">item one</el-menu-item>
                </el-sub-menu>
            </el-sub-menu>
        </el-menu>
    </div>
</template>

<script>
    import { mapGetters } from "vuex";
    export default {
        name: "qpSidebar",
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
    #qp-sidebar-nav i.mdi {
        border-radius: 6px;
        color: var(--qp-secondary);
        font-size: 24px;
        line-height: 32px;
        text-align: center;
        display: inline-block;
        width: 32px;
        height: 32px;
        padding: 0;
        margin: 0 12px 3px 0;
    }
    #qp-sidebar-nav span {
        color: var(--qp-secondary);
        font-size: 14px;
        font-weight: 500;
        line-height: 120%;
        display: block;
        padding: 0;
        margin: 0;
    }
    #qp-sidebar-nav .el-menu-item.is-active i.mdi {
        color: var(--qp-primary);
    }
    #qp-sidebar-nav .el-menu-item.is-active span {
        color: var(--qp-primary);
    }
    #qp-sidebar-nav .el-menu-item-group .el-menu-item span {
        display: inline-block;
        padding: 0;
    }
    @media (max-width: 1199px) {
        #qp-sidebar-nav span {
            display: none;
        }
    }
</style>

<style>
    #qp-sidebar-nav .el-icon.el-sub-menu__icon-arrow {
        color: var(--qp-secondary);
    }
    @media (max-width: 1199px) {
        #qp-sidebar-nav .el-icon.el-sub-menu__icon-arrow {
            display: none;
        }
    }
</style>