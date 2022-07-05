<template>
    <div class="qp-action-travel-choosetravellers">
        <el-row v-loading="isLoading" :gutter="20" justify="center">
            <el-col v-for="(traveller, n) in listTravellerHeros" :key="`traveller-${n}`" :span="6" :lg="4">
                <div class="qp-action-travel-traveller" @click="toggleTraveller('hero', n)">
                    <el-tooltip :content="traveller.name">
                        <div :class="`qp-action-travel-traveller-avatar${traveller.is_selected ? ' is_selected':''}`">
                            <el-image v-if="traveller.avatar" :src="traveller.avatar" fit="cover">
                                <template #error>
                                    <div class="image-slot"></div>
                                </template>
                            </el-image>
                        </div>
                    </el-tooltip>
                </div>
            </el-col>
        </el-row>
        <div class="dialog-footer text-center">
            <el-button @click="closeTravel()">
                <span v-text="$i18n.t('Cancel')"></span>
            </el-button>
            <el-button :disabled="!isValidChooseTravellers" type="primary" @click="goToStep('luckyroll')">
                <span v-text="$i18n.t('Continue')"></span>
            </el-button>
        </div>
    </div>
</template>

<script>
// import { API } from "@/main.js";
export default {
    name: "qpActionTravelChooseTravellers",
    data () {
        return {
            isLoading: false,
            listTravellerHeros: []
        }
    },
    computed: {
        listTravellers () {
            let result = []
            for (let item of this.listTravellerHeros) {
                if (item.is_selected) {
                    item["type"] = "hero"
                    result.push(item)
                }
            }
            return result
        },
        isValidChooseTravellers () {
            if (this.listTravellers.length) {
                return true
            }
            return false
        }
    },
    mounted () {
        this.initTravellers()
    },
    methods: {
        async initTravellers () {
            this.isLoading = true
            this.listTravellerHeros = []
            // ===---
            for (const hero of this.$store.getters.heros) {
                if (!hero.geo || (new Date(hero.geo.cooldown) - new Date(Date.now()) <= 0)) {
                    this.listTravellerHeros.push(hero)
                }
            }
            // ===---
            this.isLoading = false
        },
        toggleTraveller (type_of, index) {
            if (type_of == "hero") {
                this.listTravellerHeros[index]["is_selected"] = !this.listTravellerHeros[index]["is_selected"]
            }
            this.$emit("update", this.listTravellers)
        },
        goToStep (step) {
            this.$emit("step", step)
        },
        closeTravel () {
            this.$emit("close")
        }
    }
}
</script>

<style scoped>
.qp-action-travel-choosetravellers .qp-action-travel-traveller {
    text-align: center;
}
.qp-action-travel-choosetravellers .qp-action-travel-traveller-avatar {
    background-color: var(--qp-secondary);
    border: 6px solid var(--qp-base);
    border-radius: 100%;
    overflow: hidden;
    width: 64px;
    height: 64px;
    opacity: 0.7;
    transition: opacity 0.3s;
    margin: 0 auto;
}
.qp-action-travel-choosetravellers .qp-action-travel-traveller-avatar.is_selected {
    border-color: var(--qp-primary);
    opacity: 1;
}
.qp-action-travel-choosetravellers .qp-action-travel-traveller-avatar:hover {
    cursor: pointer;
    opacity: 1;
}
.qp-action-travel-choosetravellers .dialog-footer {
    padding: 40px 0 0;
    margin: 0 0 -10px;
}
</style>
