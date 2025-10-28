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

## *⭐ 用 WSL2 創建 Jenkins 服務 ⭐*
- #### *進入路徑 & 創建持久化空間*
  ```bash
  cd Jenkins
  md jenkins_home
  ```

- #### *啟動服務*
  ```bash
  docker-compose -p etl-task-jenkins up -d
  ```
- ![PNG](../sample/jenkins_0.PNG)

- #### *檢視服務是否正確啟用*
  ```bash
  docker ps -a
  ```

- #### *關閉服務*
  ```bash
  docker-compose -p etl-task-jenkins down
  ```
  
- #### *查看初始化密碼*
  ```bash
  docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword
  ```

- #### *Jenkins Plugin 必裝清單 ( 無腦選擇推薦安裝 )*
  | 插件名稱 | 用途 |
  | :-- | :-- |
  | Git plugin | 從 GitLab 拉原始碼 |
  | GitLab plugin| 接收 GitLab Webhook |
  | Pipeline plugin | 支援 Jenkinsfile 腳本 |
  | SSH Agent plugin | 用 SSH 部署至 Airflow |
  | Credentials Binding plugin | 管理 Token / SSH key |
  | Blue Ocean [可選] | 視覺化 Pipeline 介面 |
- ![PNG](../sample/jenkins_1.PNG)

- #### *確認是否安裝 Gitlab 插件*
- ![PNG](../sample/jenkins_2.PNG)

- #### *設定使用者設定，即完成*
  ```bash
  Account: admin
  Password: admin_pass
  Email: admin@example.com
  ```
  
<br>

## *⭐ 設定 Webhook 模式 ⭐*
- #### *⭐ 架構概念 ⭐*
  ```Bash
  GitLab [push / merge]
  
       ↓  Webhook [Trigger]
  
  Jenkins [CI/CD Pipeline]
  
       ↓  SSH Deploy
  
  Airflow Server [Copy DAGs & Other File → /opt/airflow]
  ``` 
  
- #### *新增作業步驟*
  - ![PNG](../sample/jenkins_11.jpg)
    ```Bash
    來自 Gitlab 專案 Hello World 發生 Commit 動作，間接觸法 Jenkins CI/CD 流程
    ``` 
  - ![PNG](../sample/jenkins_12.jpg)