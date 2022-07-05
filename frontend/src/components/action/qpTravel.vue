<template>
    <div class="qp-action-travel">
        <el-button :loading="isLoading" @click="doStartsTravel()">
            <span v-text="`voyager ici : ${sector}`"></span>
        </el-button>
        <!---->
        <el-dialog v-model="isShowTravel" :title="titleTravel" center destroy-on-close>
            <qpActionTravelChooseTravellers v-if="step == 'choosetravellers'" @update="updateTravellers" @step="goToStep" @close="closeTravel()" />
        </el-dialog>
        <!---->
    </div>
</template>

<script>
import { API } from "@/main.js";
import qpActionTravelChooseTravellers from "@/components/action/qpTravelChooseTravellers";
export default {
    name: "qpActionTravel",
    components: {
        qpActionTravelChooseTravellers
    },
    props: {
        sector: {
            type: Number,
            default: null
        }
    },
    data () {
        return {
            isLoading: false,
            isShowTravel: false,
            titleTravel: this.$i18n.t("Travel"),
            step: null,
            listTravellers: []
        }
    },
    mounted () {
        //
    },
    methods: {
        doStartsTravel () {
            this.goToStep("choosetravellers")
            this.openTravel()
        },
        async doEndsTravel () {
            this.isLoading = true
            // ===---
            let data = new FormData()
            data.append("test", "my test")
            // ===---
            const r = await fetch(`${API}/me/heros/1/`, {
                method: "POST",
                headers: {"Authorization": this.$store.getters.rat},
                body: data
            })
            if (r.status === 200) {
                let result = await r.json()
                console.log(result)
            } else if (r.status === 401) {
                console.log("show error dialog")
            }
            // ===---
            this.isLoading = false
        },
        goToStep (step) {
            if (step == "choosetravellers") {
                this.titleTravel = this.$i18n.t("ChooseTravellers")
            } else {
                this.titleTravel = this.$i18n.t("Travel")
            }
            this.step = step
        },
        openTravel () {
            this.listTravellers = []
            this.isShowTravel = true
        },
        closeTravel () {
            this.isShowTravel = false
            this.listTravellers = []
        },
        updateTravellers (travellers) {
            this.listTravellers = travellers
        }
    }
}
</script>
