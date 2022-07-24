export const qpcode = (text) => {
    let result = text
    result = result
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;")
        .replaceAll("\n", "<br />")
        .replaceAll("[g]", '<span style="font-weight:bold;">')
        .replaceAll("[/g]", "</span>")
        .replaceAll("[i]", '<span style="font-style:italic;">')
        .replaceAll("[/i]", "</span>")
        .replaceAll("[s]", '<span style="text-decoration:underline;">')
        .replaceAll("[/s]", "</span>")
        .replaceAll("[b]", '<span style="text-decoration:line-through;">')
        .replaceAll("[/b]", "</span>")
        .replace(/\[c=#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})\]/g, '<span style="color:#$1;">')
        .replace(/\[c=([a-zA-Z0-9_]+)\]/g, '<span style="color:var(--c-$1);">')
        .replaceAll("[/c]", "</span>")
        .replace(/\[p=(Indie Flower|Oswald|Quicksand|Roboto Condensed)\]/g, '<span style="font-family:\'$1\';">')
        .replaceAll("[/p]", "</span>")
        .replace(/\[url=([^<>[\]]+)\]/g, '<a href="$1">')
        .replaceAll("[/url]", "</a>")
        .replace(/\[urlo=([^<>[\]]+)\]/g, '<a href="$1" target="_blank">')
        .replaceAll("[/urlo]", "</a>")
        .replace(/\[ico=([a-z- ]+)\]/g, '<i class="mdi $1"></i>')
    return result
}