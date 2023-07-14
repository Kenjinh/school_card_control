<template>
  <div class="container-fluid text-center py-4 px-5 mx-auto">
    <h1 class="text-light">Adicionar Aluno</h1>
    <form @submit.prevent="createStudent" class="w-50 m-auto">
      <div class="mb-3">
        <label class="form-label text-light" for="name">Nome:</label>
        <input class="form-control" type="text" id="name" v-model="student.name" required>
      </div>
      <div class="mb-3">
        <label class="form-label text-light" for="email">Email:</label>
        <input class="form-control" type="email" id="email" v-model="student.email" required>
      </div>
      <div class="mb-3">
        <label class="form-label text-light" for="birth_date">Data de Nascimento:</label>
        <input class="form-control" type="date" id="birth_date" v-model="student.birth_date" required>
      </div>

      <button class="btn btn-light" type="submit">Criar Aluno</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'StudentPage',
  props: {
    msg: String
  },
  data() {
    return {
      student: {
        name: '',
        email: '',
        birth_date: ''
      }
    };
  },
  methods: {
    async createStudent() {
      try {
        const response = await axios.post('http://10.0.4.151:8001/student/list/', this.student);

        if (response.status === 201) {
          alert('Aluno criado com sucesso!');
          this.student.name = '';
          this.student.email = '';
          this.student.birth_date = '';
        } else {
          alert('Erro ao criar aluno');
        }
      } catch (error) {
        console.error(error);
        alert('Erro ao criar aluno');
      }
    }
  }
}
</script>
