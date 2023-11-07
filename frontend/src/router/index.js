import { createRouter, createWebHistory } from 'vue-router'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/v1/signup',
      name: 'signup',
      component: () => import('../views/Signup.vue')
    }
  ]
})

export default router
