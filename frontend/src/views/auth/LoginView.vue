<template>
  <SignupBg />
  <div class="min-h-screen flex flex-col md:flex-row">
    <!-- Left column for the form -->
    <div class="flex-1 flex justify-center pt-0 pr-6 pl-6 pb-4">
      <!-- Your form goes here -->
      <div class="w-full max-w-lg space-y-10 m-10 p-5">
        <RegisterTop />
        <form class="bg-transparent shadow-md space-y-5" @submit.prevent="onFormSubmit">
          <!-- Form inputs and submit button -->
          <BaseTextInput
            id="emailInput"
            label="Votre email"
            type="email"
            placeholder=""
            v-model="email"
            errorMessage="Veuillez entrer une adresse email valide"
            @inputChanged="validateEmail"
          />
          <div v-if="!inputsDisplayed" class="w-full">
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
                  id="firstname"
                  label="Prénom"
                  type="text"
                  errorMessage="Merci d'indiquer votre prénom"
                  @inputChanged="validateFirstname"
                />
              </div>
              <div class="w-1/2 ml-2">
                <BaseTextInput
                  id="lastname"
                  type="text"
                  label="Nom"
                  errorMessage="Indiquez votre nom de famille"
                  @inputChanged="validateLastname"
                />
              </div>
            </div>
          </transition>
          <transition>
            <PasswordInput v-if="inputsDisplayed" @inputChanged="validatePassword" />
          </transition>
          <br />
        </form>
        <div v-if="inputsDisplayed" class="w-full mt-5">
          <BaseClickButton
            id="registerEmailValidate"
            label="Suivant"
            :isClickable="formValidationEnable"
            @clicked="submitForm"
          />
        </div>
        <ToastInfo />
        <p class="text-xs text-secondary text-center pt-2">
          En vous inscrivant, vous acceptez les Conditions de service et Politique de
          confidentialité de Finary
        </p>
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
import BaseClickButton from '@/components/inputs/BaseClickButton.vue'

import ToastInfo from '@/components/common/ToastInfo.vue'
import { useToastStore } from '@/stores/toast'

// import axios from 'axios'

export default {
  name: 'SignupView',
  components: {
    SignupBg,
    RightDesign,
    RegisterTop,
    PasswordInput,
    BaseTextInput,
    BaseClickButton,
    ToastInfo
  },
  setup() {
    const toastStore = useToastStore()

    return { toastStore }
  },
  data() {
    return {
      email: '',
      firstname: '',
      lastname: '',
      password: '',

      isEmailValid: false,
      isFirstnameValid: false,
      isLastnameValid: false,
      isPasswordValid: false,

      emailValidationEnable: false,
      inputsDisplayed: false,
      formValidationEnable: false
    }
  },
  watch: {
    // We console log the value if changed
    email: function (val) {
      console.log(val)
    }
  },
  methods: {
    submitForm() {
      // const data = {
      //   email: this.email,
      //   firstname: this.firstname,
      //   lastname: this.lastname,
      //   password: this.password
      // }
      // axios
      //   .post('api/v1/user/auth/register/', data)
      //   .then((response) => {
      //     console.log(response)
      //   })
      //   .catch((error) => {
      //     console.log(error)
      //   })
      this.toastStore.showToast('inf', 'Félicitations ! Ton compte a été créé')
      this.$router.push('/login')
    },
    toggleDisplayInputs() {
      this.inputsDisplayed = !this.inputsDisplayed
    },
    validateEmail(email, isValid) {
      // Your email validation logic goes here
      if (isValid) {
        this.email = email
        this.isEmailValid = true
        this.emailValidationEnable = true
      }
      this.validateForm()
    },
    validateFirstname(firstname, isValid) {
      if (isValid) {
        this.firstname = firstname
        this.isFirstnameValid = true
      }
      this.validateForm()
    },
    validateLastname(lastname, isValid) {
      if (isValid) {
        this.lastname = lastname
        this.isLastnameValid = true
      }
      this.validateForm()
    },
    validatePassword(password, isValid) {
      if (isValid) {
        this.password = password
        this.isPasswordValid = true
      }
      this.validateForm()
    },
    validateForm() {
      if (
        this.isEmailValid &&
        this.isFirstnameValid &&
        this.isLastnameValid &&
        this.isPasswordValid
      ) {
        this.formValidationEnable = true
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
