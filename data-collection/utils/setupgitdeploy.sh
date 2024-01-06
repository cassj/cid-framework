#!/bin/bash

usage() { echo "$0 usage:" && grep " .)\ #" $0; exit 0; }
[ $# -eq 0 ] && usage

while getopts "hu:b:r:s:" arg; do
  case $arg in
    s) # Specify S3 bucket for nested templates
      BUCKET=${OPTARG}
      ;;
    h | *) # Display help.
      usage
      exit 0
      ;;
  esac
done

[[ -z $BUCKET ]] && usage

# set up the pre-push hook to sync the template bucket before every git push
cat << EOF > .git/hooks/pre-push
#!/bin/sh
# Doesn't seem like you can sync to a prefix, so fudge it so I don't have to change the yaml cfn files
mkdir -p upload/cfn/
ln -s ../../data-collection/deploy/ upload/cfn/data-collection
aws s3 sync upload/ s3://${BUCKET}/
rm -rf upload
exit 0

EOF






