+ 官方网站

  ```
  https://www.echartsjs.com/examples/zh/index.html
  ```

+ 前端使用

  + 引入js

  ```html
  /*--前端使用--*/
      <div class="row">
          <div class="page-header col-sm-6">
              <div id="case_execute_status" style="max-width: 1000px;width: 900px;height:500px;max-height: 800px;"></div>
          </div>
  
          <div class="page-header col-sm-6">
              <div id="case_pass_status" style="max-width: 1000px;width: 900px;height:500px;max-height: 800px;"></div>
          </div>
  
      </div>
  ```

  

  ```javascript
  /*--基本使用--*/
  <script>
      function case_execute_status(data) {
          option = {
              title: {
                  text: data['title_text'],
                  subtext: data['title_subtext'],
                  left: 'center'
              },
              tooltip: {
                  trigger: 'item',
                  formatter: '{a} <br/>{b}: {c} ({d}%)'
              },
              legend: {
                  orient: 'vertical',
                  left: 10,
                  data: data['legend_data']
              },
              series: [
                  {
                      name: data['series_name'],
                      type: 'pie',
                      radius: data['series_radius'],
                      avoidLabelOverlap: false,
                      label: {
                          normal: {
                              show: false,
                              position: 'center'
                          },
                          emphasis: {
                              show: true,
                              textStyle: {
                                  fontSize: '30',
                                  fontWeight: 'bold'
                              }
                          }
                      },
                      labelLine: {
                          normal: {
                              show: false
                          }
                      },
                      data: data['series_data']
                  }
              ]
          };
          var myChart = echarts.init(document.getElementById(data['id']));#为指定div标签添加图表
          myChart.setOption(option);
      }
  
      window.onload = function () {
          $.ajax({
              url: "{% url 'app01:echart_list' %}",
              type: "POST",
              data: {"csrfmiddlewaretoken": "{{ csrf_token }}"},
              success: function (data) {
                  case_execute_status(data['case_execute_status']);
                  case_execute_status(data['case_pass_status']);
              }
          })
      }
  </script>
  ```

  