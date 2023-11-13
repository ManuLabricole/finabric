<template>
  <div class="relative w-full mb-3">
    <label
      for="password"
      :class="{
        'text-finaryYellow-500': isFocused || value,
        'text-sm': isFocused || value,
        'transform -translate-y-6': isFocused || value
      }"
      class="absolute left-0 top-50% h-full flex items-center pointer-events-none text-text-secondary text-lg font-normal transition-all duration-500 ease-in-out"
    >
      Mot de passe
    </label>
    <div class="flex items-center border-b border-text-secondary">
      <input
        id="password"
        :type="showPassword ? 'text' : 'password'"
        v-model="value"
        @focus="isFocused = true"
        @blur="isFocused = false"
        class="w-full h-12 p-0 pt-2 pb-1 m-0 bg-transparent text-medium text-text-primary ring-0 border-0 focus:outline-none focus:ring-0 focus:border-finaryYellow-400 transition-colors duration-500 ease-in-out"
        placeholder=""
      />
      <button type="button" class="p-2 text-text-primary" @click="togglePasswordVisibility">
        <i :class="showPassword ? 'bi bi-eye font-medium' : 'bi bi-eye-slash'"></i>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PasswordInput',
  props: {
    label: {
      type: String,
      default: 'Mot de passe'
    }
    // ... other props
  },
  data() {
    return {
      isFocused: false,
      value: '',
      showPassword: false
    }
  },
  methods: {
    focus() {
      this.isFocused = true
    },
    blur() {
      this.isFocused = false
    },
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword
    }
  }
}
</script>
