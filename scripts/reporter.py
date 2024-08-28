import os
import openstack


def upload_to_openstack(object_storage, container_name, object_name, file_name):
    with open(file_name, 'rb') as file_data:
        object_storage.upload_object(container=container_name, name=object_name, data=file_data)

def process_reports(report_directory, container_name, auth_params):
    for file_name in os.listdir(report_directory):
        if file_name.endswith(".json"):
            file_path = os.path.join(report_directory, file_name)
            object_name = f"scan_results/{file_name}"
            upload_to_openstack(auth_params['object_storage'], container_name, object_name, file_path)

def load_vault_credentials(vault_path):
    with open(vault_path, 'r') as file:
        credentials = {}
        for line in file:
            key, value = line.strip().split('=')
            credentials[key] = value
    return credentials

if __name__ == "__main__":
    # Load vault credentials
    vault_path = "/etc/openstack/credentials"
    credentials = load_vault_credentials(vault_path)

    # Set environment variables
    os.environ['OS_PROJECT_NAME'] = "you-bucket-s3"
    os.environ['OS_AUTH_URL'] = "https://api.wavestack.de:5000"
    os.environ['OS_PROJECT_NAME'] = "project_name"
    os.environ['REGION_NAME'] = "region_name"
    os.environ['OS_AUTH_TYPE'] = "v3applicationcredential"
    os.environ['OS_APPLICATION_CREDENTIAL_ID'] = credentials['OS_APPLICATION_CREDENTIAL_ID']
    os.environ['OS_APPLICATION_CREDENTIAL_SECRET'] = credentials['OS_APPLICATION_CREDENTIAL_SECRET']

    # Auth OpenStack
    conn = openstack.connect()
    auth_params = {
        'object_storage': conn.object_store
    }

    container_name = "object_storage_container_name"
    report_directory = "/tmp/reports"

    process_reports(report_directory, container_name, auth_params)