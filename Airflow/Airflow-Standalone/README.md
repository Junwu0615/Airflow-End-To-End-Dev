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
  # 此時目錄應為 : //wsl$/Ubuntu/home/pc
  # 創建虛擬環境位置為 : //wsl$/Ubuntu/home/pc/airflow_venv
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
  ```
  
- #### *設定 Airflow 根目錄位置*
  ```bash
  export AIRFLOW_HOME=~/airflow
  echo $AIRFLOW_HOME # 預期輸出: /home/pc/airflow
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

- #### *變更預設埠*
  ```bash
  nano airflow/airflow.cfg
  # web_server_port = 8080 # <-- 改為 8150
  # 可用 VSCode 編譯器編輯
  ```
  
- #### *啟動 Airflow*
  ```bash
  airflow standalone
  ```
  
- #### *打開瀏覽器確認服務啟動*
  ```bash
  http://localhost:8150
  ```

<br>

## *⭐ 用 PyCharm + WSL2 + Airflow 斷點除錯指南 ⭐*
- #### *腳本參數務必設置正確*
- ![PNG](../../sample/pycharm_venv_0.PNG)
- ![PNG](../../sample/pycharm_venv_1.PNG)
- ![PNG](../../sample/pycharm_venv_2.PNG)
- ![PNG](../../sample/pycharm_debug_0.PNG)
  - #### *需要將欲 Debug 的 DAG 腳本放置正確位置*
  - #### *Airflow CLI 位置*
  ```Bash
  //wsl$/Ubuntu/home/pc/airflow_venv/bin/airflow
  ```
  - #### *腳本參數*
  ```Bash
  tasks test etl_branch_xcom_demo extract 2025-10-25
  ```
  - #### *工作目錄*
  ```Bash
  \\wsl$\Ubuntu\home\pc\airflow
  ```
  - #### *環境變數*
  ```Bash
  AIRFLOW_FORCE_SLICED_DAG_CODE=True;AIRFLOW_HOME=/home/pc/airflow;PYCHARM_DISPLAY_WSL_PATHS_AS_WINDOWS=0;PYTHONUNBUFFERED=1
  ```
- #### *成功進行 Debug*
- ![PNG](../../sample/pycharm_debug_1.PNG)

<br>

## *⭐ Other ⭐*
- #### *查閱當前環境有哪些 DAGs 腳本*
- ![PNG](../../sample/airflow%20dags%20list.PNG)

- #### *Airflow Info*
- ![PNG](../../sample/airflow%20info.PNG)


