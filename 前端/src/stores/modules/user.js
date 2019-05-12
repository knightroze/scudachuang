import '../../../node_modules/jquery/dist/jquery.min.js'
const state = {
  login_email: '',
  login_token: '',
  login_name: '',
  temp_email: '',
  temp_token: '',
  temp_name: '',
  home_show: 1,
  setlists: [],
  messagedata: []
}

const getters = {
  // Filtering currentUser
  currentUser: state => {
    return {
      email: state.login_email,
      token: state.login_token,
      name: state.login_name
    }
  }
}

const mutations = {
  loadmessage (state,pay) {
    state.messagedata.length = 0
    for(var i=0; i<pay.value.length;i++){
      var dicts={}
      dicts['username']=pay.value[i]['username']
      dicts['time']=pay.value[i]['time']
      dicts['tags']=pay.value[i]['tags']
      dicts['content']=pay.value[i]['content']
      dicts['level']=pay.value[i]['level']
      state.messagedata[i] = dicts
    }
    console.log(state.messagedata)
  },
  changeHomeShow (state, pay) {
    state.home_show = pay.value
  },
  updateData (state, payload) {
    switch (payload.name) {
      case 'email':
        state.temp_email = payload.value
        break
      case 'token':
        state.temp_token = payload.value
        break
      case 'name':
        state.temp_name = payload.name
        break
      default:
        console.log('Error:Dont directly mutate Vuex store')
    }
  },
  getLocalUser (state) {
    state.login_email = localStorage.getItem('email')
    state.login_token = localStorage.getItem('token')
    state.login_name = localStorage.getItem('name')
  },
  setUser (state, payload) {
    state.login_email = payload.email
    state.login_token = payload.token
    state.login_name = payload.name
  },
  logout (state) {
    localStorage.removeItem('email')
    localStorage.removeItem('token')
    localStorage.removeItem('name')
    state.login_email = ''
    state.login_token = ''
    state.login_name = ''
  },
  updatasetlists (state, payload) {
    state.setlists.length = 0
    for (var i = 0; i < payload.value.length; i++) {
      state.setlists[i] = payload.value[i]
    }
  }
}

const actions = {
  /**
    * Login
     * new Promise((resolve, reject) => {})
     * Authorization: 'Bearer ' + token
     * email: payload.email
     * pass: payload.pass
     * name: payload.name
  */
  login ({ commit }, payload) {
    var lists = [{'email': '123@123', 'token': '123'}]
    for (var i = 0; i < lists.length; i++) {
      if (lists[i]['email'] ==payload.email && lists[i]['token']==payload.token) {//eslint-disable-line
        commit({
          type: 'setUser',
          email: payload.email,
          token: payload.token,
          name: payload.name
        })
        return
      }
    }
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}
