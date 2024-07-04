## Requirement

- Minimun 8GB RAM
- Recommended 16 GB
- Docker or Docker Desktop
- 100 GB of patience


## Prerequisites:

This is using Ollama as the inference engine, and it's running the anoob/simp2 quantized version

Install ollama:

Option 1:

```
curl -fsSL https://ollama.com/install.sh | sh
```

Option 2:

download ollama from
https://ollama.com/download

After installaing Ollama

## For CPU only 
comment out deploy: in docker-compose.yml file

## For GPU




### Nvidia GPU

Install the NVIDIA Container Toolkit.

### Install with Apt

1. Configure the repository

   ```bash
   curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey \
       | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
   curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list \
       | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' \
       | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
   sudo apt-get update
   ```

2. Install the NVIDIA Container Toolkit packages

   ```bash
   sudo apt-get install -y nvidia-container-toolkit
   ```



### Configure Docker to use Nvidia driver

```bash
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```



## Translator Model

```
# Make sure you have git-lfs installed (https://git-lfs.com)
git lfs install

# clone this on the backend directory 
git clone https://huggingface.co/rujengelal/my_awesome_english_to_nepali_tst



```
## Docker Compose 
In the main directory run 

```
docker compose up
```

## Frontend and Backend in directly in Host machine

If the above docker compose method does't go well, we will run only Mindsdb and Ollama through docker 

### comment out the frontend and backend service in docker-compose.yml file and hit 

```
docker compose up
```

### Run Frontend in Dev Mode.

navigate to frontend/

```
   npm install
   npm run dev
```
### Run backend 
Set up a virtual environment and activate it:

```
python3 -m venv myenv
source myenv/bin/activate
```

Install all the necessary Python packages from the requirements file in the backend/ directrory:

```
pip3 install -r requirements.txt
```


### Run Backend

navigate to backend/simplifai/

```
python3 manage.py runserver
```


### Note

login as guest
