#!/bin/bash

usage() { echo "$0 usage:" && grep " .)\ #" $0; exit 0; }
[ $# -eq 0 ] && usage

while getopts "hu:b:r:" arg; do
  case $arg in
    u) # Specify Github Username
      USER=${OPTARG}
      ;;
    r) # Specify Github Repository name (cid-framework)
      REPO=${OPTARG}
      ;;
    b) # Specify Github Branch (deploy)
      BRANCH=${OPTARG}
      ;;
    h | *) # Display help.
      usage
      exit 0
      ;;
  esac
done

[[ -z $USER ]] && usage
[[ -z $BRANCH ]] && BRANCH="deploy"
[[ -z $REPO ]] && REPO="cid-framework"


# create git versions of the top level stack definitions
cp data-collection/deploy/deploy-data-collection.yaml data-collection/deploy/git-deploy-data-collection.yaml
cp data-collection/deploy/deploy-data-read-permissions.yaml data-collection/deploy/git-deploy-data-read-permissions.yaml

# and replace the source bucket info with the git repo location
BUCKETPATH='https://${CFNTemplateSourceBucket}.s3.amazonaws.com/cfn/data-collection/'
GITPATH="https://raw.githubusercontent.com/$USER/$REPO/$BRANCH/data-collection/deploy/"
sed -i '' "s|$BUCKETPATH|$GITPATH|g" data-collection/deploy/git-deploy-data-collection.yaml
sed -i '' "s|$BUCKETPATH|$GITPATH|g" data-collection/deploy/git-deploy-data-read-permissions.yaml




