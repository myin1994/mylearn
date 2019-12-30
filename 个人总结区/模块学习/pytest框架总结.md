## pytest介绍

pytest是Python的单元测试框架，同自带的unittest框架类似，但pytest框架使用起来更简洁，效率更高。

```
学习链接：https://www.cnblogs.com/Neeo/articles/11832655.html#allure
```

### 特点

+ 入门简单易上手，文档支持较好。
+ 支持单元测试和功能测试。
+ 支持参数化。
+ 可以跳过指定用例，或对某些预期失败的case标记成失败。
+ 支持重复执行失败的case。
+ 支持运行由unittest编写的测试用例。
+ 有很多第三方插件，并且可自定义扩展。
+ 方便和支持集成工具进行集成。

### 安装

```
pip install pytest
```

### 测试

```shell
C:\Users\24479>pytest --version
This is pytest version 5.3.2, imported from c:\python36\lib\site-packages\pytest\__init__.py
setuptools registered plugins:
  allure-pytest-2.8.6 at c:\python36\lib\site-packages\allure_pytest\plugin.py
  pytest-shutil-1.7.0 at c:\python36\lib\site-packages\pytest_shutil\workspace.py
```

## 使用

### 单个py文件中使用

+ 定义test开头的函数或Test开头的类

+ 使用pytest.main(['-s','filename'])执行测试用例

  + `-s`，表示输出用例执行的详细结果。
  + `filename`是要执行的脚本名称。

  ```python
  import pytest
  def testfunc():
      assert 0
  class TestCase:
  
      def test_1(self):
          assert 1
  
      def test_2(self):
          assert 0
  
      def test3(self):
          assert 0
  if __name__ == '__main__':
      pytest.main(['-s','py_test.py'])
  ```

+ setup和teardown

  setup和teardown可以在每个用例前后执行，也可以在所有的用例集执行前后执行。

  + 模块级别，也就是在**整个测试脚本**文件中的用例集开始前后(只执行一次)
    + setup_module
    + teardown_module
  + 类级别，在**类中**的所有用例集执行前后（在每一个类中只执行一次）
    - setup_class
    - teardown_class
  + 在**类中**呢，也可以在进一步划分，在**每一个方法**执行前后(执行次数由类中用例数量决定)
    - setup_method
    - teardown_methd
  + 函数级别，在**用例函数**之前后(执行次数根据单独的用例函数数量决定)
    - setup_function
    - teardown_function

### 配置文件运行

+ pytest.ini文件配置

  在项目根目录下（注意，配置文件中不许有中文）

  ```ini
  [pytest]
  addopts = -s -v
  testpaths = ./scripts
  python_files = test_*.py
  python_classes = Test*
  python_functions = test_*
  ```

  + 相关参数

    + `addopts`可以搭配相关的参数，比如`-s`。多个参数以空格分割，其他参数后续用到再说。

      - `-s`，在运行测试脚本时，为了调试或打印一些内容，我们会在代码中加一些print内容，但是在运行pytest时，这些内容不会显示出来。如果带上-s，就可以显示了。
      - `-v`，使输出结果更加详细。

    + `testpaths`配置测试用例的目录，

      - 因为我们用例可能分布在不同的目录或文件中，那么这个`scripts`就是我们所有文件或者目录的顶层目录。其内的子文件或者子目录都要以`test_`开头，pytest才能识别到。
      - 另外，上面这么写，是从一个总目录下寻找所有的符合条件的文件或者脚本，那么我们想要在这个总目录下执行其中某个具体的脚本文件怎么办？

      ```ini
      [pytest]
      testpaths = ./scripts/
      python_files = test_case_01.py
      ```

      这么写就是执行`scripts`目录下面的`test_case_01.py`这个文件。

    + `python_classes`则是说明脚本内的所有用例类名必须是以`Test`开头，当然，你也可以自定义为以`Test_`开头，而类中的用例方法则当然是以`test_`开头。

    + `python_functions`则是说脚本内的所有用例函数以`test_`开头才能识别。

+ 执行测试用例

  在终端中（前提是在项目的根目录），直接输入`pytest`即可

### 跳过用例

+ 使用方法

  + @pytest.mark.skip(condition, reason)无条件跳过用例

  + @pytest.mark.skipif(condition, reason)满足条件跳过用例

    + condition表示跳过用例的条件。
    + reason表示跳过用例的原因。

    ```python
    import pytest
    
    @pytest.mark.skip(condition='我就是要跳过这个用例啦')
    def test_case_01():
        assert 1
    
    @pytest.mark.skipif(condition=1 < 2, reason='如果条件为true就跳过用例')
    def test_case_02():
        assert 1
    ```

  + 然后将它装饰在需要被跳过用例的的函数或类（将跳过类中所有函数）上面

### 标记预期失败

如果我们事先知道测试函数会执行失败，但又不想直接跳过，而是希望显示的提示

+ Pytest 使用 `pytest.mark.xfail`实现预见错误功能

  + condition，预期失败的条件，当条件为真的时候，预期失败。
  + reason，失败的原因。

+ 预期失败的几种情况

  + 预期失败，但实际结果却执行成功。
  + 预期失败，实际结果也执行执行失败。

  ```
  import pytest
  
  
  class TestCase(object):
  
      @pytest.mark.xfail(1 < 2, reason='预期失败， 执行失败')
      def test_case_01(self):
          """ 预期失败， 执行也是失败的 """
          print('预期失败， 执行失败')
          assert 0
  
      @pytest.mark.xfail(1 < 2, reason='预期失败， 执行成功')
      def test_case_02(self):
          """ 预期失败， 但实际执行结果却成功了 """
          print('预期失败， 执行成功')
          assert 1
  >>>
  ====================== test session starts =============
  platform win32 -- Python 3.6.2, pytest-5.2.2, py-1.8.0, pluggy-0.13.0
  rootdir: M:\py_tests, inifile: pytest.ini, testpaths: ./scripts/
  plugins: allure-pytest-2.8.6, cov-2.8.1, forked-1.1.3, html-2.0.0, metadata-1.8.0, ordering-0.6, rerunfailures-7.0, xdist-1.30.0
  collected 2 items                                                                                                                         
  
  scripts\demo1.py xX                                                                                                                 [100%]
  
  =============== 1 xfailed, 1 xpassed in 0.15s ======================
  ```

  + pytest 使用 `x` 表示预见的失败（XFAIL）

  + 如果预见的是失败，但实际运行测试却成功通过，pytest 使用 `X` 进行标记（XPASS）。

    + 需要将预期失败，结果却执行成功了的用例标记为执行失败，可以在`pytest.ini`文件中，加入

      ```ini
      [pytest]
      xfail_strict=true
      ```

      

### 参数化

将一组参数传递给用例进行测试

+ pytest.mark.parametrize(argnames, argvalues)

  + argnames表示参数名。

  + argvalues表示列表形式的参数值。

  + 只有一个参数的测试用例

    ```python
    import pytest
    
    mobile_list = ['10010', '10086']
    
    @pytest.mark.parametrize('mobile', mobile_list)
    def test_register(mobile):
        """ 通过手机号注册 """
        print('注册手机号是: {}'.format(mobile))
    ```

  + 多个参数的测试用例

    ```
    import pytest
    
    mobile_list = ['10010', '10086']
    code_list = ['x2zx', 'we2a']
    
    @pytest.mark.parametrize('mobile', mobile_list)
    @pytest.mark.parametrize('code', code_list)
    def test_register(mobile, code):
        """ 通过手机号注册 """
        print('注册手机号是: {} 验证码是: {}'.format(mobile, code))
    ```

    ```python
    l1 = [{"a": 1}, 10010, 110]
    code = ['xxx', 'ppppp', 'oooo', 'wwww']
    
    @pytest.mark.parametrize("mobile,code", zip(l1, code))
    def test_case(mobile, code):
        print(mobile, code)
        assert 1
    ```

    

### 固件

固件（Fixture）是一些函数，pytest 会在执行测试函数之前（或之后）加载运行它们，也称测试夹具。我们可以利用固件做任何事情，其中最常见的可能就是数据库的初始连接和最后关闭操作。

+ Pytest 使用 `pytest.fixture()` 定义固件

  ```python
  import pytest
  
  @pytest.fixture()
  def login():
      print('登录....')
  
  def test_index(login):
      print('主页....')
  ```

  

### 作用域

pytest通过`scope`参数来控制固件的使用范围，也就是作用域

+ 在定义固件时，通过 `scope` 参数声明作用域，可选项有

  + `function`: 函数级，每个测试函数都会执行一次固件；
  + `class`: 类级别，每个测试类执行一次，所有方法都可以使用；
  + `module`: 模块级，每个模块执行一次，模块内函数和方法都可使用；
  + `session`: 会话级，一次测试只执行一次，所有被找到的函数和方法都可用。

  ```python
  import pytest
  
  @pytest.fixture(scope='function')
  def login():
      print('登录....')
  
  def test_index(login):
      print('主页....')
  ```

  

### 预处理和后处理

很多时候需要在测试前进行预处理（如新建数据库连接），并在测试完成进行清理（关闭数据库连接）。当有大量重复的这类操作，最佳实践是使用固件来自动化所有预处理和后处理。

+ Pytest 使用 `yield` 关键词将固件分为两部分

  + `yield` 之前的代码属于预处理，会在测试前执行
  + `yield` 之后的代码属于后处理，将在测试完成后执行

  ```python
  #以下测试模拟数据库查询，使用固件来模拟数据库的连接关闭
  import pytest
  
  @pytest.fixture()
  def db():
      print('Connection successful')
  
      yield
  
      print('Connection closed')
  
  def search_user(user_id):
      d = {
          '001': 'xiaoming',
          '002': 'xiaohua'
      }
      return d[user_id]
  
  def test_case_01(db):
      assert search_user('001') == 'xiaoming'
  
  def test_case_02(db):
      assert search_user('002') == 'xiaohua'
  ```

  

## pytest测试报告插件

### 下载

```
pip install pytest-html
```

### 使用

在配置文件中，添加参数

```ini
[pytest]
addopts = -s --html=report/report.html
```

### allure插件

+ 库下载

  ```
  pip install allure-pytest
  ```

+ allure工具下载

  + 在下载allure工具之前，它依赖Java环境，我们还需要先配置Java环境。

+ 配置`pytest.ini`

  ```ini
  [pytest]
  addopts =  -v -s --html=report/report.html --alluredir ./report/result
  testpaths = ./scripts/
  python_files = test_allure_case.py
  python_classes = Test*
  python_functions = test_*
  # xfail_strict=true
  ```

+ 终端下使用allure工具来生成HTML报告（先执行pytest）

  ```
  allure generate report/result -o report/allure_html --clean
  ```

+ 可用参数

  + title，自定义用例标题，标题默认是用例名。

  + description，测试用例的详细说明。

    ```python
    import pytest
    import allure
    
    @allure.title('测试用例标题1')
    @allure.description('这是测试用例用例1的描述信息')
    def test_case_01():
        assert 1
    
    def test_case_02():
        assert 0
    
    def test_case_03():
        assert 1
    
      
    #参数化时：
  allure.dynamic.title(data.get("case_project"))
    allure.dynamic.description(data.get("case_description"))
    ```
  
  + feature和story被称为行为驱动标记，因为使用这个两个标记，通过报告可以更加清楚的掌握每个测试用例的功能和每个测试用例的测试场景。或者你可以理解为feature是模块，而story是该模块下的子模块。
  
    ```python
    import pytest
    import allure
    
    @allure.feature('登录模块')
    class TestCaseLogin(object):
    
        @allure.story('登录模块下的子模块: test1')
        def test_case_01(self):
            assert 1
    
        @allure.story('登录模块下的子模块: test1')
        def test_case_02(self):
            assert 1
    
        @allure.story('登录模块下的子模块: test2')
        def test_case_03(self):
            assert 1
    
        @allure.story('登录模块下的子模块: test3')
        def test_case_04(self):
            assert 1
    
    @allure.feature('注册模块')
    class TestCaseRegister(object):
        @allure.story('注册模块下的子模块: test1')
        def test_case_01(self):
            assert 1
    
        @allure.story('注册模块下的子模块: test1')
        def test_case_02(self):
            assert 1
    
        @allure.story('注册模块下的子模块: test1')
        def test_case_03(self):
            assert 1
  
        @allure.story('注册模块下的子模块: test2')
      def test_case_04(self):
            assert 1
    ```
  
  + allure中对severity级别的定义：
  
  - Blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）
    - Critical级别：临界缺陷（ 功能点缺失）
    - Normal级别：普通缺陷（数值计算错误）
    - Minor级别：次要缺陷（界面错误与UI需求不符）
    - Trivial级别：轻微缺陷（必输项无提示，或者提示不规范）
  
    ```python
    import pytest
    import allure
    
    @allure.feature('登录模块')
    class TestCaseLogin(object):
    
        @allure.severity(allure.severity_level.BLOCKER)
        def test_case_01(self):
            assert 1
    
        @allure.severity(allure.severity_level.CRITICAL)
        def test_case_02(self):
            assert 1
    
        @allure.severity(allure.severity_level.MINOR)
        def test_case_03(self):
            assert 1
    
        @allure.severity(allure.severity_level.TRIVIAL)
        def test_case_04(self):
          assert 1
    
      def test_case_05(self):
            assert 1
    ```
  
  + dynamic，动态设置相关参数。
  
    ```python
    import pytest
    import allure
    
    @allure.feature('登录模块')
    class TestCaseLogin(object):
  
        @pytest.mark.parametrize('name', ['动态名称1', '动态名称2'])
        def test_case_05(self, name):
            allure.dynamic.title(name)
    ```
  
    