if [ -d federation_service_venv ];
     then rm -f -r federation_service_venv;
fi

python3 -m venv federation_service_venv
cd federation_service_venv
source bin/activate
git clone git@github.com:CanDIG/federation_service.git
cd federation_service
pip install -r requirements.txt
python ../../add_service.py
python -m candig_federation
