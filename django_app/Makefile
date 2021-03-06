GCLOUD_PROJECT:=$(shell gcloud config list project --format="value(core.project)")

.PHONY: all
all: deploy

.PHONY: create-cluster
create-cluster:
	gcloud container clusters create article-test \
		--scope "https://www.googleapis.com/auth/userinfo.email","cloud-platform"

.PHONY: create-bucket
create-bucket:
	gsutil mb gs://$(GCLOUD_PROJECT)
    gsutil defacl set public-read gs://$(GCLOUD_PROJECT)

.PHONY: build
build:
	docker build -t gcr.io/$(GCLOUD_PROJECT)/article .

.PHONY: push
push: build
	gcloud docker push gcr.io/$(GCLOUD_PROJECT)/article

.PHONY: template
template:
	sed -i ".tmpl" "s/\$$GCLOUD_PROJECT/$(GCLOUD_PROJECT)/g" app.yaml

.PHONY: deploy
deploy: push template
	kubectl create -f app.yaml

.PHONY: update
update:
	kubectl rolling-update polls --image=gcr.io/${GCLOUD_PROJECT}/article

.PHONY: delete
delete:
	kubectl delete rc article-test
	kubectl delete service article-test
