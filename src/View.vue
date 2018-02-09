<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="card horizontal">
          <div class="card-image">
            <img src="http://images.all-free-download.com/images/graphiclarge/beautiful_scenery_05_hd_picture_166257.jpg">
          </div>
          <div class="card-stacked">
            <div class="card-content">
              <h3>{{datax.title}}</h3>
              <br>
              <p style="font-size:larger;">{{datax.subtitle}}</p>
              <br>
              <p>Available Size</p>
              <b>{{datax.size}}</b>
              <h4 class="right-align">&#8377; {{datax.price}}</h4>
            </div>
            <div class="card-action">
              <span class="grey-text"><i class="material-icons left">remove_red_eye</i>{{datax.view}}</span>
              <button class="btn orange darken-3 right" @click="expand()">Buy</button>
            </div>
          </div>
        </div>
      </div>
      <ul class="collapsible hide">
        <li>
          <div class="collapsible-header orange darken-3 white-text"><i class="material-icons">mail</i>Contact for buying</div>
          <div class="collapsible-body white">
            <form class="col s12">
              <div class="row">
                <div class="input-field col s6">
                  <input id="fname" type="text" class="validate">
                  <label for="fname">Full Name</label>
                </div>
                <div class="input-field col s6">
                  <input id="email" type="text" class="validate">
                  <label for="email">Email</label>
                </div>
              </div>

              <div class="row">
                <div class="input-field col s12">
                  <input id="address" type="text" class="validate">
                  <label for="address">Delivery Address</label>
                </div>
              </div>

              <div class="row">
                <div class="input-field col s6">
                  <input id="pin" type="text" class="validate">
                  <label for="pin">Delivery Pincode</label>
                </div>
                <div class="input-field col s6">
                  <input id="mobile" type="text" class="validate">
                  <label for="mobile">Mobile</label>
                </div>
              </div>


              <div class="row">
                <div class="input-field col s12">
                  <textarea id="comment" class="materialize-textarea"></textarea>
                  <label for="comment">Comments (If Any)</label>
                </div>
              </div>
              <div class="row">
                <div class="col s4 m4 l4"></div>
                <div class="col s4 m4 l4">
                  <button class="btn btn-large waves-effect waves-light btn-block teal white-text"><i class="material-icons left">send</i>Send</button>
                </div>
                <div class="col s4 m4 l4"></div>
              </div>
            </form>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  props:['id'],
  data(){
    return {
      news:[],
      datax:''
    };
  },
  mounted:function(){
    $(document).ready(function(){
      $('.collapsible').collapsible();
      M.textareaAutoResize($('#textarea1'));
    });
  },
  created:function(){
    this.fetch();
    this.updateView();
    
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
      this.datax=this.news[0];
    });
    },
    updateView(){
      this.$http.get('http://localhost:5000/views/'+this.$route.params.id)
    },
    expand()
    {
      var elem = document.querySelector('.collapsible');
      var instance = M.Collapsible.init(elem);
      $('.collapsible').removeClass('hide');
      instance.open(0);
    }
  }
}
</script>
