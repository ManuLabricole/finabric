<template>
  <div class="relative w-full">
    <label
      for="password"
      :class="{
        'text-finaryYellow-500': isFocused || value,
        'text-sm': isFocused || value,
        'transform -translate-y-6': isFocused || value
      }"
      class="absolute left-0 top-50% h-full flex items-center pointer-events-none text-text-secondary text-lg font-normal transition-all duration-500 ease-in-out"
    >
      Mot de passe
    </label>
    <input
      id="password"
      type="password"
      v-model="value"
      @focus="isFocused = true"
      @blur="isFocused = false"
      :class="{
        'border-finaryYellow-500': isFocused || value,
        'border-text-secondary': !isFocused && !value,
        'text-finaryYellow-500': isFocused || value,
        'text-text-secondary': !isFocused && !value
      }"
      class="w-full h-12 p-0 pt-2 pb-1 m-0 bg-transparent text-text-primary ring-0 border-0 border-b focus:outline-none focus:ring-0 focus:border-finaryYellow-400 transition-colors duration-500 ease-in-out"
      placeholder=""
    />
  </div>
</template>

<script>
export default {
  name: 'BaseInput',
  props: {},
  data() {
    return {
      isFocused: false,
      value: ''
    }
  },
  computed: {
    validationClass() {
      switch (this.validationState) {
        case 'success':
          return 'text-green-500'
        case 'error':
          return 'text-red-500'
        default:
          return ''
      }
    },
    borderClass() {
      switch (this.validationState) {
        case 'success':
          return 'border-green-500'
        case 'error':
          return 'border-red-500'
        default:
          return 'border-text-secondary'
      }
    }
  },
  methods: {
    focus() {
      this.isFocused = true
    },
    blur() {
      this.isFocused = false
    }
  }
}
</script>
