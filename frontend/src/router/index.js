import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Login from '@/components/Login'
import Signup from '@/components/Signup'
import GPHome from '@/components/GPHome'
import Tickets from '@/components/Tickets'
import GPForm from '@/components/GPForm'
import TicketForm from '@/components/TicketForm'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/gps',
    name: 'GPHome',
    component: GPHome
  },
  {
    path: '/gps/add',
    name: 'GPForm',
    component: GPForm
  },
  {
    path: '/tickets/:gp_id',
    name: 'Tickets',
    component: Tickets
  },
  {
    path: '/tickets/add',
    name: 'TicketForm',
    component: TicketForm,
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
