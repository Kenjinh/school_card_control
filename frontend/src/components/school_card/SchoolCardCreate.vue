<template>
  <div class="container-fluid text-center py-4 px-5">
    <form @submit.prevent="createSchoolCard" class="row w-50 mx-auto p-5">
      <div class="mb-3">
        <label class="form-label text-light" for="student">Aluno:</label>
        <select class="form-select" id="student" v-model="selectedStudent" required>
          <option v-for="student in students" :key="student.id" :value="student.id">{{ student.name }}</option>
        </select>
      </div>

      <div class="mb-3">
        <label class="form-label text-light" for="delivery_date">Data de Entrega:</label>
        <input class="form-control" type="date" id="delivery_date" v-model="selectedDeliveryDate" required>
      </div>
      <div class="mb-3">
        <p class="fs-5 fw-bold text-light text-decoration-underline">Notas</p>
        <div v-for="subject in subjects" :key="subject.id">
          <div class="mb-3 col-12">
            <label class="form-label text-light" :for="'grade_' + subject.id">{{ subject.name }}:</label>
            <input min="0" max="10" step="0.01" class="form-control" :id="'grade_' + subject.id" type="number" v-model="grades[subject.id]" required>
          </div>
        </div>
      </div>
      <div class="mx-auto">
        <button class="btn btn-outline-light fw-bold" type="submit">Criar</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'BoletimPage',
  data() {
    return {
      students: [],
      subjects: [],
      selectedStudent: null,
      selectedDeliveryDate: null,
      grades: {},
    };
  },
  async mounted() {
    try {
      const studentResponse = await axios.get('http://localhost/api//student/list/');
      this.students = studentResponse.data;

      const subjectResponse = await axios.get('http://localhost/api/subject/list/');
      this.subjects = subjectResponse.data;

      this.subjects.forEach((subject) => {
        this.grades[subject.id] = 0;
      });
    } catch (error) {
      console.error(error);
      alert('Erro ao carregar alunos e matérias');
    }
  },
  methods: {
    async createSchoolCard() {
      try {
        const schoolCardResponse = await axios.post('http://localhost/api/school_card/list/', {
          student: this.selectedStudent,
          delivery_date: this.selectedDeliveryDate,
        });

        if (schoolCardResponse.status !== 201) {
          alert('Erro ao criar boletim');
          return;
        }

        const schoolCardId = schoolCardResponse.data.id;

        const gradePromises = Object.keys(this.grades).map((subjectId) => {
          return axios.post('http://localhost/api/school_card/grade/list/', {
            school_card: schoolCardId,
            subject: subjectId,
            grade: this.grades[subjectId],
          });
        });

        const gradeResponses = await Promise.all(gradePromises);

        const isSuccess = gradeResponses.every((response) => response.status === 201);
        if (isSuccess) {
          alert('Boletim e notas criados com sucesso!');
          this.selectedStudent = null;
          this.selectedDeliveryDate = null;
          Object.keys(this.grades).forEach((subjectId) => {
            this.grades[subjectId] = 0;
          });
        } else {
          alert('Erro ao criar notas');
        }
      } catch (error) {
        console.error(error);
        alert('Erro ao criar boletim e notas');
      }
    },
  },
};
</script>
