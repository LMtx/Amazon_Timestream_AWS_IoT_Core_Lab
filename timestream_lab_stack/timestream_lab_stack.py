from aws_cdk import (
    Stack,
    aws_timestream as timestream,
)
from constructs import Construct

class TimestreamLabStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a Timestream Database
        timestream_db = timestream.CfnDatabase(
            self, "TimestreamDatabase",
            database_name="TestDatabase"
        )

        # Create a Timestream Table
        timestream_table = timestream.CfnTable(
            self, "TimestreamTable",
            database_name=str(timestream_db.database_name),
            table_name="TestTable",
            retention_properties=timestream.CfnTable.RetentionPropertiesProperty(
                memory_store_retention_period_in_hours="1",
                magnetic_store_retention_period_in_days="1"
            )
        )
        
        timestream_table.node.add_dependency(timestream_db)
        