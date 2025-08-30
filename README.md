# Kube-Mini-Cloud Project

This repository demonstrates a modern DevOps workflow for deploying a containerized web application into a Kubernetes cluster. The entire process is automated using Ansible and GitLab CI/CD.

This project was created to showcase hands-on experience with the core technologies required for a modern Linux System Administrator / SRE role.

## Technologies Demonstrated
-   **Kubernetes:** Application is deployed into a local Minikube cluster. Includes manifests for `Deployment` and `Service`.
-   **Ansible:** An Ansible playbook (`ansible/setup_playbook.yml`) is provided to automate the setup and deployment process on a local machine.
-   **GitLab CI/CD:** The `.gitlab-ci.yml` pipeline automatically builds the application's Docker image and pushes it to the GitLab container registry on every commit.
-   **Docker:** The application is containerized using a multi-stage `Dockerfile`.
-   **Nginx Ingress:** (Next Step) An `ingress.yml` is included to show understanding of how to expose services to the outside world.
-   **PostgreSQL:** (Next Step) The application can be extended to connect to a PostgreSQL database, also running within the Kubernetes cluster.

## How to Run Locally
1.  **Prerequisites:** Minikube, kubectl, Ansible.
2.  **Start the cluster:** `minikube start`
3.  **Run the Ansible playbook:**
    ```sh
    ansible-playbook ansible/setup_playbook.yml
    ```