<script setup lang="ts">
defineProps<{
  msg: string
}>()
</script>

<template>
  <img alt="kwotes logo" class="logo" src="@/assets/app-icon.png" width="64" height="64" />
  <div class="greetings">
    <h1 class="orange app-title">{{ msg }}</h1>
    <p>
      Dive into an ocean of wisdom.
    </p>
  </div>
</template>

<style scoped>
.greetings {
  h1 {
    font-size: 1.2rem;
    font-weight: 600;
    position: relative;
    font-family: "Poetsen One";
    /* top: -10px; */
  }
  
  p {
    font-size: 0.8rem;
  }
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
