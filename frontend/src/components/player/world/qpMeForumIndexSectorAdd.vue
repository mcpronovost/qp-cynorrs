<template>
    <div>
        <el-form ref="formSectorRef" :model="formSector" :label-position="app.win.w < 1200 ? 'top' : 'right'" :rules="formSectorRules" label-width="120px" status-icon :style="app.win.w < 1200 ? 'margin-top:12px;' : 'padding-right:60px;margin-top:12px;'">
            <el-form-item :label="$t('Name')" prop="name">
                <el-input v-model="formSector.name" :placeholder="$t('NameOfTheSector')" :maxlength="32" show-word-limit />
            </el-form-item>
            <el-form-item :label="$t('Description')" prop="description">
                <el-input v-model="formSector.description" :placeholder="$t('AShortDescription')" type="textarea" :rows="4" />
            </el-form-item>
            <el-form-item :label="$t('Colour')" prop="colour">
                <el-color-picker v-model="formSector.colour" />
            </el-form-item>
            <el-form-item :label="$t('Width')" prop="flexbasis">
                <el-select v-model="formSector.flexbasis" :placeholder="$t('CardWidth')">
                    <el-option :label="$t('Fullwide')" :value="'100%'" />
                    <el-option :label="'1/2'" :value="'50%'" />
                    <el-option :label="'1/3'" :value="'33.3333%'" />
                    <el-option :label="'1/4'" :value="'25%'" />
                </el-select>
            </el-form-item>
        </el-form>
        <footer class="qp-dialog-footer text-right">
            <el-button @click="closeAddSector()">
                <span v-text="$t('Cancel')"></span>
            </el-button>
            <el-button type="primary" @click="doAddSector()">
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
    territory: {
        type: Object,
        default: () => {}
    }
})

const isLoadingSend = ref(false)

const formSectorRef = ref()
const formSector = reactive({
    id: 0,
    name: "",
    description: "",
    colour: "",
    flexbasis: "100%"
})
const formSectorRules = reactive({
    name: [
        {
            required: true,
            message: t("Thisfieldisrequired"),
            trigger: "blur"
        }
    ]
})

const closeAddSector = () => {
    emit("close")
}

const doAddSector = async () => {
    isLoadingSend.value = true
    // ===---
    await formSectorRef.value.validate((valid, fields) => {
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
        data.append("territory", props.territory.id)
        data.append("name", formSector.name)
        data.append("description", formSector.description ? formSector.description : "")
        data.append("colour", formSector.colour ? formSector.colour : "")
        data.append("flexbasis", formSector.flexbasis)
        let response = await fetch(`${API}/me/territories/${props.territory.id}/sectors/create/`, {
            method: "POST",
            headers: {"Authorization": rat.value},
            body: data
        })
        let r = await response.json()
        if (response.status === 201) {
            ElMessage.success(t("SectorAddedSuccessfully"))
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
