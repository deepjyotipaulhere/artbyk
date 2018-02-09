<template>
  <div class="grey lighten-3">
    <hr style="margin:0;padding:0">
    <Header></Header>
      <div style="min-height:50vh;">
        <router-view></router-view>
      </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from './Header.vue'
import Footer from './Footer.vue'
import Util from './Util.vue'
export default {
  components:{
    Header,
    Footer,
    Util
  }
}
</script>
