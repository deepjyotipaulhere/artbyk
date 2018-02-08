<template>
  <div>
  <div class="grey lighten-3">
    <div class="container" style="padding-top:5vh;padding-bottom:5vh;">
      <h3>Watercolors</h3>
    </div>
  </div>

  <div class="row">
        <div class="card col s12 m3" v-for="x in news">
          <div class="card-image">
            <img src="http://images.all-free-download.com/images/graphiclarge/beautiful_scenery_05_hd_picture_166257.jpg">
            
          </div>
          <div class="card-content">
            <span class="card-title">{{x.title}} </span>
            
            <p>{{x.subtitle}}</p>
            <p>Size available: <span style="font-weight:bolder">{{x.size}}</span></p>
            <h4 style="text-align:right">&#8377; {{x.price}}</h4>
          </div>
          <div class="card-action">
            <router-link :to="{path:'/view/'+x.id}" class="btn blue btn-block">View</router-link>
          </div>
        </div>
    </div>


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
      this.$http.get('http://localhost:5000/art/all/water').then(response=>{
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
