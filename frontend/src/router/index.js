import { createRouter, createWebHistory } from 'vue-router'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/auth/LoginView.vue')
    },
    {
      path: '/api/v1/signup',
      name: 'signup',
      component: () => import('../views/auth/SignupView.vue')
    },
    {
      path: '/api/v1/login',
      name: 'login',
      component: () => import('../views/auth/LoginView.vue')
    },
    {
      path: '/app/v1/dashboard',
      name: 'dashboard',
      component: () => import('../views/pages/DashboardView.vue')
    }
  ]
})

export default router
