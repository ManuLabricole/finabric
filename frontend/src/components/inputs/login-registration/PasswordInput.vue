<template>
  <div class="relative w-full">
    <label
      :for="id"
      :class="{
        'text-sm': isFocused || value,
        'transform -translate-y-6': isFocused || value
      }"
      class="absolute left-0 top-50% h-full flex items-center pointer-events-none text-secondary text-lg font-normal transition-all duration-500 ease-in-out"
    >
      Mot de passe
    </label>
    <div
      :class="borderClass"
      class="flex items-center border-b border-text-secondary transition-colors duration-500"
    >
      <input
        :id="id"
        :type="showPassword ? 'text' : 'password'"
        v-model="value"
        @focus="isFocused = true"
        @blur="isFocused = false"
        @input="validatePassword"
        class="w-full h-12 p-0 pt-2 pb-1 m-0 bg-transparent text-medium text-primary ring-0 border-0 focus:outline-none focus:ring-0 focus:border-finaryYellow-500 transition-colors duration-500 ease-in-out"
        placeholder=""
      />
      <button type="button" class="p-2 text-primary" @click="togglePasswordVisibility">
        <i :class="showPassword ? 'bi bi-eye font-medium' : 'bi bi-eye-slash'"></i>
      </button>
    </div>
    <ErrorMessage :show="validationState == 'error' && showMessage == true" :message="validationMessage" />
    <WarningMessage :show="validationState == 'warning' && showMessage == true" :message="validationMessage" />
    <SuccessMessage :show="validationState == 'success' && showMessage == true" :message="validationMessage" />
  </div>
</template>

<script>
import ErrorMessage from '@/components/feedback_messages/ErrorMessage.vue'
import WarningMessage from '@/components/feedback_messages/WarningMessage.vue'
import SuccessMessage from '@/components/feedback_messages/SuccessMessage.vue'

export default {
  name: 'PasswordInput',
  components: {
    ErrorMessage,
    WarningMessage,
    SuccessMessage
  },
  props: {
    id: {
      type: String,
      required: true
    },
    showMessage: {
      type: Boolean,
      default: true
    }
  },
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
      if (this.isFocused && !this.showMessage) return 'border-finaryYellow-500'
      else if (this.showMessage) {
        switch (this.validationState) {
          case 'success':
            return 'border-finaryYellow-500'
          case 'warning':
            return 'border-warning'
          case 'error':
            return 'border-danger'
          default:
            return 'border-secondary'
        }
      } else return 'border-secondary'
    }
  },
  methods: {
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
        console.log('warning')
        this.validationMessage =
          'Votre mot de passe pourrait être plus sécurisé en y ajoutant des caractères.'
        // this.$emit('inputChanged', this.value, this.validationState)
      } else {
        this.validationState = 'success'
        this.validationMessage = 'Beau travail, ceci est un excellent mot de passe.'
        // this.$emit('inputChanged', this.value, this.validationState)
      }
      this.$emit('inputChanged', this.value, this.validationState)
    }
  }
}
</script>
