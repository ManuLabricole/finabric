<template>
  <div class="relative w-full" :class="borderClass">
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
      @blur="handleBlur"
      :class="{
        'border-finaryYellow-500': isFocused || (value && validationState != 'error'),
        'border-text-secondary': !isFocused && !value && validationState != 'error',
        'text-finaryYellow-500': isFocused || (value && validationState != 'error'),
        'text-text-secondary': !isFocused && !value && validationState != 'error',
        'border-danger': validationState == 'error'
      }"
      class="w-full h-12 p-0 pt-2 pb-1 m-0 bg-transparent text-primary ring-0 border-0 border-b focus:outline-none focus:ring-0 focus:border-finaryYellow-500 transition-colors duration-500 ease-in-out"
      placeholder=""
      @input="onInput(value, type)"
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
    borderClass() {
      switch (this.validationState) {
        case 'error':
          console.log('error')
          return 'border-danger'
        default:
          return 'border-text-secondary'
      }
    }
  },
  methods: {
    focus() {
      this.isFocused = true
    },
    handleBlur() {
      this.isFocused = false
      console.log('VALUE', this.value)
      this.$emit('inputChanged', this.value)
      console.log('blur')
    },
    onInput(value, type) {
      if (value == '') {
        this.validationState = 'error'
        this.$emit('inputChanged', this.value, false)
      } else {
        if (type == 'email') {
          const emailRegex = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i
          if (emailRegex.test(value)) {
            this.validationState = 'success'
            this.$emit('inputChanged', this.value, true)
          } else {
            this.validationState = 'error'
          }
        } else if (type == 'text') {
          this.validationState = 'success'
          this.$emit('inputChanged', this.value, true)
        }
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
