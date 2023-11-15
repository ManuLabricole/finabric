<template>
  <div class="flex-1 xl:block items-center justify-center p-4 bg-transparent border border-red-500">
    <ToastInfo />
    <p class="text-secondary">OUI</p>
    <!-- Your design elements or picture goes here -->
    <!-- <div class="max-w-lg">
     <img src="path-to-your-image.jpg" alt="Design Element" /> -->
    <!-- Other design stuff -->
    <!-- </div> -->
  </div>
</template>

<script>
import ToastInfo from '../common/ToastInfo.vue'
export default {
  name: 'RightDesign',
  components: { ToastInfo }
}
</script>

<style lang="postcss" scoped></style>
