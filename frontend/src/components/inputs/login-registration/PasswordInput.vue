<template>
  <div class="relative w-full mb-3">
    <label
      for="password"
      :class="{
        'text-sm': isFocused || value,
        'transform -translate-y-6': isFocused || value
      }"
      class="absolute left-0 top-50% h-full flex items-center pointer-events-none text-secondary text-lg font-normal transition-all duration-500 ease-in-out"
    >
      Mot de passe
    </label>
    <div :class="borderClass" class="flex items-center border-b border-text-secondary">
      <input
        id="password"
        :type="showPassword ? 'text' : 'password'"
        v-model="value"
        @focus="isFocused = true"
        @blur="isFocused = false"
        @input="validatePassword"
        class="w-full h-12 p-0 pt-2 pb-1 m-0 bg-transparent text-medium text-primary ring-0 border-0 focus:outline-none focus:ring-0 focus:border-finaryYellow-400 transition-colors duration-500 ease-in-out"
        placeholder=""
      />
      <button type="button" class="p-2 text-primary" @click="togglePasswordVisibility">
        <i :class="showPassword ? 'bi bi-eye font-medium' : 'bi bi-eye-slash'"></i>
      </button>
    </div>
    <p :class="textClass">
      <i v-if="validationMessage" class="bi bi-exclamation-circle"></i>
      {{ validationMessage }}
    </p>
  </div>
</template>

<script>
export default {
  name: 'PasswordInput',
  data() {
    return {
      isFocused: false,
      value: '',
      showPassword: false,
      validationMessage: '',
      validationState: '' // 'success', 'warning', 'error'
    }
  },
  computed: {
    borderClass() {
      switch (this.validationState) {
        case 'success':
          return 'border-finaryYellow-500'
        case 'warning':
          return 'border-yellow-500'
        case 'error':
          return 'border-red-500'
        default:
          return 'border-text-secondary'
      }
    },
    textClass() {
      switch (this.validationState) {
        case 'success':
          return 'text-green-500'
        case 'warning':
          return 'text-yellow-500'
        case 'error':
          return 'text-red-500'
        default:
          return 'text-text-secondary'
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
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword
    }
  }
}
</script>
