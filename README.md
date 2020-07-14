# **项目名及简介**
## **python3+selenium+unittest 实现UI自动化测试**
### **目录结构**
#### **1.Base**
**存放公共方法文件**
#### **2.driver**
**存放驱动文件**
#### **3.log**
**按天为文件夹存放日志数据，错误截屏图片**
#### **4.PageObject**
**存放PO模式每个页面操作的方法  逻辑层**
#### **5.report**
**存放测试报告**
#### **6.TestCase**
**存放测试用例 控制层**
#### **7.TestData**
**存放测试数据**
**以模块名做文件夹 在写每个用例的yaml文件 根据TestCase目录架构 路径编写**
#### **8.TestSuite**
**存放测试套件 组装测试用例**

<br/>

### **实现需求**
#### **1.通过读取TestData内的测试数据文件 yaml格式 进行测试**
#### **2.通过TestCase 创建测试用例。利用数据驱动ddt对TestData里的测试数据进行测试**
#### **3.通过TestSuite 组装测试套件。自定义执行多个TestCase**
#### **4.使用HTMLTestRunner 产出html的测试报告**
**函数传参说明 title:html标题 ,description: 测试用例执行情况,tester: 测试人员**
#### **5.测试流程结束 获取最新测试报告并发送邮件**
    new_report 返回两个参数 第一个文件路径 第二个文件名
    send_email 函数传参说明 email_Subject：邮件主题,file_path：传递文件路径,  filename传递文件名, received_Email 列表形式支持多个邮箱可不传，用默认

<br/>

### **待实现需求**
#### **1.读取execl的测试数据集 生产execl的测试报告**
#### **2.每次执行 初始化测试数据 读取sql文件，生成已存在测试数据**
#### **3.与前台测试系统对接 对数据库待处理用例进行自动测试**
#### **4.手机端UI自动化测试**
<br/>

## **技术文档**
#### 1.unittest.TestSuite()  生成测试套件
    1.先实例化套件
    suite=unittest.TestSuite() (suite：为TestSuite实例化的名称)
    2. 添加某个测试用例的具体测试方法：
    suite.addTest("ClassName(MethodName)")    (ClassName：为类名；MethodName：为方法名)
    3. 添加某个测试用例的所有测试方法
    suite.addTest(unittest.makeSuite(ClassName))  (搜索指定ClassName内test开头的方法并添加到测试套件中)
    4.执行    TestSuite需要配合TextTestRunner才能被执行
    runner=unittest.TextTestRunner()  1. 实例化：(runner：TextTestRunner实例化名称)
    runner.run(suite)           2. 执行： (suite：为测试套件名称)

#### 2.unittest.TestLoader()   用于生成测试套件
    TestCases = unittest.TestLoader().loadTestsFromModule(module)  从模块 py文件 中加载所有测试方法    参数py文件名
    TestCases = unittest.TestLoader().loadTestsFromTestCase(classname)     从类中添加  这个类中的所有的测试方法   参数类名，类必须继承unittest.TestCase
    TestCases = unittest.TestLoader().loadTestsFromName(Name)     加载某个单独的测试方法 必须是字符串   “module.class.def”
    TestCases = unittest.TestLoader().loadTestsFromNames()      加载某个单独的测试方法 必须是列表   [“module.class.def1”,“module.class.def2”]
    suite.addTest(TestCases)
    runner=unittest.TextTestRunner()  1. 实例化：(runner：TextTestRunner实例化名称)
    runner.run(suite)           2. 执行： (suite：为测试套件名称)

#### 3.unittest.defaultTestLoader()  通过该类下面的discover()方法自动搜索指定目录下指定开头的.py文件，并将查找到的测试用例组装到测试套件；
    test_dir = './'  (test_dir为要指定的目录 ./为当前目录；pattern：为查找的.py文件的格式  支持正则 )
    disconver = unittest.defaultTestLoader.discover(test_dir, pattern='iweb_*.py')
    runner=unittest.TextTestRunner()    运行
    runner.run(disconver)````
    
#### 4.装饰器
    1.@unittest.skip(reason)   无条件强制跳过某条测试方法
    2.@unittest.skipif(condition，reason)  根据条件判断，条件为真 无条件强制跳过某条测试方法
    3.@unittest.skipunless(condition，reason)  根据条件判断，条件为假  无条件强制跳过某条测试方法
    4.@unittest.expectedFailure   预期就是失败  测试方法成功时标记为失败，测试方法失败，忽略这次失败
    
#### 5.yaml文档
    https://www.runoob.com/w3cnote/yaml-intro.html