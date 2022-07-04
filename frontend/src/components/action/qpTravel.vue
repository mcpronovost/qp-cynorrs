<template>
    <div class="qp-action-travel">
        <el-button :loading="isLoading" @click="doEndsTravel()">
            <span v-text="`voyager ici : ${sector}`"></span>
        </el-button>
    </div>
</template>

<script>
import { API } from "@/main.js";
export default {
    name: "qpActionTravel",
    props: {
        sector: {
            type: Number,
            default: null
        }
    },
    data () {
        return {
            isLoading: false
        }
    },
    methods: {
        async doEndsTravel () {
            this.isLoading = true
            // ===---
            const r = await fetch(`${API}/me/heros/1/`, {
                method: "POST",
                headers: {"Authorization": this.$store.getters.rat}
            })
            if (r.status === 200) {
                let result = await r.json()
                console.log(result)
            } else if (r.status === 401) {
                console.log("show error dialog")
            }
            // ===---
            this.isLoading = false
        }
    }
}
</script>
