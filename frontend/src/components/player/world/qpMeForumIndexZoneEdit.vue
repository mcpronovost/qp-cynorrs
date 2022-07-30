<template>
    <div>
        <el-form ref="formZoneRef" :model="formZone" :label-position="app.win.w < 1200 ? 'top' : 'right'" :rules="formZoneRules" label-width="120px" status-icon :style="app.win.w < 1200 ? 'margin-top:12px;' : 'padding-right:60px;margin-top:12px;'">
            <el-form-item :label="$t('Name')" prop="name">
                <el-input v-model="formZone.name" :placeholder="$t('NameOfTheZone')" :maxlength="32" show-word-limit />
            </el-form-item>
            <el-form-item :label="$t('Description')" prop="description">
                <el-input v-model="formZone.description" :placeholder="$t('AShortDescription')" type="textarea" :rows="4" />
            </el-form-item>
            <el-form-item :label="$t('Ordering')" prop="ordering">
                <el-input-number v-model="formZone.ordering" :min="1" :max="3000" />
            </el-form-item>
            <el-form-item>
                <el-button type="danger" size="small" @click="doDeleteZone()">
                    <span v-text="$t('Delete')"></span>
                </el-button>
            </el-form-item>
        </el-form>
        <footer class="qp-dialog-footer text-right">
            <el-button @click="closeEditZone()">
                <span v-text="$t('Cancel')"></span>
            </el-button>
            <el-button type="primary" @click="doEditZone()">
                <span v-text="$t('Send')"></span>
            </el-button>
        </footer>
    </div>
</template>

<script setup>
import { computed, onMounted, reactive, ref } from "vue";
import { useStore } from "vuex";
import { ElMessage, ElMessageBox } from "element-plus";
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

onMounted(() => {
  resetFormZone()
})

const isLoadingSend = ref(false)

const formZoneRef = ref()
const formZone = reactive({
    id: 0,
    name: "",
    description: "",
    ordering: 0
})
const formZoneRules = reactive({
    name: [
        {
            required: true,
            message: t("Thisfieldisrequired"),
            trigger: "blur"
        }
    ]
})

const resetFormZone = () => {
    formZone.id = props.zone.id
    formZone.name = props.zone.name
    formZone.description = props.zone.description
    formZone.ordering = props.zone.ordering
}

const closeEditZone = () => {
    emit("close")
}

const doEditZone = async () => {
    isLoadingSend.value = true
    // ===---
    await formZoneRef.value.validate((valid, fields) => {
        if (valid) {
            doSendEditZone()
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

const doSendEditZone = async () => {
    isLoadingSend.value = true
    // ===---
    try {
        let data = new FormData()
        data.append("name", formZone.name)
        data.append("description", formZone.description ? formZone.description : "")
        data.append("ordering", formZone.ordering)
        let response = await fetch(`${API}/me/zones/${formZone.id}/edit/`, {
            method: "PATCH",
            headers: {"Authorization": rat.value},
            body: data
        })
        let r = await response.json()
        if (response.status === 200) {
            ElMessage.success(t("ZoneUpdatedSuccessfully"))
            closeEditZone()
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

const doDeleteZone = () => {
    ElMessageBox.confirm(
        t("Areyousureyouwanttodeletethiszone"),
        t("DeleteZone"),
        {
            confirmButtonText: t("Delete"),
            cancelButtonText: t("Cancel"),
            type: "warning"
        }
    ).then(() => {
        sendDeleteZone()
    }).catch(() => {
        isLoadingSend.value = false
    })
}

const sendDeleteZone = async () => {
    isLoadingSend.value = true
    // ===---
    try {
        let data = new FormData()
        data.append("id", formZone.id)
        let response = await fetch(`${API}/me/zones/${formZone.id}/delete/`, {
            method: "DELETE",
            headers: {"Authorization": rat.value},
            body: data
        })
        if (response.status === 204) {
            ElMessage.success(t("ZoneDeletedSuccessfully"))
            closeEditZone()
            emit("init-forum")
        } else {
            let r = await response.json()
            ElMessage.error(`${t('AnErrorOccurred')} : ${JSON.stringify(r)}`)
        }
    } catch {
        ElMessage.error(t("AnErrorOccurred"))
    }
    // ===---
    isLoadingSend.value = false
}

</script>
