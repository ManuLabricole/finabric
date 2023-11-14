<template>
  <div class="relative w-full">
    <label
      :for="id"
      :class="{
        // 'text-finaryYellow-500': isFocused || value,
        'text-sm': isFocused || value,
        'transform -translate-y-6': isFocused || value
      }"
      class="absolute left-0 top-50% h-full flex items-center pointer-events-none text-secondary text-lg font-normal transition-all duration-500 ease-in-out"
    >
      {{ label }}
    </label>
    <input
      :id="id"
      :type="type"
      v-model="value"
      @focus="isFocused = true"
      @blur="isFocused = false"
      :class="{
        'border-finaryYellow-500': isFocused || value,
        'border-text-secondary': !isFocused && !value,
        'text-finaryYellow-500': isFocused || value,
        'text-text-secondary': !isFocused && !value
      }"
      class="w-full h-12 p-0 pt-2 pb-1 m-0 bg-transparent text-primary ring-0 border-0 border-b focus:outline-none focus:ring-0 focus:border-finaryYellow-400 transition-colors duration-500 ease-in-out"
      placeholder=""
      @input="onInput(value)"
    />
    <div v-if="validationState == 'error'" class="w-full absolute mt-2">
      <p class="flex text-sm text-danger h-full">
        <i class="bi bi-exclamation-circle mr-2"></i>
        {{ errorMessage }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BaseInput',
  props: {
    id: {
      type: String,
      required: true
    },
    label: {
      type: String,
      required: true
    },
    type: {
      type: String,
      default: 'text' // Default input type is 'text'
    },
    errorMessage: String
  },
  data() {
    return {
      isFocused: false,
      value: '',
      validationState: 'neutral' //'error'
    }
  },
  computed: {
    validationClass() {
      switch (this.validationState) {
        case 'error':
          return 'text-red-500'
        default:
          return ''
      }
    },
    borderClass() {
      switch (this.validationState) {
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
    },
    onInput(value) {
      if (value == '') {
        this.validationState = 'error'
      }
    }
  }
}
</script>
<style postcss scoped>
input:-webkit-autofill,
input:-webkit-autofill:hover,
input:-webkit-autofill:focus,
input:-webkit-autofill:active {
  transition: background-color 5000s ease-in-out 0s;
  -webkit-text-fill-color: theme('colors.primary') !important;
}
</style>
