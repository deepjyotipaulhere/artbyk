<template>
  <div>
    <Header></Header>
      <div style="min-height:50vh;" class="container">
        <div class="grey lighten-2">
          <router-view></router-view>
        </div>
      </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from './Header.vue'
import Footer from './Footer.vue'
export default {
  components:{
    Header,
    Footer
  }
}
</script>
