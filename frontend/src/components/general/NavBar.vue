<template>
  <div class="nav-bar bg-black fixed-top">
    <ul class="nav justify-content-center">
      <li class="nav-item">
        <a class="nav-link active text-light" aria-current="page" href="/">Home</a>
      </li>
      <li class="nav-item">
        <router-link class="nav-link text-light" to="/boletim">Boletim</router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link text-light" to="/aluno">Aluno</router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link text-light" to="/materia/create">Materia</router-link>
      </li>
      <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle text-success" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Perfil
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Logout</a></li>
          </ul>
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