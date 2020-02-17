# 路飞学城项目前端

[TOC]

# 笔记

# 1. 项目分析

```
首页
	导航、登录注册栏、轮播图、地板导航
登录注册
	选项卡
免费课
	课程分类、筛选、课程列表
免费课详情
	课程封面视频、优惠活动倒计时、选项卡
我的购物车
	全选、商品价格统计
购买结算
	
购买成功
	
我的订单
	
课程\课时播放页面
	
```



# 2. 项目搭建

## 2.1 创建项目目录

```
cd 项目目录
vue init webpack luffy
```

例如，我要把项目保存在桌面下 ~/Desktop/luffy ，可以如下操作：

```shell
cd Desktop
vue init webpack luffy
```

根据需要在生成项目时，我们选择对应的选项。

根据上面的提示，我们已经把vue项目构建好了，接下来我们可以在pycharm编辑器中把项目打开并根据上面黄色提示，运行测试服务器。

打开项目已经，在pycharm的终端下运行vue项目，查看效果。

```
npm run dev
```

接下来，我们根据终端上效果显示的对应地址来访问项目(如果有多个vue项目在运行，8080端口被占据了，服务器会自动改端口，所以根据自己实际在操作中看到的地址来访问。)

访问：http://localost:8080

## 2.2 初始化项目

清除默认的HelloWorld.vue组件和APP.vue中的默认模板代码和默认样式

```vue
<template>
  <div id="app">
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
  }
}
</script>

<style>
</style>

```

修改后效果：



接下来，我们可以查看效果了，一张白纸~



## 2.3 安装路由vue-router

### 2.3.1 下载路由组件

```
npm i vue-router -S
#是npm install vue-router --save的简写
#全局
npm i vue-router -g
```

执行效果：



### 2.3.2 配置路由

#### 2.3.2.1 初始化路由对象

在src目录下创建routers路由目录，在routers目录下创建index.js路由文件

效果：

index.js路由文件中，编写初始化路由对象的代码 .

```javascript
//引入vue和vue-router组件核心对象
import Vue from "vue"
import Router from "vue-router"

// 这里导入可以让让用户访问的组件
//在vue中通过use注册vue-router组件
Vue.use(Router);

//导入组件
import 组件名 from "..\components\"

export default new Router({
  // 设置路由模式为‘history’，去掉默认的#，工作中常用的模式
  mode: "history",
  routes:[
    // 路由列表
		{name:'',path:'',component:''},  // name路由别名,path路由地址,component路由对应的组件类名
    {name:'',path:'',component:''},
  ]
})
#name的作用是替代url地址进行url跳转，或者用于显示内容
```

#### 2.3.2.2 注册路由信息

打开main.js文件，把router路由规则对象注册到vue中.

代码：

```javascript
// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router/index'  
//1、引入，这样引入文件那么会直接拿到这个文件中export default后面的对象，export default的意思是将对象暴露出去，让别人可以引入
import router from '@/router/index'   
// @符号表示的是src的目录路径，这样写起来更靠谱一些，因为引入src目录里面的内容的时候就不需要知道当前文件和src目录里面的文件隔着基层了
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,  2、注册
  components: { App },
  template: '<App/>'
});

```



#### 2.3.2.3 在视图中显示路由对应的内容

在App.vue组件中，添加显示路由对应的内容。

代码：

```vue
<template>
  <div id="app">
    <router-view/>  <!-- 在组件中使用子组件的写法 -->
      <router-view/ name="name别名">
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {

  }
}
</script>

<style>

</style>

```

**注：如果项目初始化时选择安装vue-router组件，则上述步骤自动执行**



## 3. 引入ElementUI

对于前端页面布局，我们可以使用一些开源的UI框架来配合开发，Vue开发前端项目中，比较常用的就是ElementUI了。

ElementUI是饿了么团队开发的一个UI组件框架，这个框架提前帮我们提供了很多已经写好的通用模块，我们可以在Vue项目中引入来使用，这个框架的使用类似于我们前面学习的bootstrap框架，也就是说，我们完全可以把官方文档中的组件代码拿来就用，有定制性的内容，可以直接通过样式进行覆盖修改就可以了。

中文官网：http://element-cn.eleme.io/#/zh-CN

文档快速入门：http://element-cn.eleme.io/#/zh-CN/component/quickstart



### 3.1 快速安装ElementUI

项目根目录执行以下命令:

```
npm i element-ui -S
```

上面的命令等同于 `npm install element-ui --save`

执行命令效果：



### 3.2 配置ElementUI到项目中

在main.js中导入ElementUI，并调用。代码：

```javascript
// elementUI 导入
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';  // 需要import引入一下css文件，和我们的link标签引入是一个效果，而import .. from ..是配合export default来使用的
// 调用插件
Vue.use(ElementUI);
```

效果：



成功引入了ElementUI以后，接下来我们就可以开始进入前端页面开发，首先是首页。



# 4. 首页

首页采用了上下页面布局，首页是导航栏、轮播图。。。脚部等几个小模块。所以我们可以把首页作为一个组件进行开发，然后把首页的这些小模块作为单独的组件来进行开发。

## 4.1 创建首页组件

在src/components目录下创建文件 Home.vue

代码：

```vue
<template>
  <div id="home">
    首页
  </div>
</template>

<script>
export default {
  name:"Home",
  data(){
    return {

    }
  }
}
</script>

<style scoped>

</style>

```

效果：



### 4.1.1 创建首页对应的路由

在router/index.js中引入Home组件，并设置Home组件作为首页路由。

代码：

```javascript
import Vue from "vue"
import Router from "vue-router"

// 后面这里引入可以被用户访问的页面组件
import Home from "../components/Home"

Vue.use(Router);

export default new Router({
  // 路由跳转模式，注意使用 history
  mode: "history",

  // 路由规则
  routes:[
    {
      // name:"路由别名",
      name:"Home",
      // path: "路由地址",
      path: "/",
      // component: 组件类名,
      component: Home,
    },{
      // name:"路由别名",
      name:"Home",
      // path: "路由地址",
      path: "/home",
      // component: 组件类名,
      component: Home,
    },
  ]
})

```



效果：

![1556416079117](assets/1556416079117.png)



## 4.2 开发导航子组件

经过前面的观察，可以发现导航不仅在首页出现，其他页面也有，所以对于这些不同页面中公共的内容，可以创建一个单独的组件目录存放。

![1552501540495](assets/1552501540495.png)



创建src/components/common/Header.vue目录路径，编写代码：

```vue
<template>

</template>

<script>
  export default {
    name: "Header",
    data(){
      return {
        
      };
    }
  }
</script>

<style scoped>

</style>
```

效果：

![1552501465055](assets/1552501465055.png)



### 4.2.1 在首页引入导航组件

代码：

```vue
<template>
  <div class="home">
    <Header/>
  </div>
</template>

<script>
  import Header from "./common/Header"
  export default {
    name: "Home",
    data(){
      return {

      };
    },
    components:{
      Header,
    }
  }
</script>

<style scoped>

</style>

```



效果：

![1552502367059](assets/1552502367059.png)



接下来，我们就可以在组件中参考ElementUI文档来进行样式开发了。

![1552503046597](assets/1552503046597.png)



Header的子组件代码：

```vue
<template>
  <div class="header">
    <el-container>
      <el-header>
        <el-row>
          <el-col class="logo" :span="3">
            <a href="/">
              <img src="@/assets/head-logo.svg" alt="">
            </a>
          </el-col>
          <el-col class="nav" :span="16">
              <el-row>
                <el-col :span="3"><router-link to="/">免费课</router-link></el-col>
                <el-col :span="3"><router-link to="/">轻课</router-link></el-col>
                <el-col :span="3"><router-link to="/">学位课</router-link></el-col>
                <el-col :span="3"><router-link to="/">题库</router-link></el-col>
                <el-col :span="3"><router-link to="/">教育</router-link></el-col>
              </el-row>
          </el-col>
          <el-col class="login-bar" :span="5">
            <el-row>
              <el-col class="cart-ico" :span="9">
                <router-link to="">
                  <b class="goods-number">0</b>
                  <img class="cart-icon" src="@/assets/cart.svg" alt="">
                  <span>购物车</span>
                </router-link>
              </el-col>
              <el-col class="study" :span="8" :offset="2"><router-link to="">学习中心</router-link></el-col>
              <el-col class="member" :span="5">
                <el-menu class="el-menu-demo" mode="horizontal">
                  <el-submenu index="2">
                    <template slot="title"><router-link to=""><img src="@/assets/logo@2x.png" alt=""></router-link></template>
                    <el-menu-item index="2-1">我的账户</el-menu-item>
                    <el-menu-item index="2-2">我的订单</el-menu-item>
                    <el-menu-item index="2-3">我的优惠卷</el-menu-item>
                    <el-menu-item index="2-3">退出登录</el-menu-item>
                  </el-submenu>
                </el-menu>
              </el-col>
            </el-row>
          </el-col>
        </el-row>
      </el-header>
    </el-container>
  </div>
</template>

<script>
  export default {
    name: "Header",
    data(){
      return {
        // 设置一个登录标识，表示是否登录
        token: false,
      };
    }
  }
</script>

<style scoped>
  .header{
    box-shadow: 0 0.5px 0.5px 0 #c9c9c9;
  }
  .header .el-container{
    width: 1200px;
    margin: 0 auto;
  }
  .el-header{
    height: 80px!important;
    padding:0;
  }
  .logo{

  }
  .logo img{
    padding-top: 22px;
  }

  .nav{
    margin-top: 22px;
  }

  .nav .el-col a{
    display: block;
    text-align: center;
    padding-bottom: 16px;
    padding-left: 5px;
    padding-right: 5px;
    position: relative;
    font-size: 16px;
  }

  .login-bar{
    margin-top: 22px;
  }
  .cart-ico{
    position: relative;
    border-radius: 17px;
  }
  .cart-ico:hover{
    background: #f0f0f0;
  }
  .goods-number{
    width: 16px;
    height: 16px;
    line-height: 17px;
    font-size: 12px;
    color: #fff;
    text-align: center;
    background: #fa6240;
    border-radius: 50%;
    transform: scale(.8);  /* 字体缩放 */
    position: absolute;
    left: 16px;
    top: -1px;
  }
  .cart-icon{
    width: 15px;
    height: auto;
    margin-left: 6px;
  }
  .cart-ico span{
    margin-left: 12px;
  }
  .member img{
    width: 26px;
    height: 26px;
    border-radius: 50%;
    display: inline-block;
  }
  .member img:hover{
    border: 1px solid yellow;
  }

</style>

```

App.vue，中设置一些公共样式的代码：

```vue
<style>
  body{
    padding: 0;
    margin:0;
  }
  a{
    text-decoration: none;
    color: #4a4a4a;
  }
  a:hover{
    color: #000;
  }
  .header .el-menu li .el-submenu__title{
    height: 26px!important;
    line-height: 26px!important;
  }
  .el-menu--popup{
    min-width: 140px;
  }
</style>
```





Home组件中引入使用Header子组件，代码无需改变，直接访问效果：

![1556423948867](assets/1556423948867.png)





## 4.3 开发轮播图子组件

![1552503138518](assets/1552503138518.png)

### 4.3.1 创建Banner.vue组件文件

代码：

```vue
<template>
  <div class="banner">

  </div>
</template>

<script>
  export default {
    name:"Banner",
    data(){
      return {};
    }
  }
</script>

<style scoped>

</style>

```



![1552532166152](assets/1552532166152.png)



### 4.3.1 在Home组件中引入Banner子组件

```vue
<template>
  <div class="home">
    <Header/>
    <Banner/>
  </div>
</template>

<script>
  import Header from "./common/Header"
  import Banner from "./common/Banner"
  export default{
    name:"Home",
    data(){
      return {};
    },
    components:{
      Header,
      Banner,
    }
  }
</script>

<style scoped>
.home{
  padding-top: 80px;
}
</style>

```

效果：

![1552532278649](assets/1552532278649.png)



接下来，在ElementUI中有对应的轮播图[跑马灯]效果，可以直接提取过来使用。

![1556424098873](assets/1556424098873.png)

注意，图片保存到static目录下。保存在assets目录下的图片等同于保存在static/img目录下。

![1556424903235](assets/1556424903235.png)

对于图片的使用，如果是vue代码中直接要使用的图片，可以保存accets目录下，如果是第三方插件要使用到的图片，需要保存在static目录下。其实本质上来说，所有的图片都是保存在static目录下的，而assets目录下的内容,最终被vue解析成地址的时候,也是在static目录的.



Banner.vue组件,代码:

```vue
<template>
  <div class="banner">
      <el-carousel trigger="click" height="506px">
        <el-carousel-item v-for="banner in banner_list">
          <a :href="banner.link"><img width="100%" :src="banner.img" alt=""></a>
        </el-carousel-item>
      </el-carousel>
  </div>
</template>

<script>
  export default {
    name:"Banner",
    data(){
      return {
        banner_list:[
          {link:"http://www.baidu.com",img:"/static/banner/1.png"},
          {link:"http://www.baidu.com",img:"/static/banner/2.png"},
          {link:"http://www.baidu.com",img:"/static/banner/3.png"},
        ]
      };
    }
  }
</script>

<style scoped>

</style>

```

效果:

![1552533179082](assets/1552533179082.png)



## 4.5 页面脚部

### 4.5.1 创建脚部组件文件

![1552535310891](assets/1552535310891.png)

代码：

```vue
<template>
  <div class="footer">

  </div>
</template>

<script>
  export default {
    name:"Footer",
    data(){
      return {}
    }
  }
</script>


<style scoped>

</style>

```

### 4.5.2 在Home组件中引入Footer组件

Home组件代码：

```vue
<template>
  <div class="home">
    <Header/>
    <Banner/>
    <Footer/>
  </div>
</template>

<script>
  import Header from "./common/Header"
  import Banner from "./common/Banner"
  import Footer from "./common/Footer"
  export default{
    name:"Home",
    data(){
      return {};
    },
    components:{
      Header,
      Banner,
      Footer,
    }
  }
</script>

<style scoped>
.home{
  padding-top: 80px;
}
</style>

```

效果:

![1552535407021](assets/1552535407021.png)



### 4.5.3 编写脚部样式

```vue
<template>
  <div class="footer">
    <el-container>
      <el-row>
        <el-col :span="4"><router-link to="">关于我们</router-link></el-col>
        <el-col :span="4"><router-link to="">联系我们</router-link></el-col>
        <el-col :span="4"><router-link to="">商务合作</router-link></el-col>
        <el-col :span="4"><router-link to="">帮助中心</router-link></el-col>
        <el-col :span="4"><router-link to="">意见反馈</router-link></el-col>
        <el-col :span="4"><router-link to="">新手指南</router-link></el-col>
        <el-col :span="24"><p class="copyright">Copyright © luffycity.com版权所有 | 京ICP备17072161号-1</p></el-col>
      </el-row>
    </el-container>
  </div>
</template>

<script>
  export default {
    name:"Footer",
    data(){
      return {}
    }
  }
</script>


<style scoped>
.footer{
  width: 100%;
  height: 128px;
  background: #25292e;
}
.footer .el-container{
  width: 1200px;
  margin: auto;
}
.footer .el-row {
  align-items: center;
  padding: 0 200px;
  padding-bottom: 15px;
  width: 100%;
  margin-top: 38px;
}
.footer .el-row a{
  color: #fff;
  font-size: 14px;
}
.footer .el-row .copyright{
  text-align: center;
  color: #fff;
  font-size: 14px;
}
</style>

```



效果：

![1556425996044](assets/1556425996044.png)



首页的三大块我们已经完成了，但是我们开始新的页面出现之前，我们需要把链接补充上， 新增课程的导航链接.

接下来,我们就可以创建免费课的组件.



# 5. 免费课

在组件目录components下创建Couses.vue组件文件,代码如下:

```vue
<template>
  <div class="courses">

  </div>
</template>

<script>
  export default {
    name:"Courses",
    data(){
      return {

      }
    }
  }
</script>


<style scoped>
  
</style>

```

### 5.1 在router/index.js路由中注册路由

```javascript
import Vue from "vue"
import Router from "vue-router"

// 导入可以被用户访问的组件
import Home from "@/components/Home"
import Courses from "@/components/Courses"

Vue.use(Router);

export default new Router({
  mode: "history",
  routes:[
    // 路由列表
    {
      path: "/",
      name: "Home",
      component:Home,
    },
    {
      path: "/home",
      name: "Home",
      component:Home,
    },
    {
      path: "/courses",
      name: "Courses",
      component:Courses,
    },

  ]
})

```

