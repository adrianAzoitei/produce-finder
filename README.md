# Produce Finder
This is a simple application that, upon uploading an image with groceries, will:
1. Store the detected items in a database, adding up quantities of the same item.
2. Update external systems (e.g. an Excel sheet, Notion board etc.).
3. Return the original image, with bounding boxes overlayed, to the user.

![demo](docs/demo.png)

## Architecture
For now the architecture is kept simple:
1. A frontend written in Vue.js, interacting, over HTTP with a
2. Backend written in Python (Django)*, which in turns saves detection results in a
3. PostgreSQL database.
![architectural diagram](docs/archi.png)

> :warning: **Object detection models**: At the moment, only the [YOLO family](https://github.com/ultralytics/ultralytics) of models is supported. More coming soon.

## Deployment
The application is meant to be deployed with:
1. [Docker compose](/docker-compose.yml) for development / testing.
2. Helm + Kubernetes in production.

## CICD
![cicd](docs/cicd.png)

# TODO
## Security
- [ ] Add auth (OAuth2 w/ Keycloak).

## Features
- [ ] Show table with individual items (crops using bboxes) and detected class (FE).
- [ ] Store uploaded images in Blob Storage w/ UUID (add this ID to the detection row) (BE).
- [ ] Allow drawing bbox, choosing a class and sending the classification to BE for later retraining. See COCO format.
- [ ] Add `upload model` (weights) feature.
- [ ] Add `select model` feature.
- [ ] Integrate with Google Sheets (inventory)
- [ ] Integrate with Notion (inventory)

## Deployment
- [ ] Write Helm Chart
- [ ] Create K8s namespace
- [ ] Create K8s imagePullSecret
- [ ] Expose with Azure Application Gateway
- [ ] Write Ansible Playbook to:
    - [ ] Deploy Azure Container Registry
    - [ ] Create Service Principal
    - [ ] Deploy Azure Kubernetes Service
    - [ ] Prepare K8s namespace
    - [ ] Install Helm chart

## Training
- [ ] Train models ([Azure ML ?](https://docs.ultralytics.com/guides/azureml-quickstart/#what-is-azure-machine-learning-azureml))
    - [ ] [SKU110k](https://paperswithcode.com/dataset/sku110k) ?
    - [ ] [Grocery Store Dataset](https://github.com/marcusklasson/GroceryStoreDataset) ?
    - [ ] Custom dataset (needs labelling) ?

## Observavility
- [ ] Trace requests w/ OpenTelemetry
