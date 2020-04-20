if [ -d htsget_app_venv ];
     then rm -f -r htsget_app_venv;
fi
python3 -m venv htsget_app_venv
cd htsget_app_venv
source bin/activate
pip install -U pip
git clone git@github.com:CanDIG/htsget_app.git
cd htsget_app
pip install Werkzeug==0.15.6
pip install pysam
python setup.py install
python ../../change_hts_config.py
python htsget_server/server.py
