<template>
<nav class="navbar navbar-default" role="navigation" style="padding:0">
  <div class="container-fluid" id="header-bar">
    <div class="col-lg-2" id="title">
      <router-link style="color:azure;font-size:1rem" :to="{ name: 'HomePage'}">
        某某平台
      </router-link>
    </div>
    <div class="col-lg-6" id="nav">
    </div>
    <div class="col-lg-4" id="head-user">
        <div v-if="IsLogin()==false">
        <!-- <router-link :to="{ name: 'login'}"><button class="talion">登录</button></router-link> -->
          <router-link style="color:azure;font-size:1rem" :to="{ name: 'LoginPage'}"><i class="fa fa-user-o" aria-hidden="true"></i>登录</router-link>
        </div>
        <div v-if="IsLogin()==true" class="row">
          <div class="col-lg-2">
            <router-link :to="{name: 'UserPage'}" style="color:white"><i class="fa fa-bell-o" aria-hidden="true" style="padding-top:70%"></i></router-link>
          </div>
          <div class="col-lg-10">
            <!-- <router-link style="color:azure" :to="{ name: 'UserPage'}"><i class="fa fa-user-circle" aria-hidden="true"></i>
            欢迎您：{{loginuser}}</router-link> -->
            <button class="btn dropdown-toggle" id="dropdownMenu1" data-toggle="dropdown" style="color: white;margin:0"><i class="fa fa-user-circle" aria-hidden="true"></i>
            欢迎您：{{loginuser}}</button>
          <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1" id="headbar-menu">
            <li role="presentation" id="HeadbarMenuLi">
              <div role="menuitem" tabindex="-1">
                <router-link :to="{name: 'UserPage'}" style="color:black"><i class="fa fa-user" aria-hidden="true"></i>{{loginuser}}</router-link>
              </div>
            </li>
            <hr class="line">
            <li role="presentation" id="HeadbarMenuLi">
              <div role="menuitem" tabindex="-1">
                <a role="menuitem" tabindex="-1" href="#" style="color:black">修改密码</a>
              </div>
            </li>
            <li role="presentation" class="divider"></li>
            <li role="presentation" id="HeadbarMenuLi">
              <div role="menuitem" tabindex="-1" style="color:red">
                <button style="color:red;background-color: aliceblue;padding:0;border:0" @click="UserLogout">注销</button>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</nav>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'header-bar',
  data () {
    return {
      loginuser: ''
    }
  },
  computed: {
    ...mapState({
      email: state => state.user.login_email,
      token: state => state.user.login_token
    })
  },
  methods: {
    // showTalion: function () {
    //   this.$emit('showTalion')
    // }
    IsLogin: function () {
      if (this.email == '' && this.token == '') {//eslint-disable-line
        return false
      }
      this.loginuser = this.email
      return true
    },
    UserLogout: function () {
      this.$store.commit({
        type: 'logout'
      })
      this.$router.push({name: 'LoginPage'})
    }
  }
}
</script>

<style>
#header-bar{
  z-index: 10;
  /* display: flex;
  flex-direction: row; */
  height: 40px;
  width: 100%;
  background-color: black;
  text-align: center;
  font-style: inherit;
  color: azure;
  padding: 0;
}
#title {
  height: 100%;
  background-size: cover;
  font-size: 1.2rem;
  padding-top: 0.7%;
}
a {
  display: block;
}
#nav {
  height: 100%;
  padding-top: 0.7%;
}
.headbar-middle{
  text-align: left;
  height: 100%;
  width: 100%;
}
.middle-li{
  display: inline-block;
  font-size: 1rem;
  margin-right: 1%;
  text-align: center;
}
/* .talion {
  text-align: center;
  font-size: 0.7rem;
  background-size: cover;
  background-color:gainsboro;
  height: 100%;
  border-radius: 0.4rem;
} */
#head-user{
  display: flex;
  flex-direction: row-reverse;
}
#headbar-menu{
  background-color: aliceblue;
  border-radius: 0.5rem;
  border: 0.1rem solid #ccc;
  height: 150px;
  padding-left:5%;
}
#HeadbarMenuLi{
  margin-bottom: 5%;

}
</style>
