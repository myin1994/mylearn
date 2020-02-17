# 客户端项目搭建基本流程

## 创建项目目录

+ 创建

  ```
  cd 项目目录[荏苒资讯]
  vue init webpack renran
  ```

+ pycharm运行

  ```
  add Configuration中配置npm run dev
  ```

+ 访问

  ```
  #访问对应地址即可
  http://localost:8080
  ```

## 初始化项目

清除默认的HelloWorld.vue组件和APP.vue中的默认模板代码和默认css样式

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

## 安装路由vue-router

官方文档：https://router.vuejs.org/zh/

### 下载路由组件

```
npm i vue-router -S
npm install vue-router --save
----------------------------
#全局
npm i vue-router -g
```

### 配置路由流程

1. 在src目录下创建routers路由目录，在routers目录下创建index.js路由文件

   ```javascript
   //index.js路由文件中，编写初始化路由对象的代码 
   
   //引入vue和vue-router组件核心对象
   import Vue from "vue";
   import Router from "vue-router";
   
   // 这里导入可以让让用户访问的组件
   //在vue中通过use注册vue-router组件
   Vue.use(Router);
   
   //导入组件
   import 组件名 from "..\components\"
   
   export default new Router({
     // 设置路由模式为‘history’，去掉默认hash模式中的#，工作中常用的模式
     mode: "history",
     routes:[
       // 路由列表
   		{name:'',path:'',component:''},  // name路由别名,path路由地址,component路由对应的组件类名(使用时不需要加引号)
       {name:'',path:'',component:''},
     ]
   })
   #name的作用是替代url地址进行url跳转，或者用于显示内容
   ```

2. 注册路由信息

   打开main.js文件，把router路由规则对象注册到vue中.

   ```javascript
   import Vue from 'vue'
   import App from './App'
   //import router from './routers/index'  
   
   import router from '@/routers/index'   
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

3. 在视图中显示路由对应的内容

   在App.vue组件中，添加显示路由对应的内容。

   ```vue
   <template>
     <div id="app">
       <router-view/>  <!-- 在组件中使用子组件的写法 -->
         <router-view/ name="name别名"><!--直接指定唯一路由的写法-->
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

### 路由对象提供的操作

#### 页面跳转

+ router-link标签跳转（例如，在Home.vue组件中，使用router-link跳转到User.vue组件中。）

  + routes/index.js，代码

    ```javascript
    import Vue from "vue";
    import Router from "vue-router";
    import Home from "../components/Home";
    import User from "../components/User";
    Vue.use(Router);
    export default new Router({
      mode: "history",
      routes:[
    		{name:'home',path:'/',component:Home},
    		{name:'user',path:'/user',component:User},
      ]
    });
    ```

  + Home.vue代码

    ```vue
    <template>
        <div>
          home页面
          <a href="/user">a标签跳转</a>
            <!-- router-link标签，本质上就是a标签，只是由vue-router进行加工处理
          可以显示局部页面刷新，不会重新加载内容，进行ajax跳转
           -->
    		<!--      直接写路由-->
          <router-link to="/user">个人中心</router-link>
    		<!--      传入data数据路由-->
          <router-link :to="url">个人中心</router-link>
    		<!--      通过路由别名跳转-->
          <router-link :to="{name:'user'}">个人中心</router-link>
        </div>
    </template>
    
    <script>
        export default {
            name: "Home",
            data(){
              return {
                url:"/user"
              }
            }
        }
    </script>
    
    <style scoped>
    
    </style>
    ```

+ `this.$router.push()`跳转

  在`<script>`中使用`this.$router.push(url地址)`来跳转

  在`<script>`中还可以使用`this.$router.go(整数)`，表示跳转返回上一页或者上几页，下一个或者下几页

  ```vue
  <template>
      <div>
        home页面
        <button @click="push">push跳转</button>
      </div>
  </template>
  
  <script>
      export default {
          name: "Home",
          methods:{
            push(){
              // 跳转到站内的制定地址页面中，本质上就是 location.href
              // 注意,this.$router.push() 不能跳转到其他网站。如果真的要跳转外站，则使用location.href="站外地址，记得加上http://协议"
              this.$router.push("/user");
              // 开发中可以先进行权限，登录之类的判断，然后再进行跳转
              // this.$router.back(); // 返回上一页，本质上就是 location.back()
              // this.$router.go(-1); // 返回上一页，本质上就是 location.go()
              // this.$router.forward(); // 跳转到下一页，本质上就是 location.forward()
            }
          }
      }
  </script>
  
  <style scoped>
  
  </style>
  ```

#### 参数传递

`vue-router`提供了`this.$route`，可以让我们接受来自其他页面的附带参数。

+ 查询字符串(`query string`)，就是地址栏上面`?`号后面的参数，

  例如：`http://localhost:8008/user?name=xiaoming&pwd=123`，这里`name=xiaoming&pwd=123`就是查询字符串参数。

  + Home.vue代码---提供参数

    ```vue
    <template>
        <div>
          home页面
          <router-link :to="`/user/?uname=${uname}&pwd=${pwd}`">跳转</router-link>
        </div>
    </template>
    
    <script>
        export default {
            name: "Home",
            data(){
              return {
                uname:"用户名",
                pwd:"密码"
              }
            }
        }
    </script>
    
    <style scoped>
    
    </style>
    ```

  + User.vue代码---获取查询参数

    ```vue
    <template>
        <div>
          user页面
        </div>
    </template>
    
    <script>
        export default {
            name: "User",
            created() {
              // this.$route是vue-router提供的一个用于接收地址参数的对象。
              // query是this.$route里面的一个数组，this.$route会自动收集地址栏上所有的参数保存到query里面
              let uname = this.$route.query.uname;
              let pwd = this.$route.query.pwd;
              console.log(`name=${name}&pwd=${pwd}`)
            }
        }
    </script>
    
    <style scoped>
    
    </style>
    ```

+ 路由参数(`router params`)，就是地址栏上面路由路径的一部分，

  例如：`http://localhost:8080/user/300/xiaoming`，此时，300属于路由路径的一部分，这个300就是路由参数.，当然，xiaoming,或者user也可以理解是路由参数，就是看我们的页面中是否需要接收而已。

  + src/routes/index.js设置路由参数

    ```javascript
    #冒号:后的内容即为路由参数
    routes:[
    		{name:'home',path:'/',component:Home},
    		{name:'user',path:'/user/:id/img-/:img_id',component:User},
      ]
    ```

  + Home.vue代码---提供参数

    ```vue
    <template>
        <div>
          home页面
          <router-link to="/user/100/img-/10086">路由参数</router-link>
        </div>
    </template>
    
    <script>
        export default {
            name: "Home",
        }
    </script>
    
    <style scoped>
    
    </style>
    ```

  + User.vue代码---获取路由参数

    ```vue
    <template>
        <div>
          user页面
        </div>
    </template>
    
    <script>
        export default {
            name: "User",
            created() {
              // params是this.$route里面的一个数组，this.$route会自动收集路由列表中已经标记为路由参数所有内容保存到params中
              let id = this.$route.params.id;
              console.log(id);
              let img_id = this.$route.params.img_id;
              console.log(`img_id = ${img_id}`);
            }
        }
    </script>
    
    <style scoped>
    
    </style>
    ```

## ElementUI

对于前端页面布局，我们可以使用一些开源的UI框架来配合开发，常用的UI框: bootstap，H-ui框架，lay-UI框架，Amaze UI，zui框架，ElementUI.

Vue开发前端项目中，比较常用的就是ElementUI了。

ElementUI是饿了么团队开发的一个UI组件框架，这个框架提前帮我们提供了很多已经写好的通用模块，我们可以在Vue项目中引入来使用，这个框架的使用类似于我们前面学习的bootstrap框架，也就是说，我们完全可以把官方文档中的组件代码拿来就用，有定制性的内容，可以直接通过样式进行覆盖修改就可以了。

中文官网：http://element-cn.eleme.io/#/zh-CN

文档快速入门：http://element-cn.eleme.io/#/zh-CN/component/quickstart

### 快速安装ElementUI

```
npm i element-ui -S
npm install element-ui --save
```

### 配置ElementUI到项目中

在main.js中导入ElementUI，并调用。

```javascript
// elementUI 导入
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
// 调用插件
Vue.use(ElementUI);
```

成功引入了ElementUI以后，接下来我们就可以开始进入前端页面开发。