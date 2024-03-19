import { createRouter, createWebHistory } from 'vue-router'
import MainContentView from '../views/MainContentView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainContentView
    },
  ]
})

export default router
