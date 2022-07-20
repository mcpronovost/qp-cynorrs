import AuthView from "@/views/AuthView.vue"

export const authRoutes = [
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
  }
]