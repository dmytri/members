# Load namespace extension
load('ext://namespace', 'namespace_create', 'namespace_inject')

# Get namespace from flag or use default
namespace = config.parse().get('namespace', 'members')

# Create namespace
namespace_create(namespace)

# Load and inject namespace into YAML
k8s_yaml(namespace_inject(read_file('k8s/members.yaml'), namespace))

# Build with dev dependencies and fast sync for all code
docker_build('flask-app', '.', 
    build_args={'ENV': 'dev'},
    live_update=[
        sync('.', '/srv')
    ]
)

# Port forward
k8s_resource('flask-app', port_forwards='8000:8000')

# Add local resource for tests
local_resource(
    'tests',
    cmd='pytest',
    deps=['tests/', 'app/'],
    resource_deps=['flask-app'],
    auto_init=False,
    labels=['testing']
)

# Manual migration sync from container to local
local_resource(
    name='fetch-migrations',
    cmd='''
    POD=$(kubectl get pods -l app=flask-app -o jsonpath="{.items[0].metadata.name}")
    kubectl cp $POD:/srv/migrations/ ./
    ''',
    auto_init=False,
    trigger_mode=TRIGGER_MODE_MANUAL,
    labels=['sync']
)