<template>
  <div class="input-container">
    <input
      v-model="inputValue"
      placeholder="Email"
      @focus="isFocused = true"
      @blur="isFocused = false"
      class="border-b-2 border-red-300 focus:border-red-500 p-2 text-base outline-none transition-all duration-300"
    />
    <label :class="{ 'text-sm transform translate-y-[-1.5rem] translate-x-[-0.5rem] text-red-500': isFocused }">Your Label</label>
  </div>
</template>

<script>
export default {
  name: 'RegistrationBg'
}
</script>

<style lang="postcss" scoped></style>
