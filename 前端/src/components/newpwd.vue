<template>
    <div class="container-fluid" style="padding:0">
      <form class="col-lg-12 form-horizontal" method="get" role="form" style="margin:3% 0 0 0">
          <label style="font-size: 1.5rem;font-style: inherit">修改密码</label>
          <div>
          新密码<input placeholder="password" type="password" name="token" id="newpwd-input">
          </div>
          <label></label>
          <div>
          确认
          <input placeholder="password" type="password" name="token" id="newpwd-input">
          </div>
          <div v-if="IsSame==false" style="color:red">
              两次输入不相同，请确认输入！！！
          </div>
          <button class="col-lg-1 btn btn-primary" type="submit" id="newpwd-button">提交</button>
      </form>
    </div>
</template>

<script>
export default {
  name: 'newpwd',
  data () {
    return {
      pwd1: '',
      pwd2: '',
      IsSame: true
    }
  }
}
</script>

<style>
#newpwd-input{
  display: inline-block;
  width: 100%;
  height: 3rem;
  padding: 0 0.8rem;
  box-sizing: border-box;
  font-size: 1.5rem;
  background: #fff;
  border: 0.1rem solid #ccc;
  border-radius: 0.3rem;
  outline: 0;
}
#newpwd-button{
    background-color: lightblue;
    margin-top: 5%;
    border: lightgrey solid;
}
</style>
