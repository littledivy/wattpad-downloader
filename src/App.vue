<template>
  <div id="app">
    <Navbar />
    <Input />
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
import Input from './components/InputField.vue'

export default {
  name: 'App',
  components: {
    Input,
    Navbar
  }
}
</script>
