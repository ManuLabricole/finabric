<template>
  <div
    class="flex items-center justify-center rounded-full bg-success border-2 border-green-700 p-2"
  >
    <span class="text-3xl mr-2">🎉</span>
    <!-- Increase emoji size with text-3xl -->
    <div class="mx-2">Félicitations ! Ton compte a été créé</div>
    <!-- Add some margin for spacing -->
    <span class="text-3xl ml-2">🎉</span>
    <!-- Increase emoji size with text-3xl -->
  </div>
</template>

<script>
import { useToastStore } from '@/stores/toast'
export default {
  name: 'ToastInfo',
  setup() {
    const toastStore = useToastStore()
    return { toastStore }
  }
}
</script>

<style postcss scoped></style>
