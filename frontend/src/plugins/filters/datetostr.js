export const datetostr = (date, showhour = true) => {
    const options = {
        year: "numeric",
        month: "long",
        day: "numeric",
        hour: showhour ? "numeric" : null,
        minute: showhour ? "numeric" : null,
        hour12: false
    };
    return new Date(date).toLocaleString("fr", options)
}