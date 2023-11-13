<template>
  <div>
    <BaseTextInput id="email" label="Votre email" type="email" placeholder="" v-model="email"/>
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
      password: ''
      // Other data properties
    }
  },
  watch: {
    email(newValue) {
      console.log('Email changed:', newValue)
    }
  }
  // Other methods and logic
}
</script>
