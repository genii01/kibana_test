# FastAPI Logging with ELK Stack

This project demonstrates how to collect and monitor logs from a FastAPI application using the ELK (Elasticsearch, Logstash, Kibana) stack.

## Project Structure
```plaintext
.
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── logging_config.py
│   └── routes/
│       └── api.py
├── docker/
│   └── app.dockerfile
├── docker-compose.yml
├── filebeat.yml
├── pyproject.toml
└── README.md
```

## Running the Project

### Start Docker Containers
```bash
docker-compose up --build
```

### View Logs
```bash
docker-compose logs -f
```

### Check All Container Statuses
```bash
docker-compose ps
```

### View Logs for Specific Services
```bash
docker-compose logs app
docker-compose logs elasticsearch
docker-compose logs filebeat
docker-compose logs kibana
```

## Testing the Application

### Health Check
```bash
curl http://localhost:8000/
```

### Test API Endpoints
```bash
curl http://localhost:8000/api/hello
curl http://localhost:8000/api/warning
curl http://localhost:8000/api/error
curl -X POST "http://localhost:8000/api/items?name=test-item"
```

### Elasticsearch Health Check
```bash
curl http://localhost:9200/cluster/health
```

### List Elasticsearch Indices
```bash
curl http://localhost:9200/cat/indices
```

### Search FastAPI Logs in Elasticsearch
```bash
curl http://localhost:9200/fastapi-logs/_search?pretty
```

## Filebeat Testing and Troubleshooting

### Check Filebeat Logs
```bash
docker-compose logs filebeat
```

### Test Filebeat Configuration
```bash
docker-compose exec filebeat filebeat test config
```

### Test Filebeat Output
```bash
docker-compose exec filebeat filebeat test output
```

### Check Permissions
```bash
docker-compose exec filebeat ls -l /var/lib/docker/containers
```

## Kibana Testing and Troubleshooting

### Check Kibana Logs
```bash
docker-compose logs kibana
```

### Verify Elasticsearch Connection
```bash
curl http://localhost:9200
```

## Container Management

### Stop and Remove Containers
```bash
docker-compose down --rmi all
docker system prune -a
```

### Restart Containers
```bash
docker-compose up --build
```

### Monitor Logs
```bash
docker-compose logs -f
```

## Searching Logs

### Search for Logs with Level `ERROR`
```plaintext
log.level: ERROR
```

### Search for Logs Containing `hello`
```plaintext
message: hello
```

### Search for Logs with Level `WARNING` or `ERROR`
```plaintext
log.level: WARNING or log.level: ERROR
```

## Kibana Index Pattern Setup

### Step-by-Step Guide to Configure Index Pattern in Kibana
1. **Access Kibana**:
   - Open Kibana in your browser at `http://localhost:5601`.
2. **Create Index Pattern**:
   - Navigate to **Management** → **Stack Management**.
   - Under the **Kibana** section, click on **Data Views**.
3. **Set Data View**:
   - Click on **Create data view**.
   - Enter `fastapi-logs-*` as the index pattern.
4. **Confirm Configuration**:
   - Verify that the data view matches the expected indices and save it.