<template>
  <div class="nav-bar bg-black">
    <ul class="nav justify-content-center">
      <li class="nav-item">
        <a class="nav-link active text-light" aria-current="page" href="#">Active</a>
      </li>
      <li class="nav-item">
        <a class="nav-link text-light" href="#">Link</a>
      </li>
      <li class="nav-item">
        <a class="nav-link text-light" href="#">Link</a>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled text-secondary">Disabled</a>
      </li>
    </ul>
  </div>
</template>
<script>
export default {
  name: 'NavBar',
  props: {
    msg: String
  },
}
</script>
<style>
</style>