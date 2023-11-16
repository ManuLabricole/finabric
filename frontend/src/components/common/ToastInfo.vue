<template>
  <transition name="toast-slide">
    <div v-if="toastStore.isVisible" class="r">
      <div
        class="inline-flex items-center justify-between rounded-lg p-3 bg-success border-2 border-green-700"
        :style="toastStore.showAnimation ? 'transform: translateY(0); opacity: 1;' : ''"
      >
        <div class="flex items-center">
          <span class="emoji_left text-3xl -rotate-90">🎉</span>
          <div class="mx-6">Félicitations ! Ton compte a été créé</div>
          <span class="emoji_right text-3xl">🎉</span>
        </div>
        <!-- Close button -->
        <button @click="closeToast" class="flex ml-10 text-lg font-bold">&times;</button>
      </div>
    </div>
  </transition>
  <button @click="toastAppear" class="flex bg-red">SHOW TOAST</button>
</template>

<script>
import { useToastStore } from '@/stores/toast'

export default {
  name: 'ToastInfo',
  setup() {
    const toastStore = useToastStore()

    const closeToast = () => {
      toastStore.showAnimation = false // Disable the animation
      setTimeout(() => {
        toastStore.isVisible = false // Hide the toast after the animation
      }, 500) // Adjust the timing to match your animation duration
    }

    const toastAppear = () => {
      toastStore.showToast('inf', 'Félicitations ! Ton compte a été créé')
    }

    return { toastStore, closeToast, toastAppear }
  }
}
</script>

<style postcss scoped>
.toast-slide-enter-active,
.toast-slide-leave-active {
  transition:
    transform 0.5s ease-out,
    opacity 0.5s ease-out;
}

.toast-slide-enter-from,
.toast-slide-leave-to {
  transform: translateY(150%); /* Start from below the parent element */
  opacity: 0; /* Start with opacity 0 */
}

.close-button {
  cursor: pointer;
  background-color: transparent;
  border: none;
  font-size: 1.2rem;
  color: white;
}

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
  animation: rotateAndScaleRight 0.2s ease-in-out 6; /* duration, timing function, iteration count */
}
.emoji_left {
  animation: rotateAndScaleLeft 0.2s ease-in-out 6; /* duration, timing function, iteration count */
}
</style>
