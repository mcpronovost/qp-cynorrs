<template>
    <div class="qp-vue" id="qp-sagars">
        <h1>Sagars</h1>
    </div>
</template>

<script>
export default {
    name: "SagarsView",
    data () {
        return {
            listZones: []
        }
    },
    mounted () {
        this.initStyle()
    },
    beforeUnmount () {
        document.getElementById("qp-style-sagars").remove();
    },
    methods: {
        initStyle () {
            let styletag = document.createElement("style");
            styletag.setAttribute("id", "qp-style-sagars");
            styletag.innerHTML = ":root{--qp-bg:#f00;}";
            document.head.appendChild(styletag);
        }
    }
}
</script>
