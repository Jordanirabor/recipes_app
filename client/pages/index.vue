<template>
  <header>
    <div class="text-box">
      <h1>La Recipes 😋</h1>
      <p class="mt-3">Recipes for the meals we love ❤️ ️</p>
      <nuxt-link class="btn btn-outline btn-large btn-info" to="/recipes">
        View Recipes <span class="ml-2">&rarr;</span>
      </nuxt-link>
    </div>
  </header>
</template>
<script>
export default {
  head() {
    return {
      title: "Home page"
    };
  },
};
</script>
<style>
header {
  min-height: 100vh;
  background-image: linear-gradient(
      to right,
      rgba(0, 0, 0, 0.9),
      rgba(0, 0, 0, 0.4)
    ),
    url("/images/banner.jpg");
  background-position: center;
  background-size: cover;
  position: relative;
}
.text-box {
  position: absolute;
  top: 50%;
  left: 10%;
  transform: translateY(-50%);
  color: #fff;
}
.text-box h1 {
  font-family: cursive;
  font-size: 5rem;
}
.text-box p {
  font-size: 2rem;
  font-weight: lighter;
}
</style>