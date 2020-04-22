echo "Installing Federation Service"

if [ -d federation_service_venv ]; then 
    echo "Found previous Federation Service virtual environment. Deleting it.";
    rm -f -r federation_service_venv;
fi

echo "Creating virtual environment for Federation Service";
python3 -m venv federation_service_venv
cd federation_service_venv
source bin/activate
echo "Cloning federation_service repository"
git clone git@github.com:CanDIG/federation_service.git
cd federation_service
echo "Installing requirements"
pip install -r requirements.txt
echo "Adding Htsget App to service list"
python ../../scripts/add_service.py
echo "Starting Federation service."
python -m candig_federation
