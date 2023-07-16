<template>
  <div class="container-fluid text-center py-4 px-5 mx-auto">
    <form @submit.prevent="addSubject" class="w-50 m-auto p-5">
      <div class="mb-3">
        <label for="name" class="form-label text-light">Nome da Materia</label>
        <input type="text" id="name" v-model="subject.name" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="hourly_load" class="form-label text-light">Carga Horária</label>
        <input type="number" id="hourly_load" v-model="subject.hourly_load" class="form-control" required>
      </div>
      <button type="submit" class="btn btn-outline-light fw-bold">Adicionar</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SubjectPage',
  props: {
    msg: String
  },
  data() {
    return {
      subject: {
        name: '',
        hourly_load: ''
      },

    };
  },
  methods: {
    addSubject() {
      const response = axios.post('http://localhost/api/subject/list/', this.subject)
      if (response.status === 201) {
        alert('Matéria criada com sucesso!');
        this.subject.name = '';
        this.subject.hourly_load = '';
      } else {
        alert('Erro ao criar a matéria');
      }
    },
  },
};
</script>
