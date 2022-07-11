import { createRouter, createWebHistory } from "vue-router"
import store from "@/plugins/store"
import HomeView from "@/views/HomeView.vue"
import AboutView from "@/views/AboutView.vue"
import HeroDetailView from "@/views/player/HeroDetailView.vue"
import ErrorView from "@/views/ErrorView.vue"

import SagarsView from "@/views/test/SagarsView";
import RhansidorView from "@/views/test/RhansidorView";

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomeView
  },
  {
    path: "/about",
    name: "About",
    component: AboutView
  },
  {
    path: "/profile",
    name: "Profile",
    component: AboutView
  },
  /* ===--- PLAYER ---=== */
  {
    path: "/heros/:pk",
    name: "HeroDetail",
    component: HeroDetailView
  },
  /* ===--- test ---=== */
  {
    path: "/sagars",
    name: "Sagars",
    component: SagarsView
  },
  {
    path: "/rhansidor",
    name: "Rhansidor",
    component: RhansidorView
  },
  /* ===--- FALLBACK ---=== */
  {
    path: "/:catchAll(.*)",
    name: "Error",
    component: ErrorView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach(async (to, from, next) => {
    store.dispatch("getPlayer")
    await store.restored
    next()
})

export default router
