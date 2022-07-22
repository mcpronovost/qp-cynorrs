<template>
    <article v-if="props.message" :id="`m${props.message.id}`" class="qp-forum-message">
        <div class="qp-forum-message-inner">
            <header class="qp-forum-header">
                <div v-text="props.message.author.name"></div>
            </header>
            <div class="qp-forum-message-text">
                <div class="qp-forum-message-text-inner">
                    <div v-text="props.message.text"></div>
                </div>
            </div>
        </div>
    </article>
</template>

<script setup>

const props = defineProps({
    world: {
        type: Object,
        default: () => {}
    },
    chapter: {
        type: Object,
        default: () => {}
    },
    message: {
        type: Object,
        default: () => {}
    }
})

</script>

<style scoped>
.qp-forum-message {
    padding: 12px;
}
.qp-forum-message-inner {
    background-color: var(--qp-base);
    border-radius: 4px;
    box-shadow: 0 0 3px rgb(0, 0, 0, 4%);
    text-align: center;
    align-content: center;
    justify-content: center;
    height: 100%;
    padding: 0;
}
</style>
