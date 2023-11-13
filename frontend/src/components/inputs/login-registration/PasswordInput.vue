<template>
  <div class="relative w-full">
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
    <div v-if="validationState == 'error'" class="w-full absolute mt-2 ml-2">
      <p class="flex text-sm text-danger h-full">
        <i class="bi bi-exclamation-circle mr-2"></i>
        {{ validationMessage }}
      </p>
    </div>
    <div v-if="validationState == 'warning'" class="w-full absolute mt-2 ml-2">
      <p class="flex text-sm text-warning h-full">
        <i class="bi bi-exclamation-circle mr-2"></i>
        {{ validationMessage }}
      </p>
    </div>
    <div v-if="validationState == 'success'" class="w-full absolute mt-2 ml-2">
      <p class="flex text-sm text-success h-full">
        <i class="bi bi-exclamation-circle mr-2"></i>
        {{ validationMessage }}
      </p>
    </div>
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
          return 'border-danger'
        default:
          return 'border-text-secondary'
      }
    },
    textClass() {
      switch (this.validationState) {
        case 'success':
          return 'text-success'
        case 'warning':
          return 'text-finaryYellow-400'
        case 'error':
          return 'text-danger'
        default:
          return 'text-text-secondary'
      }
    }
  },
  watch: {
    value(newValue) {
      if (!newValue) {
        this.validationState = 'neutral'
        this.validationMessage = ''
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
    },
    validatePassword() {
      const hasLength = this.value.length >= 8
      const hasUppercase = /[A-Z]/.test(this.value)
      const hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/.test(this.value)

      if (!hasLength) {
        this.validationState = 'error'
        this.validationMessage = 'Le mot de passe doit comporter au moins 8 caractères.'
      } else if (!hasUppercase) {
        this.validationState = 'error'
        this.validationMessage = 'Le mot de passe doit comporter au moins une majuscule.'
      } else if (!hasSpecialChar) {
        this.validationState = 'error'
        this.validationMessage = 'Le mot de passe doit comporter au moins un caractère spécial.'
      } else if (this.value.length < 12) {
        this.validationState = 'warning'
        this.validationMessage =
          'Votre mot de passe pourrait être plus sécurisé en y ajoutant des caractères.'
      } else {
        this.validationState = 'success'
        this.validationMessage = 'Beau travail, ceci est un excellent mot de passe.'
      }
    }
  }
}
</script>
