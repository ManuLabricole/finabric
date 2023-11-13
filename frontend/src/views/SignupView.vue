<template>
  <SignupBg />
  <div class="min-h-screen flex flex-col md:flex-row">
    <!-- Left column for the form -->
    <div class="flex-1 flex justify-center pt-0 pr-6 pl-6 pb-4">
      <!-- Your form goes here -->
      <div class="w-full max-w-lg space-y-6 m-10">
        <RegisterTop />
        <form class="bg-transparent shadow-md space-y-12">
          <!-- Form inputs and submit button -->
          <EmailInput />
          <div class="w-full flex align-items">
            <div class="w-1/2 mr-2">
              <BaseTextInput id="lastname" label="Prénom" />
            </div>
            <div class="w-1/2 ml-2">
              <BaseTextInput id="firstname" label="Nom" />
            </div>
          </div>
          <PasswordInput />
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
import EmailInput from '@/components/inputs/login-registration/EmailInput.vue'
import PasswordInput from '@/components/inputs/login-registration/PasswordInput.vue'
import BaseTextInput from '@/components/inputs/BaseTextInput.vue'

export default {
  name: 'SignupView',
  components: { SignupBg, RightDesign, RegisterTop, EmailInput, PasswordInput, BaseTextInput }
}
</script>
<style postcss></style>
