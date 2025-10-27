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

## *⭐ 用 WSL2 創建 Airflow 環境 ⭐*
- #### *啟動 PostgreSQL Docker 容器 ( 首次啟動前 )*
  ```bash
  # Debug 需要進入子進程時，SQLite 無法支援多重進程操作
  docker run --name airflow-postgres -e POSTGRES_USER=airflow -e POSTGRES_PASSWORD=airflow -e POSTGRES_DB=airflow -p 5432:5432 -d postgres:13
  ```
  
- #### *PowerShell ( 管理員身分 )*
  ```bash
  wsl --install -d Ubuntu
  ```

- #### *創建並進入虛擬環境*
  ```bash
  sudo apt update
  sudo apt install python3.12-venv
  sudo python3 -m venv airflow_venv
  source airflow_venv/bin/activate
  
  # 此時目錄應為 : //wsl$/Ubuntu/home/your_username
  # 創建虛擬環境位置為 : //wsl$/Ubuntu/home/your_username/airflow_venv
  ```
- ![PNG](../../sample/linux_airflow_venv.PNG)

- #### *將該目錄賦予權限給使用者*
  ```bash
  whoami # 預期輸出: your_username
  
  sudo chown -R pc:pc ~/airflow_venv
  # sudo chown -R <您的使用者名稱>:<您的使用者名稱> <虛擬環境路徑>
  # 使用 sudo chown -R 指令，將整個虛擬環境目錄的擁有權遞迴地 ($\text{-R}$) 轉移給使用者
  ```

- #### *安裝 Airflow*
  ```bash
  pip install "apache-airflow==2.9.1" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.1/constraints-3.11.txt"
  pip install psycopg2-binary~=2.9.11
  pip install pydevd_pycharm~=253.27864.50
  ```
  
- #### *設定 Airflow 根目錄位置*
  ```bash
  export AIRFLOW_HOME=~/airflow
  echo $AIRFLOW_HOME # 預期輸出: /home/your_username/airflow
  ```

- #### *初始化 Airflow 資料庫 ( 首次啟動前 )*
  ```bash
  airflow db migrate
  ```
  
- #### *創建管理員用戶*
  ```bash
  airflow users create \
    --username airflow \
    --firstname admin \
    --lastname user \
    --role Admin \
    --email airflow@example.com
  ```

- #### *變更預設埠 & Debug 模式*
  ```bash
  # 法 1: nano airflow/airflow.cfg
  # 法 2: 可用 VSCode 編譯器編輯

  # web_server_port = 8080
  web_server_port = 8150
  
  # executor = SequentialExecutor
  executor = LocalExecutor
  
  # sql_alchemy_conn = sqlite:////home/pc/airflow/airflow.db
  sql_alchemy_conn = postgresql+psycopg2://airflow:airflow@localhost:5432/airflow
  ```
  
- #### *啟動 Airflow*
  ```bash
  airflow standalone
  ```
  
- #### *打開瀏覽器確認服務啟動*
  ```bash
  http://localhost:8150
  ```