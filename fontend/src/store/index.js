import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    rumbs: [],
    content: null,
    title: null
  },
  mutations: {
    setContent (state, con) {
      state.content = con
    },
    setTitle (state, title) {
      state.title = title
    }
  },
  getters: {

  }
})

export default store
