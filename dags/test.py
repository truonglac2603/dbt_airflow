from airflow.operators.python_operator import PythonOperator
from operators.get_workspace import GetWorkspaceOperator
from operators.create_source import CreateSourceOperator
from operators.create_destination import CreateDestinationOperator
from operators.create_connection import CreateConnectionOperator
from operators.delete import DeleteAllOperator
from airflow.operators.bash import BashOperator
from datetime import timedelta, datetime
from airflow import DAG

default_args = {
        'owner' : 'airflow',
        'start_date' : datetime(2023, 1, 1),
        'provide_context': True
}

dag = DAG (
        dag_id='create_connection',
        default_args=default_args,
        schedule_interval='@once', 
        catchup=False
)

### get workspace ID
get_workspace = GetWorkspaceOperator(
        task_id="get_workspace",
        dag = dag, 
)

### create GGSheet source 
create_source = CreateSourceOperator(
        task_id= "create_source",
        dag = dag, 
)

### create Iceberg destination
create_destination = CreateDestinationOperator(
        task_id= "create_destination",
        dag = dag, 
)

### create airbyte connection
create_connection = CreateConnectionOperator(
        task_id= "create_connection",
        dag = dag,
        trigger_rule ='all_done'
)

### delete source, destination and connection
delete_all = DeleteAllOperator(
        task_id= "delete_all",
        dag = dag, 
) 


# ### Sleep task 
# sleep_task = BashOperator(
#     task_id = 'sleep_task',
#     dag = dag,
#     bash_command = 'sleep 1m'
# )

get_workspace >> [create_source, create_destination] >> create_connection >> delete_all