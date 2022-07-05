<template>
    <div class="qp-vue">
        <div v-for="(zone, n) in listZones" :key="`zones-${n}`">
            <h1>
                <span v-text="zone.name"></span>
            </h1>
            <div v-for="(territory, nn) in zone.territories" :key="`territory-${n}-${nn}`">
                <h2>
                    <span v-text="territory.name"></span>
                </h2>
                <div v-for="(sector, nnn) in territory.sectors" :key="`sector-${n}-${nn}-${nnn}`">
                    <h3>
                        <span v-text="sector.name"></span>
                    </h3>
                    <qp-action-travel :sector="sector.id" />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { API } from "@/main.js";
import qpTravel from "@/components/action/qpTravel.vue";
export default {
    name: "HomeView",
    components: {
        "qpActionTravel": qpTravel
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
