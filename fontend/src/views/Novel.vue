<template>
  <div>
    <a-drawer
      title="小说列表"
      :placement="placement"
      :width="500"
      @close="onClose"
      :visible="visible"
    >
      <a-row>
        <a-col :span="8">
          <a-list size="large" bordered :dataSource="novel_infos" style="height: 100%;">
            <a-list-item slot="renderItem" slot-scope="novel, index">
              <a-button :type="current_novel === novel.id ? 'primary' : 'dashed'" block @click="on_click_novel(novel.id)">{{novel.name}}</a-button>
            </a-list-item>
            <div slot="header" style="font-size: 16px; color: #000;">小说列表</div>
          </a-list>
        </a-col>
        <a-col :span="14">
          <a-list size="large" bordered :dataSource="novel_chapters" style="height: 100%;">
            <a-list-item slot="renderItem" slot-scope="chapters, index">
              <a @click="on_click_chapters(chapters.id)" :class="{red:current_chapter === chapters.id}">{{chapters.title}}</a>
            </a-list-item>
            <div slot="header" style="font-size: 16px; color: #000;">章节列表</div>
            <div v-if="showLoadingMore" slot="loadMore" :style="{ textAlign: 'center', height: '32px', lineHeight: '32px' }">
              <a-spin v-if="loadingMore" />
              <a-button v-else @click="onLoadMore">加载更多</a-button>
            </div>
          </a-list>
        </a-col>
      </a-row>
    </a-drawer>
  </div>
</template>

<script>
export default {
  name: 'Novel',
  props: {
    visible: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      placement: 'left',
      novel_infos: [], // 小说列表
      novel_chapters: [], // 章节列表
      current_page: 1, // 当前是第几页
      total_chapters: 0, // 总共有多少章
      novel_id: 0, // 小说ID
      flag: false, // 小说是否可以阅读
      next_url: null, // 加载更多小说连接
      showLoadingMore: false,
      loadingMore: false,
      current_novel: null, // 当前阅读的小说
      current_chapter: null // 当前阅读的章节
    }
  },
  methods: {
    onClose () {
      this.$emit('close', false)
    },
    on_click_novel (id) {
      let that = this
      that.current_novel = id
      that.current_chapter = null
      that.novel_chapters.length = 0
      this.$http.get('/api/novel/' + that.current_novel + '/').then(function (response) {
        that.total_chapters = response.data.count
        that.next_url = response.data.next
        that.novel_chapters = response.data.results
        if (that.novel_chapters.length < that.total_chapters) {
          that.showLoadingMore = true
        } else {
          that.showLoadingMore = false
        }
      })
    },
    on_click_chapters (id) {
      let that = this
      that.current_chapter = id
      this.$http.get('/api/chapter/' + that.current_chapter + '/').then(function (response) {
        that.$store.commit('setContent', response.data.content)
        that.$store.commit('setTitle', response.data.title)
      })
    },
    onLoadMore () {
      this.current_page += 1
      let that = this
      this.loadingMore = true
      this.$http.get(that.next_url).then(function (response) {
        that.next_url = response.data.next
        that.novel_chapters = that.novel_chapters.concat(response.data.results)
        if (that.novel_chapters.length >= that.total_chapters) {
          that.showLoadingMore = false
        } else {
          that.showLoadingMore = true
        }
        that.loadingMore = false
        that.$nextTick(() => {
          window.dispatchEvent(new Event('resize'))
        })
      })
    },
    getData () {
      let that = this
      this.$http.get('/api/novel/').then(function (response) {
        that.novel_infos = response.data.results
      })
    }
  },
  created () {
    this.getData()
    this.current_novel = null
    this.current_chapter = null
  }
}
</script>

<style scoped>
  .red {
    color: chartreuse;
  }
</style>
