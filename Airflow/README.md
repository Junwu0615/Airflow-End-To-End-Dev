<a href='https://github.com/Junwu0615/Airflow-End-To-End-Dev'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/Junwu0615/Airflow-End-To-End-Dev.svg'>
[![](https://img.shields.io/badge/Operating_System-Windows_10-blue.svg?style=plastic)](https://www.microsoft.com/zh-tw/software-download/windows10) 
[![](https://img.shields.io/badge/Project-Apache_Airflow-blue.svg?style=plastic)](https://github.com/Junwu0615/Airflow-End-To-End-Dev) <br>
[![](https://img.shields.io/badge/Technology-Python-yellow.svg?style=plastic)](https://github.com/Junwu0615/Airflow-End-To-End-Dev)
[![](https://img.shields.io/badge/Technology-Airflow-yellow.svg?style=plastic)](https://github.com/Junwu0615/Airflow-End-To-End-Dev)
[![](https://img.shields.io/badge/Technology-Docker-yellow.svg?style=plastic)](https://github.com/Junwu0615/Airflow-End-To-End-Dev) <br>
[![](https://img.shields.io/badge/Technology-GitLab-yellow.svg?style=plastic)](https://github.com/Junwu0615/Airflow-End-To-End-Dev)
[![](https://img.shields.io/badge/Technology-Jenkins-yellow.svg?style=plastic)](https://github.com/Junwu0615/Airflow-End-To-End-Dev)
[![](https://img.shields.io/badge/Technology-Grafana-yellow.svg?style=plastic)](https://github.com/Junwu0615/Airflow-End-To-End-Dev)
[![](https://img.shields.io/badge/Technology-Loki-yellow.svg?style=plastic)](https://github.com/Junwu0615/Airflow-End-To-End-Dev)
[![](https://img.shields.io/badge/Technology-ELK-yellow.svg?style=plastic)](https://github.com/Junwu0615/Airflow-End-To-End-Dev) <br>

<br>

## *⭐ Docker Build ⭐*
- #### *進入路徑 & 創建持久化空間*
  ```bash
  cd Airflow
  md dags; md logs; md plugins; md config
  ```

- #### *[ 可選 ] powershell 下載腳本*
  ```bash
  Invoke-WebRequest "https://airflow.apache.org/docs/apache-airflow/2.10.0/docker-compose.yaml" -OutFile "docker-compose.yaml"
  ```
  
- #### *初始化服務 ( 僅第一次 )*
  ```bash
  docker-compose -p etl-task-airflow up airflow-init
  
  # 預期結果如下
  # Database migrating done!
  # Added user airflow
  # User "airflow" created with role "Admin"
  # airflow-init-1 exited with code 0
  ```
- ![PNG](../sample/airflow-init.PNG)

- #### *啟動服務*
  ```bash
  docker-compose -p etl-task-airflow up -d
  ```
- ![PNG](../sample/airflow_up.PNG)

- #### *檢視服務是否正確啟用*
  ```bash
  docker ps -a
  ```

- #### *關閉服務*
  ```bash
  docker-compose -p etl-task-airflow down
  ```
  
- #### *[ 注意 ] 清除相關所有 Volume*
  ```bash
  docker volume rm $(docker volume ls -q | findstr etl-task-airflow)
  ```

- ![PNG](../sample/airflow.PNG)