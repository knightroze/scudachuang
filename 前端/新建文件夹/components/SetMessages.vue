<template>
  <div class="container-fluid" @show ="SetMlData()">
    <table class="table table-bordered table-hover">
        <thead>
          <th>推送设置</th>
          <tr>
            <th>序号</th>
            <th>关键词</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody class="col-lg-12">
          <tr v-for="(setmessages,index) in lorddata()" class="text-center" :key="setmessages">
            <td>{{index+1}}</td>
            <td>{{setmessages}}</td>
            <td>
              <button class="btn-danger btn-sm col-lg-3" data-toggle = "modal" data-target="#del" @click="changeSet('del',index)" style="border: 0.1rem solid #ccc;background-color:grey">删除</button>
            </td>
          </tr>
          <tr>
            <td colspan="5" class="text-center">
              <button class="btn-danger btn-sm col-lg-2" data-toggle = "modal" data-target="#del" @click="changeSet('add',1)" style="background-color:white;color:black;border: 0.1rem solid #ccc;">添加</button>
              <button class="btn-danger btn-sm col-lg-2" data-toggle = "modal" data-target="#del" @click="changeSet('del',-1)" style="background-color:grey;border: 0.1rem solid #ccc;">全部删除</button>
            </td>
          </tr>
        </tbody>
      </table>
      <div id="del" class="modal">
        <div class="modal-dialog">
          <div v-if="setstate=='del'" class="modal-content">
            <div class="modal-header">
              <h4 class="modal-title" v-show="nowIndex!==-1">确认删除用户么？</h4>
              <h4 class="modal-title" v-show="nowIndex===-1">确认删除所有用户么？</h4>
              <button class="close" data-dismiss = "modal">
                <span>×</span>
              </button>
            </div>
            <div class="modal-body text-center">
              <button class="btn btn-primary" data-dismiss = "modal">取消</button>
              <button class="btn btn-primary" data-dismiss = "modal" @click="deleteUser()">确认</button>
            </div>
          </div>
          <div v-if="setstate=='add'" class="modal-content">
            <div class="modal-header">
              添加关键词
              <input type="text" name="setdata" @input="updataset">
              <button class="close" data-dismiss = "modal">
                <span>×</span>
              </button>
            </div>
            <div class="modal-body text-center">
              <button class="btn btn-primary" data-dismiss = "modal">取消</button>
              <button class="btn btn-primary" data-dismiss = "modal" @click="addUser()">确认</button>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import { mapState } from 'vuex'
import Vue from 'vue'
export default {
  inject: ['reload'],
  name: 'SetMessages',
  data () {
    return {
      lists: [],
      nowIndex: '',
      setstate: '',
      setword: '123'
    }
  },
  computed: {
    ...mapState({
      setlists: state => state.user.setlists
    })
  },
  methods: {
    updataset: function (e) {
      this.setword = e.target.value
    },
    changeSet: function (e, i) {
      this.setstate = e
      this.nowIndex = i
    },
    lorddata: function () {
      this.lists.length = 0
      for (var i = 0; i < this.setlists.length; i++) {
        this.lists[i] = this.setlists[i]
      }
      Vue.set(this.lists)
      return this.lists
    },
    SetMlData: function () {
      this.$http.get('/SetMessage/setmessage').then(response => {
        this.lists.length = 0
        for (var i = 0; i < response['data']['data']['sendlist'].length; i++) {
          this.lists[i] = response['data']['data']['sendlist'][i]
        }
        this.$store.commit({
          type: 'updatasetlists',
          value: response['data']['data']['sendlist']
        })
        this.lorddata()
        console.log(this.lists)
        Vue.set(this.lists)
        return this.lists
      }, response => {
        console.log('数据加载失败')
      })
      this.reload()
    },
    addUser: function () {
      this.lists.push(this.setword)
      this.$store.commit({
        type: 'updatasetlists',
        value: this.lists
      })
      Vue.set(this.lists)
      this.setword = ''
    },
    deleteUser: function () {
      if(this.nowIndex==-1) {//eslint-disable-line
        this.lists = []
      } else {
        this.lists.splice(this.nowIndex, 1)
      }
      console.log(this.lists)
      this.$store.commit({
        type: 'updatasetlists',
        value: this.lists
      })
      Vue.set(this.lists)
    }
  }
}
</script>
