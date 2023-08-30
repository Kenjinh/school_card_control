<template>
  <div id="app">
    <NavBar/>
    <div class="router-view-container">
      <router-view/>
    </div>
  </div>
</template>

<script>
import '@/assets/scss/general.scss'
import NavBar from "@/components/general/NavBar";
export default {
  name: 'App',
  components: {
    NavBar
  }
}
</script>
