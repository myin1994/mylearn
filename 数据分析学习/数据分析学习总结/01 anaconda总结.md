+ 下载与安装

  ```
  https://www.anaconda.com/download/ 进行下载
  ```

+ 虚拟环境

  + 创建虚拟环境

    ```
    conda create -n 虚拟环境名称 python=版本号
    ```

  + 删除虚拟环境

    ```
    conda remove -n 虚拟环境名称 --all
    ```

  + 激活（进入）虚拟环境

    ```
    source activate 虚拟环境名称
    ```

  + 离开虚拟环境

    ```
    source deactivate
    ```

  + 显示当前所有虚拟环境与当前处于那个虚拟环境

    ```
    conda info --envs
    
    conda info 显示更多信息  
    ```

    

  + 说明

    + 当创建虚拟环境后，就会在Anaconda安装目录下的envs目录下，创建虚拟环境相关的文件。

    + 在Linux环境下，需要使用source，Windows需要省去source。

    + 创建虚拟环境后，虚拟环境中仅会安装一些必须的软件包，例如pip等。如果需要安装Anaconda所有的库，需要：

      ```anaconda
      conda create -n 虚拟环境名称 python=版本号 anaconda
      ```

+ conda包管理器

  + 安装包
    `conda install 包`
  + 卸载包
    `conda remove 包`
  + 更新包
    `conda update 包`
  + 查看包
    `conda list`

+ Anaconda Navigator

  Anaconda Navigator是Anaconda提供的一款图形化界面工具，我们可以方便的实现虚拟环境以及软件包的管理。