import { createRouter, createWebHistory } from "vue-router"
import store from "@/plugins/store"
import HomeView from "@/views/HomeView.vue"
import AuthView from "@/views/AuthView.vue"
import AboutView from "@/views/AboutView.vue"
import HeroDetailView from "@/views/player/HeroDetailView.vue"
import ForumIndexView from "@/views/forum/IndexView.vue"
import ErrorView from "@/views/ErrorView.vue"

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomeView
  },
  {
    path: "/register",
    name: "AuthRegister",
    component: AuthView
  },
  {
    path: "/login",
    name: "AuthLogin",
    component: AuthView
  },
  {
    path: "/logout",
    name: "AuthLogout",
    component: AuthView
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
  /* ===--- WORLD ---=== */
  {
    path: "/w:world_pk(\\d+)-:slug",
    name: "World",
    component: ForumIndexView
  },
  {
    path: "/w:world_pk(\\d+)-:slug/z:zone_pk(\\d+)-:zone_slug",
    name: "WorldZone",
    component: ForumIndexView
  },
  {
    path: "/w:world_pk(\\d+)-:slug/z:zone_pk(\\d+)-:zone_slug/t:territory_pk(\\d+)-:territory_slug",
    name: "WorldTerritory",
    component: ForumIndexView
  },
  {
    path: "/w:world_pk(\\d+)-:slug/z:zone_pk(\\d+)-:zone_slug/t:territory_pk(\\d+)-:territory_slug/s:sector_pk(\\d+)-:sector_slug",
    name: "WorldSector",
    component: ForumIndexView
  },
  {
    path: "/w:world_pk(\\d+)-:slug/z:zone_pk(\\d+)-:zone_slug/t:territory_pk(\\d+)-:territory_slug/c:chapter_pk(\\d+)-:chapter_slug",
    name: "WorldChapter",
    component: ForumIndexView
  },
  {
    path: "/w:world_pk(\\d+)-:slug/z:zone_pk(\\d+)-:zone_slug/t:territory_pk(\\d+)-:territory_slug/s:sector_pk(\\d+)-:sector_slug/c:chapter_pk(\\d+)-:chapter_slug",
    name: "WorldSectorChapter",
    component: ForumIndexView
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
