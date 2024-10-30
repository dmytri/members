# Members

A platform for member organization and coordination.

## Development

1. Install:
   - [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl) - Kubernetes command-line tool
   - [Tilt](https://docs.tilt.dev/install.html) - Modern dev environment for teams

2. Set up a Kubernetes context:
   - Enable [Docker Desktop Kubernetes](https://docs.docker.com/desktop/kubernetes/) (easiest), or
   - Install [minikube](https://minikube.sigs.k8s.io/docs/start/) (more configurable)
   
   Kubernetes is used to run the app in containers. A "context" tells kubectl which cluster to use.
   Verify your context is set up:
   ```bash
   kubectl config current-context
   kubectl get nodes  # Should show at least one node
   ```

3. Start development environment:
   ```bash
   tilt up
   ```
   Tilt will build, deploy and manage the app in Kubernetes. It automatically rebuilds when files change.

4. Visit:
   - App: http://localhost:8000
   - Tilt UI: http://localhost:10350 (see build status, logs, and services)

Press `Ctrl+C` to stop Tilt.