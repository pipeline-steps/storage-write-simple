from google.cloud import storage
from steputil import StepArgs, StepArgsBuilder


def main(step: StepArgs):
    # Initialize GCS client
    print(f"Uploading file to gs://{step.config.bucket}/{step.config.path}")
    storage_client = storage.Client(project=step.config.get("project"))
    bucket = storage_client.bucket(step.config.bucket)
    blob = bucket.blob(step.config.path)

    # Upload file from input
    input_file = step.input.getPath()
    blob.upload_from_filename(input_file)

    print(f"Successfully uploaded {input_file} to gs://{step.config.bucket}/{step.config.path}")
    print(f"Done")


if __name__ == "__main__":
    main(StepArgsBuilder()
         .input()
         .config("bucket")
         .config("path")
         .build()
         )
