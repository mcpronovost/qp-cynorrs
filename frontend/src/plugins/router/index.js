import { createRouter, createWebHistory } from "vue-router"
import store from "@/plugins/store"

import HomeView from "@/views/HomeView.vue";
import ErrorView from "@/views/ErrorView.vue";

import { authRoutes } from "@/plugins/router/auth";
import { playerRoutes } from "@/plugins/router/player";
import { worldRoutes } from "@/plugins/router/world";

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomeView
  },
  /* ===--- FALLBACK ---=== */
  {
    path: "/:catchAll(.*)",
    name: "Error",
    component: ErrorView
  }
]

routes.push(...authRoutes)
routes.push(...playerRoutes)
routes.push(...worldRoutes)

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach(async (to, from, next) => {
    if (!("slug" in to.params)) {
        if (document.getElementById("qp-custom-style")) {
            document.getElementById("qp-custom-style").remove();
        }
    }
    store.dispatch("getPlayer")
    await store.restored
    next()
})

export default router
