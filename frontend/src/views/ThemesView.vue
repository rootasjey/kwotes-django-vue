<template>
  <div class="container">
    <!-- <div v-if="loading" class="loading">
      <img alt="kwotes logo" class="logo center" src="@/assets/animation.gif" width="125" height="125" />
      <p>Loading...</p>
    </div> -->

    <div class="idle">
      <div class="header">
        <img alt="kwotes logo" class="logo center" src="@/assets/app-icon.png" width="48" height="48" />

        <div class="sections">
          <div class="title" :class="{ active: value === option }" @click="value = option" v-for="option in options"
            :key="option">
            {{ option }}
          </div>
        </div>

      </div>

      <RainbowHR />

      <div v-if="loading" class="loading">
        <img alt="kwotes logo" class="logo center" src="@/assets/animation.gif" width="90" height="90" />
        <p>loading...</p>
      </div>

      <div v-else class="content">
        <div v-for="quote in quotes" :key="quote.id" class="quote">
          <h2 class="name">{{ quote.name }}</h2>
          <p class="author">- {{ quote.author__name }}</p>
          <!-- <p class="author">- {{ quote.author.name }}</p> -->
          <hr>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, type Ref, watch } from 'vue'
import RainbowHR from '@/components/RainbowHR.vue'

const loading = ref(false)
const error = ref("")
const quotes: Ref<any[]> = ref([])

const value = ref('recent');
const options = ref(['recent', 'einstein', 'le petit prince']);

watch(value, () => {
  if (value.value === 'recent') {
    fetchRecent()
    return
  }
  
  fetchTheme(value.value)
})

async function fetchRecent() {
  loading.value = true
  
  try {
    quotes.value = []
    const response = await fetch('http://127.0.0.1:8000/api/recent')
    const data = await response.json()
    const quotesArray = data.response.quotes

    for (const quote of quotesArray) {
      quotes.value.push(quote)
    }
  } catch (err) {
    error.value = "error"
  } finally {
    loading.value = false
  }
}

async function fetchTheme(themeKey: string) {
  loading.value = true
  
  try {
    quotes.value = []
    const response = await fetch('http://127.0.0.1:8000/api/search?q=' + themeKey)
    const data = await response.json()
    const quotesArray = data.response.quotes

    for (const quote of quotesArray) {
      quotes.value.push(quote)
    }
  } catch (err) {
    error.value = "error"
  } finally {
    loading.value = false
  }
}

fetchRecent()

</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  margin: 3rem auto;
  padding: 0 1rem;

  min-height: 100vh;
  width: 900px;
}

.loading {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin: auto;
  margin-top: 5rem;

  p {
    margin-top: 0rem;
    font-size: 1rem;
    font-weight: 400;
    text-transform: uppercase;
  }
}

.idle {
  display: flex;
  flex-direction: column;
  align-items: start;
}

.header {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;

  .sections {
    display: flex;
    
    .title {
      font-size: 1rem;
      font-weight: bold;
      line-height: 1rem;
      text-transform: uppercase;
      margin-right: 1rem;
      
      cursor: pointer;
      transition: all 0.2s;
    }
    
    .title.active {
      cursor: pointer;
      font-weight: 600;

      color: var(--primary-color);
    }

    .title::before {
      content: "•";
      margin-right: 1rem;
    }
  }

}

.quote {
  margin-bottom: 4rem;

  .name {
    font-size: 3rem;
    line-height: 5rem;
    font-weight: 200;
  }

  .author {
    font-size: 0.8rem;
    font-weight: 400;
  }

  hr {
    opacity: 0.1;
    margin: 2rem 0;
  }
}

.quote {
  margin-bottom: 1rem;
}

</style>
