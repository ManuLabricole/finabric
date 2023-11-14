<template>
  <div>
    <BaseTextInput
      id="email"
      label="Votre email"
      type="email"
      placeholder=""
      v-model="email"
      errorMessage="Veuillez entrer une adresse email valide"
      @keyup.enter="onEnter"
    />
    <!-- More inputs as needed -->
  </div>
</template>

<script>
import BaseTextInput from '@/components/inputs/BaseTextInput.vue'

export default {
  components: {
    BaseTextInput
  },
  data() {
    return {
      wasFocused: false,
      email: '',
      validationState: 'neutral',
      validationClass: ''
    }
  },
  methods: {
    onEnter() {
      // Regex from https://emailregex.com/
      const emailRegex = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i
      if (emailRegex.test(this.email)) {
        this.validationState = 'success'
        this.$emit('email-validated', { email: this.email, valid: true })
      } else {
        this.validationState = 'error'
        this.$emit('email-validated', { email: this.email, valid: false })
      }
    }
  }
}
</script>
