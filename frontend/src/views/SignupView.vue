<template>
  <SignupBg />
  <div class="min-h-screen flex flex-col md:flex-row">
    <!-- Left column for the form -->
    <div class="flex-1 flex justify-center pt-0 pr-6 pl-6 pb-4">
      <!-- Your form goes here -->
      <div class="w-full max-w-lg space-y-6 m-10 p-5">
        <RegisterTop />
        <form class="bg-transparent shadow-md space-y-12" @submit.prevent="onFormSubmit">
          <!-- Form inputs and submit button -->
          <BaseTextInput
            id="emailInput"
            label="Votre email"
            type="email"
            placeholder=""
            v-model="email"
            errorMessage="Veuillez entrer une adresse email valide"
            @input-unfocused="validateEmail"
          />
          <div v-if="!inputsDisplayed" class="w-full mt-5">
            <transition>
              <BaseClickButton
                id="registerEmailValidate"
                label="Suivant"
                :isClickable="emailValidationEnable"
                @clicked="toggleDisplayInputs"
              />
            </transition>
          </div>
          <transition>
            <div v-if="inputsDisplayed" key="additionalInputs" class="w-full flex align-items">
              <div class="w-1/2 mr-2">
                <BaseTextInput
                  id="lastname"
                  label="Prénom"
                  type="text"
                  errorMessage="Merci d'indiquer votre prénom"
                />
              </div>
              <div class="w-1/2 ml-2">
                <BaseTextInput
                  id="firstname"
                  type="text"
                  label="Nom"
                  errorMessage="Indiquez votre nom de famille"
                />
              </div>
            </div>
          </transition>
          <transition>
            <PasswordInput />
          </transition>
        </form>
      </div>
    </div>
    <!-- Right column for pictures or design elements -->
    <RightDesign />
  </div>
</template>

<script>
import SignupBg from '@/components/backgrounds/SignupBg.vue'
import RightDesign from '@/components/login-registration/RightDesign.vue'
import RegisterTop from '@/components/login-registration/RegisterTop.vue'
import PasswordInput from '@/components/inputs/login-registration/PasswordInput.vue'
import BaseTextInput from '@/components/inputs/BaseTextInput.vue'
import BaseClickButton from '../components/inputs/BaseClickButton.vue'

export default {
  name: 'SignupView',
  components: {
    SignupBg,
    RightDesign,
    RegisterTop,
    PasswordInput,
    BaseTextInput,
    BaseClickButton
  },
  data() {
    return {
      isEmailValid: false,
      email: '',
      emailValidationEnable: false,
      inputsDisplayed: false
    }
  },
  watch: {
    // We console log the value if changed
    email: function (val) {
      console.log(val)
    }
  },
  methods: {
    onFormSubmit() {
      console.log('Form submitted')
    },
    toggleDisplayInputs() {
      this.inputsDisplayed = !this.inputsDisplayed
    },
    validateEmail(email) {
      // Your email validation logic goes here
      const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      if (regex.test(email)) {
        // Email is valid
        console.log('Valid email:', email)
        this.emailValidationEnable = true
      } else {
        // Email is not valid
        console.log('Invalid email:', email)
      }
    }
  }
}
</script>
<style postcss>
.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
