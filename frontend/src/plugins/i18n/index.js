import { createI18n } from "vue-i18n/index";
import fr from "@/plugins/i18n/fr";

const setDateTimeFormats = {
    short: {
        year: "numeric",
        month: "long",
        day: "2-digit"
    }
}

const dateTimeFormats = {
    fr: setDateTimeFormats
}

const i18n = createI18n({
    locale: "fr",
    fallbackLocale: "fr",
    messages: { fr },
    dateTimeFormats,
    legacy: false,
    globalInjection: true,
    silentTranslationWarn: true
})

export default i18n