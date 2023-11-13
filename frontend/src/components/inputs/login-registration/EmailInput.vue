<template>
  <div class="relative w-full">
    <label
      for="email"
      :class="{
        'text-finaryYellow-500': isFocused || email,
        'text-sm': isFocused || email,
        'transforme -translate-y-6': isFocused || email
      }"
      class="absolute left-0 top-50% h-full flex items-center pointer-events-none text-text-secondary text-lg font-normal transition-all duration-500 ease-in-out"
      >Votre email</label
    >
    <input
      id="email"
      type="email"
      v-model="email"
      @focus="isFocused = true"
      @blur="isFocused = false"
      :class="{
        'border-finaryYellow-500': isFocused || email,
        'border-text-secondary': !isFocused && !email,
        'text-finaryYellow-500': isFocused || email,
        'text-text-secondary': !isFocused && !email
      }"
      class="w-full h-12 p-0 pt-2 pb-1 m-0 bg-transparent text-text-primary ring-0 border-0 border-b focus:outline-none focus:ring-0 focus:border-finaryYellow-400 transition-colors duration-500 ease-in-out"
      placeholder=""
    />
  </div>
</template>

<script>
export default {
  name: 'EmailInput',
  data() {
    return {
      email: '',
      isFocused: false
    }
  }
}
</script>

<style postcss scoped></style>
