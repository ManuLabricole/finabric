<template>
  <SignupBg />
  <div class="min-h-screen flex flex-col md:flex-row">
    <!-- Left column for the form -->
    <div class="flex-1 flex justify-center pt-0 pr-6 pl-6 pb-4">
      <!-- Your form goes here -->
      <div class="w-full max-w-lg space-y-10 m-10 p-5">
        <RegisterTop
          title="Se connecter"
          subtitle="Vous n'avez pas encore de compte ?"
          anchorText="S'incrire"
          anchorLink="signup"
          breakText="OU SE CONNECTER PAR EMAIL"
        />
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

          <transition>
            <PasswordInput
              id="passwordLogin"
              :showMessage="false"
              @inputChanged="validatePassword"
            />
          </transition>
          <br />
        </form>
        <div class="w-full mt-5">
          <BaseClickButton
            id="registerEmailValidate"
            label="Suivant"
            :isClickable="inputsFilled"
            @clicked="submitForm"
          />
        </div>
        <p
          class="flex justify-center mt-5 text-sm text-finaryYellow-500 hover:text-finaryYellow-700"
        >
          <a href="">Mot de passe oublié ?</a>
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

// import axios from 'axios'

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
  setup() {},
  data() {
    return {
      email: '',
      password: '',

      isEmailValid: false,
      isFirstnameValid: false,
      isLastnameValid: false,
      isPasswordValid: false,

      emailValidationEnable: false,
      inputsFilled: false,
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
    validateEmail(email, isValid) {
      // Your email validation logic goes here
      if (isValid) {
        this.email = email
        this.isEmailValid = true
        this.emailValidationEnable = true
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
