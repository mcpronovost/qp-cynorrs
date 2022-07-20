import ForumIndexView from "@/views/forum/IndexView.vue"

export const worldRoutes = [
  {
    path: "/w:world_pk(\\d+)-:slug",
    name: "WorldForum",
    component: ForumIndexView
  },
  {
    path: "/w:world_pk(\\d+)-:slug/z:zone_pk(\\d+)-:zone_slug",
    name: "WorldForumZone",
    component: ForumIndexView
  },
  {
    path: "/w:world_pk(\\d+)-:slug/z:zone_pk(\\d+)-:zone_slug/t:territory_pk(\\d+)-:territory_slug",
    name: "WorldForumTerritory",
    component: ForumIndexView
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