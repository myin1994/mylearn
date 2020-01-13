from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from copy import deepcopy
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.jq22.com/demo/pintu20151229/')
# driver.maximize_window()

div1 = driver.find_element_by_id('container')
image_list1 = div1.find_elements_by_tag_name('div')
list1 = [i.get_attribute('style').rsplit(';',1)[0] for i in image_list1]

driver.find_element_by_id('start').click()
div2 = driver.find_element_by_id('container')
image_list2 = div2.find_elements_by_css_selector('.container div')
list2 = [i.get_attribute('style').rsplit(';',4)[0] for i in image_list2]

try:
    print(list1,len(list1))
    print('----------------------------')
    # list2 = sorted(list1,reverse=True)
    print(list2)
    position = {list2.index(i):[list1.index(i),list2.index(i)] for i in list1}
    print(position, len(position))
    # position = [i for i in position if reversed(i) not in position ]
    sleep(1)
    action = ActionChains(driver)
    # position2 = deepcopy(position)
    # print(position2)
    # for k,v in position.items():
    #     print(k,v[0],v[1])
    #     # action.drag_and_drop(image_list2[v[1]],image_list2[v[0]])
    #     ActionChains(driver).drag_and_drop(image_list2[v[1]],image_list2[v[0]]).perform()
    #
    #     sleep(1)
    #     position[v[0]] = [position[v[0]][0],v[1]]
    # position = sorted(position,key=lambda x:position[x][1])
    # print(position)

    for i in range(len(position.keys())):
        index1,index2 = position[i]
        action.drag_and_drop(image_list2[index2], image_list2[index1])
        position[index1] = [position[index1][0], index2]
    print(position)

    # for k,v in position.items():
    #     print(k,v[0],v[1])
    #     action.drag_and_drop(image_list2[v[1]],image_list2[v[0]])
    #     # ActionChains(driver).drag_and_drop(image_list2[v[1]],image_list2[v[0]]).perform()
    #
    #     sleep(1)
    #     position[v[0]] = [position[v[0]][0],v[1]]
    action.perform()
    driver.save_screenshot('1.png')
except Exception as e:
    print(e)
finally:
    sleep(2)
    driver.quit()
