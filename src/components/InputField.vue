<template>
<div>
<section class="hero is-primary">
  <div class="hero-body">
    <div class="container">
      <h1 class="title">
        Wattpad Story Downloader
      </h1>
      <h2 class="subtitle">
        Enter URL below
      </h2>
      <div class="container">
        <b-input :disabled="isProcessing" placeholder="https://wattpad.com" v-model="url" @keyup.enter.native="enterClicked" maxlength="2083"></b-input>
      </div>
    </div>
  </div>
</section>
<div class="section">
  <b-progress v-if="isProcessing"></b-progress>
  <div v-if="results">
    <a v-bind:href="results" class="button is-success">Download</a>
  </div>
</div>
</div>
</template>
<script>
import { HTTP } from '../http-common';

export default {
  name: 'InputField',
  data() {
    return { url:"", isProcessing:false, results:"" }
  },
  methods: {
    enterClicked() {
      console.log(this.url);
      this.results = "";
      this.isProcessing = true;
      HTTP.post('api', { url: this.url }).then((r) => {
        this.isProcessing = false;
        this.results = "/cdn/"+r.data;
      })
    }
  }
}
</script>
