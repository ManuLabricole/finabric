<template>
  <div v-if="show" class="w-full absolute mt-2">
    <p class="flex text-sm text-warning h-full">
      <i class="bi bi-exclamation-circle mr-2"></i>
      {{ message }}
    </p>
  </div>
</template>

<script>
export default {
  name: 'feedback-messages/SuccessMessage',
  props: {
    show: {
      type: Boolean,
      required: true
    },
    message: {
      type: String,
      required: true
    }
  }
}
</script>

<style lang="postcss" scoped></style>
