<template>
    <nav class="qp-menav">
        <el-collapse v-model="currentTab" accordion>
            <el-collapse-item v-for="(nav, n) in props.navs" :key="`nav-${n}`" :name="nav.tab">
                <template #title>
                    <div @click="$emit('goto', nav.tab)">
                        <div class="qp-menav-icon">
                            <el-icon :class="nav.icon" />
                        </div>
                        <div class="qp-menav-text">
                            <span class="qp-menav-title" v-text="nav.title"></span>
                            <span class="qp-menav-caption" v-text="nav.caption"></span>
                        </div>
                    </div>
                </template>
                <ul>
                    <li @click="$emit('goto', nav.tab)" :class="nav.tab == tab ? 'qp-active' : ''">
                        <span v-text="$t('General')"></span>
                    </li>
                    <li v-for="(sub, nn) in nav.subs" :key="`nav-${n}-sub-${nn}`" :class="sub.tab == tab ? 'qp-active' : ''" @click="$emit('goto', sub.tab)">
                        <span v-text="sub.title"></span>
                    </li>
                </ul>
            </el-collapse-item>
        </el-collapse>
    </nav>
</template>

<script setup>
import { onMounted, ref } from "vue";
const props = defineProps({
    navs: {
        type: Array,
        default: () => []
    },
    tab: {
        type: String,
        default: ""
    }
})

const currentTab = ref("")

onMounted(() => {
    currentTab.value = props.tab
})
</script>
