"""
# Integration test for Cost Optimization Data Collection

## About
    This test will:
    - deploy Cost Optimization Data Collection stacks (all in one account)
    - update all nested stacks to the git version
    - trigger collection
    - test that collection works  (tables are not empty)
    - delete all stacks and tables

## Prerequisites in account:
    1. Activate Organizations
    2. Opt-In Compute Optimizer
    3. Activate Business or Enterprise Support (for ta collection only)
    4. Create:
        RDS instance, Budget, Unattached EBS, ECS cluster with at least 1 Service,
    FIXME: add CFM for Prerequisites

## Install:
    pip3 install cfn-flip boto3 pytest

## Run (expect 15 mins):
Pytest:

    pytest

Python:
    python3 Test/test-from-scratch.py


"""
import logging
import sys

import pytest

from utils import athena_query


logger = logging.getLogger(__name__)


def test_deployment_works(athena):
    pass

def test_budgets_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."budgets_data" LIMIT 10;')
    assert len(data) > 0, 'budgets_data is empty'


def test_cost_explorer_rightsizing_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."cost_explorer_rightsizing_data" LIMIT 10;')
    assert len(data) > 0, 'cost_explorer_rightsizing_data is empty'


def test_cost_anomaly_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."cost_anomaly_data" LIMIT 10;')
    assert len(data) > 0, 'cost_anomaly_data is empty'

def test_support_cases_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."support_cases_data" LIMIT 10;')
    assert len(data) > 0, 'support_cases_data is empty'

def test_support_cases_communications(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."support_cases_communications" LIMIT 10;')
    assert len(data) > 0, 'support_cases_communications is empty'

def test_support_cases_status(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."support_cases_status" LIMIT 10;')
    assert len(data) > 0, 'test_support_cases_status is empty'

def test_ecs_chargeback_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."ecs_chargeback_data" LIMIT 10;')
    assert len(data) > 0, 'ecs_chargeback_data is empty'


def test_inventory_ami_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."inventory_ami_data" LIMIT 10;')
    assert len(data) > 0, 'inventory_ami_data is empty'

def test_inventory_ebs_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."inventory_ebs_data" LIMIT 10;')
    assert len(data) > 0, 'inventory_ebs_data is empty'

def test_inventory_snapshot_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."inventory_snapshot_data" LIMIT 10;')
    assert len(data) > 0, 'inventory_snapshot_data is empty'

def test_inventory_ec2_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."inventory_ec2_instances_data" LIMIT 10;')
    assert len(data) > 0, 'inventory_ec2_data is empty'

def test_inventory_vpc_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."inventory_vpc_data" LIMIT 10;')
    assert len(data) > 0, 'inventory_vpc_data is empty'

def test_inventory_rds_snapshot_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."inventory_rds_db_snapshots_data" LIMIT 10;')
    assert len(data) > 0, 'inventory_rds_db_snapshots_data is empty'

def test_inventory_lambda_functions_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."inventory_lambda_functions_data" LIMIT 10;')
    assert len(data) > 0, 'inventory_lambda_functions_data is empty'

def test_rds_usage_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."rds_usage_data" LIMIT 10;')
    assert len(data) > 0, 'rds_usage_data is empty'

def test_organizations_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."organization_data" LIMIT 10;')
    assert len(data) > 0, 'organizations_data is empty'

def test_trusted_advisor_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."trusted_advisor_data" LIMIT 10;')
    assert len(data) > 0, 'trusted_advisor_data is empty'


def test_transit_gateway_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."transit_gateway_data" LIMIT 10;')
    assert len(data) > 0, 'transit_gateway_data is empty'


def test_opensearch_domains_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."inventory_opensearch_domains_data" LIMIT 10;')
    assert len(data) > 0, 'opensearch_domains_data is empty'


def test_elasticache_clusters_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."inventory_elasticache_clusters_data" LIMIT 10;')
    assert len(data) > 0, 'elasticache_clusters_data is empty'


def test_rds_db_instances_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."inventory_rds_db_instances_data" LIMIT 10;')
    assert len(data) > 0, 'rds_db_instances_data is empty'

def test_pricing_computesavingsplan_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."pricing_computesavingsplan_data" LIMIT 10;')
    assert len(data) > 0, 'pricing_computesavingsplan_data is empty'

def test_pricing_ec2_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."pricing_ec2_data" LIMIT 10;')
    assert len(data) > 0, 'pricing_ec2_data is empty'

def test_pricing_elasticache_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."pricing_elasticache_data" LIMIT 10;')
    assert len(data) > 0, 'pricing_elasticache_data is empty'

def test_pricing_opensearch_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."pricing_opensearch_data" LIMIT 10;')
    assert len(data) > 0, 'pricing_opensearch_data is empty'

def test_pricing_rds_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."pricing_rds_data" LIMIT 10;')
    assert len(data) > 0, 'pricing_rds_data is empty'

def test_pricing_lambda_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."pricing_lambda_data" LIMIT 10;')
    assert len(data) > 0, 'pricing_lambda_data is empty'

def test_pricing_regionnames_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."pricing_regionnames_data" LIMIT 10;')
    assert len(data) > 0, 'pricing_regionnames_data is empty'

def test_compute_optimizer_export_triggered(compute_optimizer, start_time):
    jobs = compute_optimizer.describe_recommendation_export_jobs()['recommendationExportJobs']
    logger.debug(f'Jobs in: {jobs}')
    jobs_since_start = [job for job in jobs if job['creationTimestamp'].replace(tzinfo=None) > start_time.replace(tzinfo=None)]
    assert len(jobs_since_start) == 7, f'started {len(jobs_since_start)} jobs. Expected 7. Not all jobs launched'
    jobs_failed = [job for job in jobs_since_start if job.get('status') == 'failed']
    assert len(jobs_failed) == 0, f'Some jobs failed {jobs_failed}'
    # TODO: check how we can add better test, taking into account 15-30 mins delay of export in CO

def test_health_events_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."health_events_detail_data" LIMIT 10;')
    assert len(data) > 0, 'health_events_detail_data is empty'

def test_license_manager_grants(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."license_manager_grants" LIMIT 10;')
    assert len(data) > 0, 'license_manager_grants is empty'

def test_license_manager_licenses(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."license_manager_licenses" LIMIT 10;')
    assert len(data) > 0, 'license_manager_licenses is empty'

def test_quicksight_users(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."quicksight_user_data" LIMIT 10;')
    assert len(data) > 0, 'quicksight_user_data is empty'

def test_quicksight_groups(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."quicksight_group_data" LIMIT 10;')
    assert len(data) > 0, 'quicksight_group_data is empty'

def test_quicksight_groupmembership(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."quicksight_groupmembership_data" LIMIT 10;')
    assert len(data) > 0, 'quicksight_groupmembership_data is empty'

def test_servicequotas_data(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."service_quotas_data" LIMIT 10;')
    assert len(data) > 0, 'service_quotas_data is empty'

def test_servicequotas_history(athena):
    data = athena_query(athena=athena, sql_query='SELECT * FROM "optimization_data"."service_quotas_history" LIMIT 10;')
    assert len(data) > 0, 'service_quotas_history is empty'

if __name__ == '__main__':
    pytest.params = {}
    if '--no-teardown' in sys.argv:
        sys.argv.remove('--no-teardown')
        pytest.params['mode'] = 'no-teardown'

    sys.argv = sys.argv[:1]
    pytest.main()
