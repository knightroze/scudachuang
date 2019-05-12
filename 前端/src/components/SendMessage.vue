<template>
  <div class="tTable container-fluid col-lg-10 ml-sm-auto col-md-9 px-4">
    <div class="form-group col-lg-12">
      <div class="form-group col-lg-12">
        <div class="page-header col-lg-12">
            <h3>消息推送</h3>
        </div>
        <div v-for="item in arrayData" :key="item" id="sendmessage-content">
            用户{{item.username}}您好，我们于{{item.time}}发现了您关注的{{item.tags}}类数据发生泄露，
                包含如下内容：{{item.content}}。我们估计他的危险等级为{{item.level}}级
          </div>
        <div class="pager row col-lg-12" id="pager">
          <span class="form-inline">
            <select class="form-control" v-model="pagesize" v-on:change="showPage(pageCurrent,$event,true)" number>
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="3">3</option>
              <option value="5">5</option>
            </select>
          </span>
          <span v-for="item in pageCount+1" :key="item">
            <span v-if="item==1" class="btn btn-default" v-on:click="showPage(1,$event)" :class="{'disabled':fDisabled}">
              首页
            </span>
            <span v-if="item==1" class="btn btn-default" v-on:click="showPage(pageCurrent-1,$event)" :class="{'disabled':fDisabled}">
              上一页
            </span>
            <span v-if="item==1" class="btn btn-default" v-on:click="showPage(item,$event)">
              {{item}}
            </span>
            <span v-if="item==1&&item<showPagesStart-1" class="btn btn-default disabled">
              ...
            </span>
            <span v-if="item>1&&item<=pageCount-1&&item>=showPagesStart&&item<=showPageEnd&&item<=pageCount" class="btn btn-default" v-on:click="showPage(item,$event)">
              {{item}}
            </span>
            <span v-if="item==pageCount&&item>showPageEnd+1" class="btn btn-default disabled">
              ...
            </span>
            <span v-if="item==pageCount" class="btn btn-default" v-on:click="showPage(item,$event)" >
              {{item}}
            </span>
            <span v-if="item==pageCount" class="btn btn-default" v-on:click="showPage(pageCurrent+1,$event)" :class="{'disabled':lDisabled}">
              下一页
            </span>
            <span v-if="item==pageCount" class="btn btn-default" v-on:click="showPage(pageCount,$event)" :class="{'disabled':lDisabled}">
              尾页
            </span>
          </span>
          <span>{{pageCurrent}}/{{pageCount}}</span>
        </div>
      </div>
    </div>
  </div>
 </template>
 <script >
 import Vue from 'vue'
 import { mapState } from 'vuex'
 export default {
  inject: ['reload'],
  data(){
    return{
         //为第一页或者最后一页时，首页，尾页不能点击
        fDisabled:false,
        lDisabled:false,
         //总项目数
        totalCount: 200,
        //分页数
        pageCount: 20,
        //当前页面
        pageCurrent: 1,
        //分页大小
        pagesize: 2,
        //显示分页按钮数
        showPages: 11,
        //开始显示的分页按钮
        showPagesStart: 1,
        //结束显示的分页按钮
        showPageEnd: 100,
        //分页数据
        array_Data2: [{'username':'123','time':'123:45','tags':'晚饭','content':'砸哇撸多，托克友托马叠','level':'3'},{'username':'456','time':'123:45','tags':'晚饭','content':'砸哇撸多，托克友托马叠','level':'3'}],
        arrayData: []
    }
  },
  computed: {
    ...mapState({
      arrayData1:state => state.user.messagedata
    })
  },
  methods:{
    // setmessagedata() {
    //   this.$http.get('/SetMessage/message').then(response => {
    //       console.log(response)
    //     for (var i=0;i<response['data']['data'].length;i++){
    //         var dicts={}
    //         dicts['username']=response['data']['data'][i]['username']
    //         dicts['time']=response['data']['data'][i]['time']
    //         dicts['tags']=response['data']['data'][i]['tags']
    //         dicts['content']=response['data']['data'][i]['content']
    //         dicts['level']=response['data']['data'][i]['level']
    //         this.array_Data[this.array_Data.length]=dicts
    //     }
    //     console.log("_Data_"+this.array_Data[0]['username'])
    //   }, response => {
    //     console.log('message数据加载失败')
    //   })
    // },
    showPage(pageIndex, $event, forceRefresh){
      if (pageIndex > 0) {
        if (pageIndex > this.pageCount) {
          pageIndex = this.pageCount;
        }
        //判断数据是否需要更新
        var currentPageCount = Math.ceil(this.totalCount / this.pagesize);
        if (currentPageCount != this.pageCount) {
          pageIndex = 1;
          this.pageCount = currentPageCount;
        }
        else if (this.pageCurrent == pageIndex && currentPageCount == this.pageCount && typeof (forceRefresh) == "undefined") {
          console.log("not refresh");
          return;
        }
        //处理分页点中样式
        var buttons = $("#pager").find("span");
        for (var i = 0; i < buttons.length; i++) {
          if (buttons.eq(i).html() != pageIndex) {
            buttons.eq(i).removeClass("testclass");
          }
          else {
            buttons.eq(i).addClass("testclass");
          }
        }
        //测试数据 随机生成的
        // var newPageInfo = [];
        // var time=new Date();
        // for (var i = 0; i < this.pagesize; i++) {
        //   newPageInfo[newPageInfo.length] = {
        //     timestamp: time,
        //     count: (i + (pageIndex - 1) * 20)
        //   };
        // }
        this.arrayData.length = 0
        for (var i = (pageIndex-1)*this.pagesize; i < Math.min(this.pagesize,this.arrayData1.length)+(pageIndex-1)*this.pagesize; i++) {
          this.arrayData[i-(pageIndex-1)*this.pagesize]=this.arrayData1[i]
        }
        console.log("data"+this.arrayData)
        this.pageCurrent = pageIndex;
        // this.arrayData = newPageInfo;
        //如果当前页首页或者尾页，则上一页首页就不能点击，下一页尾页就不能点击
         if(this.pageCurrent===1){
            this.fDisabled=true;
          }else if(this.pageCurrent===this.pageCount){
            this.lDisabled=true;
          }else{
             this.fDisabled=false;
             this.lDisabled=false;
          }
        //计算分页按钮数据
        if (this.pageCount > this.showPages) {
          if (pageIndex <= (this.showPages - 1) / 2) {
            this.showPagesStart = 1;
            this.showPageEnd = this.showPages - 1;
            console.log("showPage1")
          }
          else if (pageIndex >= this.pageCount - (this.showPages - 3) / 2) {
            this.showPagesStart = this.pageCount - this.showPages + 2;
            this.showPageEnd = this.pageCount;
            console.log("showPage2")
          }
          else {
            console.log("showPage3")
            this.showPagesStart = pageIndex - (this.showPages - 3) / 2;
            this.showPageEnd = pageIndex + (this.showPages - 3) / 2;
          }
        }
        console.log("showPagesStart:" + this.showPagesStart + ",showPageEnd:" + this.showPageEnd + ",pageIndex:" + pageIndex);
      }
    }
  },
  mounted(){
    this.showPage(this.pageCurrent, null, true)
  }
}
 </script>

<style>
#sendmessage-content{
  border-radius: 1rem;
  margin-top: 5%; 
  margin-bottom: 5%;
  padding: 3%;
  border: 0.1rem solid #ccc;   
}
.testclass{
  background-color: lightgray;
}
</style>
