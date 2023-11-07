<template>
  <h1>Hello World</h1>
  <button @click="sayHello">Say Hello</button>
</template>

<script>
export default {
  name: 'SignupView',
  data() {
    return {
      title: 'Hello World'
    }
  },
  methods: {
    sayHello() {
      alert(this.title)
    }
  }
}
</script>

<style lang="postcss" scoped></style>
