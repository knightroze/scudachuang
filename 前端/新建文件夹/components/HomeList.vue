<template>
    <nav class="col-lg-2 d-none d-md-block bg-light sidebar">
      <div class="sidebar-sticky">
        <ul class="nav flex-column">
          <li class="nav-item">
            <a class="nav-link" href="#" @click="HomeShowChange(1)">
              首页 <span class="sr-only">(current)</span>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#" @click="HomeShowChange(2)">
              Orders
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">
              Products
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">
              Customers
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">
              Reports
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">
              Integrations
            </a>
          </li>
        </ul>

        <h6 class="sidebar-heading d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-muted">
          <span>Saved reports</span>
          <a class="d-flex align-items-center text-muted" href="#">
            <span data-feather="plus-circle"></span>
          </a>
        </h6>
        <ul class="nav flex-column mb-2">
          <li class="nav-item">
            <a class="nav-link" href="#">
              Current month
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">
              Last quarter
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">
              Social engagement
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">
              Year-end sale
            </a>
          </li>
        </ul>
      </div>
    </nav>
</template>

<script>

export default {
  name: 'HomeList',
  data () {
    return {
    }
  },
  methods: {
    HomeShowChange: function (e) {
      this.$store.commit({
        type: 'changeHomeShow',
        value: e
      })
    }
  }
}
</script>

<style>
#HomeList{
    padding:0;
    border-right: 0.1rem solid #ccc;
    height:100%;
    margin:0;
    background-color: whitesmoke;
}
.panel-title{
    font-size: 1rem;
    font-style: inherit;
    padding-left: 20%;
}
#homelist-panels{
    border: 0;

}
#homelist-panel-heading{
    border: 0.1rem solid #ccc;
}
.bd-placeholder-img {
  font-size: 1.125rem;
  text-anchor: middle;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

@media (min-width: 768px) {
.bd-placeholder-img-lg {
    font-size: 3.5rem;
    }
}

.sidebar {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  /* z-index: 100; Behind the navbar */
  padding: 48px 0 0; /* Height of navbar */
  box-shadow: inset -1px 0 0 rgba(0, 0, 0, .1);
}

.sidebar-sticky {
  position: relative;
  top: 0;
  height: calc(100vh - 48px);
  padding-top: .5rem;
  overflow-x: hidden;
  overflow-y: auto; /* Scrollable contents if viewport is shorter than content. */
}

@supports ((position: -webkit-sticky) or (position: sticky)) {
  .sidebar-sticky {
    position: -webkit-sticky;
    position: sticky;
  }
}

.sidebar .nav-link {
  font-weight: 500;
  color: #333;
}

.sidebar .nav-link .feather {
  margin-right: 4px;
  color: #999;
}

.sidebar .nav-link.active {
  color: #007bff;
}

.sidebar .nav-link:hover .feather,
.sidebar .nav-link.active .feather {
  color: inherit;
}

.sidebar-heading {
  font-size: .75rem;
  text-transform: uppercase;
}

/*
 * Content
 */

[role="main"] {
  padding-top: 133px; /* Space for fixed navbar */
}

@media (min-width: 768px) {
  [role="main"] {
    padding-top: 48px; /* Space for fixed navbar */
  }
}
</style>
