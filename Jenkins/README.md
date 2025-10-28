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

## *⭐ Docker Build In WSL2 ⭐*
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
  docker volume rm $(docker volume ls -q | findstr etl-task-jenkins)
  ```

- #### *Jenkins Plugin 必裝清單*
  | 插件名稱 | 用途 |
  | :-- | :-- |
  | Git plugin | 從 GitLab 拉原始碼 |
  | GitLab plugin| 接收 GitLab Webhook |
  | Pipeline plugin | 支援 Jenkinsfile 腳本 |
  | SSH Agent plugin | 用 SSH 部署至 Airflow |
  | Credentials Binding plugin | 管理 Token / SSH key |
  | Blue Ocean [可選] | 視覺化 Pipeline 介面 |

- #### *確認主機能從 Jenkins 登入 Airflow Server*
  ```bash
  ssh airflow@192.168.0.158
  ```
  
- #### *在 Jenkins → Manage Jenkins → Credentials → Global 新增*
  ```bash
  # 類型：SSH Username with private key
  # ID：airflow-server-key
  # Username：airflow
  # Private Key：貼上私鑰內容（或勾「From Jenkins master ~/.ssh」）
  ```