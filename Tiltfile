# Load namespace extension
load('ext://namespace', 'namespace_create', 'namespace_inject')

# Get namespace from flag or use default
namespace = config.parse().get('namespace', 'members')

# Create namespace
namespace_create(namespace)

# Load and inject namespace into YAML
k8s_yaml(namespace_inject(read_file('k8s/members.yaml'), namespace))

# Build app image with all dependencies
docker_build('flask-app', '.', 
    live_update=[
        sync('.', '/srv')
    ]
)

# Port forward
k8s_resource('flask-app', port_forwards=['8000:8000'])

# Add local resource for tests in container
local_resource(
    'tests',
    cmd='kubectl exec -it -n {} deployment/flask-app -- pytest -v --capture=tee-sys --html=app/static/tests/index.html'.format(namespace),
    deps=['tests/', 'app/'],
    resource_deps=['flask-app'],
    auto_init=False,
    labels=['testing'],
    links=[
        link('http://localhost:8000/tests', 'Test Report')
    ]
)

# Manual migration sync from container to local
local_resource(
    name='fetch-migrations',
    cmd='kubectl cp -n {} deployment/flask-app:/srv/migrations/ ./'.format(namespace),
    auto_init=False,
    trigger_mode=TRIGGER_MODE_MANUAL,
    labels=['sync']
)
