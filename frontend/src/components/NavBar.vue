<template>
  <div class="navbar">
    <h1 class="navbar-brand">DeloitteSchool</h1>
    <ul v-if="cards && cards.length">
      <div v-for="card in cards" v-bind:key="card.id">
        {{ card.student_name }} - {{ card.delivery_date }}
        <table v-if="card.grades && card.grades">
          <thead>
            <tr>
              <th>Subject</th>
              <th>Grade</th>
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
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'NavBar',
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