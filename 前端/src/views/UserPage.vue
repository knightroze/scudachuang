<template>
  <div class="container-fluid" style="padding:0">
    <headbar class="col-lg-12" style="padding:0"></headbar>
    <div class="col-lg-12" id="user-pic"></div>
    <div class="col-lg-12" style="padding: 5% 5%">
      <div class="row">
        <div class="col-lg-12" id="user-middle" style="height:220px">
          <div class="col-lg-1 offset-lg-1" id="userpic">
          </div>
        </div>
        <div class="col-lg-2" id="left">
          <div class="col-lg-12" id="left-head">
            设置
          </div>
          <div class="col" id="left-set">
            <div class="col-lg-12" id="set-li" :class="{choosedset: rightshow=='userdata'}">
              <span v-if="rightshow!=='userdata'" @click="change('userdata')"><i class="fa fa-address-book-o" aria-hidden="true"></i>个人资料</span>
              <span v-if="rightshow=='userdata'"><i class="fa fa-address-book" aria-hidden="true"></i>查看资料</span>
            </div>
            <div class="col-lg-12" id="set-li" :class="{choosedset: rightshow=='message'}">
              <span v-if="rightshow=='message'"><i class="fa fa-envelope-open" aria-hidden="true"></i>正在设置</span>
              <span v-if="rightshow!=='message'" @click="change('message')"><i class="fa fa-envelope" aria-hidden="true"></i>推送设置</span>
            </div>
            <div class="col-lg-12" id="set-li" :class="{choosedset: rightshow=='changepwd'}">
              <span v-if="rightshow=='changepwd'"><i class="fa fa-pencil-square-o" aria-hidden="true"></i>正在修改</span>
              <span v-if="rightshow!=='changepwd'" @click="change('changepwd')"><i class="fa fa-pencil" aria-hidden="true"></i>修改密码</span>
            </div>
          </div>
        </div>
        <div class="col-lg-9 offset-lg-1" id="right">
          <userinfo v-if="rightshow=='userdata'" class="col-lg-12 offset-lg-0" id="userinfo"></userinfo>
          <newpwd v-if="rightshow=='changepwd'" class="col-lg-12 offset-lg-0" id="userinfo"></newpwd>
          <setmessages v-if="rightshow=='message'" class="col-lg-12 offset-lg-0" id="userinfo"></setmessages>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import headbar from '../components/HeadBar'
import { mapState } from 'vuex'
import userinfo from '../components/UserInfo'
import newpwd from '../components/newpwd'
import setmessages from '../components/SetMessages'
export default {
  name: 'UserPage',
  components: {headbar, userinfo, newpwd, setmessages},
  data () {
    return {
      rightshow: 'userdata',
      username: ''
    }
  },
  computed: {
    ...mapState({
      email: state => state.user.login_email,
      token: state => state.user.login_token,
    })
  },
  methods: {
    change: function (e) {
      this.rightshow = e
    }
  }
}
</script>

<style>
#left{
    height: 500px;
    border-radius: 0.5rem;
    filter: alpha(opacity=0);
    opacity: 100;
    padding: 0;
}
#left-head{
  font-size: 1.5rem;
  font-style: inherit;
  padding: 5% 5% 5% 10%;
}
#left-set{
  padding: 0;
}
#set-li{
  padding: 5% 10% 5% 10%;
  font-size: 1.6rem;
  font-style:inherit;
}
.choosedset{
  color:grey;
  font-style: oblique;
  border: 0.1rem solid #ccc;
  border-radius: 0.5rem;
}
#right{
  height: 500px;
  border-radius: 0.5rem;
  border: 0.1rem solid #ccc;
  padding: 0 0 0 0;
  background-color: ghostwhite;
}
#userpic{
  height: 100px;
  border-radius: 0.5rem;
  z-index: 5;
}
#user-pic{
  z-index: -1;
  position: absolute;
  background:linear-gradient(to bottom left,lightblue,lightgrey);
  background-size: cover;
  height: 340px;
}
#userinfo{
  margin: 0;
  padding: 0;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
  height: 500px;
  border: 0;
}
</style>
