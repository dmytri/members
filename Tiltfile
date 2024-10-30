# Load namespace extension
load('ext://namespace', 'namespace_create', 'namespace_inject')

# Get namespace from flag or use default
namespace = config.parse().get('namespace', 'members')

# Create namespace
namespace_create(namespace)

# Load and inject namespace into YAML
k8s_yaml(namespace_inject(read_file('k8s/members.yaml'), namespace))

# Build
docker_build('flask-app', '.')

# Port forward
k8s_resource('flask-app', port_forwards='8000:8000')