import { createI18n } from "vue-i18n/index";
import fr from "@/locales/fr";

const setDateTimeFormats = {
    short: {
        year: "numeric",
        month: "long",
        day: "2-digit"
    }
}

const dateTimeFormats = {
    en: setDateTimeFormats,
    fr: setDateTimeFormats
}

const i18n = createI18n({
    locale: "fr",
    fallbackLocale: "fr",
    messages: { fr },
    dateTimeFormats,
    silentTranslationWarn: true
})

export default i18n