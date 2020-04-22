if [ ! -f "minio" ]; then
    echo "Downloading MinIO"
    wget https://dl.min.io/server/minio/release/linux-amd64/minio
    chmod +x minio
fi
echo "Starting MinIO Service"
python3 scripts/run_minio.py 
