<template>
  <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
  <input
    id="email"
    type="email"
    class="mt-1 block w-full rounded-md border-gray-300 text-input focus:border-input-focus focus:ring focus:ring-input-focus focus:ring-opacity-50"
    placeholder="you@example.com"
  />
  <p class="mt-2 text-sm text-validation-error">
    <!-- Error message will go here -->
  </p>
</template>
