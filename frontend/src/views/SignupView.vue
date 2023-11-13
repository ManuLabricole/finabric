<template>
  <SignupBg />
  <div class="min-h-screen flex flex-col md:flex-row">
    <!-- Left column for the form -->
    <div class="flex-1 flex justify-center pt-0 pr-6 pl-6 pb-4 border border-green-500">
      <!-- Your form goes here -->
      <div class="w-full max-w-lg border space-y-6 m-10">
        <RegisterTop />
        <form class="bg-transparent shadow-md">
          <!-- Form inputs and submit button -->
          <EmailInput />
        </form>
      </div>
    </div>

    <!-- Right column for pictures or design elements -->
    <RightDesign />
  </div>
</template>

<script>
import SignupBg from '@/components/backgrounds/SignupBg.vue'
import RightDesign from '../components/login-registration/RightDesign.vue'
import RegisterTop from '../components/login-registration/RegisterTop.vue'
import EmailInput from '../components/inputs/login-registration/EmailInput.vue'

export default {
  name: 'SignupView',
  components: { SignupBg, RightDesign, RegisterTop, EmailInput }
}
</script>
<style postcss></style>
