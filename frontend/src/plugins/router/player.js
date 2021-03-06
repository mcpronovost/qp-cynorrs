import MeProfileView from "@/views/player/MeProfileView.vue";
import MeCharactersView from "@/views/player/MeCharactersView.vue";
import MeCharactersHerosDetailView from "@/views/player/MeCharactersHerosDetailView.vue";
import MeWorldsView from "@/views/player/MeWorldsView.vue";
import MeWorldsDetailView from "@/views/player/MeWorldsDetailView.vue";

export const playerRoutes = [
    {
        path: "/me/profile",
        name: "MeProfile",
        component: MeProfileView
    },
    {
        path: "/me/characters",
        name: "MeCharacters",
        component: MeCharactersView
    },
    {
        path: "/me/characters/heros/:pk",
        name: "MeCharactersHerosDetail",
        component: MeCharactersHerosDetailView
    },
    {
        path: "/me/worlds",
        name: "MeWorlds",
        component: MeWorldsView
    },
    {
        path: "/me/worlds/:pk",
        name: "MeWorldsDetail",
        component: MeWorldsDetailView
    }
]