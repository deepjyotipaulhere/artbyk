<template>
  <div>
    <div class="" style="background-image:url('http://www.dailyfreepsd.com/wp-content/uploads/2013/09/atlantic-blurred-background.jpg');background-size:cover;
    background-position:center">
      <div class="container" style="padding-top:10vh;padding-bottom:10vh;">
        <h3 style="font-weight:lighter;" class="white-text">Quillings</h3>
      </div>
    </div>

    
    <div class="row">
        <div class="card col s12 m3" v-for="x in news">
          <div class="card-image">
            <img src="http://images.all-free-download.com/images/graphiclarge/beautiful_scenery_05_hd_picture_166257.jpg">
            
          </div>
          <div class="card-content">
            <span class="card-title">{{x.title}}</span>
            <p>{{x.subtitle}}</p>
            <p>Size available: <span style="font-weight:bolder">{{x.size}}</span></p>
            <h4 style="text-align:right">&#8377; {{x.price}}</h4>
          </div>
          <div class="card-action">
            <router-link :to="{path:'/view/'+x.id}" class="btn blue btn-block">View</router-link>
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
