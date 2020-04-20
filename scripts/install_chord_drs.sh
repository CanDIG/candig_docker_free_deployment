if [ -d chord_drs_venv ];
     then rm -f -r chord_drs_venv;
fi

python3 -m venv chord_drs_venv
cd chord_drs_venv
source bin/activate
git clone https://github.com/c3g/chord_drs.git
cd chord_drs
export MINIO_URL=http://10.9.208.132:9000
export MINIO_USERNAME=minioadmin
export MINIO_PASSWORD=minioadmin
export MINIO_BUCKET=minio/samples
pip install -r requirements.txt
flask db upgrade
FLASK_DEBUG=True flask run -p 5556
