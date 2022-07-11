<template>
    <div class="qp-vue">
        <div class="qp-container">
            <section v-for="(zone, n) in listZones" :key="`zones-${n}`">
                <qpForumZone :zone="zone" />
            </section>
        </div>
    </div>
</template>

<script>
import { API } from "@/main.js";
import qpZone from "@/components/forum/qpZone.vue";
export default {
    name: "HomeView",
    components: {
        "qpForumZone": qpZone
    },
    data () {
        return {
            listZones: []
        }
    },
    mounted () {
        this.setZones()
    },
    methods: {
        async setZones () {
            // ===---
            let r = await fetch(`${API}/worlds/1/`, {
                method: "GET",
                headers: {"Authorization": this.$store.getters.rat}
            })
            if (r.status === 200) {
                let result = await r.json()
                this.listZones = result.zones
            } else if (r.status === 401) {
                console.log(r)
            }
            // ===---
        }
    }
}
</script>
