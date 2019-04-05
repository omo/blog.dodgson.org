
Push:

```
$ ~/.local/bin/aws s3 sync --acl=public-read --delete --storage-class=REDUCED_REDUNDANCY . s3://blog.dodgson.org
```