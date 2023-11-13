<template>
  <div>
    <BaseTextInput
      id="email"
      label="Votre email"
      type="email"
      placeholder=""
      v-model="email"
      validationState="validationState"
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
      email: '',
      validationState: 'neutral',
      validationClass: ''
    }
  },
  watch: {
    email(newValue) {
      console.log('Email changed:', newValue)
    }
  },
  methods: {
    onEnter() {
      // Regex from https://emailregex.com/
      const emailRegex = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i
      if (emailRegex.test(this.email)) {
        this.validationState = 'success'
        console.log('Email is valid')
      } else {
        this.validationState = 'error'
        console.log('Email is invalid')
      }
    }
  }
}
</script>
