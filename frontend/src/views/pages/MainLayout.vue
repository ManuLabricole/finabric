<!-- MainLayout.vue -->
<template>
  <NavigationBar />
  <HeaderComponent />
  <slot></slot>
  <!-- This is where page-specific content will go -->
</template>

<script>
import NavigationBar from '../../components/navbar/NavigationBar.vue'
import HeaderComponent from '../../components/header/HeaderComponent.vue'
export default {
  components: {
    NavigationBar,
    HeaderComponent
  }
}
</script>
