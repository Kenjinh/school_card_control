import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router';
import StudentPage  from './components/StudentPage.vue';
import SchoolCards from "@/components/SchoolCards";
import SchoolCardCreate from "@/components/SchoolCardCreate";
import SchoolCardEdit from "@/components/SchoolCardEdit";
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: SchoolCards
  },
  {
    path: '/aluno',
    name: 'Aluno',
    component: StudentPage
  },
  {
    path: '/boletim',
    name: 'Criar Boletim',
    component: SchoolCardCreate
  },
  {
    path: '/boletim/edit/:cardId',
    name: 'Editar Boletim',
    component: SchoolCardEdit
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

createApp(App).use(router).mount('#app')
