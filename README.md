# local llm
Simple docker compose setup to load Huggingface TGI supported model and a UI/Service layer.

Env Variables
- LOCAL_MODEL_CACHE_DIR= # location on your host machine for the huggingface cache
- LLAMA_TOKEN= # if you are wanting to run llama2 from huggingface you will need a token
- MODEL_ID= # huggingface model id example: mistralai/Mistral-7B-Instruct-v0.2
- QUANTIZATION= # quantization option example: bitsandbytes-nf4
- MAX_PREFILL_TOKENS= # How many prefill tokens
- MAX_TOTAL_TOKENS= # max total tokens 
- MAX_INPUT_LENGTH= # max input length


## Requirements:
TODO

## Quickstart:
To run the containers on a local machine you first should build the containers via `make build`.

After that you should only need to run the following commands to start stop or view the logs of the containers.

`make start`

`make stop`

`make logs`