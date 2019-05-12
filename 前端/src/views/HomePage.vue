<template>
<div>
 <headbar class="col-lg-12 fixed-top" style="padding:0;margin:0;z-index:500"></headbar>
<div class="container col-lg-12" style="padding:0;magrin:0">
  <div class="row col-lg-12">
    <homelist  style="padding0;margin:0"></homelist>
    <TestShow class="" v-if="HomeShow==1" style="padding0;margin:0"></TestShow>
    <sendmessage class="" v-if="HomeShow==2" style="padding:0;margin:0;margin-top:60px;"></sendmessage>
  </div>
</div>
</div>
</template>

<script src="https://cdnjs.cloudflare.com/ajax/libs/feather-icons/4.9.0/feather.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.3/Chart.min.js"></script>
<script>
import headbar from '../components/HeadBar'
import homelist from '../components/HomeList'
import TestShow from '../components/TestHomeShow'
import homemap from '../components/HomeMap'
import sendmessage from '../components/SendMessage'
import { mapState } from 'vuex';
export default {
  name: 'HomePage',
  components: {headbar, homelist, TestShow, homemap, sendmessage},
  data () {
    return {
    }
  },
  computed: {
    ...mapState({
      HomeShow: state => state.user.home_show
    })
  },
  methods: {
    HomeState: function () {
      return this.HomeShow
    }
  }
}
</script>

<style>
#HomePage{
  height: 500px;
  padding: 0;
}
#home-headbar{
  margin:0;
  z-index:500;
}
</style>
