<template>
    <nav class="qp-forum-breadcrumbs">
        <ul>
            <li v-for="(crumb, n) in props.crumbs" :key="`crumb-${n}`" @click="goToView(crumb.go)">
                <span v-text="crumb.name"></span>
            </li>
        </ul>
    </nav>
</template>

<script setup>

// import { ref } from "vue";
// import i18n from "@/plugins/i18n";
import { useRouter } from "vue-router";

// =================================================================================== //

// const { t } = i18n.global
const router = useRouter()

// =================================================================================== //
// ===--- PROPS

const props = defineProps({
    crumbs: {
        type: Array,
        default: () => []
    }
})

// =================================================================================== //
// ===--- METHODS

const goToView = (go) => {
    if (go) {
        router.push(go)
    }
}

// =================================================================================== //

</script>
