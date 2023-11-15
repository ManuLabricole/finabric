<template>
  <button :class="buttonClasses" :disabled="!isClickable" @click="handleClick">{{ label }}</button>
</template>

<script>
export default {
  name: 'BaseClickButton',
  props: {
    isClickable: {
      type: Boolean,
      default: true
    },
    label: {
      type: String,
      default: 'Click me'
    }
  },
  computed: {
    buttonClasses() {
      return {
        'w-full p-3 rounded-full bg-finaryYellow-500 hover:bg-finaryYellow-600 cursor-pointer transition-all duration-500':
          this.isClickable,
        'w-full p-3 rounded-full bg-disabled text-secondary cursor-not-allowed transition-all duration-500':
          !this.isClickable
      }
    }
  },
  methods: {
    handleClick() {
      if (this.isClickable) {
        this.$emit('clicked')
      }
    }
  }
}
</script>

<style lang="postcss" scoped>
/* You can add additional scoped styles if needed */
</style>
