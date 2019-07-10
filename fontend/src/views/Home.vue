<template>
  <a-layout class="container">
    <a-layout-header class="header">小说阅读网</a-layout-header>
    <a-layout-content class="content">
      <Novel :visible="is_show" @close="hideDrawer"></Novel>
      <div style="position: fixed;top: 40%">
        <a-button type="dashed" @click="showDrawer" style="color: #1890ff;display: block">小说列表</a-button>
        <a-button type="dashed" @click="showModal" style="color: #1890ff;display: block">增加小说</a-button>
      </div>
      <a-row type="flex" justify="center">
        <a-col :span="12" style="overflow:auto">
          <h1 style="text-align: center">{{title}}</h1>
          <p style="font-size: 20px;line-height: 40px">{{content}}</p>
        </a-col>
      </a-row>

      <a-modal title="新增小说" v-model="visible" :footer="null">
        <a-form :form="form" @submit="handleSubmit">
          <a-form-item label="小说名称" :label-col="{ span: 5 }" :wrapper-col="{ span: 12 }">
            <a-input v-decorator="['novel_name', {rules: [{ required: true, message: '请输入小说名称'}]}]"></a-input>
          </a-form-item>
          <a-form-item label="首页地址" :label-col="{ span: 5 }" :wrapper-col="{ span: 12 }">
            <a-input v-decorator="['novel_url', {rules: [{ required: true, message: '请输入小说首页地址'}]}]"></a-input>
          </a-form-item>
          <a-form-item :wrapper-col="{ span: 12, offset: 5 }">
            <a-button type="primary" html-type="submit">
              提交
            </a-button>
          </a-form-item>
        </a-form>
      </a-modal>
    </a-layout-content>
    <a-layout-footer class="footer">小说阅读 ©2019 Created by 星星在线</a-layout-footer>
  </a-layout>
</template>
<script>
import ARow from 'ant-design-vue/es/grid/Row'
import ACol from 'ant-design-vue/es/grid/Col'
import Novel from '@/views/Novel'
import AFormItem from 'ant-design-vue/es/form/FormItem'
import qs from 'Qs'

export default {
  name: 'Home',
  components: {AFormItem, ACol, ARow, Novel},
  data () {
    return {
      visible: false,
      form: this.$form.createForm(this),
      is_show: false,
      available: 0
    }
  },
  methods: {
    showModal () {
      this.visible = true
    },
    showDrawer () {
      this.is_show = true
    },
    hideDrawer () {
      this.is_show = false
    },
    handleSubmit (e) {
      e.preventDefault()
      let that = this
      this.form.validateFields((err, values) => {
        if (!err) {
          that.visible = false
          let data = {'name': values.novel_name, 'home': values.novel_url}
          this.$http.post('/api/novel/', qs.stringify(data)).then(function (response) {
            if (response.data.id) {
              that.$message.success('添加成功：' + response.data.name)
            }
          }).catch(function (response) {
            that.$message.error(response.response.data.home[0])
          })
        }
      })
    },
    handleScroll () {
      var scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
      this.height1 = scrollTop
      this.height2 = document.body.scrollHeight
      this.height3 = document.compatMode === 'CSS1Compat' ? document.documentElement.clientHeight : document.body.clientHeight
      console.log(this.height1, this.height2, this.height3)
      if (this.height3 + this.height1 >= this.height2 - 200 && this.available) {
        this.available = 0
        console.log(this.available)
      } else if (this.height3 + this.height1 < this.height2 - 100) {
        this.available = 1
      }
    }
  },
  computed: {
    content () {
      return this.$store.state.content
    },
    title () {
      return this.$store.state.title
    }
  },
  created () {
  },
  mounted () {
    window.addEventListener('scroll', this.handleScroll)
  }
}
</script>
<style scoped>
  .header {
    color: black;
    text-align: center;
    font-size: 22px;
    box-sizing: border-box;
    background-color: ghostwhite;
  }
  .content {
    overflow: auto;
  }
  .footer {
    text-align: center;
    background: gainsboro;
    bottom: 0px;
    width: 100%;
  }
</style>
