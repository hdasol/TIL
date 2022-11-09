<template>
  <div class="about">
    <h1>This is an about page</h1>
    <!-- 프로그램방식 -->
    <router-link :to="{ name: 'home' }">홈으로!</router-link>
    <!-- 선언적방식 -->
    <button @click="toHome">홈으로!</button>
    <input 
    type="text"
    v-model="inputData" 
    @keyup.enter="goToHello">
  </div>
</template>

<script>
export default {
  name: 'AboutView',
  data() {
    return {
      inputData: null,
    }
  },
  methods: {
    toHome() {
      this.$router.push({ name: 'home'})
    },
    goToHello() {
      this.$router.push({ name: 'hello', params: { userName: this.inputData }})
    },
  }

}
</script>
