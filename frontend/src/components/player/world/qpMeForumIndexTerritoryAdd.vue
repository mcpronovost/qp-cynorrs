<template>
    <div>
        <el-form ref="formTerritoryRef" :model="formTerritory" :label-position="app.win.w < 1200 ? 'top' : 'right'" :rules="formTerritoryRules" label-width="120px" status-icon :style="app.win.w < 1200 ? 'margin-top:12px;' : 'padding-right:60px;margin-top:12px;'">
            <el-form-item :label="$t('Name')" prop="name">
                <el-input v-model="formTerritory.name" :placeholder="$t('NameOfTheTerritory')" :maxlength="32" show-word-limit />
            </el-form-item>
            <el-form-item :label="$t('Description')" prop="description">
                <el-input v-model="formTerritory.description" :placeholder="$t('AShortDescription')" type="textarea" :rows="4" />
            </el-form-item>
            <el-form-item :label="$t('Colour')" prop="colour">
                <el-color-picker v-model="formTerritory.colour" />
            </el-form-item>
            <el-form-item :label="$t('Width')" prop="flexbasis">
                <el-select v-model="formTerritory.flexbasis" :placeholder="$t('CardWidth')">
                    <el-option :label="$t('Fullwide')" :value="'100%'" />
                    <el-option :label="'1/2'" :value="'50%'" />
                    <el-option :label="'1/3'" :value="'33.3333%'" />
                    <el-option :label="'1/4'" :value="'25%'" />
                </el-select>
            </el-form-item>
        </el-form>
        <footer class="qp-dialog-footer text-right">
            <el-button @click="closeAddTerritory()">
                <span v-text="$t('Cancel')"></span>
            </el-button>
            <el-button type="primary" @click="doAddTerritory()">
                <span v-text="$t('Send')"></span>
            </el-button>
        </footer>
    </div>
</template>

<script setup>
import { computed, reactive, ref } from "vue";
import { useStore } from "vuex";
import { ElMessage } from "element-plus";
import { API } from "@/main.js";
import i18n from "@/plugins/i18n";

const { t } = i18n.global

const store = useStore();
const app = computed(() => store.getters.app)
const rat = computed(() => store.getters.rat)

const emit = defineEmits(["init-forum", "close"])

const props = defineProps({
    zone: {
        type: Object,
        default: () => {}
    }
})

const isLoadingSend = ref(false)

const formTerritoryRef = ref()
const formTerritory = reactive({
    id: 0,
    name: "",
    description: "",
    colour: "",
    flexbasis: "100%"
})
const formTerritoryRules = reactive({
    name: [
        {
            required: true,
            message: t("Thisfieldisrequired"),
            trigger: "blur"
        }
    ]
})

const closeAddTerritory = () => {
    emit("close")
}

const doAddTerritory = async () => {
    isLoadingSend.value = true
    // ===---
    await formTerritoryRef.value.validate((valid, fields) => {
        if (valid) {
            doSendAddTerritory()
        } else {
            for (let [key, val] of Object.entries(fields)) {
                let k = t(`error${key}`)
                for (let v of val) {
                    ElMessage.error(`${k} : ${v.message}`)
                }
            }
            isLoadingSend.value = false
        }
    })
}

const doSendAddTerritory = async () => {
    isLoadingSend.value = true
    // ===---
    try {
        let data = new FormData()
        data.append("zone", props.zone.id)
        data.append("name", formTerritory.name)
        data.append("description", formTerritory.description ? formTerritory.description : "")
        data.append("colour", formTerritory.colour ? formTerritory.colour : "")
        data.append("flexbasis", formTerritory.flexbasis)
        let response = await fetch(`${API}/me/zones/${props.zone.id}/territories/create/`, {
            method: "POST",
            headers: {"Authorization": rat.value},
            body: data
        })
        let r = await response.json()
        if (response.status === 201) {
            ElMessage.success(t("TerritoryAddedSuccessfully"))
            emit("init-forum")
        } else {
            ElMessage.error(`${t('AnErrorOccurred')} : ${JSON.stringify(r)}`)
        }
    } catch {
        ElMessage.error(t("AnErrorOccurred"))
    }
    // ===---
    isLoadingSend.value = false
}

</script>
