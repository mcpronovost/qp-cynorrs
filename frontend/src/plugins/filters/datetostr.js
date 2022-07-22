export const datetostr = (date) => {
    const options = {
        year: "numeric",
        month: "long",
        day: "numeric",
        hour: "numeric",
        minute: "numeric",
        hour12: false
    };
    return new Date(date).toLocaleString("fr", options)
}