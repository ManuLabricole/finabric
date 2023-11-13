<template>
  <div class="w-full">
    <label
      for="email"
      :class="{
        'text-finaryYellow-500': isFocused,
        'text-sm': isFocused
      }"
      class="w-full absolute transition-all pointer-events-none text-text-secondary text-lg font-semibold"
      >Votre email</label
    >
    <input
      id="email"
      type="email"
      v-model="email"
      @focus="isFocused = true"
      @blur="isFocused = false"
      class="w-full bg-transparent ring-0 focus:ring-0 border-0 border-b-2 focus:border-finaryYellow-500 text-text-primary text-lg font-semibold focus:transition-all ease-in-out transition delay-200"
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
<style postcss scoped>
/* Additional styles if needed */
label {
  transition: all 0.5s ease;
}
</style>
