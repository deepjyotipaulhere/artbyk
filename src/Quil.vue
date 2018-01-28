<template>
  <div>
    <h1>Quillings</h1>
    <ul class="collapsible popout">
      <li v-for="(x,i) in news">
        <div class="collapsible-header"><i class="material-icons">filter_drama</i>{{i+1}}</div>
        <div class="collapsible-body"><span v-html="x.message"></span><br><span v-html="x.link"></span></div>
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
      this.$http.get('http://www.mstcindia.co.in/mstcwebservice/Service.svc/GetHighlights').then(response=>{
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
