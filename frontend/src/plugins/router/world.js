import WorldView from "@/views/WorldView.vue"
import ForumIndexView from "@/views/forum/IndexView.vue"
import ForumZoneView from "@/views/forum/ZoneView.vue"
import ForumTerritoryView from "@/views/forum/TerritoryView.vue"

export const worldRoutes = [
  {
    path: "/w/:slug",
    name: "World",
    component: WorldView,
    children: [
      {
        path: "forum",
        name: "WorldForum",
        component: ForumIndexView
      },
      {
        path: "forum/z:zone_pk(\\d+)-:zone_slug",
        name: "WorldForumZone",
        component: ForumZoneView
      },
      {
        path: "forum/z:zone_pk(\\d+)-:zone_slug/t:territory_pk(\\d+)-:territory_slug",
        name: "WorldForumTerritory",
        component: ForumTerritoryView
      }
    ]
  },
  {
    path: "/w:world_pk(\\d+)-:slug/z:zone_pk(\\d+)-:zone_slug/t:territory_pk(\\d+)-:territory_slug/s:sector_pk(\\d+)-:sector_slug",
    name: "WorldForumSector",
    component: ForumIndexView
  },
  {
    path: "/w:world_pk(\\d+)-:slug/z:zone_pk(\\d+)-:zone_slug/t:territory_pk(\\d+)-:territory_slug/c:chapter_pk(\\d+)-:chapter_slug",
    name: "WorldForumChapter",
    component: ForumIndexView
  },
  {
    path: "/w:world_pk(\\d+)-:slug/z:zone_pk(\\d+)-:zone_slug/t:territory_pk(\\d+)-:territory_slug/s:sector_pk(\\d+)-:sector_slug/c:chapter_pk(\\d+)-:chapter_slug",
    name: "WorldForumSectorChapter",
    component: ForumIndexView
  }
]