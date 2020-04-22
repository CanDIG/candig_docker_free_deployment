echo "Installing Htsget App"

if [ -d htsget_app_venv ]; then
    echo "Found previous Htsget App virtual environment. Deleting it."; 
    rm -f -r htsget_app_venv;
fi
echo "Creating virtual environment for Htsget App"; 
python3 -m venv htsget_app_venv
cd htsget_app_venv
source bin/activate
pip install -U pip
echo "Cloning htsget_app repository"
git clone git@github.com:CanDIG/htsget_app.git
cd htsget_app
echo "Installing requirements"
pip install Werkzeug==0.15.6
pip install pysam
echo "Installing Htsget App"
python setup.py install
echo "Chaging Htsget configuration"
python ../../scripts/change_hts_config.py
echo "Starting Htsget App service."
python htsget_server/server.py
