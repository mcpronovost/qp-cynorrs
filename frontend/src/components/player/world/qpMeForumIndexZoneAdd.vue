<template>
    <div>
        <el-form ref="formZoneRef" :model="formZone" :label-position="app.win.w < 1200 ? 'top' : 'right'" :rules="formZoneRules" label-width="120px" status-icon :style="app.win.w < 1200 ? 'margin-top:12px;' : 'padding-right:60px;margin-top:12px;'">
            <el-form-item :label="$t('Name')" prop="name">
                <el-input v-model="formZone.name" :placeholder="$t('NameOfTheZone')" :maxlength="32" show-word-limit />
            </el-form-item>
            <el-form-item :label="$t('Description')" prop="description">
                <el-input v-model="formZone.description" :placeholder="$t('AShortDescription')" type="textarea" :rows="4" />
            </el-form-item>
        </el-form>
        <footer class="qp-dialog-footer text-right">
            <el-button @click="closeAddZone()">
                <span v-text="$t('Cancel')"></span>
            </el-button>
            <el-button type="primary" @click="doAddZone()">
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
    world: {
        type: Object,
        default: () => {}
    },
    forum: {
        type: Object,
        default: () => {}
    }
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

const closeAddZone = () => {
    emit("close")
}

const doAddZone = async () => {
    isLoadingSend.value = true
    // ===---
    await formZoneRef.value.validate((valid, fields) => {
        if (valid) {
            doSendAddZone()
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

const doSendAddZone = async () => {
    isLoadingSend.value = true
    // ===---
    try {
        let data = new FormData()
        data.append("forum", props.forum.id)
        data.append("name", formZone.name)
        data.append("description", formZone.description ? formZone.description : "")
        let response = await fetch(`${API}/me/forums/${props.forum.id}/zones/create/`, {
            method: "POST",
            headers: {"Authorization": rat.value},
            body: data
        })
        let r = await response.json()
        if (response.status === 201) {
            ElMessage.success(t("ZoneAddedSuccessfully"))
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
