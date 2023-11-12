<template>
  <SignupBg />
  <div class="min-h-screen flex flex-col md:flex-row">
    <!-- Left column for the form -->
    <div
      class="flex-1 flex items-center justify-center m-4 pt-0 pr-6 pl-6 pb-4 border border-green-500"
    >
      <!-- Your form goes here -->
      <div class="w-full max-w-md border space-y-4">
        <div class="border">Logo</div>
        <div class="mb-4">
          <h1 class="text-white text-4xl font-normal tracking-wider mb-1">Créer mon compte</h1>
          <span class="text-gray-500 font-small"
            >J'ai déjà un compte. <a class="text" href="/">Se connecter > </a></span
          >
        </div>
        <div class="flex flex-col w-full space-y-2">
          <button class="bg-button-google w-full rounded-full p-3 text-text-primary">
            Continuer avec google
          </button>
          <button class="bg-button-apple w-full rounded-full p-3 text-text-black">
            Continuer avec Apple
          </button>
        </div>
        <p>Séparateur ou s'inscrire par mail</p>
        <form class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
          <!-- Form inputs and submit button -->
        </form>
      </div>
    </div>

    <!-- Right column for pictures or design elements -->
    <div
      class="flex-1 hidden md:flex items-center justify-center p-4 bg-transparent border border-red-500"
    >
      <!-- Your design elements or picture goes here -->
      <div class="max-w-lg">
        <!-- <img src="path-to-your-image.jpg" alt="Design Element" /> -->
        <!-- Other design stuff -->
      </div>
    </div>
  </div>
</template>

<script>
import SignupBg from '@/components/backgrounds/SignupBg.vue'
export default {
  name: 'SignupView',
  components: { SignupBg }
}
</script>
<style postcss></style>
