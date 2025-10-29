## *Hello-World*

```
Hello-World/
│
├── dags/
│   ├── __init__.py
│   └── etl_branch_xcom_demo.py
│
├── etl_lib/
│   ├── __init__.py
│   ├── etl_processor.py           # 可單元測試
│   └── db/
│       ├── models.py              # SQLAlchemy Model
│       └── session.py             # SQLAlchemy: DB Session Factory
│
├── tests/
│   ├── __init__.py
│   ├── init_db.py                 # 測試前初始化資料庫
│   └── test_etl_processor.py
│
├── .env
├── .gitignore
├── Jenkinsfile                    # CI / CD Pipeline
├── README.md
└── requirements.txt
```