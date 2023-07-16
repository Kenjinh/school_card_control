<template>
  <div class="container-fluid text-center pt-4">
    <form @submit.prevent="updateSchoolCard" class="w-50 m-auto p-5">
      <div class="mb-3">
        <label class="form-label text-light" for="student">Aluno:</label>
        <select class="form-select" id="student" v-model="boletimData.student" required>
          <option v-for="student in students" :key="student.id" :value="student.id">{{ student.name }}</option>
        </select>
      </div>

      <div class="mb-3">
        <label class="form-label text-light" for="delivery_date">Data de Entrega:</label>
        <input class="form-control" type="date" id="delivery_date" v-model="boletimData.delivery_date" required>
      </div>

      <div class="mb-3">
        <h2 class="text-light">Notas</h2>
        <div v-for="(grade, index) in boletimData.grades" :key="index" class="mb-3">
          <label class="form-label text-light" :for="'grade_' + index">{{ getSubjectName(grade.subject) }}:</label>
          <input class="form-control" :id="'grade_' + index" type="number" min="0" max="10" step="0.01"
                 v-model="grade.grade" required>
        </div>
      </div>

      <button class="btn btn-outline-light" type="submit">Atualizar Boletim</button>
    </form>
      <div v-if="!getAvailableSubjects">
        <form @submit.prevent="createGrade" class="w-50 m-auto">
          <h2 class="text-light">Adicionar Nova Grade</h2>
          <div class="mb-3">
            <label class="form-label text-light" for="new_grade_subject">Disciplina:</label>
            <select class="form-select" id="new_grade_subject" v-model="newGrade.subjectId" required>
              <option v-for="subject in getAvailableSubjects" :key="subject.id" :value="subject.id">{{ subject.name }}</option>
            </select>
          </div>
          <div class="mb-3">
            <label class="form-label text-light" for="new_grade_value">Nota:</label>
            <input class="form-control" id="new_grade_value" type="number" min="0" max="10" step="0.01"
                   v-model="newGrade.grade" required>
          </div>
          <button class="btn btn-outline-light" type="submit">Criar Grade</button>
        </form>
      </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'EditarBoletim',
  data() {
    return {
      boletimData: {
        student: null,
        delivery_date: '',
        grades: []
      },
      students: [],
      subjects: [],
      newGrade: {
        subjectId: null,
        grade: null
      }
    };
  },
  async mounted() {
    try {
      const subjectResponse = await axios.get('http://localhost/api/subject/list/');
      this.subjects = subjectResponse.data;
    } catch (error) {
      console.error(error);
      alert('Erro ao carregar matérias');
    }
  },
  created() {
    this.fetchData();
  },
  beforeRouteEnter(to, from, next) {
    const cardId = to.params.cardId;
    axios.get(`http://localhost/api/school_card/list/${cardId}/`)
        .then(response => {
          const boletimData = response.data;
          next(vm => {
            vm.boletimData = {
              student: boletimData.student,
              delivery_date: boletimData.delivery_date,
              grades: boletimData.grades
            };
          });
        })
        .catch(error => {
          console.error(error);
          next();
        });
  },
  computed: {
    getAvailableSubjects() {
      const usedSubjectIds = this.boletimData.grades.map(grade => grade.subject);
      return this.subjects.filter(subject => !usedSubjectIds.includes(subject.id));
    }
  },
  methods: {
    fetchData() {
      axios.get('http://localhost/api/student/list/')
          .then(response => {
            this.students = response.data;
          })
          .catch(error => {
            console.error(error);
          });

      axios.get('http://localhost/api/subject/list/')
          .then(response => {
            this.subjects = response.data;
          })
          .catch(error => {
            console.error(error);
          });
    },
    async updateSchoolCard() {
      const cardId = this.$route.params.cardId;
      try {
        const boletimData = {
          student: this.boletimData.student,
          delivery_date: this.boletimData.delivery_date,
          grades: this.boletimData.grades
        };
        await axios.put(`http://localhost/api/school_card/list/${cardId}/`, boletimData);
        for (let grade of this.boletimData.grades) {
          await axios.put(`http://localhost/api/school_card/grade/list/${grade.id}/`, grade);
        }

        alert('Boletim atualizado com sucesso!');
        this.$router.push('/');
      } catch (error) {
        console.error(error);
      }
    },
    createGrade() {
      const cardId = this.$route.params.cardId;
      const gradeData = {
        subject: this.newGrade.subjectId,
        school_card: cardId,
        grade: this.newGrade.grade
      };

      axios.post('http://localhost/api/school_card/grade/list/', gradeData)
        .then(response => {
          if (response.status === 201) {
            console.log('Grade criada com sucesso!');
            this.getGrades(cardId);
            this.newGrade.subjectId = null;
            this.newGrade.grade = null;
            window.location.reload()
          } else {
            alert('Erro ao criar grade');
          }
        })
        .catch(error => {
          console.error(error);
          alert('Erro ao criar grade');
        });
    },
    getSubjectName(subjectId) {
      const subject = this.subjects.find(subject => subject.id === subjectId);
      return subject ? subject.name : '';
    },
    getGrades(cardId) {
      return axios.get(`http://localhost/api/school_card/grade/list/?school_card=${cardId}`)
          .then(response => {
            console.log(response.data);
            return response.data;
          })
          .catch(error => {
            console.error(error);
          });
    },
  }
};
</script>
