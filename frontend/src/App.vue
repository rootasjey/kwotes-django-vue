<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'

// The debounce function receives our function as a parameter
const debounce = (fn: Function) => {
  // This holds the requestAnimationFrame reference, so we can cancel it if we wish
  let frame: number | null = null;

  // The debounce function returns a new function that can receive a variable number of arguments
  return (...params: any) => {
    // If the frame variable has been defined, clear it now, and queue for next frame
    if (frame) {
      cancelAnimationFrame(frame);
    }

    // Queue our function call for the next frame
    frame = requestAnimationFrame(() => {

      // Call our function and pass any params we received
      fn(...params);
    });
  }
};


// Reads out the scroll position and stores it in the data attribute
// so we can use it in our stylesheets
const storeScroll = () => {
  document.documentElement.dataset.scroll = window.scrollY + '';
}

// Listen for new scroll events, here we debounce our `storeScroll` function
document.addEventListener('scroll', debounce(storeScroll), { passive: true });

// Update scroll position for first time
storeScroll();
</script>

<template>
  <div class="content">
    <RouterView />
  </div>

  <footer>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/themes">Themes</RouterLink>
      <RouterLink to="/about">About</RouterLink>
    </nav>
  </footer>
</template>

<style scoped>
.content {
  padding-bottom: 0px;
}

header {
  line-height: 1.5;
  max-height: 100vh;
  position: relative;
  top: 4rem;
  position: absolute;
  left: 0rem;
  right: 0;
}

nav {
  font-size: 12px;
  text-align: center;
  
  position: relative;
  bottom: 1.8rem;

  background-color: var(--color-background);
  border-radius: 24px;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    flex-direction: column;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
    align-items: center;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}

footer {
  display: flex;
  justify-content: center;
  align-items: center;
  justify-items: center;
  
  padding-top: 2rem;
  
  position: fixed;
  bottom: 0rem;
  left: 0;
  right: 0;
}
</style>
