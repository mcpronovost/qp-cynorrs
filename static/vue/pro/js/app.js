(function(){"use strict";var e={8569:function(e,t,n){var r=n(9242),a=n(3396);const o={id:"qp-app"},l={id:"qp-app-main"};function i(e,t,n,r,i,u){const d=(0,a.up)("qp-header"),s=(0,a.up)("qp-sidebar"),p=(0,a.up)("router-view"),m=(0,a.up)("el-scrollbar"),c=(0,a.up)("qp-smallbar");return(0,a.wg)(),(0,a.iD)("div",o,[(0,a.Wm)(d),(0,a.Wm)(s),(0,a._)("div",l,[(0,a.Wm)(m,{height:"100%"},{default:(0,a.w5)((()=>[(0,a.Wm)(p)])),_:1})]),(0,a.Wm)(c)])}const u={id:"qp-app-header"},d={id:"qp-header-logo"},s=["src"];function p(e,t,n,r,o,l){const i=(0,a.up)("el-col"),p=(0,a.up)("el-row");return(0,a.wg)(),(0,a.iD)("div",u,[(0,a.Wm)(p,{gutter:20},{default:(0,a.w5)((()=>[(0,a.Wm)(i,{span:24},{default:(0,a.w5)((()=>[(0,a._)("div",d,[(0,a._)("img",{src:o.logo,alt:""},null,8,s)])])),_:1})])),_:1})])}var m={name:"qpHeader",data(){return{logo:"/static/ico/favicon-180.png"}}},c=n(89);const f=(0,c.Z)(m,[["render",p],["__scopeId","data-v-62b314d8"]]);var w=f,_=n(7139);const v=e=>((0,a.dD)("data-v-e87590ec"),e=e(),(0,a.Cn)(),e),g={id:"qp-app-sidebar"},W={id:"qp-sidebar-profile"},b={id:"qp-sidebar-banner"},h=v((()=>(0,a._)("div",{class:"image-slot"},null,-1))),x={id:"qp-sidebar-avatar"},q=v((()=>(0,a._)("div",{class:"image-slot"},null,-1))),S={id:"qp-sidebar-name"},y=["textContent"],k={id:"qp-sidebar-title"},C=["textContent"],O={id:"qp-sidebar-nav"},Z=v((()=>(0,a._)("i",{class:"mdi mdi-home"},null,-1))),T=v((()=>(0,a._)("span",{textContent:"Home"},null,-1))),E=v((()=>(0,a._)("i",{class:"mdi mdi-hops"},null,-1))),U=v((()=>(0,a._)("span",{textContent:"About"},null,-1))),D=v((()=>(0,a._)("i",{class:"mdi mdi-bookshelf"},null,-1))),I=v((()=>(0,a._)("span",null,"Navigator One",-1))),$=v((()=>(0,a._)("span",{textContent:"item one"},null,-1))),A=v((()=>(0,a._)("span",{textContent:"item two"},null,-1))),N=v((()=>(0,a._)("span",null,"Navigator two",-1))),j=v((()=>(0,a._)("span",{textContent:"item one"},null,-1))),H=v((()=>(0,a._)("span",{textContent:"item two"},null,-1))),P=v((()=>(0,a._)("i",{class:"mdi mdi-home"},null,-1))),z=v((()=>(0,a._)("span",null,"Navigator One",-1))),G=(0,a.Uk)("item one"),M=(0,a.Uk)("item one"),R=(0,a.Uk)("item three"),F=(0,a.Uk)("item four"),J=(0,a.Uk)("item one"),V=v((()=>(0,a._)("i",{class:"mdi mdi-home"},null,-1))),L=v((()=>(0,a._)("span",null,"Navigator One",-1))),Q=(0,a.Uk)("item one"),B=(0,a.Uk)("item one"),K=(0,a.Uk)("item three"),X=(0,a.Uk)("item four"),Y=(0,a.Uk)("item one");function ee(e,t,n,r,o,l){const i=(0,a.up)("el-image"),u=(0,a.up)("el-menu-item"),d=(0,a.up)("el-sub-menu"),s=(0,a.up)("el-menu-item-group"),p=(0,a.up)("el-menu"),m=(0,a.up)("el-scrollbar");return(0,a.wg)(),(0,a.iD)("div",g,[(0,a.Wm)(m,{height:"100%"},{default:(0,a.w5)((()=>[(0,a._)("div",W,[(0,a._)("div",b,[(0,a.Wm)(i,{src:o.banner,fit:"cover"},{error:(0,a.w5)((()=>[h])),_:1},8,["src"])]),(0,a._)("div",x,[(0,a.Wm)(i,{src:o.avatar,fit:"cover"},{error:(0,a.w5)((()=>[q])),_:1},8,["src"])]),(0,a._)("div",S,[(0,a._)("h2",null,[(0,a._)("span",{textContent:(0,_.zw)(o.name)},null,8,y)])]),(0,a._)("div",k,[(0,a._)("p",null,[(0,a._)("span",{textContent:(0,_.zw)(o.title)},null,8,C)])])]),(0,a._)("div",O,[(0,a.Wm)(p,{router:"",collapse:e.app.win.w<1200},{default:(0,a.w5)((()=>[(0,a.Wm)(u,{index:"1",route:{name:"Home"}},{default:(0,a.w5)((()=>[Z,T])),_:1}),(0,a.Wm)(u,{index:"2",route:{name:"About"}},{default:(0,a.w5)((()=>[E,U])),_:1}),(0,a.Wm)(d,{index:"3"},{title:(0,a.w5)((()=>[D,I])),default:(0,a.w5)((()=>[(0,a.Wm)(u,{index:"1-1"},{default:(0,a.w5)((()=>[$])),_:1}),(0,a.Wm)(u,{index:"1-2"},{default:(0,a.w5)((()=>[A])),_:1}),(0,a.Wm)(d,{index:"8"},{title:(0,a.w5)((()=>[N])),default:(0,a.w5)((()=>[(0,a.Wm)(u,{index:"1-1"},{default:(0,a.w5)((()=>[j])),_:1}),(0,a.Wm)(u,{index:"1-2"},{default:(0,a.w5)((()=>[H])),_:1})])),_:1})])),_:1}),(0,a.Wm)(d,{index:"4"},{title:(0,a.w5)((()=>[P,z])),default:(0,a.w5)((()=>[(0,a.Wm)(s,{title:"Group One"},{default:(0,a.w5)((()=>[(0,a.Wm)(u,{index:"1-1"},{default:(0,a.w5)((()=>[G])),_:1}),(0,a.Wm)(u,{index:"1-2"},{default:(0,a.w5)((()=>[M])),_:1})])),_:1}),(0,a.Wm)(s,{title:"Group Two"},{default:(0,a.w5)((()=>[(0,a.Wm)(u,{index:"1-3"},{default:(0,a.w5)((()=>[R])),_:1})])),_:1}),(0,a.Wm)(d,{index:"1-4"},{title:(0,a.w5)((()=>[F])),default:(0,a.w5)((()=>[(0,a.Wm)(u,{index:"1-4-1"},{default:(0,a.w5)((()=>[J])),_:1})])),_:1})])),_:1}),(0,a.Wm)(d,{index:"5"},{title:(0,a.w5)((()=>[V,L])),default:(0,a.w5)((()=>[(0,a.Wm)(s,{title:"Group One"},{default:(0,a.w5)((()=>[(0,a.Wm)(u,{index:"1-1"},{default:(0,a.w5)((()=>[Q])),_:1}),(0,a.Wm)(u,{index:"1-2"},{default:(0,a.w5)((()=>[B])),_:1})])),_:1}),(0,a.Wm)(s,{title:"Group Two"},{default:(0,a.w5)((()=>[(0,a.Wm)(u,{index:"1-3"},{default:(0,a.w5)((()=>[K])),_:1})])),_:1}),(0,a.Wm)(d,{index:"1-4"},{title:(0,a.w5)((()=>[X])),default:(0,a.w5)((()=>[(0,a.Wm)(u,{index:"1-4-1"},{default:(0,a.w5)((()=>[Y])),_:1})])),_:1})])),_:1})])),_:1},8,["collapse"])])])),_:1})])}var te=n(65),ne={name:"qpSidebar",data(){return{banner:"",avatar:"",name:"M-C Pronovost",title:"Qui ne fait que passer"}},computed:{...(0,te.Se)(["app"])},methods:{clickMenu(e){console.log(e)}}};const re=(0,c.Z)(ne,[["render",ee],["__scopeId","data-v-e87590ec"]]);var ae=re;const oe={id:"qp-app-smallbar"};function le(e,t,n,r,o,l){return(0,a.wg)(),(0,a.iD)("div",oe," smallbar ")}var ie={name:"qpSmallbar"};const ue=(0,c.Z)(ie,[["render",le],["__scopeId","data-v-32db5772"]]);var de=ue,se={name:"App",components:{qpHeader:w,qpSidebar:ae,qpSmallbar:de},data(){return{test:this.$route}},mounted(){this.$store.commit("SET_DRAT","start"),this.$store.commit("SET_FRAT","end")}};const pe=(0,c.Z)(se,[["render",i]]);var me=pe,ce=n(678);const fe={class:"qp-vue"},we=(0,a.Uk)("card"),_e=(0,a.Uk)("card"),ve=(0,a.Uk)("card");function ge(e,t,n,r,o,l){const i=(0,a.up)("qp-card"),u=(0,a.up)("el-col"),d=(0,a.up)("el-row");return(0,a.wg)(),(0,a.iD)("div",fe,[(0,a.Wm)(d,{gutter:20},{default:(0,a.w5)((()=>[(0,a.Wm)(u,{span:24},{default:(0,a.w5)((()=>[(0,a.Wm)(i,null,{default:(0,a.w5)((()=>[we])),_:1})])),_:1})])),_:1}),(0,a.Wm)(d,{gutter:20},{default:(0,a.w5)((()=>[(0,a.Wm)(u,{md:12,lg:8},{default:(0,a.w5)((()=>[(0,a.Wm)(i,null,{default:(0,a.w5)((()=>[(0,a._)("pre",null,(0,_.zw)(e.$store.state),1)])),_:1})])),_:1}),(0,a.Wm)(u,{md:12,lg:8},{default:(0,a.w5)((()=>[(0,a.Wm)(i,{color:"primary"},{default:(0,a.w5)((()=>[(0,a._)("pre",null,(0,_.zw)(e.$store.getters),1)])),_:1})])),_:1}),(0,a.Wm)(u,{lg:4},{default:(0,a.w5)((()=>[(0,a.Wm)(i,null,{default:(0,a.w5)((()=>[_e])),_:1})])),_:1}),(0,a.Wm)(u,{lg:4},{default:(0,a.w5)((()=>[(0,a.Wm)(i,null,{default:(0,a.w5)((()=>[ve])),_:1})])),_:1})])),_:1})])}const We={class:"qp-card-main"};function be(e,t,n,r,o,l){return(0,a.wg)(),(0,a.iD)("div",{class:(0,_.C_)(`qp-card ${l.bgColor}`),style:(0,_.j5)(`${l.bgColor}`)},[(0,a._)("div",We,[(0,a.WI)(e.$slots,"default",{},void 0,!0)])],6)}var he={name:"qpCard",props:{color:{type:String,default:"base"}},computed:{bgColor(){return"base"!=this.color?`qp-card-bg-${this.color}`:""}}};const xe=(0,c.Z)(he,[["render",be],["__scopeId","data-v-429ede94"]]);var qe=xe,Se={name:"HomeView",components:{qpCard:qe}};const ye=(0,c.Z)(Se,[["render",ge]]);var ke=ye;const Ce={class:"about"},Oe=(0,a._)("h1",null,"This is an about page",-1),Ze=[Oe];function Te(e,t){return(0,a.wg)(),(0,a.iD)("div",Ce,Ze)}const Ee={},Ue=(0,c.Z)(Ee,[["render",Te]]);var De=Ue;const Ie={class:"qp-vue"},$e=(0,a.Uk)("error");function Ae(e,t,n,r,o,l){const i=(0,a.up)("qp-card"),u=(0,a.up)("el-col"),d=(0,a.up)("el-row");return(0,a.wg)(),(0,a.iD)("div",Ie,[(0,a.Wm)(d,{gutter:20},{default:(0,a.w5)((()=>[(0,a.Wm)(u,{span:24},{default:(0,a.w5)((()=>[(0,a.Wm)(i,null,{default:(0,a.w5)((()=>[$e])),_:1})])),_:1})])),_:1})])}var Ne={name:"ErrorView",components:{qpCard:qe}};const je=(0,c.Z)(Ne,[["render",Ae]]);var He=je;const Pe=[{path:"/",name:"Home",component:ke},{path:"/about",name:"About",component:De},{path:"/:catchAll(.*)",name:"Error",component:He}],ze=(0,ce.p7)({history:(0,ce.PO)("/"),routes:Pe});var Ge=ze,Me=n(5361),Re=n(5103),Fe=n(680);const Je=new Re.ZP({key:"qpcynorrs",storage:window.localStorage,reducer:e=>({drat:e.drat})}),Ve=new Re.ZP({key:"qpcynorrs",storage:window.sessionStorage,reducer:e=>({player:e.player})}),Le=new Re.ZP({key:"qpcynorrs",restoreState:e=>{if(Fe.Z.get(e))return JSON.parse(Me.lW.from(Fe.Z.get(e),"base64").toString("utf8"))},saveState:(e,t)=>{t&&Fe.Z.set(e,Me.lW.from(JSON.stringify(t)).toString("base64"),{expires:30})},modules:["frat"]}),Qe=e=>{e.commit("SET_WINSIZES"),window.addEventListener("resize",(()=>{e.commit("SET_WINSIZES")}))},Be=(0,te.MT)({getters:{app:e=>({win:e.app.win}),player:e=>e.player,rat:e=>{if(e.drat.drat&&e.frat.frat){let t=Me.lW.from(e.drat.drat,"base64").toString("utf8"),n=Me.lW.from(e.frat.frat,"base64").toString("utf8");return`Token ${t}${n}`}return null}},modules:{app:{state:()=>({win:{w:1880,h:980}}),mutations:{SET_WINSIZES(e){e.win={w:window.innerWidth,h:window.innerHeight}}}},player:{state:()=>({})},drat:{state:()=>({drat:null}),mutations:{SET_DRAT(e,t){if(t){let n=e.drat?Me.lW.from(e.drat,"base64").toString("utf8"):null;n=t,e.drat=Me.lW.from(n).toString("base64")}else e.drat=null}}},frat:{state:()=>({frat:null}),mutations:{SET_FRAT(e,t){if(t){let n=e.frat?Me.lW.from(e.frat,"base64").toString("utf8"):null;n=t,e.frat=Me.lW.from(n).toString("base64")}else e.frat=null}}}},plugins:[Je.plugin,Ve.plugin,Le.plugin,Qe]});var Ke=Be,Xe=n(7979),Ye=n(4242);n(4415);const et=(0,r.ri)(me);et.use(Ke),et.use(Ge),et.use(Xe.Z,{locale:Ye.Z}),et.mount("#app")}},t={};function n(r){var a=t[r];if(void 0!==a)return a.exports;var o=t[r]={exports:{}};return e[r].call(o.exports,o,o.exports,n),o.exports}n.m=e,function(){var e=[];n.O=function(t,r,a,o){if(!r){var l=1/0;for(s=0;s<e.length;s++){r=e[s][0],a=e[s][1],o=e[s][2];for(var i=!0,u=0;u<r.length;u++)(!1&o||l>=o)&&Object.keys(n.O).every((function(e){return n.O[e](r[u])}))?r.splice(u--,1):(i=!1,o<l&&(l=o));if(i){e.splice(s--,1);var d=a();void 0!==d&&(t=d)}}return t}o=o||0;for(var s=e.length;s>0&&e[s-1][2]>o;s--)e[s]=e[s-1];e[s]=[r,a,o]}}(),function(){n.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return n.d(t,{a:t}),t}}(),function(){n.d=function(e,t){for(var r in t)n.o(t,r)&&!n.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:t[r]})}}(),function(){n.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)}}(),function(){var e={143:0};n.O.j=function(t){return 0===e[t]};var t=function(t,r){var a,o,l=r[0],i=r[1],u=r[2],d=0;if(l.some((function(t){return 0!==e[t]}))){for(a in i)n.o(i,a)&&(n.m[a]=i[a]);if(u)var s=u(n)}for(t&&t(r);d<l.length;d++)o=l[d],n.o(e,o)&&e[o]&&e[o][0](),e[o]=0;return n.O(s)},r=self["webpackChunk_mcpronovost_cynorrs"]=self["webpackChunk_mcpronovost_cynorrs"]||[];r.forEach(t.bind(null,0)),r.push=t.bind(null,r.push.bind(r))}();var r=n.O(void 0,[998],(function(){return n(8569)}));r=n.O(r)})();