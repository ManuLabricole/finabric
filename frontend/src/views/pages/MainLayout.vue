<!-- MainLayout.vue -->
<template>
  <NavigationBar />
  <TopBar />
  <slot></slot>
  <!-- This is where page-specific content will go -->
</template>

<script>
import NavigationBar from '../../components/navbar/NavigationBar.vue'
import TopBar from '../../components/header/HeaderComponent.vue'

export default {
  components: {
    NavigationBar,
    TopBar
  }
}
</script>
