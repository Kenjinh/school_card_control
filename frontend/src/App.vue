<template>
  <div class="container text-center">
    <div class="row">
      <NavBar/>
    </div>
    <div class="row">
      <SchoolCards/>
    </div>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar";
import SchoolCards from "@/components/SchoolCards";

export default {
  name: 'App',
  components: {
    NavBar,
    SchoolCards
  }
}
</script>

<style>
</style>
