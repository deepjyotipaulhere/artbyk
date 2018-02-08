<template>
  <div>
    {{this.news}}
  </div>
</template>

<script>
export default {
  props:['id'],
  data(){
    return {
      news:[]
    };
  },
  created:function(){
    this.fetch();
    console.log(this.news)
  },
  methods:{
    fetch(){
      this.$http.get('http://localhost:5000/art/'+this.$route.params.id).then(response=>{
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
