<template>
  <div class="flex flex-col justify-between space-y-8">
    <div class="w-1/4 mb-8">
      <img src="../../assets/finabric_high.png" alt="" />
    </div>
    <div class="mb-8 mt-8">
      <h1 class="text-white text-4xl font-normal tracking-wider mb-1">{{ title }}</h1>
      <span class="flex align-center text-gray-500 font-small"
        >{{ subtitle }}
        <router-link
          :to="{name : anchorLink}"
          class="ml-2 text-finaryYellow-500 hover:text-finaryYellow-600"
        >
          {{ anchorText }}<i class="bi bi-caret-right-fill ml-2"></i>
        </router-link>
      </span>
    </div>
    <!-- Button connexion Apple / Google -->
    <div class="flex flex-col w-full space-y-2">
      <button class="bg-button-google w-full rounded-full p-3 text-primary">
        <i class="bi bi-google mr-2 font"></i>
        Continuer avec Google
      </button>
      <button class="bg-button-apple w-full rounded-full p-3 text-black">
        <i class="bi bi-apple mr-2 font-bold"></i>
        Continuer avec Apple
      </button>
    </div>
    <div class="flex items-center justify-center my-4">
      <div class="flex-1 border-t border-secondary"></div>
      <span class="px-4 text-xs text-gray-600 uppercase">{{ breakText }}</span>
      <div class="flex-1 border-t border-secondary"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RegisterTop',
  props: {
    title: String,
    subtitle: String,
    anchorText: String,
    anchorLink: String,
    breakText: String
  }
}
</script>

<style lang="postcss" scoped></style>
