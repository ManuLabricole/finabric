<template>
  <div class="container-bg">
    <div class="transparency-bluring"></div>
    <div class="top-gradient"></div>
    <div class="bottom-blue"></div>
  </div>
</template>

<script>
export default {
  name: 'RegistrationBg'
}
</script>

<style postcss>
.container-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  background-color: #000000;
  overflow: hidden;
  z-index: -1;
}

.transparency-bluring {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  backdrop-filter: blur(100px);
  /* -webkit-backdrop-filter: blur(150px); */
  background: rgba(0, 0, 0, 0.6);
  overflow: hidden;
  z-index: 0;
}

.top-gradient {
  position: fixed;
  top: -200px;
  left: -225px;
  width: 350px;
  height: 600px;
  background: linear-gradient(
    to bottom,
    theme('colors.finaryYellow.500'),
    theme('colors.finaryYellow.500') 30%,
    theme('colors.finaryBlue.500') 75%
  );
  border-radius: 50%;
  z-index: -1;
}

.bottom-blue {
  position: fixed;
  bottom: -160px;
  left: -160px;
  width: 600px;
  height: 400px;
  background: linear-gradient(
    to bottom,
    theme('colors.finaryBlue.500'),
    theme('colors.finaryBlue.500') 30%,
    theme('colors.finaryBlue.500') 80%
  );
  border-radius: 50%;
  transform: rotate(-10deg);
  z-index: -1;
}
</style>
