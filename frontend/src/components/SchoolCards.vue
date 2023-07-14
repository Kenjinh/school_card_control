<template>
  <div class="container-fluid text-center pt-4">
    <div class="row">
      <ul v-if="cards && cards.length">
        <div v-for="card in cards" :key="card.id" class="school-card p-4 mt-5 shadow-lg">
          <table class="table table-hover table-bordered">
            <thead>
              <tr>
                <th class="col">{{ card.student_name }}</th>
                <th class="col">{{ card.delivery_date }}</th>
                <th class="col"><a class="link-primary p-2" @click="editCard(card.id)">Editar</a></th>
                <th class="col"><a class="link-danger p-2" @click="deleteCard(card.id)">Deletar</a></th>
              </tr>
            </thead>
          </table>
          <table v-if="card.grades && card.grades" class="table table-hover table-bordered" :id="card.id">
            <thead>
              <tr>
                <th class="col">Subject</th>
                <th class="col">Grade</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="grade in card.grades" :key="grade.id">
                <td>{{ grade.subject_name }}</td>
                <td>{{ grade.grade }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </ul>
      <div v-if="isLoading" class="text-center mt-3">
        <span class="spinner-border"></span>
      </div>
      <div v-if="!isAllLoaded" class="text-center mt-3">
        <button class="btn btn-primary" @click="loadMoreCards">Carregar Mais</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SchoolCards',
  props: {
    msg: String,
  },
  data() {
    return {
      cards: [],
      errors: [],
      isLoading: false,
      isAllLoaded: false,
      offset: 0,
      limit: 10,
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      axios
        .get(`http://10.0.4.151:8001/school_card/list/?offset=${this.offset}&limit=${this.limit}`)
        .then((response) => {
          this.cards = response.data;
          if (response.data.length < this.limit) {
            this.isAllLoaded = true;
          }
        })
        .catch((e) => {
          this.errors.push(e);
        });
    },
    editCard(cardId) {
      this.$router.push(`/boletim/edit/${cardId}`);
      console.log('Editar boletim:', cardId);
    },
    deleteCard(cardId) {
      if (confirm('Tem certeza que deseja excluir este boletim?')) {
        axios
          .delete(`http://10.0.4.151:8001/school_card/list/${cardId}/`)
          .then((response) => {
            if (response.status === 204) {
              alert('Boletim excluído com sucesso!');
              this.fetchData();
            } else {
              alert('Erro ao excluir o boletim');
            }
          })
          .catch((error) => {
            console.error(error);
            alert('Erro ao excluir o boletim');
          });
      }
    },
    loadMoreCards() {
      this.isLoading = true;
      this.offset += this.limit;

      axios
        .get(`http://10.0.4.151:8001/school_card/list/?offset=${this.offset}&limit=${this.limit}`)
        .then((response) => {
          const newCards = response.data;
          if (newCards.length === 0) {
            this.isAllLoaded = true;
          } else {
            this.cards = [...this.cards, ...newCards];
          }
          this.isLoading = false;
        })
        .catch((error) => {
          console.error(error);
          alert('Erro ao carregar mais cards');
          this.isLoading = false;
        });
    },
  },
};
</script>
