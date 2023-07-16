import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router';
import StudentPage  from '@/components/student/StudentPage.vue';
import SchoolCards from "@/components/school_card/SchoolCards";
import SchoolCardCreate from "@/components/school_card/SchoolCardCreate";
import SchoolCardEdit from "@/components//school_card/SchoolCardEdit";
import SubjectPage from "@/components/subject/SubjectPage"
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
  },
  {
    path: '/materia/create',
    name: 'Criar Matéria',
    component: SubjectPage

  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

createApp(App).use(router).mount('#app')
