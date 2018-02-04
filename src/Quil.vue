<template>
  <div>
    <div class="grey lighten-3">
      <div class="container" style="padding-top:5vh;padding-bottom:5vh;">
        <h3>Quillings</h3>
      </div>
    </div>

    
    <div class="row">
        <div class="card col s12 m3" v-for="x in news">
          <div class="card-image">
            <img src="http://images.all-free-download.com/images/graphiclarge/beautiful_scenery_05_hd_picture_166257.jpg">
            <span class="card-title">{{x.title}}</span>
          </div>
          <div class="card-content">
            <p>{{x.subtitle}}</p>
          </div>
          <div class="card-action">
            <a href="#">This is a link</a>
          </div>
        </div>
    </div>
            

    <!-- <ul class="collapsible popout">
      <li v-for="(x,i) in news">
        <div class="collapsible-header"><i class="material-icons">filter_drama</i>{{i+1}}</div>
        <div class="collapsible-body"><span v-html="x.title"></span><br><span v-html="x.price"></span></div>
      </li>
    </ul> -->
  </div>
</template>

<script>
export default {
  data(){
    return {
      news:[]
    };
  },
  created:function(){
    $(document).ready(function(){
        $('.collapsible').collapsible();
      });
    this.fetch();
  },
  methods:{
    fetch(){
      this.$http.get('http://localhost:5000/art/all/quil').then(response=>{
      return response.json();
    }).then(data=>{
      const dataarr=[];
      for(var key in data)
        dataarr.push(data[key]);
      this.news=dataarr;
    });
    }
  }
}
</script>
