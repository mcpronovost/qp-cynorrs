import { createRouter, createWebHistory } from "vue-router"
import store from "@/plugins/store"

import HomeView from "@/views/HomeView.vue";
import MeWorldsView from "@/views/player/MeWorldsView.vue";
import HeroDetailView from "@/views/player/HeroDetailView.vue";
import ErrorView from "@/views/ErrorView.vue";

import { authRoutes } from "@/plugins/router/auth";
import { worldRoutes } from "@/plugins/router/world";

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomeView
  },
  /* ===--- PLAYER ---=== */
  {
    path: "/me/characters",
    name: "MeCharacters",
    component: MeWorldsView
  },
  {
    path: "/me/worlds",
    name: "MeWorlds",
    component: MeWorldsView
  },
  {
    path: "/heros/:pk",
    name: "HeroDetail",
    component: HeroDetailView
  },
  /* ===--- FALLBACK ---=== */
  {
    path: "/:catchAll(.*)",
    name: "Error",
    component: ErrorView
  }
]

routes.push(...authRoutes)
routes.push(...worldRoutes)

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach(async (to, from, next) => {
    if (!("world_pk" in to.params)) {
        if (document.getElementById("qp-custom-style")) {
            document.getElementById("qp-custom-style").remove();
        }
    }
    store.dispatch("getPlayer")
    await store.restored
    next()
})

export default router
