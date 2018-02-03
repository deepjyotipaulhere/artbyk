<template>
  <div>
    <div class="grey lighten-3">
      <div class="container" style="padding-top:5vh;padding-bottom:5vh;">
        <h3>Quillings</h3>
      </div>
    </div>
    <ul class="collapsible popout">
      <li v-for="(x,i) in news">
        <div class="collapsible-header"><i class="material-icons">filter_drama</i>{{i+1}}</div>
        <div class="collapsible-body"><span v-html="x.title"></span><br><span v-html="x.price"></span></div>
      </li>
    </ul>
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
