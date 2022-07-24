export const qpcode = (text) => {
    let result = text
    result = result
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;")
        .replaceAll("\n", "<br />")
        .replaceAll("[b]", "<b>")
        .replaceAll("[/b]", "</b>")
    return result
}