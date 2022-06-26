<template>
    <div id="qp-app-sidebar">
        <el-scrollbar height="100%">
            <div id="qp-sidebar-profile">
                <div id="qp-sidebar-banner">
                    <el-image :src="banner" fit="cover">
                        <template #error>
                            <div class="image-slot"></div>
                        </template>
                    </el-image>
                </div>
                <div id="qp-sidebar-avatar">
                    <el-image :src="avatar" fit="cover">
                        <template #error>
                            <div class="image-slot"></div>
                        </template>
                    </el-image>
                </div>
                <div id="qp-sidebar-name">
                    <h2>
                        <span v-text="name"></span>
                    </h2>
                </div>
                <div id="qp-sidebar-title">
                    <p>
                        <span v-text="title"></span>
                    </p>
                </div>
            </div>
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
        </el-scrollbar>
    </div>
</template>

<script>
    import { mapGetters } from "vuex";
    export default {
        name: "qpSidebar",
        data () {
            return {
                banner: "",
                avatar: "",
                name: "M-C Pronovost",
                title: "Qui ne fait que passer"
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
        vertical-align: top;
        display: inline-block;
        height: calc(100vh - 64px);
        width: 300px;
    }
    #qp-sidebar-profile {
        text-align: center;
        min-height: 240px;
        position: relative;
        margin: 0 0 32px;
    }
    #qp-sidebar-banner .el-image,
    #qp-sidebar-avatar .el-image {
        width: 100%;
        height: 100%;
    }
    #qp-sidebar-banner {
        background-color: var(--qp-secondary);
        height: 120px;
        margin: 0 0 96px;
    }
    #qp-sidebar-avatar {
        background-color: var(--qp-secondary);
        border: 8px solid var(--qp-base);
        border-radius: 100%;
        width: 120px;
        height: 120px;
        position: absolute;
        top: 60px;
        left: 0;
        right: 0;
        margin: 0 auto;
    }
    #qp-sidebar-name h2 {
        color: var(--qp-primary);
        font-size: 18px;
        font-weight: 500;
        line-height: 120%;
        padding: 0;
        margin: 0 0 6px;
    }
    #qp-sidebar-title p {
        color: var(--qp-secondary);
        font-size: 14px;
        font-weight: 400;
        font-style: italic;
        line-height: 120%;
        letter-spacing: 1px;
        padding: 0;
        margin: 0;
    }
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
        #qp-app-sidebar {
            width: 64px;
        }
        #qp-sidebar-profile {
            min-height: 76px;
        }
        #qp-sidebar-banner {
            height: 48px;
            margin-bottom: 48px;
        }
        #qp-sidebar-avatar {
            border-width: 4px;
            width: 48px;
            height: 48px;
            top: 18px;
        }
        #qp-sidebar-name,
        #qp-sidebar-title {
            display: none;
        }
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