<template>
  <div class="border">Logo</div>
  <div class="mb-4">
    <h1 class="text-white text-4xl font-normal tracking-wider mb-1">Créer mon compte</h1>
    <span class="text-gray-500 font-small"
      >J'ai déjà un compte.
      <a class="text-finaryYellow-500 hover:text-finaryYellow-600" href="/"
        >Se connecter >
      </a></span
    >
  </div>
  <!-- Button connexion Apple / Google -->
  <div class="flex flex-col w-full space-y-2">
    <button class="bg-button-google w-full rounded-full p-3 text-text-primary">
      <i class="bi bi-google mr-2 font"></i>
      Continuer avec Google
    </button>
    <button class="bg-button-apple w-full rounded-full p-3 text-text-black">
      <i class="bi bi-apple mr-2 font-bold"></i>
      Continuer avec Apple
    </button>
  </div>
  <div class="flex items-center justify-center my-4">
    <div class="flex-1 border-t border-text-secondary"></div>
    <span class="px-4 text-xs text-gray-600 uppercase">Ou s'inscrire par email</span>
    <div class="flex-1 border-t border-text-secondary"></div>
  </div>
</template>

<script>
export default {
  name: 'RegisterTop'
}
</script>

<style lang="postcss" scoped></style>
