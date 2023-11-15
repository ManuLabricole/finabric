<template>
  <div
    class="flex items-center justify-center rounded-full bg-success border-2 border-green-700 p-2"
  >
    <span class="emoji_left text-3xl -rotate-90">🎉</span>
    <!-- Increase emoji size with text-3xl -->
    <div class="mx-6">Félicitations ! Ton compte a été créé</div>
    <!-- Add some margin for spacing -->
    <span class="emoji_right text-3xl">🎉</span>
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

<style postcss scoped>
@keyframes rotateAndScaleRight {
  0%,
  100% {
    transform: rotate(-10deg) scale(1);
  }
  50% {
    transform: rotate(10deg) scale(1.1);
  }
}

@keyframes rotateAndScaleLeft {
  0%,
  100% {
    transform: rotate(-100deg) scale(1);
  }
  50% {
    transform: rotate(-80deg) scale(1.1);
  }
}

.emoji_right {
  animation: rotateAndScaleRight 0.5s ease-in-out 3; /* duration, timing function, iteration count */
}
.emoji_left {
  animation: rotateAndScaleLeft 0.5s ease-in-out 3; /* duration, timing function, iteration count */
}
</style>
