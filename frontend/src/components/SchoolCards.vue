<template>
  <ul v-if="cards && cards.length">
      <div v-for="card in cards" v-bind:key="card.id">
        <p>
          <a class="link-secondary" data-bs-toggle="collapse" role="button" aria-expanded="false" aria-controls="collapseExample" v-bind:href="'\#'+card.id">
              {{ card.student_name }} - {{ card.delivery_date }}
          </a>
        </p>
        <table v-if="card.grades && card.grades" class="table table-hover table-bordered collapse" v-bind:id="card.id">
          <thead>
            <tr>
              <th class="col">Subject</th>
              <th class="col">Grade</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="grade in card.grades" v-bind:key="grade.id">
              <td>{{grade.subject_name}}</td>
              <td>{{grade.grade}}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </ul>
</template>
<script>
import axios from 'axios'
export default {
  name: 'SchoolCards',
  props: {
    msg: String
  },
  data() {
    return {
      cards: [],
      errors: []
    }
  },
  created() {
    axios.get(`http://10.0.4.151:8001/school_card/list/`)
        .then(response => {
          // JSON responses are automatically parsed.
          this.cards = response.data
        })
        .catch(e => {
          this.errors.push(e)
        })
  }
}
</script>