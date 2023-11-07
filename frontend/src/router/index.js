import { createRouter, createWebHistory } from 'vue-router'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/SignupView.vue')
    },
    {
      path: '/api/v1/signup',
      name: 'signup',
      component: () => import('../views/SignupView.vue')
    }
  ]
})

export default router
