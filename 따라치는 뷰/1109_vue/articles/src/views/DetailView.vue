<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>글 제목 : {{ article?.title }}</p>
    <p>글 내용 : {{ article?.content }}</p>
    <!-- <p>글 작성시간 : {{ article?.createdAt }}</p> -->
    <p>작성시간 : {{ articleCreatedAt }}</p>
    <router-link :to="{ name: 'index'}">뒤로가기</router-link>
  </div>
</template>

<script>

export default {
  name: 'DetailView',
  data() {
    return {
      article: null,
    }
  },
  computed: {
    articles() {
      return this.$store.state.articles
    },
    articleCreatedAt() {
      const article = this.article
      const createdAt = new Date(article?.createAt).toLocaleString()
      return createdAt
    }
  },
  methods: {
    getArticleById(id) {
      // const id = this.$store.params.id
      for (const article of this.articles) {
        if (article.id === Number(id)) {
          this.article = article
          break
        }
      }
    }
  },
  created() {
    this.getArticleById(this.$route.params.id)
  }
}
</script>

<style>

</style>