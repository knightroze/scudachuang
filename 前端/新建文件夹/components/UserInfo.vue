<template>
<div class="container-fluid" style="padding:0">
  <div class="col-lg-12" v-if="changedata==true">
    <table class="col-lg-12 table">
      <caption class="col-lg-12"></caption>
      <thead>
        <tr>
          <th>用户资料</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>email:</td>
          <td>123@123</td>
        </tr>
        <tr>
          <td>Sachin</td>
          <td>Mumbai</td>
        </tr>
      </tbody>
    </table>
    <button @click="ChangeFormState()" id="Info-buttons">编辑资料</button>
  </div>
<form class="col-lg-12" v-if="changedata==false" style="margin:0;border:0">
  <div class="form-group">
    <label for="email">Email address:</label>
    <input type="email" class="form-control" id="email">
  </div>
  <div class="form-group">
    <label for="pwd">Password:</label>
    <input type="password" class="form-control" id="pwd">
  </div>
  <div class="form-check">
    <label class="form-check-label">
      <input class="form-check-input" type="checkbox"> Remember me
    </label>
  </div>
  <div class="row" id="bottom-buttons">
  <button type="submit" class="col-lg-1 btn btn-primary" @click="ChangeFormState()" id="Info-buttons" style="color:white;background-color:lightblue">保存</button>
  <button class="col-lg-1" id="Info-buttons" @click="ChangeFormState()">取消</button>
  </div>
</form>
</div>
</template>

<script>
export default {
  name: 'UserInfo',
  data () {
    return {
      changedata: true

    }
  },
  methods: {
    ChangeFormState: function () {
      this.changedata = !this.changedata
    }
  }
}
</script>

<style>
#Info-buttons{
  background-color: aliceblue;
  border-radius: 0.5rem;
  border: 0.1rem solid #ccc;
  padding: 1%;
}
#bottom-buttons{
  margin: 5%;
}
</style>
