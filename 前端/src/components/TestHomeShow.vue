<template>
<main role="main" class="col-lg-10 ml-sm-auto col-md-9 px-4">
   <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
        <h1 class="h2">数据泄露分布</h1>
        <div class="btn-toolbar mb-2 mb-md-0">
          <div class="btn-group mr-2">
            <button type="button" class="btn btn-sm btn-outline-secondary">Share</button>
            <button type="button" class="btn btn-sm btn-outline-secondary">Export</button>
          </div>
          <button type="button" class="btn btn-sm btn-outline-secondary dropdown-toggle">
            <span data-feather="calendar"></span>
            This week
          </button>
        </div>
      </div>

      <!-- <canvas class="my-4 w-100" id="myChart" width="900" height="380"></canvas> -->
      <homemap class="col-lg-12"></homemap>

      <h2>Section title</h2>
      <div class="table-responsive">
        <table class="table table-striped table-sm">
          <thead>
            <tr>
              <th>#</th>
              <th>City</th>
              <th>Low</th>
              <th>Mid</th>
              <th>High</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>001</td>
              <td>北京</td>
              <td>9</td>
              <td>10</td>
              <td>8</td>
            </tr>
            <tr>
              <td>002</td>
              <td>天津</td>
              <td>1</td>
              <td>1</td>
              <td>2</td>
            </tr>
            <tr>
              <td>003</td>
              <td>上海</td>
              <td>8</td>
              <td>18</td>
              <td>8</td>
            </tr>
            <tr>
              <td>004</td>
              <td>重庆</td>
              <td>2</td>
              <td>4</td>
              <td>1</td>
            </tr>
            <tr>
              <td>005</td>
              <td>河北</td>
              <td>0</td>
              <td>0</td>
              <td>0</td>
            </tr>
            <tr>
              <td>006</td>
              <td>山西</td>
              <td>1</td>
              <td>0</td>
              <td>0</td>
            </tr>
            <tr>
              <td>007</td>
              <td>辽宁</td>
              <td>0</td>
              <td>0</td>
              <td>0</td>
            </tr>
            <tr>
              <td>008</td>
              <td>吉林</td>
              <td>0</td>
              <td>1</td>
              <td>1</td>
            </tr>
            <tr>
              <td>009</td>
              <td>黑龙江</td>
              <td>0</td>
              <td>0</td>
              <td>0</td>
            </tr>
            <tr>
              <td>010</td>
              <td>江苏</td>
              <td>0</td>
              <td>2</td>
              <td>0</td>
            </tr>
            <tr>
              <td>011</td>
              <td>浙江</td>
              <td>2</td>
              <td>2</td>
              <td>1</td>
            </tr>
            <tr>
              <td>012</td>
              <td>安徽</td>
              <td>0</td>
              <td>1</td>
              <td>0</td>
            </tr>
            <tr>
              <td>013</td>
              <td>福建</td>
              <td>1</td>
              <td>1</td>
              <td>2</td>
            </tr>
            <tr>
              <td>014</td>
              <td>江西</td>
              <td>1</td>
              <td>7</td>
              <td>1</td>
            </tr>
            <tr>
              <td>015</td>
              <td>山东</td>
              <td>0</td>
              <td>0</td>
              <td>1</td>
            </tr>
            <tr>
              <td>016</td>
              <td>河南</td>
              <td>2</td>
              <td>0</td>
              <td>1</td>
            </tr>
            <tr>
              <td>017</td>
              <td>湖北</td>
              <td>0</td>
              <td>0</td>
              <td>0</td>
            </tr>
            <tr>
              <td>018</td>
              <td>湖南</td>
              <td>0</td>
              <td>2</td>
              <td>0</td>
            </tr>
            <tr>
              <td>019</td>
              <td>广东</td>
              <td>2</td>
              <td>2</td>
              <td>2</td>
            </tr>
            <tr>
              <td>020</td>
              <td>海南</td>
              <td>0</td>
              <td>0</td>
              <td>1</td>
            </tr>
            <tr>
              <td>021</td>
              <td>四川</td>
              <td>3</td>
              <td>2</td>
              <td>2</td>
            </tr>
            <tr>
              <td>022</td>
              <td>贵阳</td>
              <td>0</td>
              <td>0</td>
              <td>0</td>
            </tr>
            <tr>
              <td>023</td>
              <td>云南</td>
              <td>0</td>
              <td>0</td>
              <td>0</td>
            </tr>
            <tr>
              <td>024</td>
              <td>陕西</td>
              <td>0</td>
              <td>0</td>
              <td>0</td>
            </tr>
            <tr>
              <td>025</td>
              <td>甘肃</td>
              <td>0</td>
              <td>0</td>
              <td>0</td>
            </tr>
            <tr>
              <td>026</td>
              <td>青岛</td>
              <td>0</td>
              <td>0</td>
              <td>0</td>
            </tr>
            <tr>
              <td>027</td>
              <td>台湾</td>
              <td>1</td>
              <td>5</td>
              <td>3</td>
            </tr>
            <tr>
              <td>028</td>
              <td>内蒙古</td>
              <td>0</td>
              <td>0</td>
              <td>0</td>
            </tr>
            <tr>
              <td>029</td>
              <td>广西</td>
              <td>0</td>
              <td>0</td>
              <td>0</td>
            </tr>
            <tr>
              <td>030</td>
              <td>西藏</td>
              <td>0</td>
              <td>0</td>
              <td>0</td>
            </tr>
            <tr>
              <td>031</td>
              <td>宁夏</td>
              <td>0</td>
              <td>1</td>
              <td>0</td>
            </tr>
            <tr>
              <td>032</td>
              <td>新疆</td>
              <td>0</td>
              <td>0</td>
              <td>0</td>
            </tr>
            <tr>
              <td>033</td>
              <td>香港</td>
              <td>1</td>
              <td>0</td>
              <td>0</td>
            </tr>
            <tr>
              <td>034</td>
              <td>澳门</td>
              <td>0</td>
              <td>0</td>
              <td>1</td>
            </tr>
          </tbody>
        </table>
      </div>
</main>
</template>

<script>
import homemap from '../components/HomeMap'
export default {
  name: 'TestHomeShow',
  components: {homemap},
  data () {
    return {
      hometable: []
    }
  },
  methods:{
    changecity: function (e) {
      citydicts = [["BEJ","北京"], ["TAJ","天津"], ["SHH","上海"], ["CHQ","重庆"], ["HEB","河北"], ["SHX","山西"], ["LIA","辽宁"], ["JIL","吉林"], ["HLJ","黑龙江"], ["JSU","江苏"], ["ZHJ","浙江"], ["ANH","安徽"], ["FUJ","福建"], ["JXI","江西"], ["SHD","山东"], ["HEN","河南"], ["HUB","湖北"], ["HUN","湖南"], ["GUD","广东"], ["HAI","海南"], ["SCH","四川"], ["GUI","贵州"], ["YUN","云南"], ["SHA","陕西"], ["GAN","甘肃"], ["QIH","青海"], ["TAI","台湾"], ["NMG","内蒙古"], ["GXI","广西"], ["TIB","西藏"], ["NXA","宁夏"], ["XIN","新疆"], ["HKG","香港"], ["MAC","澳门"]]
      for(var i=0;i<citydicts.length;i++){
        if (citydicts[i][0]==e) {
          return citydicts[i][1]
        }
      }
    }
  }
}
</script>

<style>
[role="main"] {
  padding-top: 133px; /* Space for fixed navbar */
}

@media (min-width: 768px) {
  [role="main"] {
    padding-top: 48px; /* Space for fixed navbar */
  }
}
</style>
