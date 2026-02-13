# storage-write-simple

Writing a file to Google Cloud Storage

## Docker Image

This application is available as a Docker image on Docker Hub: `pipelining/storage-write-simple`

### Usage

```bash
docker run -v /path/to/config.json:/config.json \
           -v /path/to/input:/input \
           -v /path/to/credentials.json:/credentials.json \
           -e GOOGLE_APPLICATION_CREDENTIALS=/credentials.json \
           pipelining/storage-write-simple:latest \
           --config /config.json \
           --input /input/data.txt
```

To see this documentation, run without arguments:
```bash
docker run pipelining/storage-write-simple:latest
```

## Parameters

| Name    | Required | Description                                      |
|---------|----------|--------------------------------------------------|
| project |          | GCP project ID (optional, defaults to environment settings) |
| bucket  | X        | Name of the GCS bucket                           |
| path    | X        | Path (including filename) within the bucket      |

**Notes:**
  * project: (Optional) GCP project ID. If not specified, defaults to the project from your environment or service account
  * bucket: The GCS bucket where the file will be uploaded
  * path: The full path including filename where the file will be stored in the bucket (e.g., `folder/subfolder/file.txt`)
  * The service account needs to have `storage.objects.create` permission on the bucket

## Example

Config file (`config.json`):
```json
{
  "bucket": "my-bucket",
  "path": "data/output/results.json"
}
```

Or with explicit project:
```json
{
  "project": "my-gcp-project",
  "bucket": "my-bucket",
  "path": "data/output/results.json"
}
```

This will upload the input file to `gs://my-bucket/data/output/results.json`
